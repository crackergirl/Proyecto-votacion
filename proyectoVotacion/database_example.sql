CREATE DATABASE voting_data;
use voting_data;

CREATE TABLE votation (
    id int not null AUTO_INCREMENT,
    category ENUM('cat', 'dog') NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO votation(category)
VALUES ('cat'), ('dog'),('cat'),('dog'), ('dog');