from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import (
    CarouselImage, Product, Testimonial, ProductImage, Contact, WhyChooseUs, Service, GalleryItem, Subscription
)
from .forms import ContactForm, QuickEnquiryForm, SubscriptionForm
from .models import BusinessHours


# Configure logging



def home(request):
    return render(request, 'home/index.html', {
        'carousel_images': CarouselImage.objects.all(),
        'products': Product.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'why_choose_us': WhyChooseUs.objects.all(),
    })

def product_detail(request, product_id):
    return render(request, 'home/product_detail.html', {
        'product': get_object_or_404(Product, id=product_id),
        'product_images': ProductImage.objects.filter(product_id=product_id),
    })

def sub_product_detail(request, image_id):
    sub_product = get_object_or_404(ProductImage, id=image_id)
    return render(request, 'home/sub_product_detail.html', {
        'sub_product': sub_product,
        'related_images': ProductImage.objects.filter(product=sub_product.product),
    })

def contact_view(request):
    product = Product.objects.filter(id=request.GET.get("product")).first()
    sub_product = ProductImage.objects.filter(id=request.GET.get("sub_product")).first()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.product = product
            contact.sub_product_name = sub_product.description if sub_product else None
            contact.save()
            messages.success(request, "Your inquiry has been submitted successfully!")
            return redirect("thank_you_page")
        messages.error(request, "There was an error in your submission. Please check your input.")
    else:
        form = ContactForm()
    return render(request, "home/contact.html", {"form": form, "product_name": product.name if product else "Unknown Product", "sub_product_name": sub_product.description if sub_product else None})

def quick_enquiry(request):
    if request.method == "POST":
        form = QuickEnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enquiry submitted successfully!")
            return redirect('thank_you_page')
        else:
            messages.error(request, "Invalid data. Please check again.")
            return redirect(request.META.get('HTTP_REFERER'))

    # return redirect('home')   # ✅ IMPORTANT LINE

def thank_you_page(request):
    return render(request, "home/thank_you.html")

def about(request):
    return render(request, "home/about.html")

def services(request):
    return render(request, "home/services.html", {"services": Service.objects.all()})

def gallery(request):
    media_type = request.GET.get("type", "all")

    if media_type == "photos":
        items = GalleryItem.objects.filter(media_type="image")

    elif media_type == "videos":
        items = GalleryItem.objects.filter(media_type="video")

    else:  # all
        items = GalleryItem.objects.all()

    return render(request, "home/gallery.html", {
        "gallery_items": items,
        "active_filter": media_type
    })

def contact_us(request):
    form = ContactForm(request.POST or None)
    business_hours = BusinessHours.objects.all().order_by('day')

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your inquiry has been submitted successfully!")
        return redirect("thank_you_page")
    elif request.method == "POST":
        messages.error(request, "Please fix the errors in the form and try again.")
    return render(request, "home/contact_us.html", {"form": form, "business_hours": business_hours})

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            if not Subscription.objects.filter(email=email).exists():
                subscriber = form.save()

                # ✅ Send Professional Thank You Email
                subject = "Welcome to Star Lift & Controller 🚀"

                html_content = render_to_string(
                    "emails/thank_you.html",
                    {"email": email}
                )

                email_msg = EmailMultiAlternatives(
                    subject,
                    "Thank you for subscribing.",
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                )

                email_msg.attach_alternative(html_content, "text/html")
                email_msg.send(fail_silently=False)

                messages.success(request, "Thank you for subscribing!")

            else:
                messages.warning(request, "You are already subscribed!")

        else:
            messages.error(request, "Invalid email address.")

    return redirect('home')

def accept_cookies(request):
    response = JsonResponse({"message": "Cookies accepted"})
    response.set_cookie("cookiesAccepted", "true", max_age=365 * 24 * 60 * 60)
    return response



from django.shortcuts import render
from .models import Career

def careers(request):
    jobs = Career.objects.all().order_by('-posted_on')
    return render(request, "home/careers.html", {"jobs": jobs})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Career, JobApplication
from .forms import JobApplicationForm

def apply_for_job(request, job_id):
    job = get_object_or_404(Career, id=job_id)

    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect("careers")  # Redirect to careers page
        messages.error(request, "Please correct the application form and submit again.")

    else:
        form = JobApplicationForm()

    return render(request, "home/apply.html", {"job": job, "form": form})


def catogary_product_detail(request, product_id):
    return render(request, 'home/sub_product_detail.html', {
        'product': get_object_or_404(Product, id=product_id),
        'product_images': ProductImage.objects.filter(cat_product_id=product_id),
    })

def caod(request):
    return render(request, "home/caod.html")

from django.shortcuts import render, get_object_or_404
from .models import PdfCategory, PdfFile

def pdf_list(request, category_name):
    category = get_object_or_404(PdfCategory, name=category_name)
    pdfs = PdfFile.objects.filter(category=category)
    return render(request, 'home/pdf_list.html', {'category': category, 'pdfs': pdfs})

def css(request):
    return render(request, "home/output.css")



from django.shortcuts import render
from .models import Book

def books(request):
    books = Book.objects.all()
    return render(request, 'home/books.html', {'books': books})


from django.shortcuts import render
from .models import Book

def books(request):
    drive_books = Book.objects.filter(category='drive')
    control_panel_books = Book.objects.filter(category='control_panel')
    door_drive_books = Book.objects.filter(category='door_drive')
    overload_books = Book.objects.filter(category='overload')

    context = {
        'drive_books': drive_books,
        'control_panel_books': control_panel_books,
        'door_drive_books': door_drive_books,
        'overload_books': overload_books,
    }
    
    return render(request, 'index.html', context)


from django.core.mail import send_mail

def send_newsletter(request):
    subscribers = Subscription.objects.values_list('email', flat=True)

    subject = "Latest Update from Star Lift & Controller 🚀"
    message = "We have exciting updates and offers for you. Stay tuned!"

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        list(subscribers),
    )

    return HttpResponse("Newsletter sent successfully!")