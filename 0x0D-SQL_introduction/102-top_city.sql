-- script showing the temperature of the 3 main cities --
-- during July and August sorted by temperature (descending) --
SELECT `city`, AVG(`value`) 'avg_temp' FROM `temperatures` WHERE `month` = 7 OR `month` = 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;
