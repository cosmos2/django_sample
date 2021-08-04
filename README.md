# Django sample project with DRF
## 개발환경
```shell
python == 3.9.6
Django == 3.2.6
djangorestframework = 3.12.0
```
## 개발용 db 세팅
docker 사용
```shell
# 프로젝트 루트에서 실행
$ docker-compose up -d
```

## run server
```shell
$ ./manage.py runserver --settings=django_sample.settings.local
```