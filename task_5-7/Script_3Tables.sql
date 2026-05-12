create table products (
id SERIAL PRIMARY KEY,

name VARCHAR(100) NOT NULL,

category VARCHAR(50)

);

create table prices (

id SERIAL PRIMARY key,

product_id INTEGER REFERENCES products(id),

price NUMERIC(10,2) NOT null,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

create table suppliers (

id SERIAL PRIMARY key,

name VARCHAR(100) NOT null,

product_id INTEGER REFERENCES products(id)
);









