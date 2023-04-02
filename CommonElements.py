import pytest


class CE:
    def commonElements(self, list1, list2):
        # Fix for invalid inputs:
        for a in list1:
            if type(a) is not int:
                return "Invalid input"
        for a in list2:
            if type(a) is not int:
                return "Invalid input"

        result = []
        # Fix for duplicate items:
        l1 = []
        [l1.append(x) for x in list1 if x not in l1]
        l2 = []
        [l2.append(x) for x in list2 if x not in l2]

        for i1 in l1:
            for i2 in l2:
                if i1 == i2:
                    result.append(i1)
        return result


ce = CE()


def test_integer_lists():
    l1 = [1, 32, 43, 12]
    l2 = [3, 53, 12, 1, 254]

    assert ce.commonElements(l1, l2) == [1, 12]


def test_integer_lists_duplicates_firstList():
    l1 = [1, 32, 43, 12, 12]
    l2 = [3, 53, 12, 1, 254]
    assert ce.commonElements(l1, l2) == [1, 12]


def test_integer_lists_duplicates_secondList():
    l1 = [1, 32, 43, 12]
    l2 = [3, 53, 12, 1, 1, 254]
    assert ce.commonElements(l1, l2) == [1, 12]


def test_non_integer_lists():
    l1 = ['a', "b", {"key": 324}]
    l2 = ['a', "b", "x"]
    assert ce.commonElements(l1, l2) == "Invalid input"
