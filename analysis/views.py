from django.shortcuts import render
from django.views import generic
import json
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from entry.models import Purchase, PurchaseDetail
from datetime import date
from sale.models import Sale, SaleDetail
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def graphView(request):
    purchase_qs = PurchaseDetail.objects.all()
    sale_qs = SaleDetail.objects.all()
    categories = list()
    purchase_no = list()
    sale_no = list()
    sum = SaleDetail.objects.filter(
        product_name='STEEL', created_at__year='2018').aggregate(Sum('quantity'))
    sale_no.append(sum.get('quantity__sum'))
    sum = PurchaseDetail.objects.filter(
        product_name='STEEL', created_at__year='2018').aggregate(Sum('quantity'))
    purchase_no.append(sum.get('quantity__sum'))
    categories.append('STEEL')

    sum = SaleDetail.objects.filter(
        product_name='WOOD', created_at__year='2018').aggregate(Sum('quantity'))
    sale_no.append(sum.get('quantity__sum'))
    sum = PurchaseDetail.objects.filter(
        product_name='WOOD', created_at__year='2018').aggregate(Sum('quantity'))
    purchase_no.append(sum.get('quantity__sum'))
    categories.append('WOOD')

    sum = SaleDetail.objects.filter(
        product_name='PLASTIC', created_at__year='2018').aggregate(Sum('quantity'))
    sale_no.append(sum.get('quantity__sum'))
    sum = PurchaseDetail.objects.filter(
        product_name='PLASTIC', created_at__year='2018').aggregate(Sum('quantity'))
    purchase_no.append(sum.get('quantity__sum'))
    categories.append('PLASTIC')

    sum = SaleDetail.objects.filter(
        product_name='FABRIC', created_at__year='2018').aggregate(Sum('quantity'))
    sale_no.append(sum.get('quantity__sum'))
    sum = PurchaseDetail.objects.filter(
        product_name='FABRIC', created_at__year='2018').aggregate(Sum('quantity'))
    purchase_no.append(sum.get('quantity__sum'))
    categories.append('FABRIC')

    sum = SaleDetail.objects.filter(
        product_name='LEATHER', created_at__year='2018').aggregate(Sum('quantity'))
    sale_no.append(sum.get('quantity__sum'))
    sum = PurchaseDetail.objects.filter(
        product_name='LEATHER', created_at__year='2018').aggregate(Sum('quantity'))
    purchase_no.append(sum.get('quantity__sum'))
    categories.append('LEATHER')

    sum = SaleDetail.objects.filter(
        product_name='GLASS', created_at__year='2018').aggregate(Sum('quantity'))
    sale_no.append(sum.get('quantity__sum'))
    sum = PurchaseDetail.objects.filter(
        product_name='GLASS', created_at__year='2018').aggregate(Sum('quantity'))
    purchase_no.append(sum.get('quantity__sum'))
    categories.append('GLASS')

    return render(request, 'analysis/ps_analysis.html', {
        'categories': json.dumps(categories),
        'purchase_no': json.dumps(purchase_no),
        'sale_no': json.dumps(sale_no)
    })


class BalanceSheetListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'

    model = Purchase
    template_name = 'analysis/balance-sheet.html'

    def get_context_data(self, *args, **kwargs):
        today = date.today()
        context = {}
        context['purchases'] = Purchase.objects.filter(
            date__year=today.year, date__month=today.month)
        context['sales'] = Sale.objects.filter(
            date__year=today.year, date__month=today.month)
        psum = PurchaseDetail.objects.filter(
            created_at__year=today.year, created_at__month=today.month).aggregate(Sum('total'))
        ssum = SaleDetail.objects.filter(
            created_at__year=today.year, created_at__month=today.month).aggregate(Sum('total'))
        context['net'] = (int(psum.get('total__sum') or 0)-int(ssum.get('total__sum') or 0))
        return context
