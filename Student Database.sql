CREATE TABLE Students(
Student_ID INT PRIMARY KEY,
Student_Name VARCHAR (100),
Student_email VARCHAR(100) UNIQUE,
Student_phone VARCHAR (30),
Student_address VARCHAR (100)
);

CREATE TABLE Courses(
Course_ID INT PRIMARY KEY,
Course_Name VARCHAR(50),
Course_Description VARCHAR (50),
Credit_Hours INT,
Course_Department VARCHAR (50)
);


CREATE TABLE Departments(
Department_ID INT PRIMARY KEY,
Department_Name VARCHAR(50),
Department_Chairman VARCHAR(50),
Department_Office VARCHAR (50)
);


CREATE TABLE Professors(
Professor_ID INT PRIMARY KEY,
Professor_Name VARCHAR(50),
Professor_email VARCHAR(50) UNIQUE,
Professor_phone VARCHAR (20),
Professor_Office VARCHAR(50)
);

CREATE TABLE Sections(
Section_ID INT PRIMARY KEY,
Course_ID INT, 
Professor_ID INT,
Semester VARCHAR(20),
Section_Year INT,
Section_Capacity INT,
FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID) ON DELETE CASCADE,
FOREIGN KEY (Professor_ID) REFERENCES Professors(Professor_ID) ON DELETE CASCADE
);

CREATE TABLE Enrollments(
Enrollment_ID INT PRIMARY KEY,
Student_ID INT,
Section_ID INT,
Grade VARCHAR(2),
FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID) ON DELETE CASCADE,
FOREIGN KEY (Section_ID) REFERENCES Sections(Section_ID) ON DELETE CASCADE
);

CREATE TABLE Prerequisites(
Course_ID INT,
Prerequisites_ID INT,
FOREIGN KEY (Prerequisites_ID) REFERENCES Courses(Course_ID) ON DELETE CASCADE,
FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID) ON DELETE CASCADE
);
DROP TABLE Prerequisites

CREATE TABLE Transcript(
Student_ID INT,
Course_ID INT,
Grade VARCHAR(2),
FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID) ON DELETE CASCADE,
FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID) ON DELETE CASCADE
);

CREATE TABLE Department_Courses(
Department_ID INT,
Course_ID INT,
FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID) ON DELETE CASCADE,
FOREIGN KEY (Department_ID) REFERENCES Courses(Course_ID) ON DELETE CASCADE
);


SELECT * FROM Students
SELECT * FROM Courses
INSERT INTO Courses VALUES(001, 'Math 101', 'Introduction to Math', 3, 'Mathematics');
INSERT INTO Courses VALUES(002, 'English 101', 'Advanced Poetry', 4, 'English');
INSERT INTO Courses VALUES(003, 'Physics 301', 'Mechanics', 4, 'Physics');
INSERT INTO Courses VALUES(004, 'History 101', 'World History', 3, 'History');
INSERT INTO Courses VALUES(005, 'CS 202', 'Programming Fundamentals', 4, 'Computer Science');

SELECT * FROM Departments
INSERT INTO Departments VALUES(001, 'Mathematics', 'Dr. Johnson', 'MATH 101');
INSERT INTO Departments VALUES(002, 'English', 'Dr. Anderson', 'ENG 201');
INSERT INTO Departments VALUES(003, 'Physics', 'Dr. Williams', 'PHY 301');
INSERT INTO Departments VALUES(004, 'History', 'Dr. Davis', 'HIS 101');
INSERT INTO Departments VALUES(005, 'Computer Science', 'Dr. Wilson', 'CSD 101');


SELECT * FROM Professors
INSERT INTO Professors VALUES(001, 'Dr. Johnson', 'johnson@example.com', '555-123-4567', 'MATH 101');
INSERT INTO Professors VALUES(002, 'Dr. Anderson', 'anderson@example.com', '555-987-6543', 'ENG 201');
INSERT INTO Professors VALUES(003, 'Dr. Williams', 'williams@example.com', '555-555-5555', 'PHY 301');
INSERT INTO Professors VALUES(004, 'Dr. Davis', 'davis@example.com', '555-111-2222', 'HIS 101');
INSERT INTO Professors VALUES(005, 'Dr. Wilson', 'wilson@example.com', '555-777-8888', 'CSD 101');
SELECT * FROM Professors ORDER BY Professor_Name, Professor_email ASC;


SELECT * FROM Sections
INSERT INTO Sections VALUES(001, 1, 1, 'Fall', '2023-04-08', 50);
INSERT INTO Sections VALUES(002, 2, 2, 'Fall', '2023-04-09', 40);
INSERT INTO Sections VALUES(003, 3, 3, 'Fall', '2023-05-08', 30);
INSERT INTO Sections VALUES(004, 4, 4, 'Fall', '2023-07-09', 35);
INSERT INTO Sections VALUES(005, 5, 5, 'Fall', '2023-09-08', 25);
UPDATE Sections SET Semester = 'Summer'

DELETE FROM Sections WHERE Section_ID = 001 
DELETE FROM Sections WHERE Section_ID = 003 
DELETE FROM Sections WHERE Section_ID = 005

SELECT * FROM Sections WHERE Semester_Capacity > 30;

SELECT * FROM Enrollments
INSERT INTO Enrollments VALUES(001, 1, 1, 'A');
INSERT INTO Enrollments VALUES(002, 2, 1, 'B');
INSERT INTO Enrollments VALUES(003, 3, 2, 'A-');
INSERT INTO Enrollments VALUES(004, 4, 3, 'B+');
INSERT INTO Enrollments VALUES(005, 5, 4, 'C');

SELECT * FROM Prerequisites
INSERT INTO Prerequisites VALUES(002, 1);
INSERT INTO Prerequisites VALUES(003, 1);
INSERT INTO Prerequisites VALUES(003, 2);
INSERT INTO Prerequisites VALUES(004, 2);
INSERT INTO Prerequisites VALUES(005, 3);

DELETE FROM Prerequisites

SELECT * FROM Transcript
INSERT INTO Transcript VALUES(001, 1, 'A');
INSERT INTO Transcript VALUES(001, 2, 'A-');
INSERT INTO Transcript VALUES(002, 1, 'B');
INSERT INTO Transcript VALUES(002, 3, 'B+');
INSERT INTO Transcript VALUES(003, 2, 'C+');
SELECT * FROM Transcript ORDER BY course_ID ASC;

SELECT * FROM Department_Courses
INSERT INTO Department_Courses VALUES(001, 1);
INSERT INTO Department_Courses VALUES(002, 2);
INSERT INTO Department_Courses VALUES(003, 3);
INSERT INTO Department_Courses VALUES(004, 4);
INSERT INTO Department_Courses VALUES(005, 5);
