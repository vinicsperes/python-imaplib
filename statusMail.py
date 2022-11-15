import imaplib
from connection import open_connection
from parseListResponse import parse_list_response

c = open_connection()
try:
    typ, mailbox_data = c.list()
    for line in mailbox_data:
        flags, delimiter, mailbox_name = parse_list_response(line.decode())
        c.select(mailbox_name, readonly=True)
        typ, msg_ids = c.search(None, 'ALL')
        print(mailbox_name, typ)
finally:
    try:
        c.close()
    except:
        pass
    c.logout()