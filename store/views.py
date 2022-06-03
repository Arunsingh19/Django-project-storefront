# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view()
# def product_list(request):
#     return Response('ok')

# @api_view()
# def product_detail(request, id):
#     return Response(id)

# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Product
# from .serializers import ProductSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view()
# def product_list(request):
#     return Response('ok')

# @api_view()
# def product_detail(request, id):
#     product = Product.objects.get(pk=id)
#     serializer =ProductSerializer(product)
#     return Response(serializer.data)

# from multiprocessing import context
# from os import stat
# from telnetlib import STATUS
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Product,Collection
# from .serializers import ProductSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404

# @api_view()
# def product_list(request):
#     querset = Product.objects.select_related('collection').all()
#     serializer = ProductSerializer(querset, many = True,context = {'request':request})
#     return Response(serializer.data)

# @api_view()
# def product_detail(request, id):
#     # try:
#     product = get_object_or_404(Product, pk=id)
#     serializer =ProductSerializer(product)
#     return Response(serializer.data)
#     # except Product.DoesNotExist:
#     #     # return Response(status=404)
#     #     return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view()
# def collection_detail(request, pk):
#     return Response('ok')

import collections
import imp
from math import prod
from msilib.schema import ReserveCost, ServiceInstall
from multiprocessing import context
from operator import methodcaller
from os import stat
from re import T, search
from telnetlib import STATUS
from unittest.mock import NonCallableMagicMock
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from store.filters import ProductFilter
from store.pagination import DefaultPagination
from store.permissions import FullDjangoModelPermissions, IsAdminOrReadOnly
from .models import Cart, CartItem, Order, OrderItem, Product,Collection,Review, Customer
from .serializers import AddCartItemSerializer, CartItemSerializer, CartSerializer, CollectionSerializer, CreateOrderSerializer, CustomerSerializer, OrderSerializer, ProductSerializer, ReviewSerializer, UpdateCartItemSerializer, UpdateOrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET':
#         querset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(querset, many = True,context = {'request':request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # serializer = ProductSerializer(data = request.data)
#         # if serializer.is_valid():
#         #     serializer.validated_data
#         #     return Response('ok')
#         # else:
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer = ProductSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         print(serializer.validated_data)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT','DELETE'])
# def product_detail(request, id):
#     # try:
#     product = get_object_or_404(Product, pk=id)
#     if request.method == 'GET':
#         serializer =ProductSerializer(product)
#         return Response(serializer.data)
#     # except Product.DoesNotExist:
#     #     # return Response(status=404)
#     #     return Response(status=status.HTTP_404_NOT_FOUND)
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product,data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if product.orderitem_set.count()>0:
#             return Response({'error':'product cannot be deleted because it is associated with as order item'})
#         product.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

# @api_view()
# def collection_detail(request, pk):
#     return Response('ok')

# @api_view(['GET', 'POST'])
# def collection_list(request):
#     if request.method == 'GET':
#         queryset = Collection.objects.annotate(products_count=Count('products')).all()
#         serializer = CollectionSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])
# def collection_detail(request, pk):
#     collection = get_object_or_404(
#     Collection.objects.annotate(products_count=Count('products')), pk=pk)
#     if request.method == 'GET':
#         serializer = CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CollectionSerializer(collection,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if collection.products.count() > 0:
#             return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# #Apiview(class)
# from django.db.models.aggregates import Count
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .models import Collection, Product
# from .serializers import CollectionSerializer,ProductSerializer
# class ProductList(APIView):
#     def get(self, request):
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ProductDetail(APIView):
#     def get(self,request,id):
#         product = get_object_or_404(Product, pk = id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self,request,id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         if product.orderitems.count() > 0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def collection_list(request):
#     if request.method == 'GET':
#         queryset = Collection.objects.annotate(products_count=Count('products')).all()
#         serializer = CollectionSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])
# def collection_detail(request, pk):
#     collection = get_object_or_404(
#     Collection.objects.annotate(products_count=Count('products')), pk=pk)
#     if request.method == 'GET':
#         serializer = CollectionSerializer(collection)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CollectionSerializer(collection,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if collection.products.count() > 0:
#             return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# #generic view
# from rest_framework.generics import ListCreateAPIView

# class ProductList(ListCreateAPIView):
#     def get_queryset(self):
#         return Product.objects.select_related('collection').all()

#     def get_serializer_class(self):
#         return ProductSerializer
    
#     def get_serializer_context(self):
#         return {'request':self.request}

# from rest_framework.generics import ListCreateAPIView

# class ProductList(ListCreateAPIView):
#     queryset =  Product.objects.select_related('collection').all()
#     serializer_class = ProductSerializer
    
#     def get_serializer_context(self):
#         return {'request':self.request}

