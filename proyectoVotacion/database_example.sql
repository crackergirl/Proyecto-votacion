CREATE DATABASE patata;
use patata;

CREATE TABLE users(
    id int not null AUTO_INCREMENT,
    username varchar(100) NOT NULL,
    pass varchar(100) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO users(username, pass)
VALUES ("John", "Andersen"), ("Emma", "Smith");