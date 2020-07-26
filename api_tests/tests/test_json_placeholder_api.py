from random import randint

import cerberus
import pytest


class TestJsonApi():

    def test_get_posts(self, client_json):
        num = randint(1, 100)
        res = client_json.get_resourses(path=f'/posts/{num}')
        schema = {
            "id": {"type": "number"},
            "userId": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(res.json(), schema)

    @pytest.mark.parametrize('input_id, output_id',
                             [(23, '23'),
                              (12, '12'),
                              (6, '6')])
    @pytest.mark.parametrize('input_title, output_title',
                             [('title', 'title'),
                              ('Cool', 'Cool'),
                              ('Mool', 'Mool'),
                              ('Diz', 'Diz')])
    def test_api_post_request(self, client_json, input_id, output_id, input_title, output_title):
        res = client_json.post_data(
            path="/posts",
            data={'title': input_title, 'body': 'Some body about body', 'userId': input_id})
        res_json = res.json()
        assert res_json['title'] == output_title
        assert res_json['body'] == 'Some body about body'
        assert res_json['userId'] == output_id

    @pytest.mark.parametrize('userId', [1, 2, 3, 4, 5, 6, 7])
    def test_get_user_by_id(self, client_json, userId):
        res = client_json.get_resourses(path='/posts',
                                        params={'userId': userId})
        assert res.json() != [], 'Сервис прислал пустой ответ'

    @pytest.mark.parametrize('userId', [13, 'r', 34, 'y'])
    def test_get_user_by_id(self, client_json, userId):
        res = client_json.get_resourses(path='/posts',
                                        params={'userId': userId})
        assert res.json() == [], 'Ошибка фильтра'

    @pytest.mark.parametrize('postId', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test_get_comments_by_post_id(self, client_json, postId):
        res = client_json.get_resourses(path='/comments',
                                        params={'postId': postId})
        assert res.json() != [], 'Ошибка фильтра'
