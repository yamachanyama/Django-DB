from django import forms
from .models import Message
        
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)

# from.models import Friend, Message
            
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title','content', 'person']
