mc-convention
=============

The mc-convention app doesn't provide much functionality in itself, just
a Convention object model object and a few additions around that.

The object just provides the convention name, year, and a few other bits
of data that represents the convention/year. That object is used as a
parent-level object that other MCFC apps link to, so if you use any of
the `mc-` apps you'll either want this or will want to mirror its
interface.

If you already have your own model representing the convention/year, you
can have the apps link to that by configuring `CONVENTION_MODEL` in your
settings, pointing it at your own model (in the same way you might
override the `AUTH_USER_MODEL` model.) Just make sure it has a custom
manager that provides a `current()` method that gets the right object
based on site/fixed name/whatever.

Do that before running your migrations.

Even if you do, you may want to keep this app in place as it provides
the `get_convention_model()` function that does that look-up in the
first place, and the `mc-` apps assume that there will be an app named
`convention` in your `INSTALLED_APPS` where it can find it.

This wants the `django.contrib.sites` framework in place, so...

    INSTALLED_APPS = [
        ....
        'django.contrib.sites',
        'convention',
        ....
    ]

Enjoy!
