from py_bark_client import Bark, Sound
import os
import requests
import pytest


class TestBarkClient:

    def setup_class(self) -> None:
        self.key = os.environ.get('BARK_CLIENT_KEY')
        self.server = os.environ.get('BARK_SERVER')
        if not self.key:
            raise Exception('cannot found key')
        if not self.server:
            self.server = 'https://api.day.app'
        self.client = Bark(server=self.server, keys=[self.key])

    def test_push(self):
        content = 'HelloWorld'
        sound = Sound.GLASS
        res = self.client.push(content=content, sound=sound)
        assert 0 == len(res)

    def test_get_request_url(self):
        url, params = self.client.get_request_url(
            content='Hello',
            key=self.key,
            group='test'
        )
        resp = requests.get(url, params=params)
        assert resp.url == '{}/{}/Hello?group=test'.format(self.server, self.key)


if __name__ == '__main__':
    pytest.main()
