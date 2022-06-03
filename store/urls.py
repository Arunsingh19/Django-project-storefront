# from django.urls import path
# from . import views

# urlpatterns = [
#     path('products/',views.product_list),
#     path('products/<int:id>/',views.product_detail),
#     path('collections/',views.collection_list),
#     path('collections/<int:pk>/',views.collection_detail, name = 'collection-detail'),
#     ]
# urlpatterns = [
#     path('products/',views.ProductList.as_view()),
#     # path('products/<int:id>/', views.ProductDetail.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     # path('collections/<int:pk>/', views.collection_detail,name = 'collection-detail',)
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('products/',views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     # path('collections/', views.CollectionList.as_view()),
#     # path('collections/<int:pk>/', views.collection_detail,name = 'collection-detail',)
# ]

#simple router
# from django.urls import path
# from . import views
# from rest_framework.routers import SimpleRouter
# from django.urls.conf import include

# router = SimpleRouter()
# router.register('products', views.ProductViewSet)
# # router.register('collections',views.CollectionViewSet)

# urlpatterns = router.urls

# # urlpatterns = [
# #     path('products/',views.ProductList.as_view()),
# #     path('products/<int:pk>/', views.ProductDetail.as_view()),
# #     # path('collections/', views.CollectionList.as_view()),
# #     # path('collections/<int:pk>/', views.collection_detail,name = 'collection-detail',)
# # ]

# #default router
# from django.urls import path
# from . import views
# from rest_framework.routers import DefaultRouter
# # from django.urls.conf import include

# router = DefaultRouter()
# router.register('products', views.ProductViewSet)
# # router.register('collections',views.CollectionViewSet)

# urlpatterns = router.urls

# # urlpatterns = [
# #     path('products/',views.ProductList.as_view()),
# #     path('products/<int:pk>/', views.ProductDetail.as_view()),
# #     # path('collections/', views.CollectionList.as_view()),
# #     # path('collections/<int:pk>/', views.collection_detail,name = 'collection-detail',)
# # ]

# from cgitb import lookup
# from django.urls import path
# from . import views
# # from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers
# # from django.urls.conf import include

# router = routers.DefaultRouter()
# router.register('products', views.ProductViewSet)
# router.register('collections',views.CollectionViewSet)

# products_router = routers.NestedDefaultRouter(router,'products',lookup='product')
# products_router.register('reviews',views.ReviewViewSet,basename = 'product-reviews')

# urlpatterns = router.urls + products_router.urls

# urlpatterns = [
#     path('products/',views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     # path('collections/', views.CollectionList.as_view()),
#     # path('collections/<int:pk>/', views.collection_detail,name = 'collection-detail',)
# ]

# from django.urls import path
# from rest_framework_nested import routers
# from . import views

# router = routers.DefaultRouter()
# router.register('products', views.ProductViewSet,basename='products')
# router.register('collections', views.CollectionViewSet)
# router.register('carts', views.CartViewSet)

# products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
# products_router.register('reviews', views.ReviewViewSet,basename='product-reviews')
# # URLConf
# urlpatterns = router.urls + products_router.urls

# #cart-items-id
from cgitb import lookup
from django.urls import path
from rest_framework_nested import routers

from store.models import Cart
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet,basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers',views.CustomerViewSet)
router.register('orders', views.OrderViewSet,basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls
