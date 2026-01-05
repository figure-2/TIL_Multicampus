from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# django에 만들어져 있는 form을 사용
from .models import User

class CustomUserCreationForm(UserCreationForm):
    # UserCreateForm을 받아서 custom 해서 쓰겠다는 의미
    # 위에서 가져온 UserCreateFor 을 상속 CustomUserCreateForm
    
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', )


class CustomAuthenticationForm(AuthenticationForm):
    pass




