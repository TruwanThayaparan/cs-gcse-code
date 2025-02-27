-- https://www.101computing.net/online-sql/

SELECT * FROM suspects WHERE gender == "Male" AND shoe_size = 10.5 AND staff == "FALSE";
SELECT * FROM suspects WHERE firstname LIKE 'A%' AND lastname LIKE 'H%';
SELECT * FROM suspects WHERE gender == "Female" AND team == "Security";
SELECT * FROM suspects WHERE gender == "Female" AND height >= 1.85;
SELECT * FROM suspects WHERE nationality == "China" OR nationality == "Taiwan" OR nationality == "Singapore";
SELECT * FROM suspects WHERE (firstname LIKE "Oli%" OR lastname LIKE "Oli%") AND gender == "Male" AND staff == "FALSE";
SELECT * FROM suspects WHERE (nationality == "USA" OR nationality == "Canada" OR nationality == "England" OR nationality == "Australia") AND vegan == "TRUE";
SELECT * FROM suspects WHERE nationality == "Denmark" AND vegetarian == "FALSE" AND vegan == "FALSE";
SELECT * FROM suspects WHERE nationality == "France" AND gender == "Female" AND guest == "TRUE";
SELECT * FROM suspects WHERE (gender == "Female" AND 6 <= shoe_size and shoe_size <= 7) AND (nationality == "Peru" OR nationality == "Argentina" OR nationality == "Brazil" OR nationality == "Venezuela");
SELECT * FROM suspects WHERE nationality == "Ireland" AND gender == "Female";
SELECT * FROM suspects WHERE 1.70 <= height AND height <= 1.80 AND gender == "Male" AND team == "Gardening";
