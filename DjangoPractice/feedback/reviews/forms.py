from django import forms

class ReviewForm(forms.Form):
    user_name= forms.CharField(label='Your Name', required=True, max_length=100, error_messages={
        "required":"Your Name must not be empty",
        "max_length":"please enter a shorter name!"
    })
    review_text=forms.CharField(label="your feedback",widget=forms.Textarea,max_length=250)
    rating=forms.IntegerField(label="Your rating", min_value=1,max_value=5)