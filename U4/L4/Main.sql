DROP TABLE iF EXISTS CarManufacturers;

CREATE TABLE CarManufacturers(BrandID INT, BrandName TEXT, CountryOfOrigin TEXT, Category TEXT, Founded INT);

INSERT INTO CarManufacturers VALUES(1, 'Volvo', 'Sweden', 'Family',1927);
INSERT INTO CarManufacturers VALUES(2, 'Ford', 'America', 'Value',1903);
INSERT INTO CarManufacturers VALUES(3,' Mercedes',' Germany', 'Luxury',1926);
INSERT INTO CarManufacturers VALUES(4, 'BMW', 'Germany', 'Luxury',1916);
INSERT INTO CarManufacturers VALUES(5, 'VW', 'Germany', 'Value',1937);
INSERT INTO CarManufacturers VALUES(6, 'Ferrari', 'Italy', 'Sports cars',1947);
INSERT INTO CarManufacturers VALUES(7, 'Lamborghini', 'Italy', 'Sports cars',1947);
INSERT INTO CarManufacturers VALUES(8, 'Jaguar', 'England', 'Luxury',1922);
INSERT INTO CarManufacturers VALUES(9, 'Mclaren', 'England', 'Sports cars', 1963);
INSERT INTO CarManufacturers VALUES(10, 'Rolls Royce', 'England', 'Uber Luxury', 1906);

CREATE TABLE CarModels(CarID INT, ModelName TEXT, NumberOfDoors INT, YearOfRelease INT, LaunchPrice FLOAT, BrandID INT);
INSERT INTO CarModels VALUES(1, 'Focus', 5, 1998, 13995, 2);
INSERT INTO CarModels VALUES(2, 'Escort', 5, 1968, 679, 2);
INSERT INTO CarModels VALUES(3,'Mustang Mach-E', 5, 2021, 40000, 2);
INSERT INTO CarModels VALUES(4,'S cLass', 4, 2021, 78705, 3);
INSERT INTO CarModels VALUES(5,'E cLass', 4, 2019, 37795, 3);
INSERT INTO CarModels VALUES(6, 'XC40', 5, 2018, 27610, 1);
INSERT INTO CarModels VALUES(7, '3 Series', 5, 1982, 35000, 4);
INSERT INTO CarModels VALUES(8, '7 Series', 4, 1977, 80000, 4);
INSERT INTO CarModels VALUES(9, 'Tiguan', 5, 2007, 24010, 5);
INSERT INTO CarModels VALUES(10, 'Golf', 5, 1974, 20280, 5);
INSERT INTO CarModels VALUES(11, 'Enzo', 2, 2002, 450000, 6);
INSERT INTO CarModels VALUES(12, 'F40', 2, 1987, 250000, 6);
INSERT INTO CarModels VALUES(13, 'Diablo', 2, 1990, 200000, 7);
INSERT INTO CarModels VALUES(14, 'Countach', 2, 1970, 100000, 7);
INSERT INTO CarModels VALUES(15, 'iPace', 4, 2007, 64625, 8);
INSERT INTO CarModels VALUES(16,'F Type', 2, 2013, 52635, 8);
INSERT INTO CarModels VALUES(17,'720', 2, 2017, 215055, 9);
INSERT INTO CarModels VALUES(18, 'P1', 2, 2013, 866000, 9);
INSERT INTO CarModels VALUES(19,'720', 2, 2017, 215055, 9);
INSERT INTO CarModels VALUES(20, 'Ghost', 4, 2020, 233235, 10);
INSERT INTO CarModels VALUES(21, 'Cullinan', 4, 2018, 264000, 10);
INSERT INTO CarModels VALUES(20, 'Wraith', 4, 2013, 258000, 10);

SELECT BrandName, CountryOfOrigin, ModelName, LaunchPrice
FROM CarManufacturers, CarModels
WHERE CarModels.BrandID = 2 AND CarManufacturers.BrandID = 2
ORDER BY BrandName ASC;
