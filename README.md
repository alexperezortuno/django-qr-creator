=====
Django QR Code
=====

Is a package

Quick start
-----------

1. Add "django_qr_code" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_qr_creator',
    ]

2. Include the django_qr_code URLconf in your project urls.py like this::

    path('image/', include('django_qr_creator.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/image/data/qr.png to participate in the django_qr_code.

Tested in python 3.6 with Django 2.0

Example of use in a template
----------------------------
```html
{% load django_qr_creator %}

```
Load this tags in you html template

```html
{% qr url='google.com' %}
```

For QR URL

```html
{% qr tel='+56948161822' %}
```

For QR Tel

```html
{% qr email='test@test.test' %}
```

For QR Mail

```html
{% qr location='40.7127753,-74.0059728' altitude='15' %}
```

For QR Location

```html
{% qr sms='+56948161822' message='this is a test' %}
```

For QR SMS
