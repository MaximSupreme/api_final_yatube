# YAtube_API social nework



## DESCRIPTION:

- _This projects is a social network, for people who want to create posts, comment others posts, subscribe to other user profiles and view their activities._
- _This project also uses ***JWT authentication*** for providing better experience and secure interaction with API._



## LOCAL DEPLOYATION:

**To deploy this project on your computer:**
- _Clone this repository to your ***working directory***._
- _Install requirements through pip:_
```bash
pip install -r requirements.txt
```
- _Apply migrations:_
```bash
python(3) manage.py migrate
```
- _Run server:_
```bash
python(3) manage.py runserver
```



## API request examples:

- _To fetch list of posts - `GET /api/v1/posts/`._
- _To fetch list of comments - `GET /api//v1/posts/{post_id}/comments/`._
- _To fetch list of all groups - `GET /api/v1/groups/`._
- _To fetch, (put, patch, delete) certain post - `GET /api/v1/posts/{post_id}/`._
- _To fetch (put, patch, delete) certain comment - `GET /api/v1/posts/{post_id}/comments/{comment_id}/`._
- _To fetch (put, patch, delete) certain group - `GET /api/v1/groups/{group_id}/`._
- _To fetch all subscriptions of the user made a request - `GET /api/v1/follow/`._
- _To subscribe to a certain user: `POST /api/v1/follow/` with body `{'following': 'username'}`_



## CREATORS:

***Maksim Chernikov a.k.a. MaximSupreme***
_email - chernikovmaks2002@gmail.com_
