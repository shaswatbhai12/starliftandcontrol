from django import forms
from .models import QuickEnquiry

class QuickEnquiryForm(forms.ModelForm):
    class Meta:
        model = QuickEnquiry
        fields = ["name", "phone", "email", "query"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "phone": forms.TextInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "email": forms.EmailInput(attrs={"class": "w-full border border-gray-300 p-2 rounded"}),
            "query": forms.Textarea(attrs={"class": "w-full border border-gray-300 p-2 rounded", "rows": 0}),
        }
