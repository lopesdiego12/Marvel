DROP TABLE if exists characters;

CREATE TABLE characters (
    id INT PRIMARY KEY  NOT NULL,
    name VARCHAR,
    description VARCHAR,
    modified VARCHAR,
    thumbnail VARCHAR,
    resourceURI VARCHAR,
    comics VARCHAR,
    series VARCHAR,
    stories VARCHAR,
    events VARCHAR,
    urls VARCHAR
    );