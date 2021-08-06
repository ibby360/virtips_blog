from django import forms
from django.forms import TextInput, FileInput, Select
from django.forms.widgets import Textarea
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from blog.models import Post
from category.models import Category

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
                                     'class': "form-control",
                                     'placeholder': "Example: sports, game, politics",
                                     'id': "tags",
                                     'data-role': "tagsinput"
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