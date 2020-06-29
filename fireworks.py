from twython import Twython
import pickle
from geopy import Nominatim
from itertools import islice
import time


def locate(place):
    locator = Nominatim(user_agent='firework')
    location = locator.geocode(place)
    if location:
        return str(location.latitude) + ',' + str(location.longitude) + ',' + str(location) + '\n'


# A rate limiter to handle the Twython generator and the Twitter API's tweet retrieval limits
# user id as dict key filters out duplicate tweets
def rate_limit(my_gen, seconds=10):
    stop = 50
    gen_dict = {}
    while stop != 500:
        limit = islice(my_gen, stop)
        for i in limit:
            gen_dict[i['user']['id']] = i['user']['location']
        stop += 50
        time.sleep(seconds)
    return gen_dict


with open('secret_twitter_credentials.pkl', 'rb') as pkl:
    Twitter = pickle.load(pkl)

api = Twython(app_key=Twitter['Consumer Key'],
              app_secret=Twitter['Consumer Secret'],
              oauth_token=Twitter['Access Token'],
              oauth_token_secret=Twitter['Access Token Secret'])

results = api.cursor(api.search, q='firework conspiracy')

rate_dict = rate_limit(results)
with open('rate_locs.csv', 'a') as loc_file:
    # Filters out None returned from locate function when users tag locations with no lat or long
    # ie. Philly, New York State of Mind, etc.
    for loc in filter(None, map(locate, rate_dict.values())):
        loc_file.write(loc)
