from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item, Firm, Category
from .serializers import ItemSerializer, FirmSerializer, CategorySerializer


# class ItemListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#
# class FirmListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Firm.objects.all()
#     serializer_class = FirmSerializer
#
#
# @api_view(http_method_names=['GET', "POST"])
# def category_list_create_api_view(request):
#     if request.method == "GET":
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == "POST":
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemRetrieveUpdateDestroyAPIView(APIView):

    def get_item(self, item_id):
        return generics.get_object_or_404(Item, id=item_id)

    def get(self, request, item_id, *args, **kwargs):
        serializer = ItemSerializer(self.get_item(item_id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, item_id, *args, **kwargs):
        serializer = ItemSerializer(self.get_item(item_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id, *args, **kwargs):
        self.get_item(item_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FirmListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        firms = Firm.objects.all()
        serializer = FirmSerializer(firms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = FirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FirmRetrieveUpdateDestroyAPIView(APIView):

    def get_firm(self, firm_id):
        return generics.get_object_or_404(Firm, id=firm_id)

    def get(self, request, firm_id, *args, **kwargs):
        serializer = FirmSerializer(self.get_firm(firm_id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, firm_id, *args, **kwargs):
        serializer = FirmSerializer(self.get_firm(firm_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, firm_id, *args, **kwargs):
        self.get_firm(firm_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        firms = Category.objects.all()
        serializer = CategorySerializer(firms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryRetrieveUpdateDestroyAPIView(APIView):

    def get_category(self, category_id):
        return generics.get_object_or_404(Category, id=category_id)

    def get(self, request, category_id, *args, **kwargs):
        serializer = CategorySerializer(self.get_category(category_id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, category_id, *args, **kwargs):
        serializer = CategorySerializer(self.get_category(category_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id, *args, **kwargs):
        self.get_category(category_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
