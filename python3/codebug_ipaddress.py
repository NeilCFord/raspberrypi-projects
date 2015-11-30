# import modules
import socket
import codebug_i2c_tether
import time

# set-up connection to CodeBug
cb = codebug_i2c_tether.CodeBug()
cb.open()

# function to get ip address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# function for scrolling messages on CodeBug’s display
def scroll_message(message):
    length = len(message)
    for i in range(0,length*-5,-1):
        cb.write_text(i, 0, message, direction="right")
        time.sleep(.15)

# display ip address on CodeBug
scroll_message(get_ip())

# loop to redisplay on button press
while True:

    if cb.get_input('A') == True:
        scroll_message(get_ip())

    if cb.get_input('B') == True:
        scroll_message("Goodbye!")
        break
    
# clean up and exit
time.sleep(1)
cb.clear()
cb.close()
