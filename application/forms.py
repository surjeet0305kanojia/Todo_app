from django.forms import ModelForm
from application.models import Todo
class Todoform(ModelForm):
    class Meta:
        model =Todo
        fields=['title','status','priority']
        