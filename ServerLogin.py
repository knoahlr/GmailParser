from __future__ import print_function
import imaplib
from email.parser import Parser

def process_multipart_message(message):
    rtn = ''
    if message.is_multipart():
        for m in message.get_payload():
            rtn += process_multipart_message(m)
    else:
        rtn += message.get_payload()
    return rtn

url = 'imap.gmail.com'
conn = imaplib.IMAP4_SSL(url,993)
user,password = ('knoah.lr@gmail.com', 'aggrx2y1478')
conn.login(user,password)
conn.select('INBOX')
results,data = conn.search(None,'(UNSEEN)')
msg_id_list = data[0].split()
print(len(msg_id_list))

latest_email_id = msg_id_list[-1]
for e_id in msg_id_list:
    conn.store(e_id, '+FLAGS', '\Seen')
result,data = conn.fetch(latest_email_id,"(RFC822)")
raw_email = data[0][1]
p = Parser()
msg = p.parsestr(raw_email)
print(msg.get('From'))
print(msg.get('title'))

msg_constant = process_multipart_message(msg)

print(msg_constant, file=open('email.txt' ,'w'))