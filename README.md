# django_iris_deploy
iris deploy
```
설치 라이브러리

pip install django==4.2
pip install numpy pandas sklearn pickle seaborn matplotlib

djando 명령
1. 프로젝트 만들기
django-admin startproject 프로젝트이름

2. 기본 DB 생성하기
python manage.py migrate

3. 앱 만들기
python manage.py startapp 앱이름

4. 관리자 만들기
python manage.py createsuperuser

5. 서버 실행하기
python manage.py runserver

6. 데이터 모델 클래스 정의 후 DB 적용하기
python manage.py makemigrations
python manage.py migrate
```
