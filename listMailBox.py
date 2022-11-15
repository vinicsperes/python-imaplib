from pprint import pprint
from connection import open_connection

c = open_connection()
try:
    # typ, data = c.list()
    typ, data = c.list(directory='[Gmail]/Tod')

    print('Response code:', typ)
    print('Response:')
    pprint(data)
finally:
    c.logout()