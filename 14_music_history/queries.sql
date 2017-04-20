/*
Music History Exercise 14
*/

--1. Query all of the entries in the Genre table
select * from Genre;

--2. Using the INSERT statement, add one of your favorite artists to the Artist table.
insert into Artist values (null, 'Iron Maiden', 1983);

select * from Album;

--3. Using the INSERT statement, add one, or more, albums by your artist to the Album table.
insert into Album values (null, 'The Trooper', '03/20/1982', 2540, 'TBD', 28, 2);

select * from Song;

--4. Using the INSERT statement, add some songs that are on that album to the Song table.
insert into Song values (null, 'The Trooper', 460, '03/20/1982',  2, 28, 23);

/*
SELECT a.Title, s.Title 
FROM Album a 
LEFT JOIN Song s 
ON s.AlbumId = a.AlbumId;
*/

/*
SELECT a.Title, s.Title 
FROM Song s 
LEFT JOIN Album a 
ON s.AlbumId = a.AlbumId;
*/

select * from Artist;

/*
5. Write a SELECT query that provides the song titles, album title, 
and artist name for all of the data you just entered in. 
Use the LEFT JOIN keyword sequence to connect the tables, 
and the WHERE keyword to filter the results to the album and artist you added.
*/
select a.Title 'Album Title', ar.ArtistName 'Artist Name', s.Title 'Song Title' 
from Song s 
left join Album a 
on s.AlbumId = a.AlbumId 
left join Artist ar 
on s.ArtistId = ar.ArtistId 
where ar.ArtistName = 'Iron Maiden';

/*
6. Write a SELECT statement to display how many songs exist for each album. 
You'll need to use the COUNT() function and the GROUP BY keyword sequence.
*/
select count(s.SongId) 'Number Of Songs', a.Title 'Album Title'
from Song s, Album a
where s.AlbumId = a.AlbumId 
group by a.Title;

/*
7. Write a SELECT statement to display how many songs exist for each artist. 
You'll need to use the COUNT() function and the GROUP BY keyword sequence.
*/
select count(s.SongId) 'Number of Songs', a.ArtistName 'Artist Name'
from Song s, Artist a
where s.ArtistId = a.ArtistId 
group by a.ArtistName;

/*
8. Write a SELECT statement to display how many songs exist for each genre.
 You'll need to use the COUNT() function and the GROUP BY keyword sequence.
*/
select count(s.SongId) 'Number of Songs', g.Label 'Genre'
from Song s, Genre g
where s.GenreId = g.GenreId 
group by g.Label;

/*
9. Using MAX() function, write a select statement to find the album with the longest duration. 
The result should display the album title and the duration.
*/
select max(a.AlbumLength) 'Length of Album', a.Title 'Album Title'
from Album a;

/*
10. Using MAX() function, write a select statement to find the song with the longest duration. 
The result should display the song title and the duration.
*/
select max(s.SongLength) 'Length of Song', s.Title 'Song Title', a.Title 'Album Title'
from Song s, Album a 
where s.AlbumId = a.AlbumId;


