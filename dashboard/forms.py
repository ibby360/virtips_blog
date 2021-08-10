from django import forms
from django.forms import TextInput, FileInput, Select
from django.forms.widgets import Textarea
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from blog.models import Post, Author
from category.models import Category
from accounts.models import Account

class ArticleCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      empty_label="Select Category",
                                      widget=forms.Select(attrs={
                                          "class": "form-control selectpicker",
                                          "type": "text",
                                          "name": "article-category",
                                          "id": "articleCategory",
                                          "data-live-search": "true"
                                      }
    )
    )

    class Meta:
        STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
        )
        model = Post
        fields = ['title', 'category', 'tags', 'thumbnail', 'overview', 'body', 'status']

        widgets = {
            'title': TextInput(attrs={
                                     'name': "article-title",
                                     'class': "form-control",
                                     'placeholder': "Enter Article Title",
                                     'id': "articleTitle"
                                     }),

            'thumbnail': FileInput(attrs={
                                        "class": "form-control clearable-file-input",
                                        "type": "file",
                                        "id": "articleImage",
                                        "name": "article-image"
                                      }

                               ),

            'overview': Textarea(attrs={
                'name': "article_overview",
                'class': "form-control",
                'placeholder': "Enter Article Overview",
                'id': "articleOverview"
            }),

            'body': forms.CharField(widget=CKEditorUploadingWidget(config_name="default", attrs={
                    #    "rows": 10, "cols": 30,
                       'id': 'content',
                       'name': "article_content",
                       'class': "form-control",
                       })),

            'tags': TextInput(attrs={
                                     'name': "tags",
                                     'class': "form-select",
                                     'placeholder': "Example: sports, game, politics",
                                     'id': "tags",
                                     'data-allow-new': "true",
                                     'multiple': "multiple"
                                     }),

            'status': Select(choices=STATUS_CHOICES,
                             attrs=
                             {
                                 "class": "form-control selectpicker",
                                 "name": "status", "type": "text",
                                 "id": "articleStatus",
                                 "data-live-search": "true",
                                 "title": "Select Status"
                             }
                             ),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name',]

        widgets = {
                'category_name': TextInput(attrs={
                                         'name': "category_name",
                                         'class': "me-sm-1 mb-sm-0 form-control form-control-lg border-gray-300",
                                         'placeholder': "Enter Category Name",
                                         'id': "categoryName"
                                         }),
        }

class UserForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('username', 'email',)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Username'
        self.fields['email'].widget.attrs['placeholder'] = 'name@company.com'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class AuthorProfileForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'gender', 'jobtitle', 'bio', 'avatar', 'cover_photo',
                  'city', 'country', 'facebook_url', 'instagram_url', 'twitter_url', 'linkedin_url',)

        widgets = {

            'first_name': forms.TextInput(attrs={
                'name': "first-name",
                'class': "form-control",
                'id': "firstName",
                'placeholder': "Enter your FirstName"
            }),

            'last_name': forms.TextInput(attrs={
                'name': "last-name",
                'class': "form-control",
                'id': "lastName",
                'placeholder': "Also your last name"
            }),

            'jobtitle': forms.TextInput(attrs={
                'name': "job-title",
                'class': "form-control",
                'id': "job-title",
                'placeholder': "Senior Software Engineer"
            }),

            'bio': forms.Textarea(attrs={
                'name': "bio",
                'class': "form-control",
                'id': "bio",
                'rows': "4",
                'placeholder': "Enter Your Biography"
            }),

            'gender': forms.Select(attrs={
                'name': "address",
                'class': "form-select mb-0",
                'id': "address",
                'placeholder': "Your Gender"
            }),

            'city': forms.TextInput(attrs={
                'name': "city",
                'class': "form-control",
                'id': "city",
                'placeholder': "Enter Your City"
            }),

            'country': forms.Select(attrs={
                'name': "country",
                'class': "form-select w-100 mb-0",
                'id': "country",
                'select': "Select Your Country"
            }),

            'avatar': forms.FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "profileImage",
            }),

            'cover_photo': forms.FileInput(attrs={
                "class": "form-control clearablefileinput",
                "type": "file",
                "id": "bannerImage",
            }),

            'facebook_url': forms.TextInput(attrs={
                'name': "facebook-account-url",
                'class': "form-control",
                'id': "faceboolAccountUrl",
                'placeholder': "https://facebook.com/username"
            }),

            'twitter_url': forms.TextInput(attrs={
                'name': "twitter-account-url",
                'class': "form-control",
                'id': "twitterAccountUrl",
                'placeholder': "https://twitter.com/username"
            }),

            'instagram_url': forms.TextInput(attrs={
                'name': "instagram-account-url",
                'class': "form-control",
                'id': "instagramAccountUrl",
                'placeholder': "https://instagram.com/username"
            }),

            'linkedin_url': forms.TextInput(attrs={
                'name': "linkedin-account-url",
                'class': "form-control",
                'id': "linkedinAccountUrl",
                'placeholder': "https://linkedin.com/username"
            }),

        }



