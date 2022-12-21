
# MyRoutine
## 1. 프로젝트 개요
### 1.1 👩‍🦰 인력구성
  + 개인 프로젝트
### 1.2 프로젝트 동기
  + 기말고사 기간이 되어 공부를 하면서 계획을 세우지만 지키기 어렵습니다. </br>
  + 또한 스터티 플래너를 통해 주 단위로 계획을 세우면서 특정 요일에 반복되는 일정을 관리하는데에 불편함을 느꼈습니다. </br>
  + 이에 일주일에 한번 요일을 정한 루틴을 생성하고, 해당 요일에만 보여주어 상태를 업데이트하고 </br> 
    쉽게 관리할 수 있는 API를 개발하게 되었습니다. </br>
    
### 1.3 환경 및 기술스택 🔧<br>
   + **Python version** : `Python3.9` 
   + **Framework** : `Django 4.1.4`
   + **Database** : `sqlite`
   + **OS** : `window` </br></br>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/SQlite-003B57?style=flat&logo=SQLite&logoColor=white">
  + requirements.txt
   ``` requirements.txt
    asgiref==3.5.2
    autopep8==2.0.0
    Django==4.1.4
    django-multiselectfield==0.1.12
    djangorestframework==3.14.0
    factory-boy==3.2.1
    Faker==15.3.4
    pycodestyle==2.10.0
    python-dateutil==2.8.2
    pytz==2022.6
    six==1.16.0
    sqlparse==0.4.3
    tomli==2.0.1
    tzdata==2022.7
   ```
   


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
+ 생성, 수정, 삭제, 단건 조회, 목록 조회(요일별)
### 4.1 루틴 생성

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

 
### 4.2 루틴 업데이트
  + pk로 등록한 일정을 가져오고 `title`, `category`, `goal`, `is_alarm`, `days`등을 수정합니다. <br>
     days가 변경되면 변경된 해당 일정으로 등록 된 삭제 된 요일을 모두 delete 하고, 새로운 요일을 생성합니다.<br>
     
  #### 루틴 업데이트 시퀀스 다이어그램
    <img src=https://user-images.githubusercontent.com/59391473/208122840-e62f34ff-1825-474b-b9b0-18fe9239777c.png width="600" height="500"/><br>
  + 코드
  ``` python
  def put(self, request, pk):
        routine = Routine.objects.get(account=request.user, pk=pk)
        serializer = CreateUpdateRoutineSerializer(data=request.data)

        if serializer.is_valid():
            routine.title = serializer.data['title']
            routine.category = serializer.data['category']
            routine.goal = serializer.data['goal']
            routine.is_alarm = serializer.data['is_alarm']
            routine.modified_at = datetime.now()
            routine.save()
            RoutineDay.objects.filter(routine=routine).exclude(
                day__in=serializer.data['days']).delete()
            for day in serializer.data['days']:
                RoutineDay.objects.filter(Q(routine=routine) & Q(day__in=serializer.data["days"])).get_or_create(
                    day=day,
                    routine=routine
                )

        return Response({"data":  {"routine_id": pk}, "message": {"msg": "The routine has been modified.", "status":    "ROUTINE_UPDATE_OK"}}, status=status.HTTP_201_CREATED)

  ```
  + 입력 예시
    ``` json
    {
       "routine_id" : "ID to change(Optional)"
       "title" : "Title to edit(Optional)"
       "category" : "category(Optional)",
       "goal" : "goal(Optional)",
       "is_alarm" : "Alarm or not(Optional)",
       "days" : "set day(Optional)"
    }
    ```
  + 출력 예시
    ``` json
    {
       "data": {
            "routine_id": 1
        },
       "message": {
           "msg": "The routine has been modified.", 
           "status": "ROUTINE_UPDATE_OK"
       }
    }
    ```

### 4.3 루틴 목록 조회(요일별)
+ `datetime` 메소드의 요일 판별 기능으로 오늘이 무슨 요일인지 판별합니다.<br>
  day로 오늘을 가지는 루틴을 필터링하여 prefetch_related로 가져오고 리스트를 보여줍니다.<br>
 
+ 코드
``` python
def get(self, request):
      CHOICES = (
          ('MON'),
          ('TUE'),
          ('WED'),
          ('THU'),
          ('FRI'),
          ('SAT'),
          ('SUN'),
      )
      day = datetime.today().weekday()
      queryset = Routine.objects.prefetch_related(
          'result').filter(days__day=CHOICES[day])
      serializer = RoutineSerializer(queryset, many=True)
      return Response({"data": serializer.data, "message": {"msg": "Routine lookup was successful.", "status": "ROUTINE_LIST_OK"}}, status=status.HTTP_200_OK)
```
