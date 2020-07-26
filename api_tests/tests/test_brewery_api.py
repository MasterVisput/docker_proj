import pytest


class TestBreweryApi:

    def test_status_code(self, client_brewery):
        res = client_brewery.get_brewery_list()
        assert res.status_code == 200, 'Сервис не доступен'

    @pytest.mark.parametrize('by_name', ['cooper', 'Co'])
    def test_get_list_by_id(self, client_brewery, by_name):
        res = client_brewery.vr(client_brewery.get_brewery_list(path='/breweries', params={'by_name': by_name}),
                                [200, 201])
        assert res.json() != []

    @pytest.mark.parametrize('by_city', ['Cooper Landing', 'Minneapolis', 'Glens Falls'])
    def test_get_list_by_city(self, client_brewery, by_city):
        res = client_brewery.vr(client_brewery.get_brewery_list(path='/breweries', params={'by_city': by_city}),
                                [200, 201])
        assert by_city in res.json()[0]['city'], 'Некорректные данные, город'

    @pytest.mark.parametrize('by_state', ['Alaska', 'Georgia', 'Minnesota'])
    def test_get_list_by_state(self, client_brewery, by_state):
        res = client_brewery.vr(client_brewery.get_brewery_list(path='/breweries', params={'by_state': by_state}),
                                [200, 201])
        assert by_state in res.json()[0]['state'], 'Некорректные данные, штат'

    @pytest.mark.parametrize('by_type',
                             ['micro', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor'])
    def test_get_list_by_type(self, client_brewery, by_type):
        res = client_brewery.vr(client_brewery.get_brewery_list(path='/breweries', params={'by_type': by_type}),
                                [200, 201])
        assert by_type in res.json()[0]['brewery_type'], 'Некорректные данные, тип'
