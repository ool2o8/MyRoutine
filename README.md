
# MyRoutine

## ERD
<img src=https://user-images.githubusercontent.com/59391473/207026260-e8acc39c-f941-4148-9160-c9a83cb929b3.png width="350" height="300"/><br>



## URL
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


## 시퀀스 다이어그램

  + **루틴 생성**
  
  <img src=https://user-images.githubusercontent.com/59391473/208120370-abec69c3-8c0b-4a69-9197-ff3d3179d083.png width="600" height="500"/><br>
  
  + **루틴 업데이트**
  
  <img src=https://user-images.githubusercontent.com/59391473/208122840-e62f34ff-1825-474b-b9b0-18fe9239777c.png width="600" height="500"/><br>
