CREATE TABLE IF NOT EXISTS stats (
    date DATE,
    stat FLOAT
);

COPY stats
FROM '/datasets/extract-by-day.csv'
DELIMITER ','
CSV HEADER;
