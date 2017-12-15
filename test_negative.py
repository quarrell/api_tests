import requests
from dict_data import DictData

'''Should return a list of the available domains
 for a given bilingual language dataset.'''


def test_empty_results():

    # Results field in response should be empty

    r = requests.get(DictData.DOMAIN + "/nso/es", headers=DictData.HEADER)
    req = r.json()
    assert not bool(req['results'])
    assert r.status_code == requests.codes.ok


def test_same_domains():

    # Should return 400 with appropriate error message

    r = requests.get(DictData.DOMAIN + "/en/en", headers=DictData.HEADER)
    error = r.text
    assert "source language and target language can not be same" in error
    assert r.status_code == requests.codes.bad_request


def test_unknown_domains():

    # Should return 404 with appropriate error message

    r = requests.get(DictData.DOMAIN + "/en/asd", headers=DictData.HEADER)
    error = r.text
    assert "target_lang is not in" in error
    assert r.status_code == requests.codes.not_found


def test_invalid_app_id():

    # Should return 403

    r = requests.get(DictData.DOMAIN + "/en/es", headers=DictData.INVALID_HEADER)
    assert r.status_code == requests.codes.forbidden
