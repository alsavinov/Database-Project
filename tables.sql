create table users(
	user_id serial PRIMARY KEY,
	phone_number varchar (11),
	first_name varchar (50),
	last_name varchar (50),
	gender varchar(10) CHECK (gender = 'male' OR gender = 'female'),
	age integer NOT NULL
);

create table teams(
	team_id serial PRIMARY KEY,
	team_name varchar(50) 
);

create table bets(
	bet_id serial PRIMARY KEY,
	user_id integer,
	match_id integer,
	outcome varchar(1) CHECK (outcome IN ('1', 'X', '2')),
	sum_of_bet numeric(20, 2),
	coef numeric(5, 2) CHECK (coef > 1.00),
	winning numeric(20, 2) default 0,
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (match_id) REFERENCES users(user_id)
);

create table matches(
	match_id serial PRIMARY KEY,
	match_date DATE,
	team_id_home integer,
	team_id_away integer,
	match_result varchar(1) CHECK (match_result IN ('1', 'X', '2')),
	score_home int,
	score_away int,
	FOREIGN KEY (team_id_home) REFERENCES teams(team_id),
	FOREIGN KEY (team_id_away) REFERENCES teams(team_id)
);

create table players(
	player_id serial PRIMARY KEY,
	team_id int,
	player_name varchar(50),
	player_position varchar (2) CHECK (player_position IN ('GK', 'DF', 'MF', 'FW')),
	FOREIGN KEY (team_id) REFERENCES teams(team_id)
);



CREATE INDEX index_bets_outcome ON bets(outcome);


CREATE OR REPLACE FUNCTION winmoney_trigger_fnc()
  RETURNS trigger AS
$$
	BEGIN
		update bets
		set winning = sum_of_bet * coef;
		RETURN NEW;
	END;
$$
LANGUAGE 'plpgsql';
CREATE TRIGGER winning_update
AFTER INSERT ON bets FOR EACH ROW
EXECUTE PROCEDURE winmoney_trigger_fnc();



INSERT INTO users(phone_number, first_name, last_name, gender, age) VALUES 
('89344563319', 'Aleksei', 'Petrov', 'male', 20),
('89864532631', 'Alexandra', 'Baranova', 'female', 30),
('89172104521', 'Ilya', 'Volkov', 'male', 45),
('89376540981', 'Dmitrii', 'Tarasov', 'male', 19),
('89104320016', 'Svetlana', 'Voronkova', 'female', 26);



INSERT INTO teams(team_name) VALUES
('Real Madrid'), ('Arsenal'), ('Krasnodar'), ('Chelsea'), ('PSG');


INSERT INTO players(team_id, player_name, player_position) VALUES
(1, 'Cristiano Ronaldo', 'FW'),
(3, 'Sergei Krivtsov', 'MF'),
(5, 'Kilian Mbappe', 'FW'),
(2, 'Gabriel Jesus', 'FW'),
(4, 'Ngolo Kante', 'DF');

INSERT INTO bets(user_id, match_id, outcome, sum_of_bet, coef) VALUES
(1, 2, '1', 1100, 2.16),
(2, 5, 'X', 2000, 1.02),
(3, 4, '2', 20000, 4.10),
(4, 3, 'X', 17500, 2.00),
(5, 3, '1', 123456, 3.10);

INSERT INTO matches(match_date, team_id_home, team_id_away, match_result, score_home, score_away) VALUES
('2022-03-21', 2, 1, 'X', 2, 1),
('2022-02-12', 1, 5, '1', 3, 2),
('2022-01-11', 2, 3, '2', 1, 1),
('2022-01-04', 4, 3, 'X', 0, 1),
('2022-03-15', 5, 4, '1', 0, 0);





CREATE OR REPLACE FUNCTION show_table_teams()
	RETURNS TABLE(team_id int, team_name varchar(50)) AS $$
		BEGIN
			RETURN QUERY
			SELECT * FROM teams;
		END;
	$$ LANGUAGE plpgsql;
	

