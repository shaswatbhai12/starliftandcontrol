from django.contrib import admin
from django.utils.html import format_html
from .models import (
    CarouselImage, Product, ProductImage, WhyChooseUs, 
    Testimonial, Contact, QuickEnquiry, Service, 
    GalleryItem, Subscription, Career, JobApplication, PdfCategory, PdfFile, Book
)

# ✅ Carousel Image Admin
@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_tag', 'caption', 'created_at']
    search_fields = ['caption']
    list_filter = ['created_at']

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius: 5px;" />', obj.image.url)
        return "No Image"

    image_tag.short_description = "Image"


# ✅ Inline Product Image Admin (For Gallery)
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Allows adding multiple images easily
    readonly_fields = ['image_tag']  # Show image previews

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius: 5px;" />', obj.image.url)
        return "No Image"

    image_tag.short_description = "Image Preview"


# ✅ Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at']  # Display key details
    search_fields = ['name']
    list_filter = ['created_at']
    inlines = [ProductImageInline]  # Add inline gallery for product images


# ✅ Contact Admin (Handles both Contact & Quick Enquiry)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'pincode', 'product', 'sub_product_name', 'message', 'timestamp']
    list_filter = ['timestamp']
    search_fields = ['name', 'email', 'phone']

    def has_add_permission(self, request):
        """ Prevent admin from manually adding contacts via Admin panel """
        return False  # Contacts should be submitted via forms only


# ✅ Quick Enquiry Admin Panel
@admin.register(QuickEnquiry)
class QuickEnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'query', 'created_at']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['created_at']


# ✅ Subscription Admin
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')  # Display these fields in the admin panel
    search_fields = ('email',)  # Enable search by email
    list_filter = ('created_at',)  # Add filtering options by date
    ordering = ('-created_at',)  # Show the latest subscriptions first


# ✅ Registering remaining models
admin.site.register(ProductImage)
admin.site.register(WhyChooseUs)
admin.site.register(Testimonial)
admin.site.register(Service)
admin.site.register(GalleryItem)




from django.contrib import admin
from .models import Career

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'posted_on')
    search_fields = ('title', 'location')
    list_filter = ('location', 'posted_on')
    ordering = ('-posted_on',)

from django.contrib import admin
from .models import JobApplication

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "job", "email", "applied_on")  # ✅ Ensure these fields exist in the model
    list_filter = ("applied_on", "job")  # ✅ Ensure these fields exist in the model
    search_fields = ("name", "email", "job")

admin.site.register(JobApplication, JobApplicationAdmin)






from django.contrib import admin
from .models import PdfCategory, PdfFile

admin.site.register(PdfCategory)
admin.site.register(PdfFile)



from django.contrib import admin
from .models import Book

admin.site.register(Book)
