from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.


class Purchase(models.Model):
    invoice = models.SmallIntegerField(primary_key=True, blank=False)
    ch_no = models.SmallIntegerField(blank=True, null=True)
    vendor = models.CharField(max_length=128, blank=False)
    date = models.DateField(default=timezone.now, blank=False)

    def __str__(self):
        return self.vendor

    def get_absolute_url(self):
        return reverse('entry:purchase_detail', kwargs={'pk': self.pk})


class PurchaseDetail(models.Model):

    PRODUCT_CHOICES = (
        ('WOOD', 'Wood'),
        ('G LASS', 'Glass'),
        ('PLASTIC', 'Plastic'),
        ('LEATHER', 'Leather'),
        ('FABRIC', 'Fabric'),
        ('STEEL', 'Steel'),
    )
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30,
                                    choices=PRODUCT_CHOICES,
                                    default='WOOD')
    quantity = models.PositiveSmallIntegerField(blank=False)
    rate = models.IntegerField(blank=False)
    total = models.IntegerField(blank=False)
    remarks = models.CharField(max_length=250)
    created_at = models.DateField(default=timezone.now, blank=False)

    def __str__(self):
        return (self.product_name)
