#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
from datetime import datetime, timedelta

class WeatherSaxHandler(object):

	def __init__(self):
		self._weather = {}

	def start_element(self, name, attrs):

		if name == 'yweather:location':
			self._weather['city'] = attrs['city']
			self._weather['country'] = attrs['country']
		elif name == 'yweather:condition':
			self._weather['condition'] = attrs
		elif name == 'yweather:forecast':
			self._weather[attrs['date']] = attrs

	def end_element(self, name):
		pass

	def char_data(self, text):
		pass

def parse_weather(data):

	handler = WeatherSaxHandler()
	parser = ParserCreate()
	parser.StartElementHandler = handler.start_element
	parser.EndElementHandler = handler.end_element
	parser.CharacterDataHandler = handler.char_data
	parser.Parse(data)

	Dweather = {}
	Dweather['today'] = {}
	Dweather['tomorrow'] = {}

	condition = handler._weather['condition']['date'].split(',')[1].strip().split(' ')
	today = condition[0] + ' ' + condition[1] + ' ' + condition[2]
	tomorrow = datetime.strptime(today,'%d %b %Y') + timedelta(days=1)

	Dweather['city'] = handler._weather['city']
	Dweather['country'] = handler._weather['country']
	Dweather['today']['text'] = handler._weather[today]['text']
	Dweather['today']['low'] = handler._weather[today]['low']
	Dweather['today']['high'] = handler._weather[today]['high']

	Dweather['tomorrow']['text'] = handler._weather[tomorrow.strftime('%d %b %Y')]['text']
	Dweather['tomorrow']['low'] = handler._weather[tomorrow.strftime('%d %b %Y')]['low']
	Dweather['tomorrow']['high'] = handler._weather[tomorrow.strftime('%d %b %Y')]['high']

	return Dweather



data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''

if __name__ == '__main__':
	print(parse_weather(data))



