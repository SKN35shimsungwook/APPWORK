"""JSON 파일을 읽고 저장하는 데이터 접근 계층."""
import json
from pathlib import Path

DEFAULT_PRODUCTS = [
    {"id": 1, "name": "무선 키보드", "price": 31500, "stock": 5},
    {"id": 2, "name": "무선 마우스", "price": 19000, "stock": 8},
    {"id": 3, "name": "모니터", "price": 190000, "stock": 0},
]

class ProductRepository:
    """상품 목록을 JSON 파일에 저장하고 다시 읽는다."""

    def __init__(self, path: str | Path):
        # 저장 파일 경로를 Path 객체로 변환한다.
        self.path = Path(path)

    def load(self) -> list[dict]:
        # 파일이 없다면 기본 상품 목록을 복사하여 반환한다.
        if not self.path.exists():
            return [product.copy() for product in DEFAULT_PRODUCTS]
        # UTF-8 인코딩으로 JSON 파일을 읽는다.
        with self.path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        # 저장 데이터가 리스트인지 검사한다.
        if not isinstance(data, list):
            raise ValueError("상품 데이터는 리스트여야 합니다.")
        return data

    def save(self, products: list[dict]) -> None:
        # data 폴더가 없다면 자동으로 생성한다.
        self.path.parent.mkdir(parents=True, exist_ok=True)
        # 한글을 보존하고 들여쓰기를 적용해 저장한다.
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(products, file, ensure_ascii=False, indent=2)
