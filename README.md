# Backend Finance Manager

Finance Manager backend API. To check API documentation on Swagger follow the instructions to get the server running and then (click here)[http://127.0.0.1:5000/openapi/swagger#/].

---
## Installation

Install dependencies with the following command:
```(env)$ pip install -r requirements.txt```

Populate data running the following script:
```(env)$ sqlite3 database/db.sqlite3 < populate_test_db.sql```

## Usage

To start the API execute:
```
(env)$ flask run --host 0.0.0.0 --port 5000
```

In Development mode is recommended to use reload parameter. It will restart the server at every change. 
```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

## License

[MIT](https://choosealicense.com/licenses/mit/)