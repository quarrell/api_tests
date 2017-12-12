import pytest
import requests
from jsonschema import validate
from data import TestData


def test_get_all_posts():
    r = requests.get(TestData.POSTS)
    assert r.status_code == requests.codes.ok
    validate(r.json(), TestData.JSON_ALL_POSTS)


@pytest.mark.parametrize("post_id, user_id", [(1, 1), (7, 1), (14, 2), (42, 5)])
def test_get_posts_by_post_id(post_id, user_id):
    payload = {'id': post_id}
    r = requests.get(TestData.POSTS, params=payload)
    data = TestData.get_raw_json(r)
    assert r.status_code == requests.codes.ok
    assert data['userId'] == user_id


def test_negative_scenario():
    r = requests.get(TestData.POSTS + "/101")
    assert r.status_code == requests.codes.not_found