from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SalesForm, SalesDetailForm
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Sale, SaleDetail
from django.views import View
from django.utils import timezone
from datetime import date
from inventory.models import Item
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin


class SalesCreateView(LoginRequiredMixin, generic.edit.CreateView):
    """
    CreateView to create new purchase
    This is a class based view for creating new Purchase objects
    """
    login_url = '/login/'
    model = Sale
    form_class = SalesForm
    template_name = 'sale/sales.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class SalesDetailView(LoginRequiredMixin, generic.detail.DetailView):
    """
    DetailView that has SalesDetail form 
    and shows some minor details entered 
    previously in Purchase form

    """
    login_url = '/login/'
    model = Sale
    template_name = 'sale/sales_detail.html'

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        sales = get_object_or_404(Sale, pk=pk)

        return sales

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['sales'] = self.get_object()
        context['sale_form'] = SalesDetailForm
        return context

    def post(self, request, *args, **kwargs):
        form = SalesDetailForm(request.POST)
        if form.is_valid():
            data = request.POST.get('product_name')
            quantity = int(request.POST.get('quantity'))
            rate = int(request.POST.get('rate'))
            for item in Item.objects.all():
                if(data.lower() == item.item_name.lower()):
                    item.item_quantity = item.item_quantity - quantity
                item.save()
            form.save()
        # context = {}
        # context['sales'] = self.get_object()
        # context['sale_form'] = SalesDetailForm
        # return render(request, 'sale/sales_detail.html', context)

        #Multple data can be added if redirected to same page
        return HttpResponseRedirect('')


class SalesListView(LoginRequiredMixin, generic.list.ListView):
    login_url = '/login/'
    model = Sale

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DayBookListView(LoginRequiredMixin, generic.list.ListView):
    login_url = '/login/'
    model = Sale
    template_name = 'sale/daybook.html'

    def get_context_data(self, *args, **kwargs):
        today = date.today()
        context = {}
        context['sales'] = Sale.objects.filter(
            date__year=today.year, date__month=today.month, date__day=today.day)
        return context
