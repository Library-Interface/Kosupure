# Kosupure
コスプレ: Kosupure is a Social Media Platform for Cosplay

CustomUser made with the help of tutorial from Django: https://learndjango.com/tutorials/django-custom-user-model

using pillow


Levels of access: 
Visitor: Can only view images safe for kids and event schedule
Logged-in User: Ability to comment on posts, like posts, commit to events and participate in live-chatroom
Creator: Ability to Post, Host LiveChat and Create Events
Adult: See the posts with violence, halloween-themed, etc not deemed safe for kids 



Fun commands to remember when uploading django to heroku
heroku config:set DISABLE_COLLECTSTATIC=1
git push heroku main
heroku config:unset DISABLE_COLLECTSTATIC
heroku run python manage.py collectstatic