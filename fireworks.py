from twython import Twython
import pickle

with open('/Users/admin/JupyterProjects/secret_twitter_credentials.pkl', 'rb') as pkl:
    Twitter = pickle.load(pkl)

api = Twython(app_key=Twitter['Consumer Key'],
              app_secret=Twitter['Consumer Secret'],
              oauth_token=Twitter['Access Token'],
              oauth_token_secret=Twitter['Access Token Secret'])

results = api.cursor(api.search, q='firework conspiracy')
with open('/Users/admin/PycharmProjects/Fireworks/firework_locs.txt', 'a') as loc_file:
    for result in results:
        loc_file.write(result['user']['location'] + '\n')

