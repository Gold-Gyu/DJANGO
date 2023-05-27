#UCF 그대로 상속받아서 내가 바꾸고 싶은 것만 바꾼다 => 오버라이딩
# 1. 가져오기
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# 4 다른거 상속받기
from django.contrib.auth import get_user_model


# 2. 상속받기
class CustomUserCreationForm(UserCreationForm):
    # 3.  내 입맛대로 바꾸기(Meta클래스 재정의)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    # 3.  내 입맛대로 바꾸기(Meta클래스 재정의)
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 정보수정
        fields = ('email', 'first_name', 'last_name', 'username')
