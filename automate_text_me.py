from twilio.rest import Client

def text_me(message):
    account_sid = 'ACab7241b95544450e7d54683d92f3e512'
    auth = '2b186bd0596e549c51b56bd9617eec07'

    twilio_num = '+18456686094'
    cp = '+639297072214'

    twilio_cli = Client(account_sid, auth)
    twilio_cli.messages.create(body=message, from_=twilio_num, to=cp)
    
    return 'Done'


text_me('Hi')

