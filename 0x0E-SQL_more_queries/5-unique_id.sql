-- CREATE A TABLE
-- default value for id = 1 and must be unique
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1 UNIQUE,
    name  VARCHAR(256)
);