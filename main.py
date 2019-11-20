from dictipy import get_dict
import json


class Parent:

    def __init__(self, parent_field):
        self.parent_field = parent_field
        self.child = Child(1)


class Child:

    def __init__(self, child_field):
        self.child_field = child_field


if __name__ == "__main__":
    p = Parent(0)
    print("Standard Python dict:  ", p.__dict__)
    print("Dictipy get_dict:      ", get_dict(p))

    j1 = json.dumps(p)  # throws -> TypeError: Object of type Parent is not JSON serializable
    j2 = json.dumps(p.__dict__)  # throws -> TypeError: Object of type Child is not JSON serializable
    j3 = json.dumps(get_dict(p))  # returns -> '{"parent_field": 0, "child": {"child_field": 1}}'
