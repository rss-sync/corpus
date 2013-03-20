#!/usr/bin/env python3

import sys, os, urllib.request, re
from datetime import datetime

FS = re.compile(r'\s+')

with open('sources', 'r', encoding='utf-8') as f:
  for line in f:
    line = line.rstrip()
    name, url = FS.split(line)

    if not os.path.isdir(name): os.mkdir(name)

    print("%-16s" % name, end=''); sys.stdout.flush()
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (rss-sync corpus gatherer)'})) as source:
      destname = ("%s/%s.xml" % (name, datetime.utcnow().strftime('%Y%m%dT%H%M%S')))
      with open(destname, 'wb') as dest:
        feedsrc = source.read()
        dest.write(feedsrc)
        print("%d bytes" % len(feedsrc))
        dest.flush()

        
