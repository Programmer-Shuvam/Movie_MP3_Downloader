#!d:\sahil\project\web_scraping\hyperscraper\hyper\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'scrapyd-client==1.2.0a1','console_scripts','scrapyd-client'
__requires__ = 'scrapyd-client==1.2.0a1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('scrapyd-client==1.2.0a1', 'console_scripts', 'scrapyd-client')()
    )
