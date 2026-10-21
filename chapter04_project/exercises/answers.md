# 제4장 실습 과제와 모범 답안

## 과제 1. 상품 추가
`assets/app.js`의 `PRODUCTS` 배열에 다음 객체를 추가한다.

```javascript
{ id: 7, name: "모니터 받침대", price: 32000, icon: "🖥️" }
```

## 과제 2. 가격순 정렬
`renderProducts()` 함수의 `filtered` 계산 뒤에 다음 코드를 넣는다.

```javascript
filtered.sort((a, b) => a.price - b.price);
```

## 과제 3. 장바구니 수량 1개 감소
다음 함수를 `assets/app.js`에 추가한다. 수량이 1개이면 항목을 삭제한다.

```javascript
function decreaseQuantity(productId) {
  const quantity = cart.get(productId) || 0;
  if (quantity <= 1) cart.delete(productId);
  else cart.set(productId, quantity - 1);
  renderCart();
}
```

## 과제 4. 접근성 확인
검색 입력란에 연결된 `<label for="search">`와 `aria-live`의 역할을 설명한다.

**답:** `label`은 입력란의 의미를 전달하고 클릭으로 포커스를 이동시킨다. `aria-live`는 변경된 검색 결과와 장바구니 내용을 보조기술에 알리는 데 도움을 준다.
