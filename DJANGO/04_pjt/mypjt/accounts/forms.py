# 1. 가져오기
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# 4 다른거 상속받기
from django.contrib.auth import get_user_model
# 
class CustomUserCreationForm(UserCreationForm):
    # 3.  내 입맛대로 바꾸기(Meta클래스 재정의)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # 여기서 커스터 마이징

class CustomUserChangeForm(UserChangeForm):
    # 3.  내 입맛대로 바꾸기(Meta클래스 재정의)
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 여기서 커스터마이징
