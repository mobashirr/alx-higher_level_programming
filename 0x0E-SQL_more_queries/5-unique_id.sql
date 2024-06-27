-- CREATE A TABLE
-- default value for id = 1 and must be unique
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT  unique DEFAULT 1,
    name  VARCHAR(256)
);