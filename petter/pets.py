import json
import requests

resp = requests.get('https://www.petrescue.com.au/api/listings')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /listings/ {}'.format(resp.status_code))
for pets_item in resp.json():
    print('{} {}'.format(pets_item['id'], pets_item['summary']))


def pets_items(summary, description=""):
    return requests.post(_url('/listings/'), json={
        'summary': summary,
        'description': description,
        })
