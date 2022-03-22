from rest_framework.test import APITestCase, APIClient

from ..models import Polygon, Provider
from django.contrib.gis.geos import Point


class PolygonTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_can_create_a_polygon(self):
        data = {
            "name": "Provider 1",
            "email": "mudashiruagm@gmail.com",
            "phoneNumber": "+233241992669",
            "language": "English",
            "currency": "USD"
        }

        provider_create_response = self.client.post('/api/provider', data=data)

        data = {
            "name": "Polygon1",
            "price": 5000,
            "latitude": 32.12,
            "longitude": -1.23,
            "provider": provider_create_response.json()['id']
        }

        response = self.client.post('/api/polygon', data=data)

        assert response.status_code == 201

    def test_can_get_all_polygons(self):
        response = self.client.get('/api/polygon')

        assert response.status_code == 200

        assert type(response.json()) == list

    def test_can_delete_a_polygon(self):
        provider = Provider.objects.create(name='ghaff', email='email@gmail.com', phoneNumber='023424',
                                           language='English', currency='GHS')
        polygon = Polygon.objects.create(name='test', price=200, geo=Point(-12, 23), provider=provider)

        response = self.client.delete('/api/polygon/' + str(polygon.id))

        assert response.status_code == 204
