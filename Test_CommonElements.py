from CommonElements import CE
from unittest.mock import Mock
from unittest.mock import patch

ce = CE()


def test_ce_with_patch_returnValue():
    list1 = [12, 4, 34, 23]
    list2 = [5, 12, 23, 34]
    with patch.object(CE, 'commonElements', return_value=[12, 34, 23]):
        assert ce.commonElements(list1, list2) == [12, 34, 23]


def test_ce_with_patch_sideEffect():
    def ce_patched(l1, l2):
        return [12, 34, 23]
    with patch.object(CE, 'commonElements', side_effect=ce_patched):
        assert ce.commonElements([12, 4, 34, 23], [5, 12, 23, 34]) == [12, 34, 23]


def test_ce_with_mock_returnValue():
    ce.commonElements = Mock()
    ce.commonElements.return_value = [12, 34, 23]
    assert ce.commonElements([12, 4, 34, 23], [5, 12, 23, 34]) == [12, 34, 23]


def test_ce_with_mock_sideEffect():
    def ce_mocked(l1, l2):
        return [12, 34, 23]
    ce.commonElements = Mock(side_effect=ce_mocked)
    assert ce.commonElements([12, 4, 34, 23], [5, 12, 23, 34]) == [12, 34, 23]

