##Import Modules for networking and for Airmore messaging service

from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages

##Specify IP Address shown within the airmore application
ip = IPv4Address("192.168.1.4")

# Create an instance of the Session
session = AirmoreSession(ip)

# if your port is not 2333
# session = AirmoreSession(ip, 2334)  # assuming it is 2334

# Store value of request authorization from phone
was_accepted = session.request_authorization()


print("Is request accepted? ", was_accepted)  # True if accepted


service = MessagingService(session)
service.send_message("0600000000", "test msg")
