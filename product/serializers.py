from rest_framework import serializers
from product.models import Category,Product,Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id name".split()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "id title description price category".split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "id text product".split()