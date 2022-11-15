from connection import open_connection

c = open_connection()
# sender = input("Enter sender e-mail: ")
# senderFormated = "(FROM {})".format(sender)

try:
  c.select()
  typ, [msg_ids] = c.search(None, 'ALL')
  msg_ids = msg_ids.decode().split()
  print('Matching messages:', len(msg_ids))

finally:
    try:
        c.close()
    except:
        pass
    c.logout()