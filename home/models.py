from django.db import models
from django.utils.timezone import now  # Add this import

# ✅ Carousel Images Model
class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    title = models.CharField(max_length=100, blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Carousel Image"
        verbose_name_plural = "Carousel Images"

    def __str__(self):
        return self.title or self.caption or f"Image {self.id}"


# ✅ Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField( blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(default=now, editable=False)  # Add this field

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



# ✅ Sub-Product Images (Gallery)
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="products/gallery/")
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.name}"


# ✅ Why Choose Us Section Model
class WhyChooseUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='why_choose_us/icons/', null=True, blank=True)

    def __str__(self):
        return self.title


# ✅ Testimonials Model
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    feedback = models.TextField()
    rating = models.IntegerField(default=5)  # Rating out of 5
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name


# ✅ Projects Model (Linked to Products)
class Project(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='projects')
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Project for {self.product.name}"


# ✅ Contact Model (Linked to Product)
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6, blank=True, null=True)  # Made optional
    message = models.TextField(max_length=1000, blank=True, null=True)  # Made optional
    product = models.ForeignKey(Product, on_delete=models.CASCADE , blank=True, null=True)
    sub_product_name = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.name} - {self.product.name if self.product else 'No Product'}"




from django.db import models

class QuickEnquiry(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.name}"

from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to='services_icons/', blank=True, null=True)

    def __str__(self):
        return self.title

from django.db import models

class GalleryItem(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    
    title = models.CharField(max_length=255)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)  # Store YouTube/Video links

    def __str__(self):
        return self.title



from django.db import models

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Add this line

    def __str__(self):
        return self.email











from django.db import models

class Career(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

from django.db import models

class JobApplication(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, default="")  # ✅ Default value
    job = models.CharField(max_length=255)  # ✅ Add this field
    resume = models.FileField(upload_to="resumes/")
    applied_on = models.DateTimeField(auto_now_add=True)  # ✅ Add this field

    def __str__(self):
        return f"{self.name} - {self.job}"





      

from django.db import models

class PdfCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class PdfFile(models.Model):
    category = models.ForeignKey(PdfCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='pdfs/')
    title = models.CharField(max_length=255 , blank=True, null=True)

    def __str__(self):
        return self.category.name + " - " + (self.title if self.title else str(self.file))


from django.db import models

class BusinessHours(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    day = models.CharField(max_length=10, choices=DAY_CHOICES, unique=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    closed = models.BooleanField(default=False)  # If the business is closed on this day

    def __str__(self):
        return f"{self.day}: {self.opening_time} - {self.closing_time}" if not self.closed else f"{self.day}: Closed"


from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('drive', 'Drive'),
        ('control_panel', 'Control & Panel'),
        ('door_drive', 'Door Drive'),
        ('overload', 'Overload'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='books/covers/')
    pdf_file = models.FileField(upload_to='books/pdfs/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.title

