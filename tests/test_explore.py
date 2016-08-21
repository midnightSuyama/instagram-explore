import pytest
import six
import time
import instagram_explore as ie

def setup_function(function):
    time.sleep(1)

def test_user():
    user_name = 'instagram'
    res = ie.user(user_name)
    assert isinstance(res, tuple)
    assert isinstance(res.data, dict)
    assert isinstance(res.cursor, six.string_types)
    time.sleep(1)
    data, _ = ie.user(user_name, res.cursor)
    assert isinstance(data, dict)

def test_tag():
    tag_name = 'cat'
    res = ie.tag(tag_name)
    assert isinstance(res, tuple)
    assert isinstance(res.data, dict)
    assert isinstance(res.cursor, six.string_types)
    time.sleep(1)
    data, _ = ie.tag(tag_name, res.cursor)
    assert isinstance(data, dict)

def test_location():
    location_id = '7226110'
    res = ie.location(location_id)
    assert isinstance(res, tuple)
    assert isinstance(res.data, dict)
    assert isinstance(res.cursor, six.string_types)
    time.sleep(1)
    data, _ = ie.location(location_id, res.cursor)
    assert isinstance(data, dict)

def test_media():
    res = ie.media('BFRO_5WBQfc')
    assert isinstance(res, tuple)
    assert isinstance(res.data, dict)
    assert res.cursor is None
