from django.db import models
from django.utils import timezone
from django.urls import reverse


class Sale(models.Model):
    invoice = models.SmallIntegerField(primary_key=True, blank=False)
    ch_no = models.SmallIntegerField(blank=True, null=True)
    purchasers = models.CharField(max_length=128, blank=False)
    date = models.DateField(default=timezone.now, blank=False)

    def __str__(self):
        return (self.purchasers)

    def get_absolute_url(self):
        return reverse('sale:sales_detail', kwargs={'pk': self.pk})


class SaleDetail(models.Model):
    PRODUCT_CHOICES = (
        ('WOOD', 'Wood'),
        ('GLASS', 'Glass'),
        ('PLASTIC', 'Plastic'),
        ('LEATHER', 'Leather'),
        ('FABRIC', 'Fabric'),
        ('STEEL', 'Steel'),
    )
    sales = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30, choices=PRODUCT_CHOICES,
                                    default='WOOD')
    quantity = models.PositiveSmallIntegerField(blank=False)
    rate = models.IntegerField(blank=False)
    total = models.IntegerField(blank=False)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateField(default=timezone.now, blank=False)

    def __str__(self):
        return (self.product_name)
