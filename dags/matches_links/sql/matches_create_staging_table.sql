DROP TABLE IF EXISTS staging.{{params.match}}_match_links;

CREATE TABLE staging.{{params.match}}_match_links (
match varchar(50),
match_date date,
venue varchar(50),
compeition varchar(50),
season varchar(50),
competition_type varchar(50),
rugby_pass_url varchar(150)
);

COPY staging.{{params.match}}_match_links
FROM '/Users/harry/rugby_data_pipelines/data/formatted_area/matches/{{ ds }}/{{params.match}}.csv'
--FROM '/Users/harry/rugby_data_pipelines/data/formatted_area/matches/2021-05-23/autumn_nations_cup.csv'
DELIMITER ',' 
CSV HEADER;