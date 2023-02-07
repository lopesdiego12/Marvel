truncate table characters;

COPY characters
FROM '/tmp/characters_data.csv'
DELIMITER ',' CSV HEADER;