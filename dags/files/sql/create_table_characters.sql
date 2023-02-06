DROP TABLE if exists characters;

CREATE TABLE characters (
    id INT PRIMARY KEY  NOT NULL,
    name VARCHAR NOT NULL,
    description VARCHAR,
    modified VARCHAR,
    resourceURI VARCHAR,
    thumbnail VARCHAR,
    path VARCHAR,
    comics VARCHAR,
    items VARCHAR
    );