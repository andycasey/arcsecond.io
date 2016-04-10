![alt tag](http://www.arcsecond.io/static/arcsecond/img/favicon-96.png)

arcsecond.io
============

Arcsecond.io aims at integrating all sources of astronomical data and information
into a unified scheme using modern web techniques.

**This is big. Really. If you jump on board, this can be huge!**

If you don't see how big it could be, imagine a world where every _resource_ (the
word is key) has a unique, simple, stateless URL. Yes. It means every object, every planet,
every lightcurve, telegram, FITS file has a simple, unique URL which returns
well-formated fully standard JSON/XML output.

It's a kind of a super mega SIMBAD or NED services with modern tools and interfaces.
And not limited to any type of data. Allowing you to concentrate on stuff that matter:
the data. And not its formatting.

Imagine furthermore that **your own personal resources**: night log, observing runs, reduced data
are accessible the same way, through usual individual and group permissions that you personally
control.

Imagine even furthermore that **community-curated informations** is also accessible that way! This
is what has been started with observing sites (see below). Imagine now this list constantly updated, and enhanced by
informations about domes and telescopes, and further more... instruments and detectors.
All accessible freely, always the same way. A kind of scientific data-based wikipedia!

This would allow us to build a bazillion of new services and (web) apps. This is the future of
arcsecond.io.

arcsecond.io is intended to full embrace the RESTful principles (that is, the
modern way in the web to decouple data from its consumption). I know, there is also
the VO. But... Oh well.

