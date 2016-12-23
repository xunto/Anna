import json


def _json_default_tree_(o):
    if isinstance(o, Tree):
        return o.__dict__
    else:
        return str(o)


class Tree:
    def __init__(self, data=None, children=None):
        self.data = data

        if children is None:
            children = []
        self.children = children

    def to_json(self):
        return json.dumps(self, default=_json_default_tree_, sort_keys=True, indent=4)
