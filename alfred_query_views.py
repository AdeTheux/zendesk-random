#!/usr/bin/env python

__author__      = "Arnaud de Theux"
__web__ 		= "http://arnaud.detheux.org"
__twitter__     = "@AdeTheux"
__version__		= "1.1"

"""Fetches the count of a Zendesk view and prints it. Used within Alfred App"""

import sys
import os
import json
import httplib2

h= httplib2.Http(".cache")
h.add_credentials('adetheux@zendesk.com/token', 'API_TOKEN')
resp, data_file = h.request('https://ACCOUNT.zendesk.com/api/v2/views/ID_OF_THE_VIEW/count.json', "GET", headers={'content-type' : 'application/json'} )

data = json.loads(data_file)
print (data)['view_count']['value']