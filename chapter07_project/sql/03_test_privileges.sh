#!/bin/bash
# pytest(pytest-django)는 test_<DB이름> 테스트 DB를 만들었다 지운다.
# MySQL 이미지는 MYSQL_USER에게 MYSQL_DATABASE 권한만 주므로, 테스트 DB 권한을 추가로 준다.
# 볼륨이 비어 있는 첫 실행에서만 01_schema.sql, 02_seed.sql 다음에 자동 실행된다.
set -e
mysql --protocol=socket -uroot -p"${MYSQL_ROOT_PASSWORD}" <<EOSQL
GRANT ALL PRIVILEGES ON \`test_${MYSQL_DATABASE}\`.* TO '${MYSQL_USER}'@'%';
FLUSH PRIVILEGES;
EOSQL
