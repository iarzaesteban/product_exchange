CREATE DATABASE trueque_db;
CREATE USER trueque_user WITH ENCRYPTED PASSWORD 'trueque_pass';
GRANT ALL PRIVILEGES ON DATABASE trueque_db TO trueque_user;
ALTER DATABASE trueque_db OWNER TO trueque_user;
