#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers

from annoying.decorators import render_to
from pygeoip import GeoIP

@render_to('site/index.html')
def home(request):
    geoip = GeoIP(settings.GEOIP_PATH)
    client_ip = request.META['REMOTE_ADDR']
    country = geoip.country_name_by_name(client_ip)
    record = geoip.record_by_name(client_ip)
    city = record['city']
    lat = record['latitude']
    lon = record['longitude']
    return {
        'country': country,
        'city': city,
        'lat': lat,
        'lon': lon,
    }