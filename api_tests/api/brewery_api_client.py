import requests
import inspect
import logging

logger = logging.getLogger('log.'+__name__)


class BreweryApiClient:

    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host


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


    def get_brewery_list(self, path="/", params=None):
        url = self.host+path
        return self._s.get(url=url, params=params)