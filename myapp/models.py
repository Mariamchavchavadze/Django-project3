from django.db import models


class Vehicle(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    VIN = models.CharField(max_length=17, unique=True)  # Vehicle Identification Number
    make = models.CharField(max_length=50)  # Manufacturer
    model = models.CharField(max_length=50)  # Model name
    year = models.PositiveIntegerField()  # Year of manufacture
    color = models.CharField(max_length=30)  # Color
    description = models.TextField(blank=True, null=True)  # Additional information
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    image = models.ImageField(upload_to='vehicles/', null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
