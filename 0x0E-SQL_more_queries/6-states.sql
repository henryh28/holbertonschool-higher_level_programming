-- Creates database 'hbtn_0d_usa' and table 'states' in it on this server

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use newly created database and create table in it
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
