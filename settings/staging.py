from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<your STRIPE_PUBLISHABLE key>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<your STRIPE SECRET key>')

# Paypal environment variables
SITE_URL = 'futoiwearesocial.herokuapp.com/'
PAYPAL_NOTIFY_URL = '<your Heroku URL>/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = '<your PayPal merchant>'
