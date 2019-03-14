#!/usr/bin/env python

__author__      = "Arnaud de Theux"
__web__         = "http://arnaud.detheux.org"
__twitter__     = "@AdeTheux"

"""This is a python script that runs as a plugin on top of our HipChat chat bot. It displays information regarding your Zendesk account. To make it run, just complete the Settings part and your branded spokes URL. Note that some code needs our chat bot to run, you will need to modify the code for it to run without our bot"""

import sys
import os
import httplib2
from urllib import urlopen
import urllib
from xml.dom.minidom import parseString
import re

###Settings. Replace with your own Zendesk credentials and URL. If you don't use the API token (baaad) just put your password
user           = 'YOUR_USER_EMAIL_ADDRESS/token'
password       = 'YOUR_TOKEN'
zendesk        = 'http://ACCOUNT.zendesk.com/' # the / at the end is important!



###Fetches unsolved tickets view and returns only number of tickets
class ZendeskBot(BotPlugin):
    @botcmd
    def zendesk(self, mess, args):
        self.send(mess.getFrom(), "/me is preparing the statistics... ", message_type=mess.getType())
        h= httplib2.Http(".cache")
        h.add_credentials(user, password)
        resp, xml_view_opened = h.request(zendesk+"rules/YOUR_VIEW_ID.xml", "GET", headers={'content-type' : 'application/xml'} )
        opened_tickets = re.search('<tickets.+?count="([0-9]+)"', xml_view_opened).groups() 
    
    
###Fetches satisfaction score of spoke
        good = 0
        bad  = 0
        data = urlopen("http://SPOKE1.zendesk.com/satisfaction.json").readlines()[0]
        good = data.count('1')
        bad  = data.count('0')
        
#Fetches satisfaction score of spoke
        good1 = 0
        bad1  = 0
        data = urlopen("http://SPOKE2.zendesk.com/satisfaction.json").readlines()[0]
        good1 = data.count('1')
        bad1  = data.count('0')
        
#Fetches satisfaction score of spoke
        good2 = 0
        bad2  = 0
        data = urlopen("http://SPOKE3.zendesk.com/satisfaction.json").readlines()[0]
        good2 = data.count('1')
        bad2  = data.count('0')
        
#Makes a sum of the satisfaction scores
        sum_good = good + good1 + good2
        sum_bad = bad + bad1 + bad2
        sum_total = sum_good + sum_bad
        
#Convert it to % in case there are not yet 100 ratings in Zendesk account
        sum_good_percentage = round(float(sum_good)/sum_total*100,0)
        sum_bad_percentage = round(float(sum_bad)/sum_bad*100,0)
        
        
        
###Fetches the tags file
        h= httplib2.Http(".cache")
        h.add_credentials(user, password)
        resp, content = h.request(zendesk+"tags.xml", "GET", headers={'content-type' : 'application/xml'} )
        
#Displays the top 10 tags (You need to replace [1] by [0] and increment accordingly below. I start from line 1 because I don't want the first tag to be displayed.
#1
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('name')[1].toxml()
        xmlDataName=xmlTag.replace('<name>','').replace('</name>','')
        
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('count')[1].toxml()
        xmlDataTag=xmlTag.replace('<count>','').replace('</count>','')
#2
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('name')[2].toxml()
        xmlDataName1=xmlTag.replace('<name>','').replace('</name>','')
        
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('count')[2].toxml()
        xmlDataTag1=xmlTag.replace('<count>','').replace('</count>','')
#3
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('name')[3].toxml()
        xmlDataName2=xmlTag.replace('<name>','').replace('</name>','')
        
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('count')[3].toxml()
        xmlDataTag2=xmlTag.replace('<count>','').replace('</count>','')
#4
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('name')[4].toxml()
        xmlDataName3=xmlTag.replace('<name>','').replace('</name>','')
        
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('count')[4].toxml()
        xmlDataTag3=xmlTag.replace('<count>','').replace('</count>','')
#5
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('name')[5].toxml()
        xmlDataName4=xmlTag.replace('<name>','').replace('</name>','')
        
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('count')[5].toxml()
        xmlDataTag4=xmlTag.replace('<count>','').replace('</count>','')
#6
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('name')[6].toxml()
        xmlDataName5=xmlTag.replace('<name>','').replace('</name>','')
        
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('count')[6].toxml()
        xmlDataTag5=xmlTag.replace('<count>','').replace('</count>','')
#7
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('name')[7].toxml()
        xmlDataName6=xmlTag.replace('<name>','').replace('</name>','')
        
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('count')[7].toxml()
        xmlDataTag6=xmlTag.replace('<count>','').replace('</count>','')
#8
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('name')[8].toxml()
        xmlDataName7=xmlTag.replace('<name>','').replace('</name>','')
        
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('count')[8].toxml()
        xmlDataTag7=xmlTag.replace('<count>','').replace('</count>','')
#9
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('name')[9].toxml()
        xmlDataName8=xmlTag.replace('<name>','').replace('</name>','')
        
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('count')[9].toxml()
        xmlDataTag8=xmlTag.replace('<count>','').replace('</count>','')
#10
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('name')[10].toxml()
        xmlDataName9=xmlTag.replace('<name>','').replace('</name>','')
        
        dom = parseString(content)
        xmlTag = dom.getElementsByTagName('count')[10].toxml()
        xmlDataTag9=xmlTag.replace('<count>','').replace('</count>','')



######### WORK IN PROGRESS #########
###Fetches top performer
#Displays the top performer by stripping of the <assignee-name> tags on latest tickets
#        h= httplib2.Http(".cache")
#        h.add_credentials(user, password)
#        resp, xml_view_top_perf = h.request(zendesk+"rules/YOUR_VIEW_ID.xml", "GET", headers={'content-type' : 'application/xml'} )
#
#        dom = parseString(xml_view_top_perf)
#        xmlTag = dom.getElementsByTagName('assignee-name')[0].toxml()
#        xmlDataNameTopPerf=xmlTag.replace('<assignee-name type="">','').replace('</assignee-name>','')
######### WORK IN PROGRESS #########
        

        
###Display the ouput
        if sum_good_percentage >= 85:
            result='There is a %i%% satisfaction rate. Good job!\n' % sum_good_percentage
        else:
            result='There is a %i%% satisfaction rate. That\'s quite low, you should be ashamed!\n' % sum_good_percentage
        
        if opened_tickets > 1:
            result+='There is a total of %s unresolved requests at the moment. Chop chop, go solve them!\n' % opened_tickets
        else:
            result+='There is a total of %s unresolved request at the moment. Chop chop, go solve it!\n' % opened_tickets

        result+='These are the top 10 tags and their occurrences: '+xmlDataName+'('+xmlDataTag+') '+xmlDataName1+'('+xmlDataTag1+') '+xmlDataName2+'('+xmlDataTag2+') '+xmlDataName3+'('+xmlDataTag3+') '+xmlDataName4+'('+xmlDataTag4+') '+xmlDataName5+'('+xmlDataTag5+') '+xmlDataName6+'('+xmlDataTag6+') '+xmlDataName7+'('+xmlDataTag7+') '+xmlDataName8+'('+xmlDataTag8+') '+xmlDataName9+'('+xmlDataTag9+')\n'
        
#        result+='The top performer this week is %s. Give that man a raise!' % xmlDataNameTopPerf
        return result