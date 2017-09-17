# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 17:01:55 2014

@author: RuudSalym
"""
import json
import urllib
import webbrowser

class Exchange():
    def __init__(self,name,url):
        self.name = name
        self.url = url
    def openurl(self):
        webpage = webbrowser.open(self.url)

class Web_api(Exchange):
  def __init__(self,name,url):
      Exchange.__init__(self, name, url)
      self.data = None
  def openapi(self):
#grabs json data from site
    link = urllib.urlopen(self.url);
    self.data = json.loads(link.read())
    
