from django.contrib import admin

from products.models import Product, ProductCategory, Basket

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'quantity', 'category')
	list_display_links = ('name',)
	fields = (('name', 'image'), ('description', 'short_description'), ('price', 'quantity', 'category'))
	ordering = ('name',)
	search_fields = ('name',)
	readonly_fields = ('short_description',)


class BasketAdminInLine(admin.TabularInline):
	model = Basket
	fields = ('product', 'quantity', 'created_timestamp')
	readonly_fields = ('created_timestamp',)
	extra = 0
