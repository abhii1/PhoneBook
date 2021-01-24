# PhoneBook

>Application help user to ___

● Adding a contact <br />

● Modifying an existing contact  <br />

● Deleting a contact  <br />

● Get all contacts (10 contacts per page by default)  <br />

● Search a contact by name or email address (10 results per page by default)  <br />


Application has inbuild database by MongoDb atlas and uses python pymongo module to interact with database 


## Table of contents


* [Link](#Link)
* [Features](#Features)
* [Installation](#screenshots)
* [Quickstart](#Quickstart)
* [Languages_and_API](#Languages_and_API)
* [End_point](#End_point)
* [Contact](#contact)
* [License](#License)


## Link

<img src="https://avatars1.githubusercontent.com/u/9919?s=200&v=4" width="42" height="42">

- [X] GitHub : https://github.com/abhii1/CRUD-APPLICATION



## Features


- [X] User can easily create contact with unique email id (required field) .


- [X] User can modify any existing contact in database 


<img src="https://user-images.githubusercontent.com/49953175/95673653-29591200-0bc8-11eb-9ec8-02fb9f2d0b07.PNG" >



- [X] User can delete any contact from database .


<img src="https://user-images.githubusercontent.com/49953175/95673770-6ffb3c00-0bc9-11eb-8c2c-fdade20dc2f7.gif" >


- [X] user can Search contact by email (default 10) or can be any value 


<img src="https://user-images.githubusercontent.com/49953175/95673915-4ee71b00-0bca-11eb-8554-5af63bd3ba30.gif" >

- [X] User can serach contact by name (default 10) or can be any value 

<img src="https://user-images.githubusercontent.com/49953175/95674035-31668100-0bcb-11eb-964e-b3694452b255.gif" >




## Installation

>  **download repo **

     
     
```
create a virtual enviroment 

download dependencies in requirements.txt

run app.py (python app.py)

```



## Quickstart

>AFTER INSTALLATION USER NEED TO RUN THIS COMMAND IN COMMAND PROMPT after in virtual enviroment 

```
python app.py

```




**Add contact  to Phone Book  with simple steps**
  

<img src="https://user-images.githubusercontent.com/49953175/95742293-61865080-0cad-11eb-8ecd-83badd0a210d.gif" >


**Update conatct in Phone Book**





<img src="https://user-images.githubusercontent.com/49953175/95743894-19b4f880-0cb0-11eb-96b0-ced545e85a29.gif" >


**Delete contact by any field **




<img src="https://user-images.githubusercontent.com/49953175/95744370-cd1ded00-0cb0-11eb-8a34-55530cc33138.gif" >



**Search All Contact *

 



<img src="https://user-images.githubusercontent.com/49953175/95744913-ce034e80-0cb1-11eb-83e1-6c0a74e18c7c.gif" >


**Search by Email**



<img src="https://user-images.githubusercontent.com/49953175/95745492-cf814680-0cb2-11eb-8c5a-e6387124959f.gif" >


**Search by Name **




<img src="https://user-images.githubusercontent.com/49953175/95745682-24bd5800-0cb3-11eb-8b47-b81c1a9eab40.gif" >


                           

## Languages_and_API


<img src="https://miro.medium.com/max/2496/1*uYcRdZDho2AicwI9k84kpw.jpeg">



<img src="https://files.realpython.com/media/flask.3aee85149243.png">








## End_point

```
#PUT DATA 
   
localhost/add_con

#user need to enter the column name and value in the body>form-data

   ```
   
```
#GET DATA 

localhost/GET_DATA/<column>

#in place select desire column name 

```

```
#update by id 

localhost//Update/<id>/<update_column>

#user need to select id and then column to update and value of updated field in body>>form-data


```

```
#update by filter 

localhost/Update/by/<filter_except_id>/<update_column>

#user need to select filter and column to update in filter_except_id and update_column



```

```
delete by id

localhost/DELETE/<id>

#user specify id 


```

```
#Delete ALL data retrive from column

localhost/Update/ALL/by/<filter_except_id>/<update_column>


# user need to specify <filter_except_id>/<update_column>

```


## Contact


Created by Abhishek pratap singh

[<img src="https://cdns.iconmonstr.com/wp-content/assets/preview/2012/240/iconmonstr-linkedin-3.png" width="42" height="42">](https://www.linkedin.com/in/abhishek-pratap-singh-44a96816b/)

[<img src="https://9to5google.com/wp-content/uploads/sites/4/2016/08/gmail-logo.png?w=1280" width="42" height="42">](abhisheklumiamicro@gmail.com)


## License

This package is distributed under the `MIT license`.
