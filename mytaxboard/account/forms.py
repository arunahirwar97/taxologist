from django import forms
from django.forms import ClearableFileInput
from .models import Tax_Plan_page_file_upload
class multiplefiles(forms.ModelForm):
    class Meta:
        model = Tax_Plan_page_file_upload
        fields = ["files"]
        widgets = {
            "files": ClearableFileInput(attrs={'multiple': True}),
        }