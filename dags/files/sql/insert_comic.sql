truncate table comics;
COPY comics
FROM '/tmp/comics_data.csv'
DELIMITER ',' CSV HEADER;