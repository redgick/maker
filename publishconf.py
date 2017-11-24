#!/usr/bin/env python
# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://maker.redgick.com/'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = "feeds/%s.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

SOCIAL = (
    ('envelope', 'https://join.slack.com/t/laboitecc/shared_invite/enQtMjc3Mzg0NDc2MjQ1L'
     'TgzNmNhMjhjMDQ1MjAwMjM1NzNlNDk3ZDU1Yzk3MDE0M2RlMmNjMzczNTUyNDJlMmQ0MWY5YjIyZDdhNDM1MmU'),
    ('rss', SITEURL + '/feeds/all.atom.xml'),
    ('github', 'https://github.com/redgick'),
)
