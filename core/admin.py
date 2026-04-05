# # from django.contrib import admin
# # from .models import Category, Saint, Quote, Resource, Favorite

# # @admin.register(Category)
# # class CategoryAdmin(admin.ModelAdmin):
# #     list_display = ['id', 'name', 'icon']
# #     search_fields = ['name']

# # @admin.register(Saint)
# # class SaintAdmin(admin.ModelAdmin):
# #     list_display = ['id', 'name', 'feast']
# #     list_filter = ['categories']
# #     search_fields = ['name', 'feast']
# #     filter_horizontal = ['categories']

# # @admin.register(Quote)
# # class QuoteAdmin(admin.ModelAdmin):
# #     list_display = ['id', 'saint', 'rank', 'date']
# #     list_filter = ['rank', 'date', 'categories']
# #     search_fields = ['text']
# #     filter_horizontal = ['categories']

# # @admin.register(Resource)
# # class ResourceAdmin(admin.ModelAdmin):
# #     list_display = ['id', 'title', 'type']
# #     list_filter = ['type']
# #     search_fields = ['title', 'content']

# # @admin.register(Favorite)
# # class FavoriteAdmin(admin.ModelAdmin):
# #     list_display = ['id', 'user', 'session_id', 'created_at']
# #     list_filter = ['created_at']


# from django.contrib import admin
# from .models import Category, Saint, Quote

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']
#     search_fields = ['name']

# @admin.register(Saint)
# class SaintAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'feast']
#     search_fields = ['name', 'feast']
#     filter_horizontal = ['categories']

# @admin.register(Quote)
# class QuoteAdmin(admin.ModelAdmin):
#     list_display = ['id', 'saint', 'date']
#     search_fields = ['text']
#     filter_horizontal = ['categories']

from django.contrib import admin
from .models import Category, Saint, Quote

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'icon']
    search_fields = ['name']

@admin.register(Saint)
class SaintAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'feast']
    search_fields = ['name', 'feast']
    list_filter = ['categories']

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'saint', 'date']
    search_fields = ['text']
    list_filter = ['saint', 'date']
    