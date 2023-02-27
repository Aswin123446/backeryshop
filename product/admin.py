from django.contrib import admin
from .models import product_collection,comment_box

# Register your models here.
admin.site.register(product_collection)
admin.site.register(comment_box)