arcsecond.io has been first developed by [onekiloparsec](https://twitter.com/onekiloparsec) as
a new backend for a new version of his OSX/iOS app [iObserve](http://onekiloparsec/apps).

arcsecond.io has 2 feet: *api* and *www*
------------------------------------

**api.arcsecond.io** is for the data part: the REST service. To every resource, there is an URL. This
is clearly the first and main part to develop first. It is already well underway, as you can
[see for yourself](http://api.arcsecond.io).

**www.arcsecond.io** is the web/front-end part. It is a first example of consumption of the *api* part.
Other services can use *api.arcsecond.io* and ignore *www.arcsecond.io* at all. But it can nonetheless
be a very good start at creating more services that could be useful to the whole community.

Two pages exemplifies this right now already:
- See http://www.arcsecond.io/observingsites for a community-curated list of existing Observing Sites around the world!
- And http://www.arcsecond.io/archives (in beta), for a live stream of data from the VLT poured into the ESO archive.


arcsecond.io is built with Python
---------------------------------

Isn't it cool? Astronomers love python. So all the *api* part is written with **Django** and pure pythonic code.
The RESTful part uses the famous Django REST Framework, making it easy to create new models and seeing them
as REST resources. For the scientific part, it uses the excellent **AstroPy** among other excellent
libraries.

The *www* part is build with Google's **AngularJS** (v1), with Twitter Bootstrap framework (v3).


arcsecond.io is hosted on Heroku
--------------------------------

Arcsecond.io is hosted on the great [PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service):
[Heroku.com](http://heroku.com). As for now, I (onekiloparsec) am taking care of it (and pay for it...). But as the project hopefully grows,
other developers will be added to the Heroku dashboard.

In the current setup, arcsecond.io is costing roughly 30US$ a month. You can
already help arcsecond.io by using [Patreon](https://www.patreon.com/onekiloparsec?ty=h)!
That would help quite a bunch, thanks.

The code has two main branches: *staging*, which is automatically deployed to [http://arcsecond-staging.heroku.com]().
And *master*, which is automatically deployed to [http://arcsecond.io]()!

One can use the great Heroku [Review Apps](https://devcenter.heroku.com/articles/github-integration-review-apps) feature
to make an temporary app based on GitHub Pull requests! Very useful before merging.


arcsecond.io needs you!
=============

You know some Python? Great! That's all you need to help, really. Ok, almost. But this README is here to help,
or simply write me an email [cedric@arcsecond.io](mailto:cedric@arcsecond.io).

arcsecond.io backend is made with Django. Hence I use [PyCharm](https://www.jetbrains.com/pycharm/download/)
as an IDE, but feel free to choose the one you prefer.

Requirements
------

- Python 2 (I know, we must migrate to Python 3...)
- virtualenvs (```pip install virtualenv```)
- PostgreSQL [Mac App](http://postgresapp.com)
- [Bower](http://bower.io) (```npm install -g bower```)

Optionally, you can use the excellent [Paw.app](https://luckymarmot.com/paw) on Mac, to test HTTP and REST requests.
If you prefer working on the browser for that, [Postman](https://www.getpostman.com) is a very
popular Chrome extension.


Initial Setup
-------------

- Fork the project on GitHub
- ```$ createdb arcsecond```
- ```$ git clone https://github.com/<username>/arcsecond.io.git```
- ```$ cd arcsecond.io```
- ```$ git checkout staging```
- create a ```.env``` file containing:
```
SECRET_KEY='<create your own secret key>'
DATABASE_URL='postgres://localhost:5432/arcsecond'
DJANGO_SETTINGS_MODULE=project.settings.dev
WEB_CONCURRENCY = 3
```
You can create secret keys [here](http://www.miniwebtool.com/django-secret-key-generator/)

- ```$ mkvirtualenv -p /usr/bin/<your version of python> arcsecond```
- ```(arcsecond)$ pip install -r requirements.txt```
- ```(arcsecond)$ python manage.py migrate --noinput```
- ```(arcsecond)$ python manage.py bower install```
- ```(arcsecond)$ python manage.py collectstatic --noinput```
- ```(arcsecond)$ python manage.py runserver```

and that's it! You have a own local server of arcsecond.io. If you want to load some observatories:

- ```(arcsecond)$ python manage.py loaddata project/arcsecond/fixtures/*_all.json```

To test your local server, you can use: ```http://api.lvh.me:8000``` for the APIs part.


Django
-------

*Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.*
You can [get started](https://www.djangoproject.com/start/) or [read the docs](https://docs.djangoproject.com/en/1.9/)

For wonderful and up-to-date video tutorials about Django, check out
[this page](https://opbeat.com/events/djangocon-eu-2016) from OpBeats


Structure
---------

The arcsecond.io project is structured the following way:

- **arcsecond.io** (root of django project)
  - **project** (project itself)
    - **arcsecond** (arcsecond django 'app')
      - **connectors** (contains all connectors to SIMBAD, NED, ADS, ATel... good to start here!)
      - **fixtures** (contains initial data to be loaded onto project if necessary)
      - **migrations** (contains automatically-generated database migration files, don't touch)
      - **models** (contains all model classes! objects, observing sites...)
      - **serializers** (contains all serializers of model classes that allow to easily make REST stuff!)
      - **templatetags** (django-specific place for utilities used in django HTML templates)
      - **unittests** (self-explanatory...)
      - **views** (all the views, most of them associated with model serializers for REST)
      - \_\_init\_\_.py
      - admin.py (django admin entry point)
      - apps.py (django-specific app config)
      - hosts.py (djangohosts module allowing to split between *api* and *www*)
      - middleware.py (small WIP middleware – unimportant)
      - mixins.py (small WIP mixins to easily log every REST request – unimportant)
      - signals.py (WIP signals to associate actions based on specific events)
      - urls_api.py (the URL routes for the host *api.arcsecond.io*!)
      - url_www.py (the URL routes for the host *www.arcsecond.io*!)
    - **settings** (project settings)
    - **static**
      - **arcsecond** (some static stuff for the website)
      - **webapp** (the AngularJS webb app!)
      - favicon.ico
    - **templates** (django templates, some of them unused)
    - \_\_init\_\_.py
    - urls.py (the django-specific URL routes entry-point)
    - utils.py (some utilities for the project)
    - wsgi.py (used by the server)
  - **requirements** (python requirements)
  - **scripts** (project-specific custom python scripts)
  - .buildpacks (heroku-specific buildpacks to build the arcsecond app)
  - .env (the env file, cool isn't it?)
  - .gitignore (usual stuff)
  - API.paw (a Paw.app file to test arcsecond.io APIs)
  - circle.yml (a YAML file used by the continuous-deployement CircleCI service)
  - manage.py (django-specific python script to handle all django actions: runserver, etc...)
  - package.json (used by Heroku)
  - Procfile (used by Heroku)
  - README.md (this file)
  - requirements.txt (python requirements, forwarding to specific requirements in requirements directory)


Django REST Framework
---------------------

To make RESTful services, one uses here the excellent [Django REST Framework](http://www.django-rest-framework.org).
In its simplest form, the DRF allows you to create a model class, declare a serializer for it (which is
basically just a class) and associate a URL route to it, and that's it, you get a REST entry-point.


Angular JS
----------

Soon...



Update Channels
==========

The usual ones:
- http://onekilopars.ec/blog
- https://www.facebook.com/arcsecond.io
- https://twitter.com/arcsecond_io
- [cedric@arcsecond.io](mailto:cedric@arcsecond.io)



