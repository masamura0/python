from django import forms
from.models import Friend
from django import forms 
from.models import Friend, Message 

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    
class CheckForm(forms.Form):
    date = forms.DateField(label='Date', input_formats=['%d'], \
        widget=forms.DateInput(attrs={'class':'form-control'}))
    time = forms.TimeField(label='Time', \
        widget=forms.TimeInput(attrs={'class':'form-control'}))
    datetime = forms.DateTimeField(label='DateTime', \
        widget=forms.DateTimeInput(attrs={'class':'form-control'}))
    
class CheckForm(forms.Form):
    str = forms.CharField(label='String', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    
    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError('You input "NO"!')
        
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'birthday': forms.DateInput(attrs={'class':'form-control'}),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title','content','friend']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'content': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':2}),
            'friend': forms.Select(attrs={'class':'form-control form-control-sm'}),
        }