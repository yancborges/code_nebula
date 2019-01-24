CREATE TABLE ist_instrument (
  ist_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  ist_name VARCHAR(20) NULL,
  PRIMARY KEY(ist_id),
);

CREATE TABLE itm_item (
  itm_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  usu_id INTEGER UNSIGNED NOT NULL,
  ist_id INTEGER UNSIGNED NOT NULL,
  itm_state INTEGER UNSIGNED NULL,
  itm_name VARCHAR(100) NULL,
  PRIMARY KEY(itm_id),
  INDEX itm_item_FKIndex1(usu_id),
  INDEX itm_item_FKIndex2(ist_id)
);

CREATE TABLE ply_play (
  ply_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  ply_date DATE NULL,
  itm_id INTEGER UNSIGNED NOT NULL,
  usu_id INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(ply_id),
  INDEX ply_play_FKIndex1(itm_id),
  INDEX ply_play_FKIndex2(usu_id)
);

CREATE TABLE usu_user (
  usu_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  usu_name VARCHAR(16) NULL,
  usu_password VARCHAR(255) NULL,
  usu_email VARCHAR(50) NULL,
  usu_status INTEGER UNSIGNED NULL,
  PRIMARY KEY(usu_id)
);


