from django.contrib.sites.models import Site
new_site = Site.objects.create(name='ecliptis-dev', domain='localhost')
new_site.id = 1
new_site.save()