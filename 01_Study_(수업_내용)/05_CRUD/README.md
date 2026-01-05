# CRUD
> `<>`는 변수를 의미하고 생성하고 싶은 이름을 넣는 공간입니다.
1. 프로젝트 폴더 생성
2. 프로젝트 폴더로 이동 / vscode 실행   
    2-1. `.gitignore`, `README.md` 생성
3. django 프로젝트 생성  
    3-1. `<pjt-name>` 공간은 변수를 의미
```bash
django-admin startproject <pjt-name> .
```

4. 가상활경 설정
```bash
python -m venv venv
```

5. 가상환경 활성화
```bash
source venv/Scripts/activate
```

6. 가상환경에 django 설치
```bash
pip install django
```

---

7. 서버 실행 확인
```bash
python manage.py runserver
```

8. 앱 생성
```bash
django-admin startapp <appname>
```

9. 앱 등록 => `setting.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    <app_name>,
]
```

10. `url.py` -> `views.py` -> `templates/*.html` 순서로 코드 작성