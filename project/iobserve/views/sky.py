from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from project.iobserve import connectors
from project.iobserve import serializers
from project.iobserve import models


@api_view(['GET'])
def astronomical_object(request, name="."):
    obj, created = models.AstronomicalObject.objects.get_or_create(name=name)

    if created or obj.coordinates is None:
        coords, messages = connectors.get_SIMBAD_coordinates(name)

        if coords is None:
            obj.messages = messages
        else:
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

    if hasattr(obj, "messages") is False:
        obj.messages = models.Messages(http_status_code=200)

    serializer = serializers.AstronomicalObjectSerializer(obj)
    return Response(serializer.data)


@api_view(['GET'])
def astronomical_coordinates(request, name="."):
    coords = connectors.get_SIMBAD_coordinates(name)

    if coords is None:
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    serializer = serializers.AstronomicalCoordinatesSerializer(coords)
    return Response(serializer.data)


@api_view(['GET'])
def astronomical_object_aliases(request, name="."):
    aliases = connectors.get_SIMBAD_aliases(name)

    if aliases is None:
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    serializer = serializers.AliasSerializer(aliases, many=True)
    return Response(serializer.data)
