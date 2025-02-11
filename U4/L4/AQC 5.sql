*/ Advanced Query Challenge 5: Create an SQL query which returns cars whose CountryOfOrigin is Italy and LaunchPrice is less than £250,000. */
*/ Only include the fields; BrandName, ModelName and LaunchPrice; sort by LaunchPrice in ascending order */

SELECT BrandName, ModelName, LaunchPrice
FROM CarManufacturers, CarModels
WHERE CarManufacturers.CountryOfOrigin = 'Italy' AND CarModels.LaunchPrice < 250000 AND CarModels.BrandID = CarManufacturers.BrandID
ORDER BY LaunchPrice ASC;
