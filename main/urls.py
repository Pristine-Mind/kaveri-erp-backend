"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from producer.views import (
    SupplierViewSet,
    CustomerViewSet,
    ProductViewSet,
    OrderViewSet,
    SaleViewSet,
    DashboardAPIView,
    UserInfoView,
    TopSalesCustomersView,
    TopOrdersCustomersView,
    StatsAPIView,
    CityListView,
    export_producers_to_excel,
    export_customers_to_excel,
    export_products_to_excel,
    export_sales_to_excel,
    export_orders_to_excel,
)
from user.views import (
    RegisterView,
    LoginAPIView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'sales', SaleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path("login/", LoginAPIView.as_view()),
    path('api/v1/dashboard/', DashboardAPIView.as_view(), name='dashboard'),
    path('api/v1/user-info/', UserInfoView.as_view()),
    path('api/v1/customer/top-sales/', TopSalesCustomersView.as_view(), name='top-sales-customers'),
    path('api/v1/customer/top-orders/', TopOrdersCustomersView.as_view(), name='top-orders-customers'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/v1/stats/', StatsAPIView.as_view(), name='stats-api'),

    path('api/v1/cities/', CityListView.as_view(), name='city-list'),
    path("docs/", SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("api-docs/", SpectacularAPIView.as_view(), name='schema'),
    path("api-docs/swagger-ui/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # export
    path('export/producers/', export_producers_to_excel, name='export_producers'),
    path('export/customers/', export_customers_to_excel, name='export_customers'),
    path('export/products/', export_products_to_excel, name='export_products'),
    path('export/orders/', export_orders_to_excel, name='export_orders'),
    path('export/sales/', export_sales_to_excel, name='export_sales'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
