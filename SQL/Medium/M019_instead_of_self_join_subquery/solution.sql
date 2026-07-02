
### Mehtod 1 using group by and having 
    
SELECT 
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);


### Method 2 using correlated subquery 
    
SELECT 
  ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance AS i1
WHERE (
  SELECT COUNT(*) 
  FROM Insurance AS i2 
  WHERE i1.tiv_2015 = i2.tiv_2015
) > 1
AND (
  SELECT COUNT(*) 
  FROM Insurance AS i3 
  WHERE i3.lat = i1.lat 
    AND i3.lon = i1.lon
) = 1;
