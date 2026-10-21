# 문자열, 정수, 불리언 자료형을 상품 데이터에 적용한다.
name = "무선 키보드"
price = 35000
stock = 12
is_available = stock > 0
# 각 변수의 값과 자료형 이름을 출력한다.
print("상품명:", name, type(name).__name__)
print("가격:", price, type(price).__name__)
print("재고:", stock, type(stock).__name__)
print("판매 가능:", is_available, type(is_available).__name__)
