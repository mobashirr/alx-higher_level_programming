-- Query to retrieve table information
SELECT 
    CONCAT('Table: ', TABLE_NAME) AS 'Table',
    CONCAT('CREATE TABLE ', TABLE_NAME, ' (') AS 'Create Table',
    GROUP_CONCAT(
        CONCAT('  `', COLUMN_NAME, '` ', COLUMN_TYPE, 
               IF(IS_NULLABLE = 'NO', ' NOT NULL', ''), 
               IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT ', QUOTE(COLUMN_DEFAULT)), ''),
               IF(EXTRA <> '', CONCAT(' ', EXTRA), '')
        )
        ORDER BY ORDINAL_POSITION
        SEPARATOR ',\n'
    ) AS 'Table Structure'
FROM 
    information_schema.columns
WHERE 
    TABLE_SCHEMA = DATABASE()  -- This retrieves the current database name
    AND TABLE_NAME = 'first_table'
GROUP BY 
    TABLE_NAME;
