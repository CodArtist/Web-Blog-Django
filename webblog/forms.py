from django import forms
from . models import Blogs

class ImageForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields= '__all__'
        exclude=['username']
        widgets = {
        'blog':forms.Textarea(attrs={'class':'form-control shadow p-3 mb-5 bg-white rounded w-100 p-5','promptText':"Whats in your mind?"}),
        # 'privacy':forms.RadioSelect(attrs={'class':'form-control'}),
        # 'images':forms.ImageField(attrs={'class':'form-control'}),
        }
        