from dictipy import get_dict


class SimpleObject:

    def __init__(self):
        self.value = 1


def test_very_complex_object():
    so = SimpleObject()
    assert get_dict(so) == {'value': 1}


def test_simple_value():
    simple_value = "a"
    assert get_dict(simple_value) == "a"


def test_list():
    test_list = ["a", "b", {"c": 1, "d": "1"}, SimpleObject()]
    assert get_dict(test_list) == ['a', 'b', {'c': 1, 'd': '1'}, {'value': 1}]


def test_dict():
    test_dict = {"c": 1, "d": "1", "e": [1, 2, 3], "f": {"value": 1}, "g": SimpleObject()}
    assert get_dict(test_dict) == {'c': 1, 'd': '1', 'e': [1, 2, 3], 'f': {'value': 1}, 'g': {'value': 1}}


class VeryComplexObject:

    def __init__(self):
        self._number = 1
        self._string = "1"
        self._array = [1, "1", ["a", "b", "c"], {"value": 1}]
        self._dict = {
            "dict_number": 10,
            "dict_string": "10",
            "dict_array": ["a", "b", "c"],
            "dict_dict": {
                "value": 1
            }
        }


def test_very_complex_object():
    vco = VeryComplexObject()
    assert get_dict(vco) == {'_number': 1, '_string': '1', '_array': [1, '1', ['a', 'b', 'c'], {'value': 1}], '_dict': {'dict_number': 10, 'dict_string': '10', 'dict_array': ['a', 'b', 'c'], 'dict_dict': {'value': 1}}}


class Parent:

    def __init__(self, parent_field):
        self.parent_field = parent_field
        self.child = Child(1)
        self.child.child_field = Child(2)
        self.child.child_field.child_field = Child(3)


class Child:

    def __init__(self, child_field):
        self.child_field = child_field


def test_get_nested_objects():
    p = Parent(0)
    assert get_dict(p) == {'parent_field': 0, 'child': {'child_field': {'child_field': {'child_field': 3}}}}

