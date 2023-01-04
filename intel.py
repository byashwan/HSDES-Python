
import requests
from requests_kerberos import HTTPKerberosAuth
import urllib3
# this is to ignore the ssl insecure warning as we are passing in 'verify=false'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
 
headers = { 'Content-type': 'application/json' }

#ids_ =[16017656909,16017657274,16017657324,16017657457,16017088102,16017089582,16017087641,16017086883,16016736331,16016736591,16019309150,16019309188,16019309502,16019309533,16019309555]
# Note we are using the PRE-PRODUCTION URL
ids_= [16016988693,16016711471,16018744844]
def helper(url):
    #url = 'https://hsdes-api.intel.com/rest/article/16017656909'
    payload = """
    {
    "tenant": "server_platf",
    "subject": "test_case_definition",
    "fieldValues": [
        {
        "test_case_definition.free_tag_3": "PPO"
        }
    
    ]
    }
    """


    response = requests.put(url, verify=False, auth=HTTPKerberosAuth(), headers = headers, data = payload)
    print (response.text+'DOne')

for item in ids_:
    helper('https://hsdes-api.intel.com/rest/article/'+str(item))