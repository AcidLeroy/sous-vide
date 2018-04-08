CREATE TABLE temperature_table (
	id serial PRIMARY KEY, 
	timestamp timestamp, 
	temperature real 
);  

CREATE TABLE relay_table (
	id serial PRIMARY KEY, 
	timestamp timestamp, 
	relay_on BOOLEAN 
);  

CREATE TABLE setpoint_table (
	id serial PRIMARY KEY, 
	timestamp timestamp, 
	setpoint integer 
); 

CREATE TABLE sous_vide_mode_table (
	id serial PRIMARY KEY, 
	timestamp timestamp, 
	mode varchar(16) 
); 

-- Set the desired state of the relay
CREATE OR REPLACE FUNCTION set_relay_on(BOOLEAN)
RETURNS void AS $$ 
INSERT INTO relay_table
(timestamp, relay_on) values (CURRENT_TIMESTAMP, $1) 
$$ 
LANGUAGE SQL;

-- Get the latest state of the relay
CREATE OR REPLACE FUNCTION get_latest_relay_on(int) RETURNS TABLE(ts timestamp, relay_on BOOLEAN) 
AS $$
	SELECT timestamp, relay_on 
	FROM relay_table 
	ORDER BY timestamp DESC 
	LIMIT $1
$$
LANGUAGE SQL;

-- Set the mode of the sous vide ('manual' or 'auto') 
CREATE OR REPLACE FUNCTION set_mode(varchar(16))
RETURNS void AS $$ 
INSERT INTO sous_vide_mode_table
(timestamp, mode) values (CURRENT_TIMESTAMP, $1) 
$$ 
LANGUAGE SQL;

-- Add the actual temperature
CREATE OR REPLACE FUNCTION add_temperature(real)
RETURNS void AS $$ 
INSERT INTO temperature_table
(timestamp, temperature) values (CURRENT_TIMESTAMP, $1) 
$$ 
LANGUAGE SQL;

-- Add the setpoint
CREATE OR REPLACE FUNCTION add_setpoint(int)
RETURNS void AS $$ 
INSERT INTO setpoint_table
(timestamp, setpoint) values (CURRENT_TIMESTAMP, $1) 
$$ 
LANGUAGE SQL;


-- The following function get the latest temperatures from the setpoint table
CREATE OR REPLACE FUNCTION get_latest_setpoints(int) RETURNS TABLE(ts timestamp, temp integer) 
AS $$
	SELECT timestamp, setpoint 
	FROM setpoint_table 
	ORDER BY timestamp DESC 
	LIMIT $1
$$
LANGUAGE SQL;

-- The following function get the latest temperatures from the temperature table
CREATE OR REPLACE FUNCTION get_latest_temps(int) RETURNS TABLE(ts timestamp, temp real) 
AS $$
	SELECT timestamp, temperature 
	FROM temperature_table 
	ORDER BY timestamp DESC 
	LIMIT $1
$$
LANGUAGE SQL;

CREATE OR REPLACE FUNCTION get_latest_modes(int) RETURNS TABLE(ts timestamp, mode varchar(16)) 
AS $$
	SELECT timestamp, mode 
	FROM sous_vide_mode_table 
	ORDER BY timestamp DESC 
	LIMIT $1
$$
LANGUAGE SQL;
