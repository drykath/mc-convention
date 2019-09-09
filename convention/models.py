from django.db import models

from django.contrib.sites.models import Site

class ConventionManager(models.Manager):
    """Support filtering by current site's active convention"""

    def current(self):
        """Attempt to determine current convention, return None if unable."""
        site = Site.objects.get_current()
        # Should return one and only one, bail out if not
        convention = self.filter(site=site).first()
        return convention


class Convention(models.Model):
    """
    An umbrella model that apps can link to for separating data by
    convention/year, and linking to related data in other apps.
    """

    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    site = models.OneToOneField(Site, null=True, blank=True, on_delete=models.PROTECT)
    start_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=False)
    contact_email = models.EmailField()

    objects = ConventionManager()

    def __str__(self):
        return self.name
