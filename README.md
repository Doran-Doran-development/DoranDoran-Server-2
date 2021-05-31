<p align="center">
 <a><img src="images/readme-logo.png" width="70%" height="70%"></a>
</p>

_GSM 회의실 예약 관리 및 학생 이동 관리 서비스_, **`도란도란`** _의 백엔드 레포지토리 입니다_.

[![API Server](http://img.shields.io/badge/Swagger-85EA2D?style=flat&logo=Swagger&logoColor=white)](http://10.120.71.242:81/swagger) **`※ 학교 IP 내에서만 접근 가능해요!`**

<div>
<img src="https://img.shields.io/github/languages/top/Doran-Doran-development/DoranDoran-Server-2"/></a></a>
<img src="https://img.shields.io/github/release-date/Doran-Doran-development/DoranDoran-Server-2?color=skyblue"/></a></a>
<img src="https://img.shields.io/github/last-commit/Doran-Doran-development/DoranDoran-Server-2"/></a></a>
<img src="https://img.shields.io/github/commit-activity/m/Doran-Doran-development/DoranDoran-Server-2"/></a></a>
</div>

### :seat: 프로젝트 개요

GSM 교내 서비스 **도란도란**은 두 가지 기능을 가지고 있습니다.

- **학생 위치 관리**
- **회의실 예약 관리**

#### 학생 위치 관리

저희 학교의 선생님들은 **자율 학습 시간**에 **학생들의 현재 위치**를 파악에 어려움을 겪고 있습니다.
이런 학생들의 위치를 **한눈에 파악하고 관리**하기 위한 **학생 위치 관리 기능**을 제공하고 있습니다.

#### 회의실 예약 관리

하나의 건물 (학교, 회사 등) 에는 다용도로 쓸 수 있는 **여러 공간들**이 있습니다.
이런 **공간**을 효율적으로 **관리**하고 **예약 기능을** 위한 **공간 관리 기능**을 제공하고 있습니다.

### :gear: 사용한 기술

#### Backend

<div>
<img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=Django&logoColor=white"/></a></a>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/></a></a>
<img src="https://img.shields.io/badge/boto3-FFCA28?style=flat&logo=Amazon%20AWS&logoColor=white"/></a></a>
</div>

#### DevOps

<div>
<img src="https://img.shields.io/badge/Amazon%20S3-569A31?style=flat&logo=Amazon%20S3&logoColor=white"/></a></a>
</div>

<div>
<img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=Ubuntu&logoColor=white"/></a></a>
<img src="https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=Jenkins&logoColor=white"/></a></a>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=Docker&logoColor=white"/></a></a>
<img src="https://img.shields.io/badge/gunicorn-4479A1?style=flat&logo=unicode&logoColor=white"/></a></a>
</div>

<div>
<img src="https://img.shields.io/badge/Github-181717?style=flat&logo=Github&logoColor=white"/></a></a>
<img src="https://img.shields.io/badge/Github%20actions-2088FF?style=flat&logo=Github%20actions&logoColor=white"/></a></a>
<img src="http://img.shields.io/badge/Swagger-85EA2D?style=flat&logo=Swagger&logoColor=white"/></a></a>

</div>

#### Database

<div>
<img src="https://img.shields.io/badge/AWS%20RDS-232F3E?style=flat&logo=Amazon%20AWS&logoColor=white"/></a></a>
<img src="https://img.shields.io/badge/Mysql-4479A1?style=flat&logo=Mysql&logoColor=white"/></a></a>
</div>

### :fork_and_knife: 직접 실행시켜보세요!

#### 1. 레포지토리를 클론 받아주시고, 루트 디렉토리로 진입해주세요.

```bash
$ git clone https://github.com/Doran-Doran-development/DoranDoran-Server-2.git
$ cd DoranDoran-Server-2
```

#### 2. `dev.env` 파일을 생성해 주세요

```bash
$ vim dev.env
SECRET_KEY=djangosecretkey
JWT_SECRET_KEY=jwtsecretkey
JWT_ALGORITHM=HS256
DJANGO_SETTINGS_MODULE=config.settings.develop
EMAIL_HOST_USER=<이메일 주소를 적어주세요!>
EMAIL_HOST_PASSWORD=<이메일 계정의 비밀번호를 적어주세요!>

DJANGO_DB_HOST=db
DJANGO_DB_PORT=3306
DJANGO_DB_NAME=dorandoran_dev_db
DJANGO_DB_USERNAME=root
DJANGO_DB_PASSWORD=password
```

#### 3. Docker 컨테이너를 생성해주시고, 접속해보세요!

```bash
$ docker-compose -f ./docker-compose.dev.yml up -d

※ DB 헬스체크 때문에 약간의 시간이 소요되니, 조금만 기다려주세요
```

[http://localhost:8000/swagger](http://localhost:8000/swagger)
