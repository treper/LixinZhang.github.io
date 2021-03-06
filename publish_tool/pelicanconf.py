#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'LixinZhang'
SITENAME = u'Backyard of LixinZhang'
SITEURL = 'http://lixinzhang.github.io'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
#MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight, linenums=True)', 'extra']


# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('weibo', 'http://weibo.com/zhanglixin5566/'),
        ('Facebook', 'https://www.facebook.com/zhanglixin.peter'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './elegant'
GITHUB_URL = 'https://github.com/LixinZhang'
DISQUS_SITENAME = 'zhanglixinseu'
OUTPUT_PATH = './'

LANDING_PAGE_ABOUT = {'title':'Backyard of LixinZhang', 'details':'''
<p>I am a R&D Software Engineer in Tencent WeChat Group(WXG, Beijing).</p>
<p>Before I joined Tencent, I graduated from Yahoo!(Beijing R&D) on 2015-3-31. And it is my honor to used to be a Yahoo.</p>
<p>
I graduated from Beihang University(BUAA, Beijing) with master degree in Computer Science, 
and got bachelor degree in Software Engineering from Southeast University(SEU, Nanjing).
</p>
<p>
I mostly work in Python, C++/C on Mac OS, UNIX-style OS and I have rich intern experience 
in many companies on my school-days, like Yahoo(one year), Alibaba(one year) 
and Innovation Works(two month). 
Now I am focusing on Computational Advertising and Data Mining which are now very pupular in industry and academia. 
I am also familiar with distributed system, web development and network programming.
</p>
<p>
My hobbies are Winning Eleven computer game and music of Linkin Park, Taylor Swift, Avril Lavigne, Taiwan Mayday and 逃跑计划. 
</p>

 '''}

PROJECTS = [
     {'name':'Gmail',
     'url':'mailto:zhanglixinseu@gmail.com',
     'description': 'Feel free to reach me via Email'},
     {'name': 'Github',
     'url': 'https://github.com/LixinZhang',
     'description': '一些代码，放在上面托管'},
     {'name':'Facebook',
     'url':'https://www.facebook.com/zhanglixin.peter',
     'description': '联系在外国朋友的'},
     {'name':'Linkedin',
     'url':'http://www.linkedin.com/pub/lixin-zhang/72/bb/66a',
     'description': '欢迎互相关注'},
     {'name': '新浪微博',
     'url': 'http://weibo.com/zhanglixin5566',
     'description': '扯淡用的'},
     {'name':'知乎',
     'url':'http://www.zhihu.com/people/zhanglixin',
     'description': '学习各种知识'},
     {'name':'博客园',
     'url':'http://www.cnblogs.com/coser',
     'description': '之前的博客，很多是本科时候记录的东西'}
     ]
