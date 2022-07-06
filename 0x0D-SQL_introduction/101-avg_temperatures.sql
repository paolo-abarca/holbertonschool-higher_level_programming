-- script that shows the average temperature (Fahrenheit) --
-- per city sorted by temperature (descending) --
SELECT `city`, AVG(`value`) 'avg_temp' FROM temperatures GROUP BY `city` ORDER BY `avg_temp` DESC;
