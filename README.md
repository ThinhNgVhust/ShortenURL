# ShortenURL
Lib:
- Backend
    - Django, Django Memcached (for cache)
    - RestAPI
    - CeleryTask
    - Redis (for Celery Task)
- FrontEnd
    - HTML, CSS, Boostrap
    - JS
    - layout.html. error page (expire, wrong url..... ), success page(shorten url, coppy button). 

Task:
1. Create prj, set up front end using form boostrap.(3h)
2. Create DataModel, Write code in views. (3h) 
3. Build Celery Task (3h)

### Requrements:   
1. Throttling: Client can only generate 5 url links /hours. Do not miuse
2. Using csrf_token for submit form. 
3. Using cache form heavy read. => Django Memcached
4. Task Celery to schedule database cleaning. 
5. Data Model: Using only table name URLTalbe 
    - id: PK, auto increament
    - longURL: varchar
    - shortURL: varchar
    - Lastime use: Datetime
6. API :
    - GET
    - POST

Source:      
Cache: https://www.youtube.com/watch?v=iDZKqk_NH24 




### Detail 
<hr>

- Create app: django-admin startproject  PROJECT_NAME 


























## My thinking of this solution
- If i using django csrf_token, will my app be **statefull**?
- What if 