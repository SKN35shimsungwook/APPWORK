"""제4장 정적 웹 프로젝트의 파일 구성과 연결 상태를 pytest로 검증한다."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_file(name: str) -> str:
    """프로젝트 루트에서 UTF-8 파일을 읽는다."""
    return (ROOT / name).read_text(encoding="utf-8")


def test_required_files_exist():
    # 브라우저 화면 구현에 필요한 파일이 모두 있는지 확인한다.
    for name in ("index.html", "assets/style.css", "assets/app.js", "pyproject.toml"):
        assert (ROOT / name).is_file(), f"필수 파일 없음: {name}"


def test_html_links_assets():
    # HTML이 실제 CSS 및 JavaScript 경로를 참조하는지 검사한다.
    html = read_file("index.html")
    assert 'href="assets/style.css"' in html
    assert 'src="assets/app.js"' in html
    assert 'lang="ko"' in html


def test_html_contains_ui_elements():
    # JavaScript에서 접근하는 요소의 ID가 HTML에 정의되어 있는지 확인한다.
    html = read_file("index.html")
    for element_id in ("search", "product-list", "cart-items", "cart-total", "clear-cart"):
        assert f'id="{element_id}"' in html


def test_js_has_product_and_cart_functions():
    # 상품 검색 및 장바구니 처리 함수의 존재를 검사한다.
    js = read_file("assets/app.js")
    for function_name in ("renderProducts", "addToCart", "removeFromCart", "renderCart"):
        assert f"function {function_name}(" in js


def test_css_has_responsive_rules():
    # 모바일 화면에 필요한 반응형 규칙이 포함되어 있는지 확인한다.
    css = read_file("assets/style.css")
    assert "@media" in css
    assert "grid-template-columns" in css


def test_no_unsafe_inner_html():
    # 동적 상품명을 innerHTML에 넣지 않는 기본 보안 원칙을 확인한다.
    js = read_file("assets/app.js")
    assert "innerHTML" not in js
