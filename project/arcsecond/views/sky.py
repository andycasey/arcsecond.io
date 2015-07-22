
from rest_framework import generics

from project.arcsecond import connectors
from project.arcsecond import serializers
from project.arcsecond import models
from project.arcsecond import mixins


class AstronomicalObjectAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.AstronomicalObject.objects.all()
    serializer_class = serializers.AstronomicalObjectSerializer

    def get_object(self):
        name = self.kwargs.get("name", None)
        obj, created = models.AstronomicalObject.objects.get_or_create(name=name)

        if created or obj.coordinates is None:
            coords = connectors.get_SIMBAD_coordinates(name=name)
            if coords is not None:
                obj.coordinates = coords
                obj.save()

        if created or obj.aliases.all().count() == 0:
            aliases = connectors.get_SIMBAD_aliases(name)
            if len(aliases) > 0:
                obj.aliases = aliases
                obj.save()

        if created or obj.object_types.all().count() == 0:
            otypes = connectors.get_SIMBAD_object_types(name)
            if len(otypes) > 0:
                obj.object_types = otypes
                obj.save()

        if created or obj.fluxes.all().count() == 0 or len([f for f in obj.fluxes.all() if not f.is_valid()]) > 0:
            fluxes = connectors.get_SIMBAD_fluxes(name)
            if len(fluxes) > 0:
                obj.fluxes = fluxes
                obj.save()

        return obj


class ExoplanetDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveAPIView):
    queryset = models.Exoplanet.objects.all()
    serializer_class = serializers.ExoplanetSerializer
    lookup_field = "name"

    def get_object(self):
        name = self.kwargs.get("name", None)
        exoplanet, created = models.Exoplanet.objects.get_or_create(name=name)

        if exoplanet is None:
            exoplanet = connectors.get_EXOPLANET_EU_object(name)

        exoplanet.save()
        return exoplanet

class ExoplanetListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.Exoplanet.objects.all()
    serializer_class = serializers.ExoplanetSerializer
