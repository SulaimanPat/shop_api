from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    @property
    def product_count(self):
        return self.objects.all()
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def filtered_review_list(self):
        return self.review_list.filter(stars__gt=3)

    @property
    def avg_rating(self):
        lis = [review.stars for review in self.filtered_review_list.all()]
        return sum(lis) / len(lis)

STAR_CHOICES = ((iterator_, '* ' * iterator_) for iterator_ in range(1, 6))
class Review(models.Model):
    text = models.TextField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='review_list')
    stars = models.IntegerField(default=5, choices=(STAR_CHOICES))

