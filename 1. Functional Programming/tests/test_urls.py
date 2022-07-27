from urls import domain_of_url, shrunk_url, url_list


class TestUrls:
    def test_shrunk_url(self):
        url = 'http://example.com'
        result = shrunk_url(url)
        assert result == 'example.com'

    def test_domain_of_url(self):
        url = 'http://one.example.com/help/me'
        result = domain_of_url(url)
        assert result == 'example.com'

    def test_url_list(self):
        url = 'http(s)://subdomain.example.com/path1/path2/'
        result = url_list(url)
        assert result == [
            'http(s)://',
            'subdomain',
            'example',
            'com',
            'path1',
            'path2',
        ]
