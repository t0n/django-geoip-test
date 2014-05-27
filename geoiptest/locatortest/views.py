#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers

from annoying.decorators import render_to
from django.contrib.gis.geoip import GeoIP

@render_to('site/index.html')
def home(request):
    geoip = GeoIP()
    client_ip = get_client_ip(request)

    country_record = geoip.country(client_ip)
    if country_record:
        country = country_record['country_name']
    else:
        country = 'Not defined'

    city_record = geoip.city(client_ip)
    if city_record:
        city = city_record['city']
    else:
        city = 'Not defined'

    lat_lon_record = geoip.lat_lon(client_ip)
    if lat_lon_record:
        (lat, lon) = lat_lon_record
    else:
        (lat, lon) = (-1, -1)
    return {
        'client_ip': client_ip,
        'country': country,
        'city': city,
        'lat': lat,
        'lon': lon,
    }

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip