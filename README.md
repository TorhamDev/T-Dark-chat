<p align="center">
<img src='./cover.png' style="border: white;border-radius: 2pc;" alt='Dark chat'/>
</p>

# T-Dark-chat

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
<br>

> An anonymous messenger without the need for any registration information


## What is Dark Chat?
DarkChat is an anonymous messenger with one-time accounts that you do not need any registration information to enter. 
<br>

In Dark Chat, you have usernames that are created randomly by the system itself and in 25 characters.
When you register in Dark Chat, you can specify the lifespan of your account from **1** to **24** hours. After this hour, your account will be lost.
<br>
You can change your username at any time during these hours, and if you are talking to someone, your conversation will be lost because your username will change and that person will not have your new username. 
<br>

> Think of something like an **email** to understand more
<br>

### How to run this project?
```bash
git clone https://github.com/TorhamDev/T-Dark-chat.git

cd T-Dark-chat/

pip3 install -r requirement.txt

cd DarkChat/ 

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver

```

# Api endpoint
```text
1. api/v1/register/get-valid-code/ 
    [get valid code] (Method : GET)

2. api/v1/register/set-user-password/ 
    [set password] (Method : POST)

3. api/v1/messages/send 
    [send message] (Method : POST)

4. api/v1/messages/get-last-message 
    [get last message] (Method : POST)

5. api/v1/users/upadte-user-code 
    [upadte user code] (Method : POST)

6. api/v1/users/upadte-user-token 
    [upadte user token] (Method : POST)

7. api/v1/users/check-user-alive 
    [check that the user is alive] (Method : POST)

```