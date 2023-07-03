from utils.dicts import get_val


def test_get_val():
    assert get_val({'кошка': 'cat', 'собака': 'dog'}, 'кошка') == 'cat'
    assert get_val({'кошка': 'cat', 'собака': 'dog'}, 'собака') == 'dog'
    assert get_val({'кошка': 'cat', 'собака': 'dog'}, 'хомяк') == 'animal'
