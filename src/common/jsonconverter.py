class StringToJsonConverter:
    def __init__(self):
        pass

    def convert(self, **kwargs):
        try:
            json_output = {key: value for key, value in kwargs.items()}
            return json_output
        except Exception as e:
            return None

