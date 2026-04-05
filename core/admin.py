from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Saint, Quote

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
    search_fields = ('name', 'id')

@admin.register(Saint)
class SaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'feast', 'image_preview')
    search_fields = ('name', 'feast', 'id')
    list_filter = ('categories',)
    filter_horizontal = ('categories',) # Makes selecting multiple categories easier
    
    # Adds a small preview of the Cloudinary image in the list view
    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="width: 45px; height:45px; border-radius: 50%;" />', obj.img.url)
        return "No Image"
    image_preview.short_description = 'Preview'

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'saint', 'date', 'rank')
    search_fields = ('text', 'saint__name') # Allows searching by Saint's name
    list_filter = ('date', 'categories', 'saint')
    date_hierarchy = 'date' # Adds a nice date navigation bar at the top
    filter_horizontal = ('categories',)