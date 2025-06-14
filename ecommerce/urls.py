"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path,include 
from home import views as _home
from electronic import views as _electronic
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',_home.showland,name='index'),
    path('electronic',_electronic.list_electronic,name='list_electronic'),
    path('showphone/<str:phone>/',_electronic.showphone,name='showphone'),
    path('categories/',_electronic.categories,name='categories'),
    path('products/',_electronic.products),
    path('list_product/<int:id>/',_home.list_product,name='list_product'),
    path('details/<int:id>/',_home.product_details,name='details'),
    path('addtocart/',_home.add_to_cart,name='addtocart'),
    path('test/',_electronic.test),
    path('checkout/',_home.checkout,name='checkout'),
    path('get_api/',_home.get_api),
    path('accounts/',include('accounts.urls'))
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
