from django.contrib import admin

# Register your models here.
from .models import AboutUs, WhyChooseUs, Chef

admin.site.register(AboutUs)
admin.site.register(WhyChooseUs)
admin.site.register(Chef)
