from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Drug, Movement
from django.views.decorators.csrf import csrf_exempt


# Dashboard view
def dashboard(request):
    drugs = Drug.objects.all().order_by('name')
    low_stock = Drug.objects.filter(quantity__lt=10)
    return render(request, 'inventory/dashboard.html', {
        'drugs': drugs,
        'low_stock': low_stock
    })
    
# Add Drug
def add_drug(request):
    if request.method == "POST":
        Drug.objects.create(
            name=request.POST['name'],
            batch_no=request.POST['batch_no'],
            expiry_date=request.POST['expiry'],
            quantity=request.POST['quantity'],
            supplier=request.POST['supplier'],
            location=request.POST['location'],
        )
        return redirect('dashboard')

    return render(request, 'inventory/add_drug.html')

# Movement History
def movement_history(request):
    movements = Movement.objects.all().order_by('-timestamp')
    return render(request, 'inventory/movement_history.html', {
        'movements': movements
    })
def main_dashboard(request):
    return render(request, 'inventory/main_dashboard.html')

# Stock Update (IN/OUT)
@csrf_exempt
def update_stock(request):
    if request.method == "POST":
        drug_id = request.POST.get("drug_id")
        movement_type = request.POST.get("movement_type")
        quantity = int(request.POST.get("quantity"))

        try:
            drug = Drug.objects.get(id=drug_id)
        except Drug.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Drug not found"})

        # APPLY STOCK UPDATE
        if movement_type == "OUT":
            if drug.quantity < quantity:
                return JsonResponse({"status": "error", "message": "Insufficient stock"})
            drug.quantity -= quantity

        else:  # IN
            drug.quantity += quantity

        drug.save()

        Movement.objects.create(
            drug=drug,
            movement_type=movement_type,
            quantity=quantity
        )

        return JsonResponse({"status": "success", "new_quantity": drug.quantity})

    return JsonResponse({"status": "error", "message": "Invalid request"})

# QR Code Scan

@csrf_exempt
def scan_qr(request):
    print("Request method:", request.method)
    print("POST data:", request.POST)

    if request.method == "POST":
        qr_text = request.POST.get("qr_text", "").strip()
        if not qr_text:
            return JsonResponse({"status": "error", "message": "QR text empty"})

        try:
            # QR format: "Drug: Name\nBatch: BatchNo"
            lines = qr_text.split("\n")
            name = lines[0].split(":", 1)[1].strip()
            batch = lines[1].split(":", 1)[1].strip()

            drug = Drug.objects.get(name=name, batch_no=batch)

            return JsonResponse({
                "status": "success",
                "drug_id": drug.id,
                "name": drug.name,
                "batch_no": drug.batch_no,
                "quantity": drug.quantity,
                "location": drug.location
            })

        except Drug.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Drug not found"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"QR format error: {str(e)}"})

    return JsonResponse({"status": "error", "message": "Invalid request"})
def scan_page(request):
    return render(request, 'inventory/scan_qr.html')