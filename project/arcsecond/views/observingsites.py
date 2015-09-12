
import json

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from django.shortcuts import render
from django.views.generic.edit import CreateView

from project.arcsecond import models
from project.arcsecond import serializers
from project.arcsecond import mixins
from project.arcsecond import forms

class ObservingSiteListAPIView(mixins.RequestLogViewMixin, generics.ListAPIView):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer
    lookup_field = "name"

    def get_queryset(self):
        queryset = models.ObservingSite.objects.all()
        continent = self.request.query_params.get('continent', None)
        if continent is not None:
            queryset = queryset.filter(continent=continent)
        return queryset


class ObservingSiteNamedDetailAPIView(mixins.RequestLogViewMixin, generics.RetrieveUpdateAPIView):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer
    lookup_field = "name"


class ObservingSiteViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # observingsite = models.ObservingSite.get(name=original_name)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response({
            'status': 'Bad request',
            'message': 'ObservingSite could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #
    #     if serializer.is_valid():
    #         Account.objects.create_user(**serializer.validated_data)
    #
    #         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    #
    #     return Response({
    #         'status': 'Bad request',
    #         'message': 'Account could not be created with received data.'
    #     }, status=status.HTTP_400_BAD_REQUEST)


class ObservingSiteUpdateView(generics.views.APIView):
    # def get(self, request, name, format=None):
    #     observingsite = models.ObservingSite.objects.get(name=name)
    #     serialized = serializers.ObservingSiteSerializer(observingsite, context={'request': request})
    #     return Response(serialized.data)

    def post(self, request, format=None):
        data = json.loads(request.body)

        original_name = data.get('original_name', None)
        name = data.get('name', None)
        long_name = data.get('long_name', None)
        IAUCode = data.get('IAUCode', None)

        observingsite = models.ObservingSite.get(name=original_name)
        serialized = serializers.ObservingSiteSerializer(observingsite)

        return Response(serialized.data)

        # account = authenticate(email=email, password=password)
        #
        # if account is not None:
        #     if account.is_active:
        #         login(request, account)
        #
        #         serialized = AccountSerializer(account)
        #
        #         return Response(serialized.data)
        #     else:
        #         return Response({
        #             'status': 'Unauthorized',
        #             'message': 'This account has been disabled.'
        #         }, status=status.HTTP_401_UNAUTHORIZED)
        # else:
        #     return Response({
        #         'status': 'Unauthorized',
        #         'message': 'Username/password combination invalid.'
        #     }, status=status.HTTP_401_UNAUTHORIZED)


def observingsite_update(request):
    queryset = models.ObservingSite.objects.all()
    serializer_class = serializers.ObservingSiteSerializer
    lookup_field = "name"


# class ObservingSiteDetailAPIView(mixins.RequestLogViewMixin, generics.UpdateAPIView):
#     queryset = models.ObservingSite.objects.all()
#     serializer_class = serializers.ObservingSiteSerializer
#     lookup_field = "pk"


def observingsites(request, path=None):
    african_sites = models.ObservingSite.objects.filter(continent='Africa')
    antarctica_sites = models.ObservingSite.objects.filter(continent='Antarctica')
    asian_sites = models.ObservingSite.objects.filter(continent='Asia')
    european_sites = models.ObservingSite.objects.filter(continent='Europe')
    north_american_sites = models.ObservingSite.objects.filter(continent='North America')
    oceania_sites = models.ObservingSite.objects.filter(continent='Oceania')
    south_american_sites = models.ObservingSite.objects.filter(continent='South America')

    return render(request, 'arcsecond/observingsites.html', {'african_sites': african_sites.count,
                                                              'antarctica_sites': antarctica_sites.count,
                                                              'asian_sites': asian_sites.count,
                                                              'european_sites': european_sites.count,
                                                              'north_american_sites': north_american_sites.count,
                                                              'oceania_sites': oceania_sites.count,
                                                              'south_american_sites': south_american_sites.count})


