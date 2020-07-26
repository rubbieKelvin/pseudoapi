def make_vars_from_dict(data, container, prefix="%"):
    for key in data:
        if type(data[key]) == dict:
            make_vars_from_dict(data[key], container, prefix=f"{prefix}{key}.")
        else:
            container[f"{prefix}{key}"] = data[key]

def feedvars(data, variables):
    for key in data:
        if type(data[key]) == dict:
            feedvars(data[key], variables)
        elif type(data[key]) == str:
            data[key] = data[key].format(**variables)

def typeof(data, prefix="::"):
    if type(data) == str:
        if data.startswith(prefix) and not " " in data:
            type_ = data[len(prefix):]
            if type_ in ["int", "str", "bool", "dict", "list"]:
                return eval(type_)
    return type(data)

class TypeCheckError(BaseException): pass

def validaterequest(request, template):
    for key in template:
        if type(template[key]) == dict:
            if type(request.get(key)) != dict:
                raise TypeCheckError

            validaterequest(request[key], template[key])
        else:
            if type(request[key]) == typeof(template.get(key)):
                continue
            else:
                raise TypeCheckError

def processresponse(body:dict, request:dict, response:dict):
    try:
        validaterequest(body, request)
    except TypeCheckError:
        return dict(error="invalid type in request")

    variables = dict()
    make_vars_from_dict(body, variables)

    result = response.copy()
    feedvars(result, variables)

    return result
