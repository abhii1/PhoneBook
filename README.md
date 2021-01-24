# PhoneBook

>Phonebook allows you to upload your plain text contact file from your computer, and search contact on your phone. It's designed
for people who likes to keep all their contacts in a text file

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

<img src="https://user-images.githubusercontent.com/49953175/105624045-8493d500-5e44-11eb-9ff0-64dd65172f60.PNG" >



- [X] User can modify any existing contact in database 


<img src="https://user-images.githubusercontent.com/49953175/105623971-07686000-5e44-11eb-9266-2507e6fa0fb5.PNG" >



- [X] User can delete any contact from database .


<img src="https://user-images.githubusercontent.com/49953175/105623994-2f57c380-5e44-11eb-8e92-6faf6340c7ea.PNG" >


- [X] user can Search contact by email (default 10) or can be any value 


<img src="https://user-images.githubusercontent.com/49953175/105624015-48607480-5e44-11eb-95b8-84aa51fa8e25.PNG" >

- [X] User can serach all contact .

<img src="https://user-images.githubusercontent.com/49953175/105624031-6af28d80-5e44-11eb-9f88-bee2cb0ec1d5.PNG" >




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
  

<img src="https://user-images.githubusercontent.com/49953175/105624972-e0159100-5e4b-11eb-9820-ea8442effcc7.gif" >


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
#add contact 
   
localhost/add_contact

#user need to enter data in json in postman as given features 

   ```
   
```
#update contact 

http://localhost:5001/update_contact 

# user need to enter data in json in postman as given features 

```

```
#Delete contact 

http://localhost:5001/delete_contact

#user need to enter data in json in postman as given features 


```

```
#Get all contact 

http://localhost:5001/all_contact

#user need to enter data in json in postman as given features



```

```
search contact 

http://localhost:5001/search_contact

#user need to enter data in json in postman as given features


```



## Contact


Created by Abhishek pratap singh

[<img src="https://cdns.iconmonstr.com/wp-content/assets/preview/2012/240/iconmonstr-linkedin-3.png" width="42" height="42">](https://www.linkedin.com/in/abhishek-pratap-singh-44a96816b/)

[<img src="https://9to5google.com/wp-content/uploads/sites/4/2016/08/gmail-logo.png?w=1280" width="42" height="42">](abhisheklumiamicro@gmail.com)


## License

This package is distributed under the `MIT license`.
