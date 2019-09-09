from django.test import TestCase

from django.conf import settings

from . import models

# Test Helpers

def create_test_convention(name='Test Convention', site_id=settings.SITE_ID):
    convention = models.Convention.objects.create(
        name=name,
        site_id=site_id,
        active=True,
        contact_email='drykath@motorcityfurrycon.org',
    )
    return convention

# Model Tests

class ConventionModelTest(TestCase):
    def test_convention_model_str(self):
        convention = create_test_convention()
        self.assertEqual(str(convention), convention.name)

    def test_convention_manager_current(self):
        previous_year = create_test_convention('Last Year', site_id=None)
        current = create_test_convention('Current Year')
        self.assertEqual(models.Convention.objects.current(), current)


