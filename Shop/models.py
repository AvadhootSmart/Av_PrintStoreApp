from django.db import models
# import os
# Create your models here.

def get_upload_path(instance, filename):
    # Build the file path based on the instance's 'name' field and the original filename
    return f'print_files/{instance.name}/{filename}'
                        
class Order(models.Model):
    TYPE_CHOICES = (
        ('B&W', 'Black and White'),
        ('Color', 'Color'),
    )
    ORIENTATION_CHOICES = (
        ('Single', 'Single Page'),
        ('Double', 'Double Page'),
    )

    name = models.CharField(max_length=225, default="")
    UploadFile = models.FileField(upload_to=get_upload_path, null=True, blank=True)
    filename = models.CharField(max_length=255, blank=True,null=True)
    ColorType = models.CharField(max_length=50, choices=TYPE_CHOICES)
    orientation = models.CharField(max_length=50,choices=ORIENTATION_CHOICES)

    def save(self, *args, **kwargs):
        if self.UploadFile:
            self.filename = self.UploadFile.name
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlackAndWhitePrice(models.Model):
    Single_Page_Cost = models.IntegerField()
    Double_Page_Cost = models.IntegerField()
     
    def __str__(self):
        return f'Single:{self.Single_Page_Cost}RS   Double:{self.Double_Page_Cost}RS'
    

class ColorPrice(models.Model):
    Single_Page_Cost = models.IntegerField()
    Double_Page_Cost = models.IntegerField()
    
    def __str__(self):
        return f'Single:{self.Single_Page_Cost}RS   Double:{self.Double_Page_Cost}RS'
    

class Sales(models.Model):
    Order_amount = models.IntegerField()
    
    def __str__(self):
        return "Sales"