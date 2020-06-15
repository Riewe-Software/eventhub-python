from eventhub.eventhub import Eventhub

eventhub = Eventhub(base_url="http://127.0.0.1:5000",
                    email="fabianriewe00@gmail.com",
                    password="123456",
                    organization_name="AMS-Pro",
                    workspace_name="ams-dev",
                    app_name="ams-pro-client-b")

test_data = {"to": "1"}

eventhub.validate_event("user.created", test_data)
