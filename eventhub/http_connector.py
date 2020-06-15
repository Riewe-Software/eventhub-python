import requests
from .exceptions import Unauthorized, NotFound, EventhubException


class HttpRegistryConnector:

    def __init__(self, base_url, email, password, organization_name, workspace_name, app_name):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers['x-eventhub-app-name'] = app_name

        self.workspace_name = workspace_name
        self.organization_name = organization_name

        self.email = email
        self.password = password

        self._login()

    def _login(self):
        json = {'email': self.email, 'password': self.password}
        response = self.session.post(self.base_url + "/login", json=json)
        if response.ok:
            self.session.headers['Authorization'] = "Bearer {}".format(response.json())
        elif response.status_code == 401:
            raise Unauthorized(response.json())
        else:
            raise EventhubException("Error: {}".format(response.json()))

    def _get(self, endpoint, params):
        response = self.session.get(self.base_url + endpoint, params=params)
        if response.ok:
            return response
        elif response.status_code == 401:
            raise Unauthorized(response.json())
        elif response.status_code == 404:
            raise NotFound(response.json())
        else:
            raise EventhubException("Error: {}".format(response.json()))

    def get_event(self, event_name: str):
        params = {
            "event_name": event_name,
            "workspace_name": self.workspace_name,
            "organization_name": self.organization_name
        }
        return self._get("/event", params=params).json()
