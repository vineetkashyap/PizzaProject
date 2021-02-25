# PIZZA PROEJECT
---
### There are API Endspoints Listed Below
1. This is the endpoint to add the size size of pizza and will be stored in data base, so before creating pizza please add pizza size 
   * http://127.0.0.1:8000/size/
   
2. This is the endpoint will be used to create a pizza after defining the size of the pizza
   * http://127.0.0.1:8000/create/
   
3. This is the endpoint to show all pizza and filter can be achieved by the pizza size and pizza type
   * http://127.0.0.1:8000/list/
   
4. This is the endpoint will be used to delete or update the pizza and in the place of the **pk** (primary key) we have to pass the id of the perticuler pizza like 1,2,3....
   * http://127.0.0.1:8000/deleteorupdate/pk/

---
### Step To Run The Project
1. Make sure to create a mongoDB database and connect your database

3. Do the migrations so that collections will be created,Please Run This Command ..
   * ` python manage.py runserver `
   
4. Then Run The Command Given Below So That Migrations Code can be executed..
   * `python manage.py migrate `
   
5. After That Just Run Server By Following Command .. 
   * `python manage.py runserver `
   
6. Please Make Sure That Define The Pizza Size Before Creating The Pizza. For That Use The First Endpoint  
   * http://127.0.0.1:8000/size/
