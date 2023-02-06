# Marvel


## Docs
https://developer.marvel.com/docs
- GET /v1/public/characters
- GET /v1/public/comics
- Question: Collect the data necessary to see all characters and the quantity of comics in which they
appear

Character name: text 

quantity of comics they appear in: int

## Architecture

* [Solution Design](https://raw.githubusercontent.com/lopesdiego12/Marvel/main/image/arch_design.png)

- Docker
    
    Docker compose to make environment available with airflow+postgres

- Airflow
    
    Airflow to orchestrate all tasks

- Postgres
    
    Postgres to use as airflow metadata database and Concept of DW

- Python
    
    Python to request api data, transform, insert into database

Docker compose 

![image](https://raw.githubusercontent.com/lopesdiego12/Marvel/main/image/arch_design.png)

---

## Pipeline

* [Pipeline](https://raw.githubusercontent.com/lopesdiego12/Marvel/main/image/pipeline.png)

![image](https://raw.githubusercontent.com/lopesdiego12/Marvel/main/image/pipeline.png)

---

## Final Results

* Final results


## How to run

- Clone project
```git clone https://github.com/lopesdiego12/Marvel.git ```
- Make docker up
```cd Marvel ```
```docker compose up ```
- Run dag in airflow
Acess airflow ui (localhost:8080)
and run Marvel dag
