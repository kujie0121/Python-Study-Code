#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Htmldata = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">
<script src="/static/js/libs/modernizr.js"></script>
<link href="/static/stylesheets/style.css" rel="stylesheet" type="text/css" title="default" />
<link href="/static/stylesheets/mq.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty" />

<!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.css" rel="stylesheet" type="text/css" media="screen" />
<![endif]-->

<link rel="icon" type="image/x-icon" href="/static/favicon.ico">
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">
<link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">
<link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">

<title>无标题文档</title>
</head>
<section class="main-content with-right-sidebar" role="main">
  <header class="article-header">
    <h3>from the Python Events Calendar</h3>
  </header>
  <div class="most-recent-events">
    <div class="shrubbery">
      <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
      <p class="give-me-more"><a href="?page=2" title="More Events">More</a></p>
      <ul class="list-recent-events menu">
        <li>
          <h3 class="event-title"><a href="/events/python-events/360/">PyCon Namibia 2016</a></h3>
          <p>
            <time datetime="2016-01-25T00:00:00+00:00">25 Jan. &ndash; 30 Jan.<span class="say-no-more">2016</span></time>
            <span class="event-location">University of Namibia, Windhoek, Namibia</span></p>
        </li>
        <li>
          <h3 class="event-title"><a href="/events/python-events/359/">FOSDEM 2016</a></h3>
          <p>
            <time datetime="2016-01-30T00:00:00+00:00">30 Jan. &ndash; 01 Feb.<span class="say-no-more">2016</span></time>
            <span class="event-location">ULB Campus Solbosch, Brussels, Belgium</span></p>
        </li>
        <li>
          <h3 class="event-title"><a href="/events/python-events/380/">Swiss Python Summit 2016</a></h3>
          <p>
            <time datetime="2016-02-05T00:00:00+00:00">05 Feb. &ndash; 06 Feb.<span class="say-no-more">2016</span></time>
            <span class="event-location">HSR University of Applied Sciences, Rapperswil, Switzerland</span></p>
        </li>
        <li>
          <h3 class="event-title"><a href="/events/python-events/358/">PyCaribbean Conference 2016</a></h3>
          <p>
            <time datetime="2016-02-20T00:00:00+00:00">20 Feb. &ndash; 22 Feb.<span class="say-no-more">2016</span></time>
            <span class="event-location">Santo Domingo, Dominican Republic</span></p>
        </li>
        <li>
          <h3 class="event-title"><a href="/events/python-events/384/">PyCon SK 2016</a></h3>
          <p>
            <time datetime="2016-03-11T00:00:00+00:00">11 March &ndash; 14 March<span class="say-no-more">2016</span></time>
            <span class="event-location">Faculty of Informatics and Information Technologies STU, Bratislava, Ilkovičova,  842 16 Bratislava 4,  Slovak Republic</span></p>
        </li>
        <li>
          <h3 class="event-title"><a href="/events/python-events/369/">PythonCamp Cologne 2016</a></h3>
          <p>
            <time datetime="2016-04-02T00:00:00+00:00">02 April &ndash; 04 April<span class="say-no-more">2016</span></time>
            <span class="event-location">GFU Cyrus AG, Am Grauen Stein 27, 51105 Köln, Germany</span></p>
        </li>
      </ul>
    </div>
    <h3 class="widget-title just-missed">You just missed...</h3>
    <ul class="list-recent-events menu">
      <li>
        <h3 class="event-title"><a href="/events/python-events/367/">SciPy India 2015</a></h3>
        <p>
          <time datetime="2015-12-14T00:00:00+00:00">14 Dec. &ndash; 17 Dec.<span class="say-no-more">2015</span></time>
          <span class="event-location">LCH 102, IIT Bombay, Powai, Mumbai, India</span></p>
      </li>
      <li>
        <h3 class="event-title"><a href="/events/python-events/340/">PyCon CZ 2015</a></h3>
        <p>
          <time datetime="2015-11-14T00:00:00+00:00">14 Nov. &ndash; 16 Nov.<span class="say-no-more">2015</span></time>
          <span class="event-location">VUT FIT, Building D,  Božetěchova 1/2,  612 66 Brno,  Czech Republic</span></p>
      </li>
    </ul>
  </div>
</section>

<body>
</body>
</html>
'''


from html.parser import HTMLParser
from html.entities import name2codepoint

Stag = []
Satt = {}
events = []

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):  #attrs是含有tuple对象的列表
        Stag.append(tag)
        Satt[tag] = attrs
        if len(Stag) > 2:
            if Stag[0] in Satt:
                Satt.pop(Stag[0])
            Stag.pop(0)

        # print('<%s>' % tag)

    def handle_endtag(self, tag):
        if len(Stag) > 1:
            if Stag[1] == tag:
                if Stag[1] in Satt:
                    Satt.pop(Stag[1])
                Stag[1] = ' '

        # print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        pass
        # print('<%s/>' % tag)

    def handle_data(self, data):
        if len(Stag) > 1:
            if Stag[0] == 'h3' and Stag[1] == 'a' and ('class', 'event-title') in Satt[Stag[0]]:
                events.append([data.strip()])
            if Stag[0] == 'p' and Stag[1] == 'time':
                events[len(events)-1].append(data.strip())
            if Stag[1] == 'span' and ('class', 'event-location') in Satt[Stag[1]]:
                events[len(events)-1].append(data.strip())

        # print(data)

    def handle_comment(self, data):
        pass
        # print('<!--', data, '-->')

    def handle_entityref(self, name):
        pass
        # print('&%s;' % name)

    def handle_charref(self, name):
        pass
        # print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed(Htmldata)

n = 0
print('----重要事件----', len(events), '件')
while n < len(events):
    print(events[n])
    n = n + 1


