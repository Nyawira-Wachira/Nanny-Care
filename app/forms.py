from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import TextInput, FileInput, NumberInput, Textarea


from .models import User, UserProfile


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'bio']
        
        widgets ={
            'profile_pic': FileInput(attrs={'class': 'input', 'placeholder': 'Profile Picture'}),
            'bio': TextInput(attrs={'class': 'input', 'placeholder': 'Update Bio'}),
        }
        
        
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email',)
        
        