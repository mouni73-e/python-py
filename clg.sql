CREATE DATABASE colege;

USE colege;

CREATE TABLE student(
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(50),
    email VARCHAR(100) UNIQUE
);
INSERT INTO student(student_id, name, age, department, email)
VALUES
(101, 'Rahul', 20, 'Computer Science', 'rahul@gmail.com'),
(102, 'Priya', 21, 'Commerce', 'priya@gmail.com'),
(103, 'Arjun', 19, 'Management', 'arjun@gmail.com'),
(104, 'Sneha', 22, 'Electronics', 'sneha@gmail.com');

SELECT * FROM student;
ALTER TABLE student
ADD phone_number VARCHAR(15);
DESC student;
ALTER TABLE student
MODIFY COLUMN age TINYINT;

DESC student;

ALTER TABLE student
RENAME COLUMN department TO branch;


ALTER TABLE student
DROP COLUMN phone_number;

DESC student;

INSERT INTO student(student_id, name, age, branch, email)
VALUES
(1, 'mouniii', 65, 'AIi', 'rahull@gmail.com'),
(2, 'mamu', 45, 'CSEe', 'priyaq@gmail.com'),
(3, 'Arun', 92, 'ECEe', 'arjunf@gmail.com'),
(4, 'Sne', 5, 'ITt', 'snehag@gmail.com'),
(5, 'appu', 2, 'MEH', 'mounig@gmail.com');

SELECT * FROM student;
