from django.contrib import admin
from .models import Post
# Register your models here.
# In order to see the model on the admin page, it must be registered here.   Import the class here, register the class
# However, the interesting thing is 'blog' is not here--- but it is in settings under INSTALLED_APPS, and then also
# when running manage.py startapp blog, makemigrations blog, migrate blog, and in apps.py (maybe most importantly)
admin.site.register(Post)
