DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Books;

CREATE TABLE Authors(
    AuthorID INTEGER, 
    FirstName TEXT, 
    Surname TEXT,
    DateOfBirth DATE,
    Age INTEGER,
    CountryOfOrigin TEXT
);

CREATE TABLE Books(
    BookID INTEGER,
    BookTitle TEXT,
    PublishedDate DATE,
    Genre TEXT,
    ISBN TEXT,
    AuthorID INTEGER
);

INSERT INTO Authors VALUES(1, "Joanne", "Rowling", "1965-07-31", 55, "Scotland");
INSERT INTO Authors VALUES(2, "Bernard", "Cornwell", "1944-02-23", 77, "England");
INSERT INTO Authors VALUES(3, "John", "Le Carre", "1931-10-19", 90, "England");
INSERT INTO Authors VALUES(4, "Dan", "Brown", "1964-06-22", 56, "USA");
INSERT INTO Authors VALUES(5, "Tim", "Marshall", "1959-05-01", 61, "England");

INSERT INTO Books VALUES
(1, "Harry Potter and the Philosopher's Stone", "1997-06-26", "Fiction", "9781408855652", 1);
INSERT INTO Books VALUES
(2, "Harry Potter and the Chamber of Secrets", "1998-07-02", "Fiction", "0747538484", 1);
INSERT INTO Books VALUES
(3, "Sharpe's Triumph", "1998-02-26", "Fiction", "0007425805", 2);
INSERT INTO Books VALUES
(4, "The Last Kingdom", "2004-10-04", "Fiction", "0007218016", 2);
INSERT INTO Books VALUES
(5, "Agent Running in the Field", "2020-08-20", "Fiction", "9780241986547", 3);
INSERT INTO Books VALUES
(6, "Tinker Tailor Soldier Spy", "1974-06-01", "Thriller", "0340993766", 3);
INSERT INTO Books VALUES
(7, "The Da Vinci Code", "2009-08-28", "Thriller", "0552159719", 4);
INSERT INTO Books VALUES
(8, "Angels and Demons", "2009-08-28", "Thriller", "055216089X", 4);
INSERT INTO Books VALUES
(9, "The Lost Symbol", "2010-07-22", "Thriller", "9780552149525", 4);
INSERT INTO Books VALUES
(10, "Prisoners of Geography", "2016-06-02", "Political", "9781783962433", 5);
