from django.db import models


class Vehicle(models.Model):
    VIN = models.CharField(max_length=17, unique=True)  # Vehicle Identification Number
    make = models.CharField(max_length=50)  # Manufacturer
    model = models.CharField(max_length=50)  # Model name
    year = models.PositiveIntegerField()  # Year of manufacture
    color = models.CharField(max_length=30)  # Color
    description = models.TextField(blank=True, null=True)  # Additional information
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
