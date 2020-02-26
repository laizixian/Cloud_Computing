import requests
import json
import pprint


def get_search_parameters(cuisine, offset, limit):
    # See the Yelp API for more details
    params = {'term': cuisine, 'location': 'Manhattan', 'limit': limit, 'offset': offset}

    return params


if __name__ == '__main__':
    api_key = ''
    headers = {'Authorization': 'Bearer %s' % api_key}
    url = 'https://api.yelp.com/v3/businesses/search'
    curr_param = get_search_parameters('chinese', 0, 2)
    response = requests.get(url, params=curr_param, headers=headers)
    business_data = response.json()
    key_filter = ['id', 'name', 'location', 'coordinates', 'review_count', 'rating']
    for business in business_data['businesses']:
        filter_dict = ({x: business[x] for x in key_filter})
        new_json = json.dumps(filter_dict, indent=4)
        print(new_json)
