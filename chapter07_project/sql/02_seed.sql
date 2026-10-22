-- MySQL 컨테이너의 기본 클라이언트 문자셋이 latin1이라 한글이 깨지지 않도록 utf8mb4로 지정한다.
SET NAMES utf8mb4;
-- 초기 데이터는 처음 볼륨을 생성할 때만 삽입된다.
INSERT INTO practice_products (name, price, stock) VALUES
('노트북', 1200000, 5),
('마우스', 25000, 30),
('키보드', 65000, 12);
