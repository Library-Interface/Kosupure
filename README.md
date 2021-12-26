# Kosupure
コスプレ: Kosupure is a Social Media Platform for Cosplay
https://kosupure.herokuapp.com/

Levels of access: 
Visitor: Can only view images safe for kids and event schedule
Logged-in User: Ability to comment on posts, like posts, commit to events and participate in live-chatroom
Creator: Ability to Post, Host LiveChat and Create Events
Adult: See the posts with violence, halloween-themed, etc not deemed safe for kids 

![first](https://user-images.githubusercontent.com/65050037/147325806-83a1da4c-4a01-4e38-abb9-685e7261cbe3.JPG)
![first event](https://user-images.githubusercontent.com/65050037/147325810-0446b169-dee8-46b9-b06b-183f27c2cc18.JPG)
![first live](https://user-images.githubusercontent.com/65050037/147325812-306c2ebb-778a-46e8-81a4-dcafa5a25958.JPG)
![first calc](https://user-images.githubusercontent.com/65050037/147325816-4f9b78c3-433d-4e9d-854c-9c9102598679.JPG)


Fun commands to remember when uploading django to heroku
heroku config:set DISABLE_COLLECTSTATIC=1
git push heroku main
heroku config:unset DISABLE_COLLECTSTATIC
heroku run python manage.py collectstatic

CustomUser made with the help of tutorial from Django: https://learndjango.com/tutorials/django-custom-user-model
