from django.contrib import admin

# Register your mode*
from .models import *

# class s_and_tt(admin.ModelAdmin):
    # # list_display= ('thumbnail', 'title', 'description', 'price', 'links')

#Registre model
admin.site.register(s_and_t)
#admin.site.register(s_and_tt)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Blog)
