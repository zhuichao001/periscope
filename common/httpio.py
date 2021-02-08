#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import urllib
import urllib.request


class httpio:
    def __init__(self, host):
        self.host = host

    def __URL(self, uri):
        return 'http://%s/%s' % (self.host, uri) 

    def get(self, uri):
        url = self.__URL(uri)
        response = urllib.request.urlopen(url)
        return response.read()

    def post(self, uri, data):
        url = self.__URL(uri)
        request = urllib.request.Request(url, data)
        request.get_method = lambda:'POST'
        response = urllib2.urlopen(request)
        return response.read()

    def put(self, uri, data):
        url = self.__URL(uri)
        print("url:::", url)
        print("data:::", data)
        request = urllib.request.Request(url, bytes(data, encoding="utf8"))
        request.add_header('Content-Type', 'application/json')
        request.get_method = lambda:'PUT'
        response = urllib.request.urlopen(request)
        return response.read()

    def delete(self, uri, data):
        url = self.__URL(uri)
        request = urllib.request.Request(url, data)
        request.get_method = lambda:'DELETE'
        response = urllib.request.urlopen(request)
        return response.read()
