from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        #fields="__all__" #field to visible on screen
        exclude=["post"]
        labels={
            "user_name":'Your Name',
            "user_email":"Your Mail",
            "text": "Your Comment"
        }
