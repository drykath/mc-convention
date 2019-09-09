from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

def get_convention_model():
    """
    Return the Convention model for this project, as defined by the
    CONVENTION_MODEL setting. This is much similar to get_user_model().
    """
    try:
        return apps.get_model(getattr(settings, 'CONVENTION_MODEL', 'convention.Convention'), require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("CONVENTION_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "CONVENTION_MODEL refers to model '%s' that has not been installed" % settings.CONVENTION_MODEL
        )
