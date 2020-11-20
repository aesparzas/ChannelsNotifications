# Channels Notifications

This project is intented to be a quick example to set up django channels and to test its capabilities

## How it works

This project consists on an index page and a notifications model registered in the admin panel.
Every time an admin logged in the admin panel creates a notification, a bootstrap toast will be 
shown in the index page (no login required).
The notifications appear in the dropdown (limited to 8, ordered from newer to older) accesed via
the badge in the navbar. If a notification is clicked in there, its read status is set to `True` and
the page is reloaded. You can notice read notifications by its background color being white
(unread are yellow.) 

## Deployment

This project is intended only for development and showing purposes and it works with the Channels 
ASGI development server. Steps to set it up are shown next.

#### Prepare a virtual enviroment
`mkdir tmp`

`python -m venv tmp/venv`

`. tmp/venv/bin/activate`

`pip install -r etc/requirements.txt`

#### Run server

`cd src/`

`python manage.py runserver`

#### visit pages

to visit the index page and see the toasts

`127.0.0.1:8000`

to visit the admin panel and create notifications

`127.0.0.1:8000/admin`

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django Channels](https://channels.readthedocs.io/en/latest/) - Django tool to handle WebSockets, Chat protocol, IoT Protocol, etc.
* [jQuery](https://jquery.com/) - Javascript library that makes HTML document traversal and manipulation, event handling, animation, and Ajax much simpler.
* [Bootstrap](https://getbootstrap.com/) - Popular library for styling with js, HTML and CSS.

## Authors

* **Adolfo Esparza** - *Initial work* - [aesparzas](https://github.com/aesparzas)

## License

This project has no license yet
