from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import RegexValidator

STATUS = ((0, "Draft"), (1, "Published"))

PRICE_INCREMENT = (("p/w", "per week"), ("p/m", "per month"))

PRICE_CURRENCY = (("£", "GBP"), ("$", "USD"), ("€", "Euro"), ("¥", "Yen"), ("₩", "Won"), ("₺", "Lira"), ("₣", "Franc"), ("₹", "Rupee"), ("د.ك", "Dinar"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="market_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='market_likes', blank=True)
    listing_price = models.CharField(
        max_length=15,
        validators=[RegexValidator("^[0-9]")],
        )
    listing_currency = models.CharField(max_length=100, choices=PRICE_CURRENCY, default="GBP")
    listing_timespan = models.CharField(max_length=100, choices=PRICE_INCREMENT, default="per month")

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"comment {self.body} by {self.name}"

class GeeksModel(models.Model):
 
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="geek_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    listing_price = models.CharField(
        max_length=15,
        validators=[RegexValidator("^[0-9]")],
        )
    listing_currency = models.CharField(max_length=100, choices=PRICE_CURRENCY, default="GBP")
    listing_timespan = models.CharField(max_length=100, choices=PRICE_INCREMENT, default="per month")
 
    def __str__(self):
        return self.title