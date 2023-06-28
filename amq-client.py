import time
import sys
import stomp
import ssl

# Creating a Listener class inheriting the stomp.ConnectionListener class
class MsgListener(stomp.ConnectionListener):

    def on_error(self, message):
        print('received an error "%s"' % message.body)
    def on_message(self, frame):
        print('received a message "%s"' % frame.body)


HOST='b-84cdb391-8adf-440b-9b6f-6c389248567b-1.mq.ap-south-1.amazonaws.com'
PORT=61614
USER='NAKUL'
PASS='*********'
TOPICNAME='topic/testtopic'

hosts = [(HOST, PORT)]

# Creating a connection object by passing the hosts as an argument
conn = stomp.Connection(host_and_ports=hosts)

# the connection object to listen for messages using the Listener class we created above

conn.set_listener('stomp_listener', MsgListener())
conn.set_ssl(for_hosts=[(HOST, PORT)], cert_file='cert.pem', key_file='privateKey.key',ssl_version=ssl.PROTOCOL_TLSv1_2)
conn.connect(USER, PASS, wait=True,headers = {'client-id': 'clientname'})

conn.send(body=' '.join(sys.argv[1:]), destination=TOPICNAME)
time.sleep(50)
# Registering a consumer with ActiveMQ. This tells ActiveMQ to send all # messages received on the queue 'TOPICNAME' to this listener
conn.subscribe(destination=TOPICNAME, id=1, ack='auto')


conn.disconnect()