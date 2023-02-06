CREATE TABLE IF NOT EXISTS characters (
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