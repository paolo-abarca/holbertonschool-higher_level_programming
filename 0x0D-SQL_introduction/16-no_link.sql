-- script that lists all the records in the second_table table of --
-- the hbtn_0c_0 database on your MySQL server --
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
