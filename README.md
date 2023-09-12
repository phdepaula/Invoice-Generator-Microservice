# 🧾 Invoice Generator Microservice
Microservice responsible for generating invoices in XML format for sales made.

This project was developed for my full-stack development specialization and is related to two more microservices. For more information, just access the [project description](https://github.com/phdepaula/Full-Stack-Development-Specialization/blob/main/Sprint%203%20-%20Advanced%20Backend%20Development/README.MD).

## 🛠️ Built With
* [Flask](https://flask.palletsprojects.com/) - Web Framework
* [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) - ORM
* [OpenAPI3](https://swagger.io/specification/) - API Specification
* [SQLite](https://www.sqlite.org/index.html) - Database

##  📋 Prerequisites

Make sure you have [Docker](https://docs.docker.com/engine/install/) installed and running on your machine.

Once this is done, check if the external network **puc-microservice** is already created.
To check, run the following command in the terminal:

```
docker network ls
```

If the network does not exist, run the following command to create it:

```
docker network create puc-microservice
```

Additionally, some routes access the order-management-microservice, make sure it is active.
For more information on its creation, access its [repository](https://github.com/phdepaula/Order-Management-Microservice).

## ▶️ How to run

To start the application, simply run via terminal:

```
docker-compose up
```
> Open [http://localhost:5002/](http://localhost:5002/) in your browser to check the running project status.