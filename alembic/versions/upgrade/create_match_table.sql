CREATE TABLE rugby_pass_matches.match_links (
match_id INT GENERATED ALWAYS AS IDENTITY,
match varchar(50),
match_date date,
venue varchar(50),
compeition varchar(50),
season varchar(50),
competition_type varchar(50),
rugby_pass_url varchar(150),
dw_date timestamp
);

