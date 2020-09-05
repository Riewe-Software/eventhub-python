from eventhub import Eventhub

eventhub = Eventhub(base_url="https://eventhub-backend-dev.herokuapp.com/",
                    email="foo@bar.com",
                    password="123456",
                    organization_name="AMS-Pro",
                    workspace_name="ams-dev",
                    app_name="ams-pro-client-b")

test_data = {"firstName": "1", "lastName": "", "email": ""}

eventhub.validate_event("user.created", test_data)
