from django.test import TestCase
from ..models.earth import ObservingSite

# Create your tests here.
class ObservingSiteModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_single_observing_site_creation(self):
        self.assertTrue(True)