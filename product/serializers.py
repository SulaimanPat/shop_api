from rest_framework import serializers
from product.models import Category,Product,Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id name product_count".split()

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    filtered_review_list = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = "all".split()
    def get_category_name(self, product):
        try:
            return product.category.name
        except:
            return None
class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer
    class Meta:
        model = Review
        fields = "id text product stars".split()
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "id title description price category avg_rating".split()

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField()

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    descriptions = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.IntegerField()

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    product = serializers.IntegerField()
    stars = serializers.IntegerField()