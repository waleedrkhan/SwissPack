from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.swiss_products, name="products"),
    path('login/', views.login, name="login"),
    path('swiss-labs/', views.swiss_labs, name='swiss-labs'),
    path('swiss-product-range/', views.swiss_product_range, name='swiss_product_range'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('industries/', views.industries, name='industries'),
    path('page-edit/', views.edit_html, name='edit_html'),
    path('page-edit/<str:name>', views.edit_html, name='edit_html'),
    path('signup/', views.signup, name='signup'),
    path('babyfood/', views.babyfood, name='babyfood'),
    path('productpage/', views.productpage, name='productpage'),
    path('swiss-item/', views.item_function, name="item_function")

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)