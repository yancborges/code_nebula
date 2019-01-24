CREATE TABLE anm_anime (
  anm_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  anm_name VARCHAR(100) NULL,
  anm_score FLOAT NULL,
  anm_dateWatched DATE NULL,
  anm_episodes INTEGER UNSIGNED NULL,
  PRIMARY KEY(anm_id)
);

CREATE TABLE gnr2anm (
  gnr_genere_gnr_id INTEGER UNSIGNED NOT NULL,
  anm_anime_anm_id INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(gnr_genere_gnr_id, anm_anime_anm_id),
  INDEX gnr_genere_has_anm_anime_FKIndex1(gnr_genere_gnr_id),
  INDEX gnr_genere_has_anm_anime_FKIndex2(anm_anime_anm_id)
);

CREATE TABLE gnr_genere (
  gnr_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  gnr_name VARCHAR(30) NULL,
  PRIMARY KEY(gnr_id)
);

CREATE TABLE usu2anm (
  anm_anime_anm_id INTEGER UNSIGNED NOT NULL,
  usu_user_usu_id INTEGER UNSIGNED NOT NULL,
  usu2anm_animeScore INTEGER UNSIGNED NULL,
  PRIMARY KEY(anm_anime_anm_id, usu_user_usu_id),
  INDEX anm_anime_has_usu_user_FKIndex1(anm_anime_anm_id),
  INDEX anm_anime_has_usu_user_FKIndex2(usu_user_usu_id)
);

CREATE TABLE usu2gnr (
  gnr_genere_gnr_id INTEGER UNSIGNED NOT NULL,
  usu_user_usu_id INTEGER UNSIGNED NOT NULL,
  usu2gnr_howlike INTEGER UNSIGNED NULL,
  PRIMARY KEY(gnr_genere_gnr_id, usu_user_usu_id),
  INDEX gnr_genere_has_usu_user_FKIndex1(gnr_genere_gnr_id),
  INDEX gnr_genere_has_usu_user_FKIndex2(usu_user_usu_id)
);

CREATE TABLE usu_user (
  usu_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  usu_name VARCHAR(20) NULL,
  usu_password VARCHAR(255) NULL,
  usu_accountCreationDate DATE NULL,
  PRIMARY KEY(usu_id)
);


