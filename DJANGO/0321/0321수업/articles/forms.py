from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):

    class Meta:
        # 어떤 모델에서
        model = Article
        # 포함할 필드를 고른다.
        fields = '__all__'

    # 장고에서 유효성을 검사하는 방법

    # def clean_title(self):  # clean_내가검사하고싶은필드명(self)
    #     title = self.cleaned_data("title")
    #     if 'django' in title:
    #         return True
    #     return False