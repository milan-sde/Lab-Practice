import stomp

#create connection:
conn = stomp.Connection([('localhost',61613)])
conn.connect(wait=True)

#send message:
conn.send(destination='/queue/hello',body='Hello from Milan!')
print("message sent!!!")
conn.disconnect()

'''
why 61613 port ?
ActiveMQ supports multiple protocols:
OpenWire → 61616
STOMP → 61613
AMQP → 5672
MQTT → 1883

Each protocol gets its own port so they don’t conflict.
'''