# 과제 풀이가 예제 데이터에 대해 정확히 동작하는지 확인한다.
from exercises.solutions import count_available, filter_by_category, is_available

def test_count_available():
    assert count_available() == 2

def test_filter_by_category():
    assert len(filter_by_category("주변기기")) == 2

def test_sold_out():
    assert not is_available({"stock": 0})
