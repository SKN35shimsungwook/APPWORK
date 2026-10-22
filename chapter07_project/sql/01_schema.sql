-- Docker 볼륨이 비어 있는 최초 실행에서만 자동 실행한다.
-- Django ORM 테이블과 충돌하지 않도록 별도 연습 테이블을 만든다.
CREATE TABLE IF NOT EXISTS practice_products (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price INT NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    PRIMARY KEY (id),
    CONSTRAINT chk_practice_price CHECK (price >= 0),
    CONSTRAINT chk_practice_stock CHECK (stock >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
