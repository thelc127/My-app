from django.urls import path
from . import views

app_name = 'analysis'
urlpatterns = [
    path('ps_analysis/', views.graphView, name='ps_analysis'),
    path('monthly_balance_sheet/', views.BalanceSheetListView.as_view(),
         name='monthly_balance_sheet')
]
