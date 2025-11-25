from django.db import models

# Create your models here.
import qrcode
from io import BytesIO
from django.core.files import File

class Drug(models.Model):
    name = models.CharField(max_length=200)
    batch_no = models.CharField(max_length=100)
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    location = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr_data = f"Drug: {self.name}\nBatch: {self.batch_no}\nExpiry: {self.expiry_date}"
        qr_img = qrcode.make(qr_data)
        buffer = BytesIO()
        qr_img.save(buffer, format='PNG')
        file_name = f"{self.name}-{self.batch_no}.png"
        self.qr_code.save(file_name, File(buffer), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Movement(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=10, choices=[('IN','IN'), ('OUT','OUT')])
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.drug.name} - {self.movement_type}"
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Pharmacy(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
