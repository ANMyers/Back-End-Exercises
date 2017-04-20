DELETE FROM AlbumArtist;
DELETE FROM AlbumGenre;
DELETE FROM AlbumSong;
DELETE FROM SongArtist;
DELETE FROM Album;
DELETE FROM Artist;
DELETE FROM Song;

DROP TABLE IF EXISTS AlbumArtist;
DROP TABLE IF EXISTS AlbumGenre;
DROP TABLE IF EXISTS AlbumSong;
DROP TABLE IF EXISTS SongArtist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Song;

CREATE TABLE Genre (
	GenreId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL
);

insert into Genre values (null, 'Rock');
insert into Genre values (null, 'Pop');
insert into Genre values (null, 'Alternative');

--SELECT * FROM Genre;

CREATE TABLE Artist (
	ArtistId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL
);

insert into Artist values (null, 'Nickelback');
insert into Artist values (null, 'Iron Maiden');
insert into Artist values (null, 'Beethoven');

--SELECT * FROM Artist;

CREATE TABLE Song (
	SongId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL
);

insert into Song values (null, 'The Trooper');
insert into Song values (null, 'Photograph');
insert into Song values (null, '5th Symphony');

--SELECT * FROM Song;

CREATE TABLE Album (
	AlbumId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name TEXT NOT NULL
);

insert into Album values (null, "Beethoven's Greatest Hits");
insert into Album values (null, "Nickelback's Greatest Hits");
insert into Album values (null, "Iron Maiden's Greatest Hits");

--SELECT * FROM Album;

CREATE TABLE AlbumGenre (
	AlbumGenreId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	AlbumId INTEGER NOT NULL,
	GenreId INTEGER NOT NULL,
	FOREIGN KEY (GenreId) REFERENCES Genre(GenreId),
	FOREIGN KEY (AlbumId) REFERENCES Album(AlbumId)
);

insert into AlbumGenre 
select null, a.AlbumId, g.GenreId
from Album a, Genre g 
where a.Name = "Iron Maiden's Greatest Hits" 
and g.Name = 'Rock';

insert into AlbumGenre 
select null, a.AlbumId, g.GenreId
from Album a, Genre g 
where a.Name = "Nickelback's Greatest Hits" 
and g.Name = 'Alternative';

insert into AlbumGenre 
select null, a.AlbumId, g.GenreId
from Album a, Genre g 
where a.Name = "Beethoven's Greatest Hits" 
and g.Name = 'Pop';

--SELECT * FROM AlbumGenre;

CREATE TABLE AlbumArtist (
	AlbumArtistId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	ArtistId INTEGER NOT NULL,
	AlbumId INTEGER NOT NULL,
	FOREIGN KEY (ArtistId) REFERENCES Artist(ArtistId),
	FOREIGN KEY (AlbumId) REFERENCES Album(AlbumId)
);

insert into AlbumArtist 
select null, a.AlbumId, ar.ArtistId
from Album a, Artist ar
where a.Name = "Nickelback's Greatest Hits" 
and ar.Name = 'Nickelback';

insert into AlbumArtist 
select null, a.AlbumId, ar.ArtistId
from Album a, Artist ar
where a.Name = "Beethoven's Greatest Hits" 
and ar.Name = 'Beethoven';

insert into AlbumArtist
select null, a.AlbumId, ar.ArtistId
from Album a, Artist ar 
where a.Name = "Iron Maiden's Greatest Hits" 
and ar.Name = 'Iron Maiden';

--SELECT * FROM AlbumArtist;

CREATE TABLE AlbumSong (
	AlbumSongId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	SongId INTEGER NOT NULL,
	AlbumId INTEGER NOT NULL,
	Featured INTEGER NOT NULL,
	FOREIGN KEY (SongId) REFERENCES Song(SongId),
	FOREIGN KEY (AlbumId) REFERENCES Album(AlbumId)
);

insert into AlbumSong 
select null, a.AlbumId, s.SongId, 0
from Album a, Song s
where a.Name = "Nickelback's Greatest Hits" 
and s.Name = 'Photograph';

insert into AlbumSong 
select null, a.AlbumId, s.SongId, 0
from Album a, Song s
where a.Name = "Beethoven's Greatest Hits" 
and s.Name = '5th Symphony';

insert into AlbumSong
select null, a.AlbumId, s.SongId, 0
from Album a, Song s 
where a.Name = "Iron Maiden's Greatest Hits" 
and s.Name = 'The Trooper';

--SELECT * FROM AlbumGenre;

CREATE TABLE SongArtist (
	SongArtistId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	ArtistId INTEGER NOT NULL,
	SongId INTEGER NOT NULL,
	Featured INTEGER NOT NULL,
	FOREIGN KEY (ArtistId) REFERENCES Artist(ArtistId),
	FOREIGN KEY (SongId) REFERENCES Song(SongId)
);

insert into SongArtist 
select null, s.SongId, a.ArtistId, 0
from Song s, Artist a
where s.Name = "Photograph" 
and a.Name = 'Nickelback';

insert into SongArtist 
select null, s.SongId, a.ArtistId, 0
from Song s, Artist a
where s.Name = "5th Symphony" 
and a.Name = 'Beethoven';

insert into SongArtist
select null, s.SongId, a.ArtistId, 0
from Song s, Artist a 
where s.Name = "The Trooper" 
and a.Name = 'Iron Maiden';

--SELECT * FROM SongArtist;