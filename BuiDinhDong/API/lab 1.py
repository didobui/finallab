from sys import int_info
from requests.models import Response
import meraki_info
import requests
import pgpd
import json


########### cau : lay danh sach cac tbi trong network 
def get_devices():
    organizationID= "578149602163687854" #ID : Public API lab
    resp = pgpd.get(api="/organizations/{}/devices".format(organizationID))
    result =json.dumps(resp.json(),indent=4)
    return result

print("----------------------------")
result = get_devices()
print('Danh sach trong network : ', result)


############# cau 6 : xem danh sach cac tbi trong inventory
def get_device_inventory():
    organizationID= "578149602163687854" #ID : Public API lab
    resp = pgpd.get(api="/organizations/{}/inventoryDevices".format(organizationID))
    result =json.dumps(resp.json(),indent= 4)
    return result
print("----------------------------")
result = get_device_inventory()
print('Danh sach cac thiet bi trong inventory Public API Lab: ', result)

################# cau 7 : xem ds cac tbi chua dc su dung trong iventory 
def get_device_null():
    organizationID= "578149602163687854" #ID : Public API lab
    resp = pgpd.get(api="/organizations/{}/inventoryDevices".format(organizationID))
    result =json.dumps(resp.json(),indent= 4)
    data = json.loads(result)
    i = 0
    listtrong = []
    for item in data:
        if item["networkId"] is None:
            listtrong.append((item["mac"],item["serial"]))
    filerlist = json.dumps(listtrong)
    return filerlist

print("----------------------------")
result = get_device_null()
print('Danh sach thiet bi co Network ID la NULL trong inventory: ', result)

