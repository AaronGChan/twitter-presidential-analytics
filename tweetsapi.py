from TwitterAPI import TwitterAPI
consumer_key ="kaoZGXeEh7DHFFH3ypEiacAxm"
consumer_secret = "SmCVt5nABxgxHGhLkqFT6VKR2wjWPgaKIUnwR3XFAJ0xjyKNfh"

access_token = "865793569-uib85OwIeAQHXYkzp6rejrlU0y8z1xB4fNq6ykkV"
access_token_secret = "T8PYu6aNmLT8BOwGfDi7VFRaAK2JiiOnC9hZxQGudQnIq"
SEARCH_TERM = 'Biden'
PRODUCT = 'fullarchive'
LABEL = 'your label'
api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
#api = TwitterAPI('consumer key', 'consumer secret', 'access token key', 'access token secret')
r = api.request('tweets/search/%s/:%s' % (PRODUCT, LABEL), {'query':SEARCH_TERM})
for item in r:
    if 'text' in item:
        print(item['text'])
        print(item['user']['name'])
        print(item['followers_count'])
        print(item['user']['location'])
        print(item['user']['verified'])
        print(item['lang'])
        print(item['user']['statuses_count'])
        print(item['source'])
        print(item['favorite_count'])
        print(item['retweet_count'])
        print(item['created_at'])