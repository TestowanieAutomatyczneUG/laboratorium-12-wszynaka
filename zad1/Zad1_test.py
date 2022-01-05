import json
import unittest
from unittest.mock import *
import requests
from assertpy import assert_that
from Zad1 import RandomUser


class TestRandomUser(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_getuser_not_none(self):
        assert_that(self.temp.getRandomUser()).is_not_none()

    def test_getuser_data(self):
        assert_that(self.temp.getRandomUser()).is_instance_of(dict)

    def test_name(self):
        assert_that(self.temp.getRandomUser().get('name')).is_length(3)

    def test_location(self):
        assert_that(self.temp.getRandomUser()).contains('location')

    def test_get_location_data(self):
        assert_that(self.temp.get_location()).is_instance_of(dict)

    def test_location2(self):
        assert_that(self.temp.get_location()).is_length(7)

    def test_location3(self):
        assert_that(self.temp.get_location()).contains_key('country', 'postcode', 'city', 'state', 'street',
                                                           'coordinates', 'timezone')


class Mock_res:
    def __init__(self, a):
        self.text = a


class MockPerson(unittest.TestCase):
    def setUp(self):
        def sideEffect(arg1):
            n = {"results":[{"gender":"male","name":{"title":"Mr","first":"Miro","last":"Tikkanen"},"location":{"street":{"number":6792,"name":"Rautatienkatu"},"city":"Pyhäranta","state":"Northern Ostrobothnia","country":"Finland","postcode":78659,"coordinates":{"latitude":"-11.9923","longitude":"-122.8878"},"timezone":{"offset":"-1:00","description":"Azores, Cape Verde Islands"}},"email":"miro.tikkanen@example.com","login":{"uuid":"9e6aab6c-1c58-490d-aefc-5f070179879c","username":"whiterabbit404","password":"toolman","salt":"eXuHJaZj","md5":"ad209e397f9778994868cfee32cf41a6","sha1":"b2f7dd6d28d858700f59a0a874954192287e8460","sha256":"e1e1cec14d758973e98b71b7a8a932feca92b3ece1b66fd4e7f478af4cf60884"},"dob":{"date":"1997-05-19T08:05:48.468Z","age":25},"registered":{"date":"2002-10-16T08:15:17.492Z","age":20},"phone":"02-145-546","cell":"048-590-43-20","id":{"name":"HETU","value":"NaNNA535undefined"},"picture":{"large":"https://randomuser.me/api/portraits/men/49.jpg","medium":"https://randomuser.me/api/portraits/med/men/49.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/49.jpg"},"nat":"FI"}],"info":{"seed":"762e58d883c3efa8","results":1,"page":1,"version":"1.3"}}
            return Mock_res(json.dumps(n))

        requests.get = Mock(name='get')
        requests.get.side_effect = sideEffect
        API = requests.get('https://example.com')
        self.j = json.loads(API.text)

    def test_gender(self):
        assert_that({self.j['results'][0]['gender']}).is_subset_of({'female', 'male'})

    def test_name(self):
        assert_that(self.j['results'][0]['name']).contains_key('title', 'first', 'last')

    def test_location(self):
        assert_that(self.j['results'][0]['location']).contains_key('country', 'postcode', 'city', 'state', 'street',
                                                           'coordinates', 'timezone')

    def test_login(self):
        assert_that(self.j['results'][0]['login']).contains_key('uuid', 'username', 'password', 'salt', 'md5', 'sha1',
                                                                'sha256')
