from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "pincode", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "email": forms.EmailInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "phone": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "pincode": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "message": forms.Textarea(attrs={"class": "w-full border border-gray-300 p-2 rounded", "rows": 4}),
        }




from django import forms
from .models import QuickEnquiry

class QuickEnquiryForm(forms.ModelForm):
    class Meta:
        model = QuickEnquiry
        fields = ['name', 'phone', 'email', 'query']
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone



from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your email...',
            })
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "pincode", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "email": forms.EmailInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "phone": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "pincode": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "message": forms.Textarea(attrs={"class": "w-full border border-gray-300 p-2 rounded", "rows": 4}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone


from django import forms
from .models import JobApplication  # ✅ Ensure JobApplication model exists

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["name", "email", "phone", "resume"]  # Ensure all fields exist in the model
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full border p-2 rounded"}),
            "email": forms.EmailInput(attrs={"class": "w-full border p-2 rounded"}),
            "phone": forms.TextInput(attrs={"class": "w-full border p-2 rounded", "placeholder": "Enter your phone number"}),
            "resume": forms.ClearableFileInput(attrs={"class": "w-full border p-2 rounded"}),
        }
