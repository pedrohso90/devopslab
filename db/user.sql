CREATE TABLE [IF NOT EXISTS] user (
   user_id serial PRIMARY KEY,
   username VARCHAR ( 50 ) UNIQUE NOT NULL,
   email VARCHAR ( 255 ) UNIQUE NOT NULL,
);