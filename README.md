shlong-django
===

This is a django-itized version of shlong. Because, I'm a little bored tonight.

You can deploy this on to [Heroku](http://heroku.com) pretty easily. 

Just do the following commands

    $ git clone https://github.com/micahwalter/shlong.git  ( or your own fork )
    $ git checkout shlong-django ( this branch )
    $ cd shlong ( or whever you put it )
    $ heroku create
    $ git push heroku shlong-django:master ( heroku needs it to be on the master branch )
    $ heroku run python manage.py syncdb ( follow the instructions to set up an account )
    $ heroku open
    
You should now have shlong-django up and running on Heroku. Yay! This means you are using a free single dyno Heroku app, with a dev Postgres DB. This sort of sucks because your app will idle while not in use and means your short urls might take time to redirect. You can try setting up [Pingdom](https://www.pingdom.com/) to keep you app alive if you like.

Once you have shlong-django up and running follow Heroku's [documentation](https://devcenter.heroku.com/articles/custom-domains) to set up your short-url to point at it.
