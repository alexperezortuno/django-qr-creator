=====
Django QR Code
=====

Is a package

Quick start
-----------

1. Add "django_qr_code" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_qr_code',
    ]

2. Include the django_qr_code URLconf in your project urls.py like this::

    path('image/', include('django_qr_code.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/image/data/qr.png to participate in the django_qr_code.