from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import *
from ..simbad import *
from ..models import Messages

@api_view(['GET'])
def astronomical_object(request, name="."):
    obj, created = AstronomicalObject.objects.get_or_create(name=name)

    if created or obj.coordinates is None:
        coords, messages = get_SIMBAD_coordinates(name)

        if coords is None:
            obj.messages = messages
        else:
            obj.coordinates = coords
            obj.save()

        if created or obj.aliases.all().count() == 0:
            aliases = get_SIMBAD_aliases(name)
            if len(aliases) > 0:
                obj.aliases = aliases
                obj.save()

        if created or obj.object_types.all().count() == 0:
            otypes = get_SIMBAD_object_types(name)
            if len(otypes) > 0:
                obj.object_types = otypes
                obj.save()

        if created or obj.fluxes.all().count() == 0 or len([f for f in obj.fluxes.all() if not f.is_valid()]) > 0:
            fluxes = get_SIMBAD_fluxes(name)
            if len(fluxes) > 0:
                obj.fluxes = fluxes
                obj.save()

    if hasattr(obj, "messages") is False:
        obj.messages = Messages(http_status_code=200)

    serializer = AstronomicalObjectSerializer(obj)
    return Response(serializer.data)


@api_view(['GET'])
def astronomical_coordinates(request, name="."):
    coords = get_SIMBAD_coordinates(name)

    if coords is None:
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    serializer = AstronomicalCoordinatesSerializer(coords)
    return Response(serializer.data)


@api_view(['GET'])
def astronomical_object_aliases(request, name="."):
    aliases = get_SIMBAD_aliases(name)

    if aliases is None:
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    serializer = AliasSerializer(aliases, many=True)
    return Response(serializer.data)
