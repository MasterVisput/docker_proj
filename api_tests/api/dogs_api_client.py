import inspect
import logging

import requests

logger = logging.getLogger('log.' + __name__)


class DogsApiClient:
    _s = requests.session()
    host = None

    def __init__(self, host, num=None, breed=None, sub_breed=None):
        self.host = host
        self.num = num
        self.breed = breed
        self.sub_breed = sub_breed

    def verify_response(self, res: requests.Response, ok_status=200) -> requests.Response:
        func = inspect.stack()[1][3]
        if isinstance(ok_status, int):
            ok_status = ok_status
        elif res.status_code not in ok_status:
            raise ValueError(
                f'Verified response: function {func} failed: '
                f'server responsed {res.status_code} '
                f'witch data: {res.content}'
            )
        else:
            logger.info(
                f'Verified response: function {func} code {res.status_code}'
            )
        return res

    vr = verify_response

    def get_list_all_breeds(self):
        return self._s.get(self.host + '/breeds/list/all')

    def get_random_image(self):
        return self._s.get(self.host + '/breeds/image/random')

    def get_mult_random_image(self):
        return self._s.get(self.host + f'/breeds/image/random/{self.num}')

    def get_list_by_breed(self):
        return self._s.get(self.host + f'/breed/{self.breed}/images')

    def get_list_by_sub_breed(self):
        return self._s.get(self.host + f'/breed/{self.sub_breed}/list')