# class ProductDetail(APIView):
#     def get(self,request,id):
#         product = get_object_or_404(Product, pk = id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self,request,id):
#         product = get_object_or_404(Product, pk=id)
#         serializer = ProductSerializer(product,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self, request, id):
#         product = get_object_or_404(Product, pk=id)
#         if product.orderitems.count() > 0:
#             return Response({'error': 'Product cannot be deleted because it is associated with an order item.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class CollectionList(ListCreateAPIView):
#     queryset = Collection.objects.annotate(product_count=Count('products')).all()
#     serializer_class = CollectionSerializer

# #get,put,delete apiview
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# class ProductList(ListCreateAPIView):
#     queryset =  Product.objects.select_related('collection').all()
#     serializer_class = ProductSerializer
    
#     def get_serializer_context(self):
#         return {'request':self.request}

# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def delete(self, request, id):
#         product = get_object_or_404(Product, pk= id)
#         if product.orderitems.count()>0:
#             return Response({'error': 'Product cannot be deleted'})
#         product.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

    
# class CollectionList(ListCreateAPIView):
#     queryset = Collection.objects.annotate(product_count=Count('products')).all()
#     serializer_class = CollectionSerializer

# #viewset
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ModelViewSet

# class ProductViewSet(ModelViewSet):
#     queryset =  Product.objects.select_related('collection').all()
#     serializer_class = ProductSerializer
    
#     def get_serializer_context(self):
#         return {'request':self.request}

#     def delete(self,request,pk):
#         product = get_object_or_404(Product, pk=pk)
#         if product.orderitems.count() > 0:
#             return Response({'error':'Product cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CollectionViewSet(ModelViewSet):
#     queryset = Collection.objects.annotate(product_count=Count('products')).all()
#     serializer_class = CollectionSerializer

#     def delete(self,request,pk):
#         collection = get_object_or_404(Collection, pk=pk)
#         if collection.products.count() > 0:
#             return Response({'error':'collection cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# #viewset with destroy function
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ModelViewSet

# class ProductViewSet(ModelViewSet):
#     queryset =  Product.objects.select_related('collection').all()
#     serializer_class = ProductSerializer
    
#     def get_serializer_context(self):
#         return {'request':self.request}

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count():
#             return Response({'error':'Product cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request,*args,**kwargs)

# class CollectionViewSet(ModelViewSet):
#     queryset = Collection.objects.annotate(product_count=Count('products')).all()
#     serializer_class = CollectionSerializer

#     def destroy(self, request, *args, **kwargs):
#         if Product.objects.filter(collection_id=kwargs['pk']).count():
#             return Response({'error':'Collection cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# class ReviewViewSet(ModelViewSet):
#     # queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get_queryset(self):
#         return Review.objects.filter(product_id=self.kwargs['product_pk'])
    
#     def get_serializer_context(self):
#         return {'product_id': self.kwargs['product_pk']}

# #filtering
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ModelViewSet

# class ProductViewSet(ModelViewSet):
#     serializer_class = ProductSerializer
#     def get_queryset(self):
#         queryset = Product.objects.all()
#         collection_id = self.request.query_params['collection_id']
#         if collection_id is not None:
#             queryset = queryset.filter(collection_id = collection_id)
#         return queryset

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count():
#             return Response({'error':'Product cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request,*args,**kwargs)

# class CollectionViewSet(ModelViewSet):
#     queryset = Collection.objects.annotate(product_count=Count('products')).all()
#     serializer_class = CollectionSerializer

#     def destroy(self, request, *args, **kwargs):
#         if Product.objects.filter(collection_id=kwargs['pk']).count():
#             return Response({'error':'Collection cannot be deleted'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# class ReviewViewSet(ModelViewSet):
#     # queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get_queryset(self):
#         return Review.objects.filter(product_id=self.kwargs['product_pk'])
    
#     def get_serializer_context(self):
#         return {'product_id': self.kwargs['product_pk']}

# class ProductViewSet(ModelViewSet):
#     serializer_class = ProductSerializer
#     def get_queryset(self):
#         queryset = Product.objects.all()
#         # collection_id =
#         self.request.query_params['collection_id']
#         collection_id = self.request.query_params.get('collection_id')
#         if collection_id is not None:
#             queryset = queryset.filter(collection_id = collection_id)
#         return queryset

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Product cannot bedeleted because it is associated with an order item.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# class CollectionViewSet(ModelViewSet):
#     queryset = Collection.objects.annotate(products_count=Count('products')).all()
#     serializer_class = CollectionSerializer
#     def destroy(self, request, *args, **kwargs):
#         if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# class ReviewViewSet(ModelViewSet):
#     serializer_class = ReviewSerializer
#     def get_queryset(self):
#         return Review.objects.filter(product_id=self.kwargs['product_pk'])
#     def get_serializer_context(self):
#         return {'product_id': self.kwargs['product_pk']}

# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ModelViewSet
# from django_filters.rest_framework import DjangoFilterBackend
# from .filters import ProductFilter

# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['collection_id']
#     # filterset_fields = ['collection_id','unit_price']
#     filterset_class = ProductFilter

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Product cannot bedeleted because it is associated with an order item.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# class CollectionViewSet(ModelViewSet):
#     queryset = Collection.objects.annotate(products_count=Count('products')).all()
#     serializer_class = CollectionSerializer
#     def destroy(self, request, *args, **kwargs):
#         if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# class ReviewViewSet(ModelViewSet):
#     serializer_class = ReviewSerializer
#     def get_queryset(self):
#         return Review.objects.filter(product_id=self.kwargs['product_pk'])
#     def get_serializer_context(self):
#         return {'product_id': self.kwargs['product_pk']}

# #searching and sorting
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.filters import SearchFilter,OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from .filters import ProductFilter


# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
#     # filterset_fields = ['collection_id']
#     # filterset_fields = ['collection_id','unit_price']
#     filterset_class = ProductFilter
#     search_fields = ['title','description']
#     ordering_fields = ['unit_price','last_update']

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Product cannot bedeleted because it is associated with an order item.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# class CollectionViewSet(ModelViewSet):
#     queryset = Collection.objects.annotate(products_count=Count('products')).all()
#     serializer_class = CollectionSerializer
#     def destroy(self, request, *args, **kwargs):
#         if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# class ReviewViewSet(ModelViewSet):
#     serializer_class = ReviewSerializer
#     def get_queryset(self):
#         return Review.objects.filter(product_id=self.kwargs['product_pk'])
#     def get_serializer_context(self):
#         return {'product_id': self.kwargs['product_pk']}

# #pagination
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ModelViewSet,GenericViewSet
# from rest_framework.filters import SearchFilter,OrderingFilter
# from rest_framework.pagination import PageNumberPagination
# from django_filters.rest_framework import DjangoFilterBackend
# from .filters import ProductFilter
# from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin


# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
#     # filterset_fields = ['collection_id']
#     # filterset_fields = ['collection_id','unit_price']
#     filterset_class = ProductFilter
#     # pagination_class = PageNumberPagination
#     pagination_class = DefaultPagination
#     search_fields = ['title','description']
#     ordering_fields = ['unit_price','last_update']

#     def get_serializer_context(self):
#         return {'request': self.request}

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Product cannot bedeleted because it is associated with an order item.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# class CollectionViewSet(ModelViewSet):
#     queryset = Collection.objects.annotate(products_count=Count('products')).all()
#     serializer_class = CollectionSerializer
#     def destroy(self, request, *args, **kwargs):
#         if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

# class ReviewViewSet(ModelViewSet):
#     serializer_class = ReviewSerializer
#     def get_queryset(self):
#         return Review.objects.filter(product_id=self.kwargs['product_pk'])
#     def get_serializer_context(self):
#         return {'product_id': self.kwargs['product_pk']}

# class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
#     # queryset = Cart.objects.all()
#     queryset = Cart.objects.prefetch_related('items__product').all()
#     serializer_class = CartSerializer

# # class CartItemViewSet(ModelViewSet):
# #     serializer_class = CartItemSerializer

# #     def get_queryset(self):
# #         return CartItem.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product')

# # #add cart item
# class CartItemViewSet(ModelViewSet):
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return AddCartItemSerializer
#         return CartItemSerializer

#     def get_serializer_context(self):
#         return {'cart_id':self.kwargs['cart_pk']}

#     def get_queryset(self):
#         return CartItem.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product')

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    # filterset_fields = ['collection_id']
    # filterset_fields = ['collection_id','unit_price']
    filterset_class = ProductFilter
    # pagination_class = PageNumberPagination
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['title','description']
    ordering_fields = ['unit_price','last_update']

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot bedeleted because it is associated with an order item.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    # queryset = Cart.objects.all()
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer

# class CartItemViewSet(ModelViewSet):
#     serializer_class = CartItemSerializer

#     def get_queryset(self):
#         return CartItem.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product')

# #add cart item,get url_id using context,patch only method
class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product')

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [FullDjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    # @action(detail=False)
    # def me(self, request):
    #     return Response(request.user.id)

    # @action(detail=False)
    # def me(self, request):
    #     customer = Customer.objects.get(user_id=request.user.id)
    #     serializer = CustomerSerializer(customer)

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        customer = Customer.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

class OrderViewSet(ModelViewSet):
    # serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete','head', 'options']
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data,context={'user_id':self.request.user.id})
        serializer.is_valid(raise_exception=True) 
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer

    # def get_serializer_context(self):
    #     return {'user_id':self.request.user.id}

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        customer_id = Customer.objects.only('id').get(user_id=user.id)
        return Order.objects.filter(customer_id=customer_id)