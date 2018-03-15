from collections import namedtuple
import requests


InstagramExploreResponse = namedtuple('InstagramExploreResponse', 'data cursor')


def user(user_name, max_id=None):
    url = "https://www.instagram.com/%s/" % user_name
    payload = {'__a': '1'}
    if max_id is not None: payload['max_id'] = max_id
    
    try:
        res = requests.get(url, params=payload).json()
        body   = res['graphql']['user']
        cursor = res['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    except: raise
    
    return InstagramExploreResponse(data=body, cursor=cursor)


def user_images(user_name, max_id=None):
    try:
        body, cursor = user(user_name, max_id)
        images = [edge['node']['display_url'] for edge in body['edge_owner_to_timeline_media']['edges']]
    except: raise
    
    return InstagramExploreResponse(data=images, cursor=cursor)


def tag(tag_name, max_id=None):
    url = "https://www.instagram.com/explore/tags/%s/" % tag_name
    payload = {'__a': '1'}
    if max_id is not None: payload['max_id'] = max_id
    
    try:
        res = requests.get(url, params=payload).json()
        body   = res['graphql']['hashtag']
        cursor = res['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    except: raise
    
    return InstagramExploreResponse(data=body, cursor=cursor)


def tag_images(tag_name, max_id=None):
    try:
        body, cursor = tag(tag_name, max_id)
        images = [edge['node']['display_url'] for edge in body['edge_hashtag_to_media']['edges']]
    except: raise
    
    return InstagramExploreResponse(data=images, cursor=cursor)


def location(location_id, max_id=None):
    url = "https://www.instagram.com/explore/locations/%s/" % location_id
    payload = {'__a': '1'}
    if max_id is not None: payload['max_id'] = max_id
    
    try:
        res = requests.get(url, params=payload).json()
        body   = res['location']
        cursor = res['location']['media']['page_info']['end_cursor']
    except: raise
    
    return InstagramExploreResponse(data=body, cursor=cursor)


def location_images(location_id, max_id=None):
    try:
        body, cursor = location(location_id, max_id)
        images = [node['display_src'] for node in body['media']['nodes']]
    except: raise
    
    return InstagramExploreResponse(data=images, cursor=cursor)


def media(media_code):
    url = "https://www.instagram.com/p/%s/" % media_code
    payload = {'__a': '1'}
    
    try:
        res = requests.get(url, params=payload).json()
        body = res['graphql']['shortcode_media']
    except: raise

    return InstagramExploreResponse(data=body, cursor=None)


def media_image(media_code):
    try:
        body = media(media_code).data
        image = body['display_url']
    except: raise

    return InstagramExploreResponse(data=image, cursor=None)
