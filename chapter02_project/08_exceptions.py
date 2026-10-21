# 잘못된 사용자 입력을 예외 처리로 안전하게 다룬다.
for raw in ["3", "abc", "0"]:
    try:
        # 입력 문자열을 정수로 변환한다.
        quantity = int(raw)
        # 0 이하의 주문 수량은 허용하지 않는다.
        if quantity <= 0:
            raise ValueError("1 이상의 수량을 입력해야 한다.")
        print("수량:", quantity)
    except ValueError as error:
        # 예외가 발생해도 프로그램이 중단되지 않는다.
        print("오류:", error)
