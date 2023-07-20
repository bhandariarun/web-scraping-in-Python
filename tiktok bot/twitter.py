import time

import tweepy
import sqlite3
import re

db=sqlite3.connect('urlbot.db')
consumer_key='1rGcfen1hqwYBXnl7RIBaDDSL'
consumer_secret='F5bARpSJmYdTDQK8dcej8dZ7BrozVSyr1RVA799BY6UPZ2ozKF'
access_token='1480539044555603968-hrnCTyZ98HA6uFum0SpMHfZlaz8Onq'
access_token_secret='nb9novbsj6QNP88uvaRj0NfYEULX93OubH7NWoeFag7Tc'

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth,wait_on_rate_limit=True)



data=db.execute("SELECT * FROM urlmovie")

for d in data:
   query=d[1]
   query1='Watch '+query + ' at https://noonemovies.xyz/'+d[2]
   opening_braces = '\('
   closing_braces = '\)'
   non_greedy_wildcard = '.*?'
   re.sub(f'[{opening_braces}]{non_greedy_wildcard}[{closing_braces}]', '', query)
   query=query.replace('  ',' ')
   tweets = tweepy.Cursor(api.search_tweets, q=query, count=10, lang='en', tweet_mode='extended').items(10)
   print(query)
   for page in tweets:
      print(page)

      api.update_status(status = query1, in_reply_to_status_id = page._json['id'] , auto_populate_reply_metadata=True)
      time.sleep(2)

   print('\n\n')
   db.execute('DELETE FROM urlmovie WHERE id='+str(d[0]))
   db.commit()