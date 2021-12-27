# Kosupure
コスプレ: Kosupure is a Social Media Platform for Cosplay
https://kosupure.herokuapp.com/


This is a kid-friendly app that is designed for cosplay enthusiasts. The main page is similar to instagram with posts that have like, comment and search capabilities. There is an event page with comment and attending functionality, and a chatroom which features live-streaming from the scheduled cosplayer. Finally, there is a ‘how much cosplay can i afford’ page.

Levels of access: 
Visitor: Can only view images safe for kids and event schedule
Logged-in User: Ability to comment on posts, like posts, commit to events and participate in live-chatroom
Creator: Ability to Post, Host LiveChat and Create Events
Adult: See the posts with violence, halloween-themed, etc not deemed safe for kids 

![home](https://user-images.githubusercontent.com/65050037/147497086-53051ed5-49b5-4920-8cc9-5fa3d33d4441.JPG)
![chat](https://user-images.githubusercontent.com/65050037/147497091-fcee4a64-9155-458b-9b99-79ff7752d89b.JPG)
![game](https://user-images.githubusercontent.com/65050037/147497100-f6e56947-63cf-4685-af42-782df5cd0086.JPG)
![events page](https://user-images.githubusercontent.com/65050037/147497105-ab2a0ebb-fe1e-4011-9e11-eb5de768129f.JPG)
![first calc](https://user-images.githubusercontent.com/65050037/147325816-4f9b78c3-433d-4e9d-854c-9c9102598679.JPG)


Fun commands to remember when uploading django to heroku
heroku config:set DISABLE_COLLECTSTATIC=1
git push heroku main
heroku config:unset DISABLE_COLLECTSTATIC
heroku run python manage.py collectstatic

CustomUser made with the help of tutorial from Django: https://learndjango.com/tutorials/django-custom-user-model
