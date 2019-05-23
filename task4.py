
import requests

#import json library
import json

controller='sandboxapic.cisco.com'
#controller='devnetapi.cisco.com/sandbox/apic_em'


# put the ip address or dns of your apic-em controller in this url
url = "https://" + controller + "/api/v1/ticket"

#the username and password to access the APIC-EM Controller
payload = {"username":"devnetuser","password":"Cisco123!"}

#Content type must be included in the header
header = {"content-type": "application/json"}

#Performs a POST on the specified url to get the service ticket
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

#convert response to json format
r_json=response.json()

#print(r_json)
#parse the json to get the service ticket
ticket = r_json["response"]["serviceTicket"]

# URL for Host REST API call to get list of exisitng hosts on the network.
url = "https://" + controller + "/api/v1/host"

#Content type must be included in the header as well as the ticket
header = {"content-type": "application/json", "X-Auth-Token":ticket}

# this statement performs a GET on the specified host url
response = requests.get(url, headers=header, verify=False)

# json.dumps serializes the json into a string and allows us to
# print the response in a 'pretty' format with indentation etc.


# Taken Id as name
print ("Hosts = ")
print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

r_resp=response.json()
host_dic={}
id_list=[]
for item in r_resp['response']:
     id_list.append(item['id'])
     tup=(item['id'],item['hostIp'])
     host_dic[tup]=item['hostMac']
     
print("The Host details are::::",host_dic)   

#=====================================================================

def gethostcount(id_list):
    for id1 in id_list:
        url = "https://" + controller + "/api/v1/GET /discovery/"+id1+"/network-device/count"
        header = {"content-type": "application/json", "X-Auth-Token":ticket}
        response = requests.get(url, headers=header, verify=False)
        print(response.status_code)
        print('The Host Count for the Devices wit id::'+id1+"::::",response.text)
    

gethostcount(id_list)
#print(r_resp["response"][0]["hostIp"])



