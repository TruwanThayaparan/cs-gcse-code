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

INSERT INTO Books VALUES(1, "Harry Potter", "1997-06-26", "Fantasy", "0747532745", 1);
INSERT INTO Books VALUES(2, "The Last Kingdom", "2004-10-04", "History", "9780008139476", 2);
INSERT INTO Books VALUES(3, "Tinker Tailor Soldier Spy", "1974-06-14", "Novel", "9780340739617", 3);
INSERT INTO Books VALUES(4, "The Da Vinci Code", "2003-03-18", "Novel", "0307474275", 4);
INSERT INTO Books VALUES(5, "Prisoners of Geography", "2015-07-09", "Non-fiction", "1783961414", 5);
