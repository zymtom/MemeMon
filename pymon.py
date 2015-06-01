#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PyMon
Author: -zYMTOM'
"""
import re
import requests
from bs4 import BeautifulSoup
import time
import threading
class pastebinLinks():
	def __init__():
		r = requests.post("http://pastebin.com/archive")
		var = BeautifulSoup(r.text.encode('utf-8')).find("div", {"id": "content_left"})
		regex = re.compile('<a href="\/([A-Za-z]{1,9})">(.*?)<\/a>')
		reg = regex.findall(str(var))
		for captures in reg:
				if in_array(links, captures[0]) == False:
						links.insert(len(links)+1, [captures[0], captures[1]])
						print("Pastebin ID " + captures[0] + " Found")
		time.sleep(30)
		super(pastebinLinks).__init__()
	

class getPastebinPastes():
	def __init__():
		self.f = open('pastes.txt', 'a')
		newlinks = []
		for x in links:
			if x not in crawled:
				getlink = pastebinGet(x)
				if getlink:
					crawled.insert(len(crawled)+1, x)
					match = False
					for reg in regexes:
						if reg.match(getlink):
							match = True
					for reg in regbl:
						if reg.match(getlink):
							match = False
					if match:
						print"Found interesting paste!"
						self.f.write("PasteID: " + crawled + " \n" + getlink + "\n==================================\n")
			time.sleep(5)
		super(getPastebinPastes).__init__()
					
	def pastebinGet(link):
		r = requests.post("http://pastebin.com/raw.php?i="+link)
		if not '<div class="content_title">This paste has been removed!</div>' in r.text:
			return r.text

def in_array(array, compare0):
        exist = False
        for i in range(0, len(array)):
                if compare0[0] in array[i][0]:
                        exist = True
                        break
        return exist
def MonMain():
	print "Starting"
	pastebin_thread = threading.Thread(target=pastebinLinks)
	pastebin_threadpaste = threading.Thread(target=getPastebinPastes)
	for thread in (pastebin_thread, pastebin_threadpaste):
		
		thread.daemon = True
		thread.start()
if __name__ == "__main__":
	global crawled
	global regbl
	global regexes
	global links
	links = []
	crawled = []
	regexes = [
		re.compile(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}', re.I),
		re.compile(r'\d{3}-?\d{2}-?\d{4}'),
		re.compile(r'[^<A-F\d/]([A-F\d]{32})[^A-F\d]', re.I),
		re.compile(r'FBI\s*Friday', re.I),  # will need to work on this to not match CSS
		re.compile(r'(lulzsec|antisec)', re.I),
		re.compile(r'enable\s+secret', re.I),
		re.compile(r'enable\s+password', re.I),
		re.compile(r'\W(AIza.{35})'),
		re.compile(r'<dionaea\.capture>', re.I),
		re.compile(r'BEGIN PGP PRIVATE', re.I),
		re.compile(r'BEGIN RSA PRIVATE', re.I),
		re.compile(r'((customers?|email|users?|members?|acc(?:oun)?ts?)([-_|/\s]?(address|name|id[^")a-zA-Z0-9_]|[-_:|/\\])))', re.I),
		re.compile(r'((\W?pass(wor)?d|hash)[\s|:])', re.I),
		re.compile(r'((\btarget|\bsite)\s*?:?\s*?(([a-z][\w-]+:/{1,3})?([-\w\s_/]+\.)*[\w=/?%]+))', re.I),  # very basic URL check - may be improved later
		re.compile(r'(my\s?sql[^i_\.]|sql\s*server)', re.I),
		re.compile(r'((host|target)[-_\s]+ip:)', re.I),
		re.compile(r'(data[-_\s]*base|\Wdb)', re.I),  # added the non-word char before db.. we'll see if that helps
		re.compile(r'(table\s*?:)', re.I),
		re.compile(r'((available|current)\s*(databases?|dbs?)\W)', re.I),
		re.compile(r'(hacked\s*by)', re.I),
		re.compile(r'dox', re.I)
	]
	regbl = [
		re.compile(r'(select\s+.*?from|join|declare\s+.*?\s+as\s+|update.*?set|insert.*?into)', re.I),  # SQL
        re.compile(r'(define\(.*?\)|require_once\(.*?\))', re.I),  # PHP
        re.compile(r'(function.*?\(.*?\))', re.I),
        re.compile(r'(Configuration(\.Factory|\s*file))', re.I),
        re.compile(r'((border|background)-color)', re.I),  # Basic CSS (Will need to be improved)
        re.compile(r'(Traceback \(most recent call last\))', re.I),
        re.compile(r'(java\.(util|lang|io))', re.I),
        re.compile(r'(sqlserver\.jdbc)', re.I),
        re.compile(r'faf\.fa\.proxies', re.I),
        re.compile(r'Technic Launcher is starting', re.I),
        re.compile(r'OTL logfile created on', re.I),
        re.compile(r'RO Game Client crashed!', re.I),
        re.compile(r'Selecting PSO2 Directory', re.I),
        re.compile(r'TDSS Rootkit', re.I),
        re.compile(r'SysInfoCrashReporterKey', re.I),
        re.compile(r'Current OS Full name: ', re.I),
        re.compile(r'Multi Theft Auto: ', re.I),
        re.compile(r'Initializing cgroup subsys cpuset', re.I),
        re.compile(r'Init vk network', re.I),
        re.compile(r'MediaTomb UPnP Server', re.I)
    ]
	
	MonMain()
	
	
	

