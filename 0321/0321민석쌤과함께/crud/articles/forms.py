from django import forms
from .models import Article

class ArticleForm(forms.ModelForm): # form과 ModelForm의 차이 : form은 데이터만 일부분만 가져와서 사용할 수 있음
    #사용자의 입력이 필요한 필드 : title, content
    # title = forms.CharField(max_length=30)
    # content = forms.CharField(widget=forms.Textarea)

    class Meta:    
        model = Article
        fields = "__all__"


