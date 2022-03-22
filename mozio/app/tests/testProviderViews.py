from rest_framework.test import APITestCase, APIClient

from ..models import Provider


class TestProviderEndpoints(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_can_create_a_new_provider(self):
        data = {
            "name": "Provider 1",
            "email": "mudashiruagm@gmail.com",
            "phoneNumber": "+233241992669",
            "language": "English",
            "currency": "USD"
        }

        response = self.client.post('/api/provider',data=data)

        assert response.status_code == 201

        # check database entry for this
        provider = Provider.objects.filter(name=data['name']).first()

        assert provider.name == data['name']

    def test_can_get_all_providers(self):

        response = self.client.get('/api/provider')

        assert response.status_code == 200

        assert type(response.json()) == list

    def test_can_update_provider(self):
        data = {
            "name": "Provider 1",
            "email": "mudashiruagm@gmail.com",
            "phoneNumber": "+233241992669",
            "language": "English",
            "currency": "USD"
        }

        create_response = self.client.post('/api/provider', data=data)

        provider_id = create_response.json()['id']

        new_data = {
            "name": "Provider 1 updated"
        }

        update_response = self.client.patch('/api/provider/'+str(provider_id), data=new_data)

        assert update_response.status_code == 200

        assert update_response.json()['name'] == new_data['name']

    def test_can_delete_provider(self):
        data = {
            "name": "delete",
            "email": "mudashiruagm@gmail.com",
            "phoneNumber": "+233241992669",
            "language": "English",
            "currency": "USD"
        }

        create_response = self.client.post('/api/provider', data=data)

        delete_response = self.client.delete('/api/provider/'  + str(create_response.json()['id']))

        assert delete_response.status_code == 204

        # make sure provider does not exist
        provider = Provider.objects.filter(pk=create_response.json()['id']).first()

        assert provider is None

