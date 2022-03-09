from django.forms import ModelForm
from .models import visitor
class visitorform(ModelForm):
    class Meta:
        model=visitor
        fields=['name']