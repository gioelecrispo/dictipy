from dictipy import get_dict


class Parent:

    def __init__(self, parent_field):
        self.parent_field = parent_field
        self.child = Child(1)
        self.child.child_field = Child(2)
        self.child.child_field.child_field = Child(3)


class Child:

    def __init__(self, child_field):
        self.child_field = child_field


def test_get_dict():
    p = Parent(0)
    assert get_dict(p) == {'parent_field': 0, 'child': {'child_field': {'child_field': {'child_field': 3}}}}