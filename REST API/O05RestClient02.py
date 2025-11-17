import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getproduct/coke")

res = response.json()
# print(res)

for ky, vl in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in vl.items():
        print(k, "=>", v)
