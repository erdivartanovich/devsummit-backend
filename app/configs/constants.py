ROLE = {
    'admin': 1,
    'booth': 3,
    'speaker': 4,
    'hackaton': 5,
    'ambassador': 6,
    'user': 7,
    'partner': 8
}

TICKET_TYPES = {
    'user': 'user',
    'exhibitor': 'exhibitor',
    'hackaton': 'hackaton'
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

EVENT_BRITE = {
    'EVENTBRITE_EVENT_ID': '39451411233',
    'EVENTBRITE_OAUTH_TOKEN': 'VVZMXUZB5PY4O65KK5AO'
}

SLACK = {
    'hook': 'https://hooks.slack.com/services/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',
    'notification': True
}

MIDTRANS_API_BASE_URL = 'https://api.sandbox.midtrans.com/v2/'
# Change these consts to devsummit later
MERCHANT_ID = 'M1066775'
CLIENT_KEY = 'VT-client-g8cB-IVLwe64YIdv'
SERVER_KEY = 'VT-server-njhqghnFUZbtZgOg9ldNtY0l:'
IMAGE_QUALITY = 70

# FCM key
FCM_SERVER_KEY = 'key=AAAA-YIsKqc:APA91bHWIn3yNFCPcSP4hQKqPYyZLewI8q9AoSWCVH8Qt39rlLP_6c02NuyoNP_o5FhXYi2UNlIV-HbzLct5U3w67Xjvu602YyCzaDbFk4-LJIZxcdl5_YsLkFVfqNExSsjkw9UIbQ_S'
FCM_GENERAL_TOPIC = '/topics/devsummit_indonesia_2017'

MAILGUN = {
    'server': 'https://api.mailgun.net/v3/sandbox1be5324ff09f4cbfabeac3bc90018521.mailgun.org/messages',
    'key': 'key-cff13ec10ae9301f0867648b2ebe4274',
    'sender': 'Andy <no-replyss@devsummit.io>'
}

QISCUS = {
    'BASE_URL': 'http://devsummit-qlqwpfmuvmj.qiscus.com/api/v2/rest/',
    'SDK_SECRET': '047374a736c7472685ed7dcb7e3d97da'
}
