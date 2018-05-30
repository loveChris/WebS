# coding:utf-8

import urllib2,re

def download(url,user_agent="Mozilla/5.0", num_retries=2):
    print "Downloading:",url
    headers = {'User-agent':user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print "Download error:",e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries-1)
    return html

def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall(r'(?<=href=").*?(?!png)(?=")', sitemap)
    for link in links:
        download(link)


if __name__ == '__main__':
    url = "http://www.eastmoney.com/"
    # with open(r"E:\log.txt",'w') as f:
    #     f.write(download(url))
    crawl_sitemap(url)






















