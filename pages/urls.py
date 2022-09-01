from django import views
from django.urls import path
from .views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete
from  . import views


app_name = 'pages'
urlpatterns = [
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='pages'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
]

urlpatterns = [
    path('<int:page_id>/', views.page, name="page"),
]