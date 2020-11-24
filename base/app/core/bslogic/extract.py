"""Extract nested values from a dict."""


def dict_extract(obj, key):
    """Recursively fetch values from nested dict."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in dict tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    arr.append(v)
                elif isinstance(v, (dict, list)):
                    extract(v, arr, key)

        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values
