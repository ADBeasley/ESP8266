import network
import espnow

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()      # For ESP8266

e = espnow.ESPNow()
e.active(True)
# peer = b'\x18\xfe\x34\xed\x49\xc4'
# peer = b'\x18\xfe\x34\xed\x49\x7f' # Dot on USB connector
e.add_peer(peer)      # Must add_peer() before send()

try:
    print(e.get_peer(peer))
except:
    print("Cannot get details of peer")

print("Peer added")

e.send(peer, "Starting...")

print("First message sent")

for i in range(100):
    e.send(peer, str(i)*20, True)
e.send(peer, b'end')

print("All messages sent")
