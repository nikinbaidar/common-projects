-- --defaults-group-suffix=BookStore
-- --table
--

/* This is a test script */

show databases;

show tables;

/* creating  and deleting tables */

CREATE TABLE books (
    book_id SMALLINT, /* serial number */
    book_title VARCHAR(20) NOT NULL,
    edition YEAR(4),
    genre VARCHAR(20),
    PRICE DECIMAL(4,2),
    PRIMARY KEY (book_id)
);

CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    age INT,
    address VARCHAR(15),
    gender VARCHAR(1),
    PRIMARY KEY (customer_id)
);

DROP TABLE customer; -- deleteing a table

/* Acquireing table info */

DESCRIBE customer;

DESCRIBE books;

/* changing the datatype of a column in a table */

ALTER TABLE customer
MODIFY customer_id SMALLINT AUTO_INCREMENT;

ALTER TABLE books
MODIFY COLUMN book_id INT;

/* inserting data into tables i.e. creating records */

INSERT INTO customer (name, age, address,gender)
VALUES ("Matt", 20, "Chelsea", 'M');

INSERT INTO books
VALUES( 573, "MEIN KAMPF", 1929 , "Auto-biography", 79.00);

/* Raising QUERIES */

SELECT * FROM customer;

SELECT * FROM books;

ALTER TABLE customer_info ADD COLUMN gender char(1) NOT NUll;

ALTER TABLE customer_info DROP COLUMN gender;

UPDATE customer
SET name = "Alexa"
WHERE customer_id = 2 ;

INSERT INTO customer_info VALUES(5,'Julia',30,'Chealsea','F');

UPDATE customer_info SET customer_name = 'Christian'
WHERE customer_id = 3;

UPDATE customer_info SET customer_address = "London"
WHERE customer_address = "Chelsea" OR customer_address = "Chealsea" ;

UPDATE customer
SET name="Lucy", gender='F'
WHERE customer_id = 3;

