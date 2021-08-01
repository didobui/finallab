from requests.models import Response
import meraki_info
import requests
import json
requests.packages.urllib3.disable_warnings()

#Cau 1 -----------------------------------------------
def get(base_url=meraki_info.base_url,api='',params=''):
    payload = None
    headers = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    url = base_url + api
    resp = requests.get(url,headers=headers,params=params)
    print("\nExecuting GET '%s'\n"%url)
    return resp
#Cau 2 -----------------------------------------------
def get_devices_in_organization():
    org_ID = "578149602163687854"
    response = get(api="/organizations/{}/devices".format(org_ID))
    result =json.dumps(response.json(),indent=4)
    return result
#Cau 3 -----------------------------------------------
def get_devices_null():
    org_ID = "578149602163687854"
    response = get(api="/organizations/{}/inventory".format(org_ID))
    result = json.dumps(response.json(),indent= 4)
    data = json.loads(result)
    i = 0
    listdevicenull = []
    for item in data:
        if item["networkId"] is None:
            listdevicenull.append((item["name"],item["model"],item["mac"],item["serial"]))
    filterlist = json.dumps(listdevicenull)
    return filterlist

print("----------------------------------")
ketqua1 = get_devices_in_organization()
print("Danh sach cac thiet bi trong inventory Public API Lab: ",ketqua1)
print("----------------------------------")
ketqua2 = get_devices_null()
print("Danh sach thiet bi co Network ID la NULL trong inventory: ",ketqua2)

