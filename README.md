## Division API

A Flask-based REST API that performs  division operation between two numbers. The API stores the results and input in a SQLite database using SQLAlchemy as the ORM. 

This project includes basic logging, error handling, observability features and documentation. The application is containerized using Docker and Docker Compose.

### Author : Anita Kahenya Jul 2024

## Table of Contents

- [Division API](#division-api)
  - [Author : Anita Kahenya Jul 2024](#author--anita-kahenya-jul-2024)
- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Live Preview](#live-preview)
- [Requirements](#requirements)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Contributing and Making Changes](#contributing-and-making-changes)
- [License](#license)
- [Contact Information](#contact-information)

## Features

- Perform division operation between two numbers.
- Store the results in a SQLite database.
- Handle various input validation scenarios.
- Python3 logging to app.log file.
- Observability and monitoring using Sentry.
- Containerized using Docker and Docker Compose.
- Documentation on Apidog

## Live Preview

- To view the live project [Visit](https://divide-api.onrender.com) the root of the project and [api/divide](https://divide-api.onrender.com/api/divide) to POST.
  
## Requirements

- Python3
- Flask
- Docker
- Docker Compose

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/kahenya-anita/Divide-API
   cd Division

2. Create a .env file and add
    ```sh
    FLASK_ENV=Division
    FLASK_APP=app.py

3. Build and start the docker container
   ```sh
   docker-compose up --build

4. Run migrations and seed file
   ```sh
   flask db migrate
   flask db upgrade

5. Navigate to the localhost on the browser
    ```sh
    http://localhost:5500

6. Open postman to run your first division operation
    ```sh 
    POST : http://localhost:5500/api/divide
    Body:
        {
            "a": 10,
            "b": 5
        }


## API Documentation

- This API has been documented on [Apidog](https://sp1xk1rtgc.apidog.io/doc-572564)

## Testing

- To run the tests
    ```sh
    docker-compose run tests

## Contributing and Making Changes

1.  Create a new branch in your terminal `git checkout -b improve-feature`
2. Make necessary changes on the codebase
2.  Build and run the docker container to see the changes.
3.  Add the changes and commit them `git commit -am "Improve App"`
4.  Push to the branch `git push origin improve-app` and open a new pull request

## [License](LICENSE)

MIT License
Copyright (c) 2024 Anita Kahenya

## Contact Information
* Email : anitakahenya1@gmail.com
