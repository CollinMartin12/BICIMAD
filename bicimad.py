import os
import requests

BASE = "https://openapi.emtmadrid.es/v1"

def login():
    r = requests.get(
        f"{BASE}/mobilitylabs/user/login/",
        headers={
            "X-ClientId": os.environ["EMT_CLIENT_ID"],
            "passKey": os.environ["EMT_PASSKEY"],
        },
        timeout=15,
    )
    print("login:", r.status_code)
    print(r.text[:600])
    r.raise_for_status()
    return r.json()["data"][0]["accessToken"]

def stations(token):
    r = requests.get(
        f"{BASE}/transport/bicimad/stations/",
        headers={"accessToken": token},
        timeout=15,
    )
    print("stations:", r.status_code)
    print(r.text[:600])
    r.raise_for_status()
    return r.json()["data"]

if __name__ == "__main__":
    tok = login()
    data = stations(tok)
    print(f"\n{len(data)} stations")
    print(data[0])