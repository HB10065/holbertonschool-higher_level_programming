--
CREATE DATABASE if not EXISTS hbtn_0d_2;
USE hbtn_0d_usa;
CREATE TABLE if not EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) not NULL
);