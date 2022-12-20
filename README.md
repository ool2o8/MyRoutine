
# MyRoutine
## 1. 프로젝트 개요
### 1.1 👩‍🦰 인력구성
  + 개인 프로젝트
### 1.2 프로젝트 동기
  + 기말고사 기간이 되어 공부를 하면서 계획을 세우지만 지키기 어렵습니다. </br>
  + 또한 스터티 플래너를 통해 주 단위로 계획을 세우면서 특정 요일에 반복되는 일정을 관리하는데에 불편함을 느꼈습니다. </br>
  + 이에 일주일에 한번 요일을 정한 루틴을 생성하고, 해당 요일에만 보여주어 상태를 업데이트하고 </br> 
    쉽게 관리할 수 있는 API를 개발하게 되었습니다. </br>
    
### 1.3 환경 및 기술스택 🔧**<br>
   + ``` python3.9 ```
   + **Framework** :Django 4.1.4
   + **Database** : sqlite
   + **OS** : window </br></br>
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/></br>
    <img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=Django&logoColor=white"/></br>
    <img src="https://img.shields.io/badge/SQlite-003B57?style=flat&logo=SQLite&logoColor=white"/><br>

## 2. URL
  + **127.0.0.1:8000/accounts**

|CRUD|HTTP|URL|
|---|---|---|
|회원가입|POST|/signup|
|로그인|POST|/login|
|로그아웃|GET|/logout|


  + **127.0.0.1:8000/routines**

|CRUD|HTTP|URL|
|---|---|---|
|루틴 생성|POST||
|루틴 목록 조회|GET|/routines|
|루틴 단건 조회|GET|/routines/{post_id: int}|
|루틴 삭제|DELETE|/routines/{post_id: int}|
|루틴 수정|PUT|//routines/{post_id: int}/update|

## 3. UML

### 3.1 ERD
<img src=https://user-images.githubusercontent.com/59391473/207026260-e8acc39c-f941-4148-9160-c9a83cb929b3.png width="350" height="300"/><br>



## 4. 기능

### **4.1 루틴 생성**

+ `title`, `category`, `goal`, `day`, `is_goal` 을 입력값으로 받아 루틴을 생성합니다.<br>
  `Day`에 `Routine` 을 foriegn 으로 연결하여 함께 생성합니다.<br>
  `Result`를 OneToOne 으로 생성합니다.

  #### 루틴 생성 시퀀스 다이어그램
  <img src=https://user-images.githubusercontent.com/59391473/208120370-abec69c3-8c0b-4a69-9197-ff3d3179d083.png width="600" height="500"/><br>
+ 코드
``` python
  def post(self, request):
        serializer = CreateUpdateRoutineSerializer(data=request.data)
        if serializer.is_valid():
            routine = Routine.objects.create(
                account=request.user,
                title=serializer.data['title'],
                category=serializer.data['category'],
                goal=serializer.data['goal'],
                is_alarm=serializer.data['is_alarm']
            )
            for i in serializer.data['days']:
                RoutineDay.objects.create(
                    day=i,
                    routine=routine
                )
            RoutineResult.objects.create(
                routine=routine
            )
  ```
  + 입력 예시
    ``` json
    {
       "title" : "problem solving",
       "category" : "HOMEWORK'",
       "goal": "Increase your problem-solving skills",
       "is_alarm": true,
       "days": ["MON", "WED", "FRI"]
    }
    ```
  + 출력 예시
    ``` json
    {
       "data": {
          "routine_id": 1
        },
       "message": {
           "msg": "You have successfully created the routine.", 
            "status": "ROUTINE_CREATE_OK"
        }
    }
    ```

  
### **4.1.2 루틴 업데이트**
  + **루틴 업데이트 시퀀스 다이어그램**
  <img src=https://user-images.githubusercontent.com/59391473/208122840-e62f34ff-1825-474b-b9b0-18fe9239777c.png width="600" height="500"/><br>
