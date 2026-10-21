# Python 리스트와 딕셔너리를 JSON 형식으로 저장한다.
import json
from pathlib import Path
# 실행 위치와 무관하게 프로젝트 폴더에 저장한다.
path = Path(__file__).resolve().parent / "products.json"
data = [{"id": 1, "name": "키보드", "price": 35000, "stock": 5}]
# 한글이 깨지지 않도록 ensure_ascii=False를 사용한다.
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
# 저장한 JSON 문자열을 다시 Python 객체로 변환한다.
loaded = json.loads(path.read_text(encoding="utf-8"))
print("저장 건수:", len(loaded))
