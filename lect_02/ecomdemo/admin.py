from django.contrib import admin
from ecomdemo.models import User, Product

# admin.site.register(User) # another way to write -> use annotation & define table there.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['title','username', 'email', 'name']
    list_display = ['id','username','name']
    search_fields = ['name','id']


# admin.site.register(Product)
# we can overwrite the filed name by using @admin.register annotation.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['id']
    save_as = True
    fieldsets = (
        ('Product Info', {
            'fields': ('seller', 'name', 'description')}),
        ("Stock Info", {'fields': ('price', 'stock'),
                         'classes': ('collapse',)})
    )