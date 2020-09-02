from .http_connector import HttpRegistryConnector


class Eventhub:
    TYPE_MAPPING = {
        "string": str
    }

    def __init__(self, base_url, email, password, workspace_name, organization_name, app_name):
        self.registry = HttpRegistryConnector(
            base_url=base_url,
            workspace_name=workspace_name,
            organization_name=organization_name,
            app_name=app_name,
            email=email,
            password=password
        )

    def validate_event(self, event_name: str, event_properties: dict):
        event = self.registry.get_event(event_name)[event_name]['properties']
        self._validate_dict_types(event, event_properties)

    def _validate_dict_types(self, d_1: dict, d_2: dict):
        if d_1.keys() != d_2.keys():
            missing_keys = (set(d_1.keys()) - set(d_2.keys())) or None
            redundant_keys = (set(d_2.keys()) - set(d_1.keys())) or None
            raise TypeError(
                "Keys do not match. Missing: {}. Redundant: {}".format(missing_keys, redundant_keys))

        for i, (key, value) in enumerate(d_1.items()):
            try:
                d_2_value = d_2[key]
            except KeyError:
                raise KeyError("Missing data for '{}'".format(key))

            if isinstance(value, dict):
                self._validate_dict_types(value, d_2_value)
            else:
                try:
                    value_type = self.TYPE_MAPPING[value]
                except KeyError:
                    raise NotImplementedError("Mapping for key '{}' of type '{}' is not implemented".format(key, value))

                if not type(d_2[key]) == value_type:
                    raise TypeError(
                        "Expected type '{}' for key '{}', got '{}'".format(value_type, key, type(d_2_value)))

        return True
