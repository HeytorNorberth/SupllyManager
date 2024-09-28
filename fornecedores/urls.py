from django.urls import path
from fornecedores import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fornecedores/create/', views.cadastrar_fornecedor, name='fornecedores_create'),
    path('fornecedores/delete/<str:id>', views.deletar_fornecedor, name='fornecedores_delete'),
    path('fornecedores/active/<str:id>', views.ativar_fornecedor, name='fornecedores_active'),
    path('fornecedores/deactive/<str:id>', views.desativar_fornecedor, name='fornecedores_deactive'),
]