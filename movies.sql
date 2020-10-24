Drop Table movies;
Drop Table wiki;
CREATE TABLE movies (
Title TEXT PRIMARY KEY,
Streaming_Channel TEXT);
select * from movies;

CREATE TABLE wiki (
film TEXT PRIMARY KEY,
director TEXT);

select * from wiki;



Create view wiki_movie as
select m.title,w.director,m.streaming_channel
from movies m
join wiki w on m.title=w.film;
select * from wiki_movie;