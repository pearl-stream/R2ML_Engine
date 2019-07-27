#This script creates and fills tables with example data


#Drop tables if they exist
DROP TABLE IF EXISTS COURSE_STUDENT;

DROP TABLE IF EXISTS STUDENT;

DROP TABLE IF EXISTS COURSE;

DROP TABLE IF EXISTS PROFESSOR;


#Create table Prof
CREATE TABLE PROFESSOR(
    ProfID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255),
    FirstName varchar(255),
    University varchar(255),
    PRIMARY KEY (ProfID)
);


#Create table Course
CREATE TABLE COURSE(
    CourseID int NOT NULL AUTO_INCREMENT,
    Name varchar(255),
    Description TEXT(1000),
    ECTS int,
    ProfID int,
    FOREIGN KEY (ProfID) REFERENCES PROFESSOR(ProfID),
    PRIMARY KEY (CourseId)
);



#Create table STUDENT
CREATE TABLE STUDENT(
    StudentID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255),
    FirstName varchar(255),
    Field varchar(255),
    AverageGrade decimal,
    PRIMARY KEY (StudentID)
);



#Create table COURSE_STUDENT
CREATE TABLE COURSE_STUDENT(
    StudentID int NOT NULL,
    CourseID int NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES STUDENT(StudentID),
    FOREIGN KEY (CourseID) REFERENCES COURSE(CourseID)
);



#------------------------------------------------------------
#Fill tables with data

INSERT INTO PROFESSOR (LastName, FirstName, University)
  VALUES
  ('Jones', 'Henry', 'Connecticut'),
  ('Langdon', 'Robert', 'Harvard University'),
  ('Keating', 'John', NULL);


INSERT INTO COURSE (Name, Description, ECTS, ProfID)
  VALUES
  ('Archeology', 'Archaeology, or archeology, is the study of human activity through the recovery and analysis of material culture. The archaeological record consists of artifacts, architecture, biofacts or ecofacts and cultural landscapes. Archaeology can be considered both a social science and a branch of the humanities. In North America archaeology is a sub-field of anthropology, while in Europe it is often viewed as either a discipline in its own right or a sub-field of other disciplines.', 8, 1),
  ('Symbology', 'A symbol is a mark, sign or word that indicates, signifies, or is understood as representing an idea, object, or relationship. Symbols allow people to go beyond what is known or seen by creating linkages between otherwise very different concepts and experiences. All communication (and data processing) is achieved through the use of symbols. Symbols take the form of words, sounds, gestures, ideas or visual images and are used to convey other ideas and beliefs. For example, a red octagon may be a symbol for "STOP". On a map, a blue line might represent a river. Numerals are symbols for numbers. Alphabetic letters may be symbols for sounds. Personal names are symbols representing individuals. A red rose may symbolize love and compassion. The variable x, in a mathematical equation, may symbolize the position of a particle in space.', 4, 2),
  ('English', 'English studies (usually called simply English) is an academic discipline taught in primary, secondary, and post-secondary education in English-speaking countries; it is not to be confused with English taught as a foreign language, which is a distinct discipline. English includes: the study of literature written in the English language (especially novels, short stories, and poetry), the majority of which comes from Britain, the United States, and Ireland (although English-language literature from any country may be studied, and local or national literature is usually emphasized in any given country); English composition, including writing essays, short stories, and poetry; English language arts, including the study of grammar, usage, and style; and English sociolinguistics, including discourse analysis of written and spoken texts in the English language, the history of the English language, English language learning and teaching, and the study of World Englishes. English linguistics (syntax, morphology, phonetics, phonology, etc.) is usually treated as a distinct discipline, taught in a department of linguistics.', 6, 3);

INSERT INTO STUDENT (LastName, FirstName, Field, AverageGrade)
  VALUES
  ('Adomski', 'Adam', 'Alchemy', 1.0),
  ('Berowski', 'Berta', 'Business', 2.3),
  ('Christophski', 'Christoph', 'Computer Science', 3.4),
  ('Detlevski', 'Detlev', 'Data Science', 4.0);

INSERT INTO COURSE_STUDENT
  VALUES
  (1,1),
  (1,2),
  (2,2),
  (2,3),
  (3,1),
  (3,3),
  (4,1),
  (4,2),
  (4,3);
