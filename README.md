# Backend Finance Manager

Finance Manager backend API. To check API documentation on Swagger follow the instructions to get the server running and then (click here)[http://127.0.0.1:5000/openapi/swagger#/].

---
## External Services

Finance Manager makes use of (Open Exchange Rates)[https://openexchangerates.org/] as an external service to provide exchange rate from USD to BRL. In order for this backend to work properly you need to setup and env variable with the APP_ID provided through the admin account of Open Exchange Rates. 

```
$ export OPEN_FOREX_KEY=APP_ID
```

## Installation and Usage
Steps to run backend on dev mode:

Install dependencies with the following command:
```(env)$ pip install -r requirements.txt```

Create PostgreSQL container from (compose repo)[https://github.com/fernandosjp/puc-rio-compose]:
```$ docker-compose up db```

Export connection string to PostgreSQL database:
```$ export DB_URL=postgresql://postgres:password@localhost:5432/splitfy```

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