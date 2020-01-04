import json
import requests
from config import apikey, url

api = "%sapi/v2?apikey=%s&cmd={cmd}" %(url, apikey)

def get_play_count(days=3):
    resp = requests.get(api.format(
        apikey=apikey, cmd="get_plays_by_date&time_range={}".format(days)))
    resp_j = json.loads(resp.content)
    resp_j = resp_j.get('response')
    total = 0
    for series in resp_j['data']['series']:
        total += sum(int(v) for v in series['data'])
    return {'total': total, 'resp': resp_j}

if __name__ == "__main__":
    print(get_play_count())