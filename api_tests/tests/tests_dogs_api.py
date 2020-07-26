class TestDogsApi:

    def test_get_list_all_breeds(self, client_dogs):
        res = client_dogs.vr(client_dogs.get_list_all_breeds(), [200, 201])
        assert res.json()['status'] == "success", 'Некорректный статус ответа'

    def test_get_random_image(self, client_dogs):
        res = client_dogs.vr(client_dogs.get_random_image(), [200, 201])
        data_format = res.json()['message'][-4:]
        assert data_format == '.jpg', 'Неверный формат изображения'

    def test_get_mult_random_image(self, client_dogs):
        num = client_dogs.num
        res = client_dogs.vr(client_dogs.get_mult_random_image(), [200, 201])
        assert len(res.json()['message']) == num, 'Возвращается неправильное колличество ссылок'

    def test_get_list_by_breeds(self, client_with_params):
        breed = client_with_params.breed
        res = client_with_params.vr(client_with_params.get_list_by_breed(), [200, 201])
        assert breed in res.json()['message'][0], 'В ответе некорректные ссылки, не та порода'

    def test_get_list_by_sub_breeds(self, client_with_params_sub_breeds):
        res = client_with_params_sub_breeds.vr(client_with_params_sub_breeds.get_list_by_sub_breed(), [200, 201])
        assert len(res.json()['message'][0]) > 0, 'Сервис вернул пустой список'
