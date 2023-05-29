import requests
import json

def VTFileScan():
    url = "https://www.virustotal.com/api/v3/files"
    files = {"file": ("test.txt", open("test.txt", "rb"), "text/plain")}
    headers = {
        "accept": "application/json",
        "x-apikey": "{apikey}"
    }
    response = requests.post(url, files=files, headers=headers)
    res = response.json()
    analysis_url = res["data"]["links"]["self"]
    print(analysis_url)


VTFileScan()


