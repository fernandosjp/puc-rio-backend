CREATE TABLE IF NOT EXISTS expense (
    pk_expense INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(140) NOT NULL,
    category VARCHAR(140),
    value FLOAT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-02-01', '2023-02-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-03-01', '2023-03-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-04-01', '2023-04-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-05-01', '2023-05-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-06-01', '2023-06-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-07-01', '2023-07-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-08-01', '2023-08-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-09-01', '2023-09-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-10-01', '2023-10-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-11-01', '2023-11-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Aluguel', 'Housing', 2000, '2023-12-01', '2023-12-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-02-01', '2023-02-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-03-01', '2023-03-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-04-01', '2023-04-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-05-01', '2023-05-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-06-01', '2023-06-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-07-01', '2023-07-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-08-01', '2023-08-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-09-01', '2023-09-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-10-01', '2023-10-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-11-01', '2023-11-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Condominio', 'Housing', 1000, '2023-12-01', '2023-12-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1200, '2023-02-01', '2023-02-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1300, '2023-03-01', '2023-03-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1100, '2023-04-01', '2023-04-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1100, '2023-05-01', '2023-05-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 900, '2023-06-01', '2023-06-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 800, '2023-07-01', '2023-07-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1050, '2023-08-01', '2023-08-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1020, '2023-09-01', '2023-09-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 1010, '2023-10-01', '2023-10-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 800, '2023-11-01', '2023-11-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Mercado', 'Food at home', 900, '2023-12-01', '2023-12-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 10, '2023-02-01', '2023-02-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 20, '2023-02-01', '2023-03-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 15, '2023-02-01', '2023-04-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 40, '2023-05-01', '2023-05-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 90, '2023-05-01', '2023-06-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 30, '2023-07-01', '2023-07-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 23, '2023-07-01', '2023-08-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 44, '2023-10-01', '2023-09-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 33, '2023-10-01', '2023-10-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 23, '2023-10-01', '2023-11-01');
INSERT INTO expense (description, category, value, created_at, updated_at) VALUES ('Uber', 'Transportation', 12, '2023-10-01', '2023-12-01');