import stomp
import time

class MyListener(stomp.ConnectionListener):
    def on_message(self,frame):
        print("received : ",frame.body)

# create connection:
conn = stomp.Connection([('localhost',61613)])
conn.set_listener('',MyListener())
conn.connect(wait=True)

# Subscribe to queue
conn.subscribe(destination='/queue/hello',id=1,ack='auto')
print("Waiting for message ...")

time.sleep(10)
conn.disconnect()