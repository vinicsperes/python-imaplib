from connection import open_connection

c = open_connection()
sender = input("Enter sender e-mail: ")
senderFormated = "(FROM {})".format(sender)
#no-reply@n.dribbble.com



try:
    data = c.list(directory='[Gmail]/Tod')[1][0].decode('UTF8')
    print(data)
    c.select(data)

    # Find the message(s)
    typ, [msg_ids] = c.search(None, senderFormated)
    msg_ids = ','.join(msg_ids.decode().split(' '))
    print('Matching messages:', msg_ids)
    # What are the current flags?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print('Flags before:', response)
    
    # Change the Deleted flag
    typ, response = c.store(msg_ids, '+FLAGS', r'(\Deleted)')
    
    # What are the flags now?
    typ, response = c.store(msg_ids, '+X-GM-LABELS', '\\Trash')
    print('Flags after:', response)
    # Really delete the message.
    typ, response = c.expunge()
    print('Expunged:', response)

finally:
    try:
        c.close()
    except:
        pass
    c.logout()