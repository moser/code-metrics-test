import typing

import flask as f
import numpy

app = f.Flask("calc")

@app.route("/")
def index():
    numpy.non_existing_thing()
    typed_thing('not an integer')
    typed_thing(1.0)  # also not an integer
    return ""

def typed_thing(a: int) -> typing.List[str]:
    if a > 10:
        return [1]
    # wrong type path
    return ['a']


def request_fun(req: f.Request) -> f.Request:
    if 1:
        return []
    return req

