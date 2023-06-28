import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):
        with open("output.txt", "wt") as f:
            print("frame.body", file=f)

        # print('received a message "%s"' % frame.body)
        # print(frame)

conn = stomp.Connection( [('localhost',61613)] )
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True)
conn.subscribe(destination='nakulsending', id=1, ack='auto')

while True:
    time.sleep(5)