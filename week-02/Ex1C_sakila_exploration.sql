/*
Sakila stores information about films, actors, customers,
and rentals for a movie rental business.
*/
USE sakila;
SELECT * From actor;

SELECT * FROM actor; -- Retrieved 200 records
SELECT * FROM film;
SELECT * FROM film; -- Retrieved 1000 records

/*
a) The actor table contains each actor's ID, first name,
last name, and the date and time the record was last updated.
b) The film table contains each film's ID, title, description,
release year, language ID, original language ID, rental duration,
rental rate, length, replacement cost, rating, special features,
and the date and time the record was last updated.
c) The fim actor table contains both actor_id and film_id
d)The rental table shows reant dates, and IDs. the dates are easy to read.
To see movie titles or customer names, I need information from related tables.
e) The inventory table tracks film copies at each store.
It contains inventory_id film_id , store_id, and lastupdate.
f) I need the rental, inventory, and fim table.
The rental table provides the rental date and inventory_id 
The inventory table connects inventory_id to film_id.
The film table provides the movie title through film_id.
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;



