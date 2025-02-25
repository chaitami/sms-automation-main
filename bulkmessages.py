##Import Modules for networking and for Airmore messaging service and an added module from openpyxl.
## You can use any module that is able to read and work with python.

from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages
from openpyxl import load_workbook
import time

ip = IPv4Address("192.168.1.11")  # let's create an IP address object
# now create a session
session = AirmoreSession(ip)
# if your port is not 2333
# session = AirmoreSession(ip, 2334)  # assuming it is 2334

was_accepted = session.request_authorization()

print("Is request accepted? ", was_accepted)  # True if accepted

# path to Excel Sheet
filepath = "final.xlsx"

# column to Read from
column = "A"  # suppose it is under "A"

########################
# Needs to be specified#
########################
#length = 200

workbook = load_workbook(filename=filepath, read_only=True)
worksheet = workbook.active  # we will get the active worksheet

count = 0
for row in worksheet:
    if not all([cell.value == None for cell in row]):
        count += 1

phone_numbers = []
for i in range(count):
    cell = "{}{}".format(column, i + 1)
    number = worksheet[cell].value
    if number != "" or number is not None:
        phone_numbers.append(str(number))


message = "test msg"
for number in phone_numbers:
    service = MessagingService(session)
    service.send_message(number, message)
    print("message sent to " + number)
    # 1-2-3-4-5-10-20-15-12-11-10-9-8
    time.sleep(8)
    