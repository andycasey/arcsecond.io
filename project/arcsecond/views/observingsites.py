from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins

class ObservingSiteListAPIView(mixins.RequestLogViewMixin, generics.ListCreateAPIView):
    queryset = models.ObservingSite.objects.all().order_by('name')
    serializer_class = serializers.ObservingSiteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = "name"

    def get_queryset(self):
        queryset = models.ObservingSite.objects.all().order_by('name')
        continent = self.request.query_params.get('continent', None)
        if continent is not None:
            queryset = queryset.filter(continent=continent)
        return queryset

    def post(self, request, *args, **kwargs):
        result = super(ObservingSiteListAPIView, self).post(request, *args, **kwargs)

        obssite = None
        try:
            obssite = self.get_queryset().get(id=result.data.get("id"))
        except:
            pass

        if result.status_code == 201 and obssite is not None:
            activity = models.ObservingSiteActivity.objects.create(user=request.user)
            activity.action = models.ObservingSiteActivity.ACTION_SITE_CREATION
            activity.observing_site = obssite
            activity.method = models.ObservingSiteActivity.METHOD_WEB
            activity.save()

        return result

class ObservingSiteActivityListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.ObservingSiteActivity.objects.all().order_by('-date')
    serializer_class = serializers.ObservingSiteActivitySerializer

class ObservingSiteDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveUpdateAPIView):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def put(self, request, *args, **kwargs):
        obssite = None
        old_values = {}
        try:
            obssite = self.get_object()
        except:
            pass
        else:
            for key in request.data.keys():
                old_values[key] = getattr(obssite, key)

        result = super(ObservingSiteDetailAPIView, self).put(request, args, kwargs)

        if result.status_code == 200 and obssite is not None:
            for key in request.data.keys():
                activity = models.ObservingSiteActivity.objects.create(user=request.user)
                activity.action = models.ObservingSiteActivity.ACTION_PROPERTY_CHANGE
                activity.observing_site = obssite
                activity.property_name = key
                activity.old_value = old_values.get(key, "?")
                activity.new_value = request.data.get(key, "?")
                activity.method = models.ObservingSiteActivity.METHOD_WEB
                activity.save()

        return result


class ObservingSiteNamedDetailAPIView(ObservingSiteDetailAPIView):
    lookup_field = "name"

    def get_object(self):
        name = self.kwargs.get("name", None)
        queryset = self.get_queryset()

        try:
            obj = queryset.get(name=name)
        except ObjectDoesNotExist:
            try:
                obj = queryset.get(short_name=name)
            except ObjectDoesNotExist:
                try:
                    obj = queryset.get(alternate_name_1=name)
                except ObjectDoesNotExist:
                    try:
                        obj = queryset.get(alternate_name_2=name)
                    except ObjectDoesNotExist:
                        raise Http404()

        return obj


