-- script that lists all the cities contained in the hbtn_0d_usa database --
-- script that lists all the cities contained in the hbtn_0d_usa database --
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
