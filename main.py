#!/usr/bin/env python
import sys
import urllib2
from bs4 import BeautifulSoup

def main():
    html = urllib2.urlopen('http://www.mixcloud-downloader.com/dl/mixcloud/cremeo/dj-tlr-the-complexity-of-man-punkhardcore-clsxxx')
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
    print(soup.title.string)
    return 0

if __name__ == '__main__':
    sys.exit(main())
