import requests
import json
import sys
import meraki_info

def get(base_url=meraki_info.base_url,api='',params=''):
    headers = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    url = base_url + api
    print("\nExecuting GET '%s'\n"%url)
    try:
        resp = requests.get(url,headers=headers,params=params)
        print("GET '%s' status" %api,resp.status_code,'\n')
        return(resp)
    except:
        print("Something wrong",api)
        sys.exit()
