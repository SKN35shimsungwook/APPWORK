"""JSON 저장소에 대한 pytest 테스트."""
import json
import pytest
from catalog.repository import ProductRepository

def test_default_products(tmp_path):
    repo = ProductRepository(tmp_path / "products.json")
    assert len(repo.load()) == 3

def test_save_and_load(tmp_path):
    repo = ProductRepository(tmp_path / "products.json")
    data = [{"id": 10, "name": "테스트", "price": 100, "stock": 2}]
    repo.save(data)
    assert repo.load() == data

def test_invalid_json_structure(tmp_path):
    path = tmp_path / "products.json"
    path.write_text('{"not": "list"}', encoding="utf-8")
    with pytest.raises(ValueError, match="리스트"):
        ProductRepository(path).load()

def test_invalid_json_syntax(tmp_path):
    path = tmp_path / "products.json"
    path.write_text("{broken", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        ProductRepository(path).load()
