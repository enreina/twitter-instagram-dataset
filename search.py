import os
import json
import time
import pickle

# https://github.com/bear/python-twitter
# to install: pip install python-twitter
from twitter import Api

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

# waiting time in seconds
wait_time = 5 # 5 seconds

api = Api(consumer_key, consumer_secret, access_token, access_token_secret, sleep_on_rate_limit=True)

def main():
    # api.GetStreamFilter will return a generator that yields one status
    # message (i.e., Tweet) at a time as a JSON dictionary.
    results_all = []
    while len(results_all) < 150000:
        query = "q=instagram.com%2Fp%2F&lang=en&result_type=recent&count=100"
        if len(results_all) > 0:
            max_id = results_all[-1].id - 1
            print(max_id)
            query = query + "&max_id=" + str(max_id)
        results = api.GetSearch(
raw_query=query)
        results_all.extend(results)
        with open('./output_chunks/output_' + str(len(results_all)), 'w') as f:
            pickle.dump(results, f)
        print(len(results_all))

        
if __name__ == '__main__':
    main()