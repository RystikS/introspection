import inspect
import requests

def introspection_info(obj):
    type_obj = type(obj).__name__
    attr_obj = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods_obj = [method for method in dir(obj) if callable(getattr(obj, method)) and method.startswith("__")]
    module_obj = introspection_info.__module__
    return {'type': type_obj, 'attributes': attr_obj, 'methods': methods_obj, 'module': module_obj}

number_info = introspection_info(42)
print(number_info)

class Inspect:
    def __init__(self):
        self.value = 42

user_class = Inspect()

user_info = introspection_info(user_class)
print(user_info)


