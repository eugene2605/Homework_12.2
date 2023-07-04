import pytest

from utils.dicts import get_val

@pytest.fixture
def dict_fix():
    return {'кошка': 'cat', 'собака': 'dog'}
def test_get_val(dict_fix):
    assert get_val(dict_fix, 'кошка') == 'cat'
    assert get_val(dict_fix, 'собака') == 'dog'
    assert get_val(dict_fix, 'хомяк') == 'animal'
