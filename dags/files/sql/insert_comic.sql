COPY comics
FROM '/opt/airflow/dags/files/comics_data.csv'
DELIMITER ',' csv header;