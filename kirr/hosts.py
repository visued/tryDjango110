from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'kirr.hostconf.urls', name='wildcard'),
)
'''
from kirr.hostconf import urlsas redirect_urls
host_patterns = [
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'kirr.hostsconf.urls', name='wildcard'),
]
'''

