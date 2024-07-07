CREATE TABLE IF NOT EXISTS expense (
    pk_expense SERIAL PRIMARY KEY,
    description VARCHAR(140) NOT NULL,
    category VARCHAR(140),
    value_usd FLOAT NOT NULL,
    value_brl FLOAT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-02-01', '2023-02-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-03-01', '2023-03-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-04-01', '2023-04-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-05-01', '2023-05-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-06-01', '2023-06-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-07-01', '2023-07-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-08-01', '2023-08-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-09-01', '2023-09-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-10-01', '2023-10-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-11-01', '2023-11-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, 10000, '2023-12-01', '2023-12-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-02-01', '2023-02-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-03-01', '2023-03-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-04-01', '2023-04-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-05-01', '2023-05-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-06-01', '2023-06-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-07-01', '2023-07-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-08-01', '2023-08-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-09-01', '2023-09-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-10-01', '2023-10-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-11-01', '2023-11-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, 5000, '2023-12-01', '2023-12-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1200, 6000, '2023-02-01', '2023-02-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1300, 6500, '2023-03-01', '2023-03-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1100, 5500, '2023-04-01', '2023-04-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1100, 5500, '2023-05-01', '2023-05-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 900, 4500, '2023-06-01', '2023-06-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 800, 4000, '2023-07-01', '2023-07-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1050, 5250, '2023-08-01', '2023-08-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1020, 5100, '2023-09-01', '2023-09-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1010, 5050, '2023-10-01', '2023-10-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 800, 4000, '2023-11-01', '2023-11-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Mercado', 'Food at home', 900, 4500, '2023-12-01', '2023-12-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 10,50, '2023-02-01', '2023-02-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 20, 100, '2023-02-01', '2023-03-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 15, 75, '2023-02-01', '2023-04-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 40, 200, '2023-05-01', '2023-05-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 90, 450, '2023-05-01', '2023-06-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 30, 150, '2023-07-01', '2023-07-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 23, 115, '2023-07-01', '2023-08-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 44, 220, '2023-10-01', '2023-09-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 33, 165, '2023-10-01', '2023-10-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 23, 115, '2023-10-01', '2023-11-01');
INSERT INTO expense (description, category, value_usd, value_brl, created_at, updated_at) VALUES ('Uber', 'Transportation', 12, 60, '2023-10-01', '2023-12-01');