/*Select correct database*/
use datarepresentation;

/*Create Film Table*/
CREATE table films(
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Title varchar(250),
    Year int,
    Genre varchar(250),
    Director varchar(250),
    Language varchar(250),
    Runtime int,
    IFCO varchar(250)
    );

/*Create Series Table*/
CREATE table series(
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Title varchar(250),
    Started int,
    Ended varchar(250),
    Genre varchar(250),
    Language varchar(250),
    Seasons int,
    Episodes int
    );
