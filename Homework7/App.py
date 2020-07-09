from Homework7 import Server
from typing import List


class User(object):
    def __init__(self, id: int, name: str, message: List[int]):
        self.id = id
        self.name = name
        self.message = message


class Message(object):
    def __init__(self, id: int, author: int, text: str):
        self.id = id
        self.author = author
        self.text = text


users = {
            1: User(1, 'Spartacus', [1]),
            2: User(2, 'Crixus', [2]),
            3: User(3, 'Varon', [3]),
            4: User(5, 'Batiatus', [4])
}

messages = {
            1: Message(1, 1, "I'm Spartacus!"),
            2: Message(2, 2, "Let's go to Rome!"),
            3: Message(3, 3, "No choice"),
            4: Message(4, 4, "House of Batiatus will ascend to heaven")
}


def get_value(values, id, field):
    if id:
        obj = values.get(int(id), None)
        if not obj:
            return None
        if field:
            return getattr(obj, field, None)
        else:
            return obj.__dict__
    else:
        return [obj.__dict__ for obj in values.values()]


def handle_request(request: str) -> str:
    import json
    import re
    lines = request.split('\r\n')
    match = re.fullmatch(r'([A-Z]+) (/\S*) HTTP/(\d\.\d)', lines[0])
    if not match:
        return 'HTTP/1.0 400 Bad Request\r\n\r\n'
    method, uri, version = match.group(1), match.group(2), match.group(3)
    if method not in ('GET', 'POST'):
        return 'HTTP/1.0 405 Method Not Allowed\r\n\r\n'
    match = re.fullmatch(r'/(users|messages)(?:/(\d+)(?:/([a-z]+))?)?', uri)
    if not match:
        return 'HTTP/1.0 404 Not Found\r\n\r\n'
    var, id, field = match.group(1), match.group(2), match.group(3)
    if var == 'users':
        result = get_value(users, id, field)
    else:
        result = get_value(messages, id, field)
    if result:
        return json.dumps(result)
    else:
        return 'HTTP/1.0 404 Not Found\r\n\r\n'


Server.serve(handle_request, '127.0.0.1', 8080)
