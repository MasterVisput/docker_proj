import requests
import inspect
import logging

logger = logging.getLogger('log.'+__name__)


class JsonPlaceholderApiClient:

    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host


    def get_resourses(self, path="/", params=None):
        url = self.host+path
        return self._s.get(url=url, params=params)

    def post_data(self, path='/', params=None, data=None, headers=None):
        url = self.host+path
        return self._s.post(url=url, params=params, data=data,headers=headers)