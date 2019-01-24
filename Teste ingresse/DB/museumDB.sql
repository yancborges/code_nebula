DROP DATABASE museumdb;
CREATE DATABASE museumdb;

USE museumdb;

CREATE TABLE itm_item (
  itm_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  sec_section_sec_id INTEGER UNSIGNED NOT NULL,
  itm_name VARCHAR(100) NULL,
  itm_origin VARCHAR(100) NULL,
  itm_desc TEXT NULL,
  PRIMARY KEY(itm_id, sec_section_sec_id),
  INDEX itm_item_FKIndex1(sec_section_sec_id)
);

CREATE TABLE req_request (
  req_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  usu_user_usu_id INTEGER UNSIGNED NOT NULL,
  tkn_token_usu_user_usu_id INTEGER UNSIGNED NOT NULL,
  tkn_token_tkn_id INTEGER UNSIGNED NOT NULL,
  req_time DATETIME NULL,
  req_sog INTEGER UNSIGNED NULL,
  req_table VARCHAR(30) NULL,
  req_field VARCHAR(30) NULL,
  req_text TEXT NULL,
  PRIMARY KEY(req_id, usu_user_usu_id, tkn_token_usu_user_usu_id, tkn_token_tkn_id),
  INDEX req_request_FKIndex1(usu_user_usu_id),
  INDEX req_request_FKIndex2(tkn_token_tkn_id, tkn_token_usu_user_usu_id)
);

CREATE TABLE sec_section (
  sec_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  sec_name VARCHAR(50) NULL,
  PRIMARY KEY(sec_id)
);

CREATE TABLE tkn_token (
  tkn_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  usu_user_usu_id INTEGER UNSIGNED NOT NULL,
  tkn_hash TEXT NULL,
  tkn_status BOOL NOT NULL,
  PRIMARY KEY(tkn_id, usu_user_usu_id),
  INDEX tkn_token_FKIndex1(usu_user_usu_id)
);

CREATE TABLE usu_user (
  usu_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  usu_name VARCHAR(50) NULL,
  usu_password VARCHAR(255) NULL,
  PRIMARY KEY(usu_id)
);

