ROLE = {
    'admin': 1,
    'booth': 3,
    'speaker': 4,
    'ambassador': 6,
    'user': 7,
    'partner': 8
}

TICKET_TYPES = {
    'user': 'user',
    'exhibitor': 'exhibitor'
}

SLOT = {
	'community': 400,
	'commercial': 3600
}

EVENT_TYPES = {
    'discuss panel',
    'speaker',
    'hackaton',
    'other'
}

EVENT_DATES = {
    '1': '2017-11-21',
    '2': '2017-11-22',
    '3': '2017-11-23'
}

SPONSOR_STAGES = {
    '1': 'lead',
    '2': 'prospect',
    '3': 'official'
}

SPONSOR_TYPES = {
    '1': 'diamond',
    '2': 'platinum',
    '3': 'gold',
    '4': 'silver'
}

VA_NUMBER = {
    'bca': '877800',
    'permata': '431800',
    'mandiri_bill': '242801',
    'bni': '119800'
}

PAYPAL = {
    'mode': "live",
    'client_id': "AV5yciJeTgKzD62m7kvePBtCWMIt66LkKc-fAV8oKh3EXY-WKnfZSZS-sLJbK-lEDYhbJpyGBwR673s5",
    'client_secret': "ECcVoK_ngiZk5iZX2tysVVHpJvN9hSAxTRYwD2TkWEKOIs3xrVXfhxPloceCtDtm5s8hVQ31RTSbdl3x",
    'payee': 'toopay@taufanaditya.com',
    'return_url': 'https://api.devsummit.io/payment/execute',
    'cancel_url': 'https://api.devsummit.io/'
}

MIDTRANS_API_BASE_URL = 'https://api.sandbox.midtrans.com/v2/'
# Change these consts to devsummit later
MERCHANT_ID = 'M1066775'
CLIENT_KEY = 'VT-client-g8cB-IVLwe64YIdv'
SERVER_KEY = 'VT-server-njhqghnFUZbtZgOg9ldNtY0l:'
IMAGE_QUALITY = 70

# FCM key
FCM_SERVER_KEY = 'key=AAAA8iNOby4:APA91bGxdjtV_YTm3FnvjUiGJPPartTvM5COQFsubP-kBGP0AbmGBml1WtbYgAKc2-CDNcFGYLl4j0JzJq4AzeZwc47aURd3MTKLW_bLS6FtYokJdgjJcE7rM-9KiPlPJ029S9ua7OUF'
FCM_GENERAL_TOPIC = '/topics/devsummit_indonesia_2017'
