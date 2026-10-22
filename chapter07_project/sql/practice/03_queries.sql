-- 연습용 SQL: sql/ 바로 아래에 두면 컨테이너 첫 실행 때 자동 실행되므로 practice/ 폴더에 둔다.
-- MySQL 컨테이너의 기본 클라이언트 문자셋이 latin1이라 한글이 깨지지 않도록 utf8mb4로 지정한다.
SET NAMES utf8mb4;
-- 조회: 모든 상품을 가격순으로 출력한다.
SELECT id, name, price, stock FROM practice_products ORDER BY price DESC;
-- 조건 검색: 가격이 10만 원 미만인 상품을 찾는다.
SELECT name, price FROM practice_products WHERE price < 100000;
-- 등록: 새 상품을 추가한다.
INSERT INTO practice_products (name, price, stock) VALUES ('모니터', 220000, 8);
-- 수정: 재고가 있는 마우스의 재고를 하나 줄인다.
UPDATE practice_products SET stock = stock - 1 WHERE name = '마우스' AND stock > 0;
-- 삭제: 실습용 모니터를 삭제한다.
DELETE FROM practice_products WHERE name = '모니터';
-- 집계: 총 상품 종류와 재고 합계를 조회한다.
SELECT COUNT(*) AS product_count, SUM(stock) AS total_stock FROM practice_products;
