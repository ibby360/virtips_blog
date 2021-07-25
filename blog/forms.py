from blog.models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Name*'
        self.fields['email'].widget.attrs['placeholder'] = 'Email*'
        self.fields['comment'].widget.attrs['placeholder'] = 'Message*'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
   