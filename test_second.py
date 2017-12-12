import requests
from data import TestData


def test_put_comment():
    payload = TestData.get_json_payload(TestData.COMMENTS_PAYLOAD)
    r = requests.put(TestData.COMMENTS, data=payload, headers=TestData.HEADER)
    r_source = TestData.get_raw_json(r)
    assert r.status_code == requests.codes.ok
    assert TestData.COMMENTS_PAYLOAD == r_source


def test_post_album():
    payload = TestData.get_json_payload(TestData.ALBUM_PAYLOAD)
    r = requests.post(TestData.ALBUMS, data=payload, headers=TestData.HEADER)
    r_source = TestData.get_raw_json(r)
    assert r.status_code == requests.codes.created
    assert TestData.ALBUM_PAYLOAD == r_source


def test_patch_todos():
    payload = TestData.get_json_payload(TestData.TODOS_PAYLOAD)
    r = requests.patch(TestData.TODOS, data=payload, headers=TestData.HEADER)
    assert r.status_code == requests.codes.ok


def test_delete_user():
    r = requests.delete(TestData.USERS)
    assert r.status_code == requests.codes.ok
