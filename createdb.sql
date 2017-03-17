CREATE TABLE IF NOT EXISTS password (
    id SERIAL PRIMARY KEY,
    host TEXT,
    username TEXT,
    passwd TEXT
);
