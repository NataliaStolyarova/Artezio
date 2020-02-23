CREATE DATABASE IF NOT EXISTS staff;
USE staff;
CREATE TABLE IF NOT EXISTS person (
id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
p_rank VARCHAR(30) NOT NULL,
salary INT NOT NULL
);
INSERT INTO person ( id, first_name, last_name, p_rank, salary) VALUES ( null, 'James', 'Kirk', 'Captain', 50000);
INSERT INTO person ( id, first_name, last_name, p_rank, salary) VALUES ( null, 'Nyota', 'Uhura', 'Lieutenant', 25000);
INSERT INTO person ( id, first_name, last_name, p_rank, salary) VALUES ( null, 'Pavel', 'Chehov', 'Ensign', 15000);
INSERT INTO person ( id, first_name, last_name, p_rank, salary) VALUES ( null, 'Montgomery', 'Scott', 'Lieutenant Commander', 30000);
SELECT first_name, last_name FROM person WHERE salary < 30000;
SELECT first_name, last_name FROM person WHERE salary < 30000 AND p_rank='Lieutenant';






