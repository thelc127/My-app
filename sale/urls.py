from django.urls import path
from . import views

app_name = 'sale'
urlpatterns = [
    path('sales/', views.SalesCreateView.as_view(), name='sales'),
    path('salesdetail/<int:pk>',
         views.SalesDetailView.as_view(), name="sales_detail"),
    path('salesmade/', views.SalesListView.as_view(), name='sales_made'),
    path('sale-daybook/',views.DayBookListView.as_view(),name='daybook')
]
