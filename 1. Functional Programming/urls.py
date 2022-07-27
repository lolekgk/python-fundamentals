from urllib.parse import urlparse

# EG. 1: shrunk_url("http://example.com")` => example.com
# EG. 2: domain_of_url("http://one.example.com/help/me") => example.com
# EG. 3: url_list('http(s)://subdomain.example.com/path1/path2/') => ['http(s)://', 'subdomain', 'example', 'com', 'path1', 'path2']
# (s) means it should work with both https and http protocols


def shrunk_url(url):
    # return url.split('/')[-1]
    return urlparse(url).netloc


def domain_of_url(url):
    netloc = urlparse(url).netloc.split('.')
    return '.'.join(netloc[1:])
    # return urlparse(url).hostname


def url_list(url):
    url_components = [i for i in url.replace('.', '/').split('/') if i]
    url_components[0] += '//'
    return url_components  # can also use urlsplit, but return will be different (not the same as required)


print(shrunk_url("http://example.com"))
print(domain_of_url("http://one.example.com/help/me"))
print(url_list('https://subdomain.example.com/path1/path2/'))