CREATE OR REPLACE FUNCTION show_table_players()
	RETURNS TABLE(player_id int, team_id int, player_name varchar(50), player_position varchar(2)) AS $$
		BEGIN
			RETURN QUERY
			SELECT * FROM players;
		END;
	$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION show_table_matches()
	RETURNS TABLE(match_id int, match_date date, team_name_home varchar(50), team_name_away varchar(50), 
				  match_result varchar(1), score_home int, score_away int) AS $$
		BEGIN
			RETURN QUERY
			SELECT matches.match_id, matches.match_date, 
				(select teams.team_name
				from teams
				where teams.team_id = matches.team_id_home), 
				(select teams.team_name
				from teams
				where teams.team_id = matches.team_id_away),
				matches.match_result, matches.score_home, matches.score_away 
			FROM matches;
		END;
	$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION show_table_users()
	RETURNS TABLE(user_id int, phone_number varchar(11), first_name varchar(50), last_name varchar(50), 
				  gender varchar(50), age int) AS $$
		BEGIN
			RETURN QUERY
			SELECT * FROM users;
		END;
	$$ LANGUAGE plpgsql;	

CREATE OR REPLACE FUNCTION show_table_bets()
	RETURNS TABLE(bet_id int, user_id int, match_id int, outcome varchar(1), sum_of_bet numeric(5, 2), coef numeric(5, 2), winning numeric(5, 2)) AS $$
		BEGIN
			RETURN QUERY
			SELECT * FROM bets;
		END;
	$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION add_user(aphone_number varchar(11), afirst_name varchar(50), 
									alast_name varchar(50),	agender varchar(50), aage int)
	RETURNS void AS $$
		BEGIN
			INSERT INTO users(phone_number, first_name, last_name, gender, age) 
			VALUES (aphone_number, afirst_name, alast_name, agender, aage);
		END;
	$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION add_bet(auser_id int, amatch_id int, aoutcome varchar(1), asum_of_bet numeric(5, 2),
								   acoef numeric(5, 2))
	RETURNS void AS $$
		BEGIN
			INSERT INTO bets(user_id, match_id, outcome, sum_of_bet, coef) VALUES (auser_id, amatch_id, aoutcome, asum_of_bet, acoef);
		END;
	$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION add_match(amatch_date date, ateam_id_home int, ateam_id_away int, amatch_result varchar(1),
									 ascore_home int, ascore_away int)
	RETURNS void AS $$
		BEGIN
			INSERT INTO matches(match_date, team_id_home, team_id_away, match_result, score_home, score_away) 
			VALUES (amatch_date, ateam_id_home, ateam_id_away, amatch_result, ascore_home, ascore_away);
		END;
	$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION update_user(aid int, aphone_number varchar(11), afirst_name varchar(50), 
									alast_name varchar(50),	agender varchar(50), aage int)
	RETURNS void AS $$
		BEGIN
			UPDATE users 
			SET phone_number = aphone_number, first_name = afirst_name, last_name = alast_name, 
				gender = agender, age = aage 
			WHERE user_id = aid;
		END;
	$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_match(aid int, amatch_date int, ateam_id_home int, ateam_id_away int, amatch_result varchar(1),
									 ascore_home int, ascore_away int)
	RETURNS void AS $$
		BEGIN
			UPDATE matches 
			SET match_date = amatch_date, team_id_home = ateam_id_home, team_id_away = ateam_id_away, match_result = amatch_result,
				score_home = ascore_home, score_away = ascore_away
			WHERE match_id = aid;
		END;
	$$ LANGUAGE plpgsql;
	
	

CREATE OR REPLACE FUNCTION delete_bet(aid int)
	RETURNS void AS $$
		BEGIN
		DELETE FROM bets WHERE bet_id = aid;
		END;
	$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_match(aid int)
	RETURNS void AS $$
		BEGIN
		DELETE FROM matches WHERE match_id = aid;
		END;
	$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_all_bets()
	RETURNS void AS $$
		BEGIN
		DELETE FROM bets;
		END;
	$$ LANGUAGE plpgsql;
	
CREATE OR REPLACE FUNCTION delete_all_tables()
	RETURNS void AS $$
		BEGIN
		DELETE FROM matches;
		DELETE FROM bets;
		DELETE FROM users;
		DELETE FROM players;
		DELETE FROM teams;		
		END;
	$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION delete_bets_by_result(aoutcome varchar(1))
	RETURNS void AS $$
		BEGIN
		DELETE FROM bets WHERE bets.outcome = aoutcome;
		END;
	$$ LANGUAGE plpgsql;

	
CREATE OR REPLACE FUNCTION search_bets_by_result(aoutcome varchar(1))
	RETURNS TABLE(bet_id int, user_id int, match_id int, outcome varchar(1), sum_of_bet numeric(5, 2), coef numeric(5, 2), winning numeric(5, 2)) AS $$
		BEGIN
			RETURN QUERY
			SELECT * FROM bets WHERE bets.outcome = aoutcome;
		END;
	$$ LANGUAGE plpgsql;


