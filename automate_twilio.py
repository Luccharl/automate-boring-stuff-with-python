from twilio.rest import Client
account_sid = 'ACab7241b95544450e7d54683d92f3e512'
auth = '2b186bd0596e549c51b56bd9617eec07'
twilio_cli = Client(account_sid, auth)

twilio_num = '+18456686094'
cp = '+639456505439'

message = twilio_cli.messages.create(body='Mr. Leywin - COME HERE - I WANT TO SEE YOU. ', from_=twilio_num, to=cp)
