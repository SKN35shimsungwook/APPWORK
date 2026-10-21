"use strict";
// 상품 데이터는 제3장의 JSON 상품 관리 개념을 브라우저 배열로 확장한 예시이다.
const PRODUCTS = [
  { id: 1, name: "무선 마우스", price: 19000, icon: "🖱️" },
  { id: 2, name: "기계식 키보드", price: 79000, icon: "⌨️" },
  { id: 3, name: "USB-C 허브", price: 35000, icon: "🔌" },
  { id: 4, name: "노트북 거치대", price: 28000, icon: "💻" },
  { id: 5, name: "웹캠", price: 49000, icon: "📷" },
  { id: 6, name: "헤드셋", price: 59000, icon: "🎧" }
];
// 상품 ID별 수량을 Map 객체에 저장한다. 새로고침하면 초기화된다.
const cart = new Map();
const productList = document.querySelector("#product-list");
const searchInput = document.querySelector("#search");
const cartItems = document.querySelector("#cart-items");
const cartTotal = document.querySelector("#cart-total");
const clearButton = document.querySelector("#clear-cart");
// 한국 원화 표기 함수를 한 곳에 정의한다.
const formatPrice = (price) => `${price.toLocaleString("ko-KR")}원`;
// 검색어를 포함하는 상품만 카드로 표시한다.
function renderProducts(keyword = "") {
  const filtered = PRODUCTS.filter((product) => product.name.toLowerCase().includes(keyword.trim().toLowerCase()));
  productList.replaceChildren();
  if (filtered.length === 0) {
    const message = document.createElement("p");
    message.className = "empty";
    message.textContent = "검색 결과가 없습니다.";
    productList.append(message);
    return;
  }
  filtered.forEach((product) => {
    const card = document.createElement("article");
    card.className = "product-card";
    const icon = document.createElement("div");
    icon.className = "product-icon";
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = product.icon;
    const title = document.createElement("h3");
    title.textContent = product.name;
    const price = document.createElement("p");
    price.className = "price";
    price.textContent = formatPrice(product.price);
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = "장바구니 담기";
    button.addEventListener("click", () => addToCart(product.id));
    card.append(icon, title, price, button);
    productList.append(card);
  });
}
// 상품을 장바구니에 추가하고 화면을 갱신한다.
function addToCart(productId) {
  cart.set(productId, (cart.get(productId) || 0) + 1);
  renderCart();
}
// 장바구니에서 특정 상품 한 종류를 제거한다.
function removeFromCart(productId) {
  cart.delete(productId);
  renderCart();
}
// 수량과 가격을 계산해 장바구니를 다시 그린다.
function renderCart() {
  cartItems.replaceChildren();
  let total = 0;
  if (cart.size === 0) {
    const empty = document.createElement("li");
    empty.textContent = "장바구니가 비어 있습니다.";
    cartItems.append(empty);
  }
  cart.forEach((quantity, productId) => {
    const product = PRODUCTS.find((item) => item.id === productId);
    if (!product) return;
    const subtotal = product.price * quantity;
    total += subtotal;
    const li = document.createElement("li");
    li.append(document.createTextNode(`${product.name} × ${quantity} — ${formatPrice(subtotal)}`));
    const removeButton = document.createElement("button");
    removeButton.type = "button";
    removeButton.className = "remove";
    removeButton.textContent = "삭제";
    removeButton.setAttribute("aria-label", `${product.name} 삭제`);
    removeButton.addEventListener("click", () => removeFromCart(productId));
    li.append(removeButton);
    cartItems.append(li);
  });
  cartTotal.textContent = `총액: ${formatPrice(total)}`;
}
// 입력할 때마다 검색 결과를 갱신한다.
searchInput.addEventListener("input", (event) => renderProducts(event.target.value));
// 장바구니 전체 비우기 버튼을 연결한다.
clearButton.addEventListener("click", () => { cart.clear(); renderCart(); });
// 최초 진입 시 상품 목록과 빈 장바구니를 출력한다.
renderProducts();
renderCart();
