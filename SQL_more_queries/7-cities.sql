--
USE hbtn_0d_usa

CREATE TABLE if not EXISTS cities (
id INT UNIQUE  AUTO_INCREMENT PRIMARY KEY,
state_id INT not NULL,
name VARCHAR(256) not NULL,
FOREIGN KEY (state_id) REFERENCES states(id)
);