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
CREATE TABLE IF NOT EXISTS subordinates (
id_sub INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
name_sub VARCHAR(30) NOT NULL
);
INSERT INTO subordinates ( id_sub, name_sub) VALUES ( null, 'Ann Watson');
INSERT INTO subordinates ( id_sub, name_sub) VALUES ( null, 'Lionel Woods');
INSERT INTO subordinates ( id_sub, name_sub) VALUES ( null, 'Jane Black');
INSERT INTO subordinates ( id_sub, name_sub) VALUES ( null, 'Michael Crause');
INSERT INTO subordinates ( id_sub, name_sub) VALUES ( null, 'Robert Newman');
INSERT INTO subordinates ( id_sub, name_sub) VALUES ( null, 'Kate Ashley');
CREATE TABLE IF NOT EXISTS person_subord (
id_ps INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
id INT UNSIGNED NOT NULL,
id_sub INT UNSIGNED NOT NULL
);
INSERT INTO person_subord ( id_ps, id, id_sub) VALUES ( null, 1, 1);
INSERT INTO person_subord ( id_ps, id, id_sub) VALUES ( null, 1, 2);
INSERT INTO person_subord ( id_ps, id, id_sub) VALUES ( null, 1, 3);
INSERT INTO person_subord ( id_ps, id, id_sub) VALUES ( null, 1, 4);
INSERT INTO person_subord ( id_ps, id, id_sub) VALUES ( null, 2, 2);
INSERT INTO person_subord ( id_ps, id, id_sub) VALUES ( null, 2, 3);
INSERT INTO person_subord ( id_ps, id, id_sub) VALUES ( null, 3, 6);
INSERT INTO person_subord ( id_ps, id, id_sub) VALUES ( null, 4, 2);
INSERT INTO person_subord ( id_ps, id, id_sub) VALUES ( null, 4, 4);
INSERT INTO person_subord ( id_ps, id, id_sub) VALUES ( null, 4, 5);
ALTER TABLE staff.person ADD CONSTRAINT un_id_constraint UNIQUE (id);
ALTER TABLE staff.subordinates ADD CONSTRAINT un_id_sub_constraint UNIQUE (id_sub);
ALTER TABLE staff.person_subord ADD CONSTRAINT un_id_ps_constraint UNIQUE (id_ps);
ALTER TABLE person_subord
ADD CONSTRAINT id_sub_fk_constraint FOREIGN KEY (id_sub) REFERENCES subordinates (id_sub)
ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE person_subord
ADD CONSTRAINT id_fk_constraint FOREIGN KEY (id) REFERENCES person (id)
ON UPDATE CASCADE ON DELETE CASCADE;
SELECT subordinates.name_sub FROM (person JOIN person_subord USING (id)) JOIN subordinates USING (id_sub) WHERE person.last_name = 'Kirk';