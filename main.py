import uuid
import base64
import os
import time

from enums import DeviceType, ServerProtocol, ServerType
from pprint import pprint

from python_graphql_client import GraphqlClient
from graphql_sdk import SDK


class Client:
    def __init__(self, access_token=None, refresh_token=None, license_key=None,
                 device_type: DeviceType = DeviceType.WINDOWS, unique_id=None):
        self.endpoint = "https://api.quarielana.xyz/graphql"
        self._access_token = access_token
        self._refresh_token = refresh_token
        self._license_key = license_key
        self._device_type = device_type
        self._unique_id = str(uuid.uuid4())
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36",
            "Authorization": f"Bearer {self._access_token}",
            "X-Refresh-Token": f"{self._refresh_token}",
        }
        self._client = GraphqlClient(endpoint=self.endpoint)

    def execute(self, query, headers=None, variables=None):
        if variables is None:
            variables = {}
        if headers is None:
            headers = self.headers
        data = self._client.execute(query=query.value, headers=headers, variables=variables)
        return data["data"]

    def get_domains(self):
        return self.execute(query=SDK.select_domain_document, headers=self.headers)

    def get_languages(self):
        return self.execute(query=SDK.get_languages_document, headers=self.headers)

    def get_nodes(self, serverType: ServerType = ServerType.FREE,
                  regionId=None, serverProtocol: ServerProtocol = ServerProtocol.WIREGUARD):
        payload = {
            "payload": {
                "serverType": serverType.value if isinstance(serverType, ServerType) else serverType,
                "regionId": regionId,
                "serverProtocol": serverProtocol.value if isinstance(serverProtocol, ServerProtocol) else serverProtocol
            }
        }
        resp = self.execute(query=SDK.select_node_document,
                            headers=self.headers, variables=payload)
        select_node = resp["selectNode"]
        if select_node["success"]:
            return select_node["node"]
        raise BaseException(select_node)

    def get_purchases(self):
        return self.execute(query=SDK.get_purchases_document, headers=self.headers)

    def register_user(self):
        resp = self.execute(query=SDK.register_user_document,
                            headers=self.headers)
        register_user = resp["registerUser"]
        if register_user["success"]:
            return register_user
        raise BaseException(register_user)

    def login_user(self, license_key=None):
        payload = {
            "payload": {
                "deviceType": self._device_type.value if isinstance(self._device_type, DeviceType) else self._device_type,
                "licenseKey": license_key or self._license_key,
                "deviceUniqueId": self._unique_id
            }
        }
        resp = self.execute(query=SDK.login_user_document,
                            headers=self.headers, variables=payload)
        login_user = resp["loginUser"]
        if login_user["error"]:
            raise BaseException(login_user)
        if login_user["success"]:
            self._access_token = login_user["accessToken"]
            self.headers["Authorization"] = f"Bearer {self._access_token}"
            self._refresh_token = login_user["refreshToken"]
            self.headers["X-Refresh-Token"] = f"{self._refresh_token}"
            return login_user
        else:
            raise BaseException(login_user)


    def refresh_token(self):
        resp = self.execute(
            query=SDK.refresh_token_document, headers=self.headers)
        self._access_token = resp["refreshToken"]
        self.headers["Authorization"] = f"Bearer {self._access_token}"
        return resp

    def get_user(self):
        return self.execute(query=SDK.get_users_document, headers=self.headers)

    def use_otp(self):
        return self.execute(query=SDK.use_otp_document, headers=self.headers)

    def request_otp(self):
        return self.execute(query=SDK.request_otp_document, headers=self.headers)

    def create_otp(self):
        return self.execute(query=SDK.create_otp_document, headers=self.headers)

    def restore_user(self):
        return self.execute(query=SDK.restore_user_document, headers=self.headers)

    def set_email(self):
        return self.execute(query=SDK.set_email_document, headers=self.headers)

    def get_zones(self):
        resp = self.execute(query=SDK.get_zones_document, headers=self.headers)
        get_zones = resp["getZones"]
        if get_zones["success"]:
            return get_zones["zones"]
        raise BaseException(get_zones)


client = Client(device_type=DeviceType.ANDROID)

for i in range(0, 16):
    license_key = client.register_user()["licenseKey"]
    print(f"License key: {license_key}")
    client.login_user(license_key)
    print(f"Refresh token: {client._refresh_token}")
    zones = client.get_zones()
    for zone in zones:
        if zone["nodeIsAvailable"]:
            node = client.get_nodes(regionId=zone["regionId"], serverProtocol=zone["serverProtocol"])
            if not os.path.exists(f'./confs{i}'):
                os.mkdir(f'./confs{i}')
            with open(f'./confs{i}/{node["regionCode"]}.conf', 'w') as file:
                data = node["data"]
                data = base64.b64decode(data).decode("utf-8")
                file.write(data)
                print(f"Saved {node['regionCode']}.conf - {node['serverHost']}")
                time.sleep(3)
    time.sleep(10)

# pprint(client.login_user())
# zones = client.get_zones()
# conf_dir = "./confs2"

# if not os.path.exists(conf_dir):
#     os.mkdir(conf_dir)

# for zone in zones:
#     if zone["nodeIsAvailable"]:
#         node = client.get_nodes(regionId=zone["regionId"])
#         with open(f'{conf_dir}/{node["regionCode"]}.conf', 'w') as file:
#             data = node["data"]
#             data = base64.b64decode(data).decode("utf-8")
#             file.write(data)
