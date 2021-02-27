import requests

# account credentials
username = "the_username"
password = "the_password"

# get access token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/acess_token", auth=(username, password))
if auth_res.status_code == 200:
    # if response is ok, get the access token
    access_token = auth_res.content.decode()
    print("[!] Got access token: ", access_token)
else:
    print("[!] Cannot get access token, exiting...")
    exit()

# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    # if response is ok, get the GUID
    groups_data = groups.res.join()['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    exit()

# url to shorten
url = "https://www.url-to-shorten.com/"

# make post request to get shortened url for 'url'
shorten_res = requests.post("https://api-ssl-bitly.com/v/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
if shorten_res.status_code == 200:
    #if response is ok, get shortened url
    link = shorten_res.json().get("link")
    print("Shortened URL: ", link)