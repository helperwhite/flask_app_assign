from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(address, term):
    auth = Oauth1Authenticator(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        token=os.environ['TOKEN'],
        token_secret=os.environ['TOKEN_SECRET']
    )

    client = Client(auth)


    params = {
        'term': term,
        'lang': 'en',
        'limit': 3
    }

    response = client.search(address, **params)
    
    businesses = []

    for business in response.businesses:
        businesses.append({"name": business.name,
            "location": business.location,
            "phone": business.phone,
            "rating": business.rating,
            "url": business.url
        })
    return businesses

# businesses = get_businesses("New York City", "Food")

# for business in businesses:
#     # print(item['location'].display_address)
#     # print("The store name is: {} with it's phone number is: {} and address is:{}." .format(item['name'], item['phone'], item['location'].display_address))
#     print("The store name is: {} with it's phone number is: {} and address is:{}." .format(business['name'], business['phone'], business['location'].display_address))