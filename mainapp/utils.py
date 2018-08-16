import re
from urllib.parse import urlparse

def url_to_link_html(match):
    '''
    Convert the given url to HTML anchor
    '''
    url = match.group(0)
    
    if len(url) > 50:
        o = urlparse(url)
        return '<a href="{}">Link to {}</a>'.format(url, o.netloc)
    else:
        return url
    
def convert_urls_to_links(txt):
    '''
    Convert all the long URLs to html links in the given txt
    '''
    re.sub(r'(https?://[^ ]+)', url_to_link_html, txt)
