BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
CREATE TABLE IF NOT EXISTS "core_apoderado" ("userApoderado_id" bigint NOT NULL PRIMARY KEY REFERENCES "core_user" ("id") DEFERRABLE INITIALLY DEFERRED, "niñodelApoderado_id" bigint NOT NULL REFERENCES "core_niño" ("userNiño_id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "core_niño" ("userNiño_id" bigint NOT NULL PRIMARY KEY REFERENCES "core_user" ("id") DEFERRABLE INITIALLY DEFERRED, "apoderadodelNiño_id" bigint NOT NULL REFERENCES "core_apoderado" ("userApoderado_id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "core_planificacion" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(100) NOT NULL, "fecha" date NOT NULL);
CREATE TABLE IF NOT EXISTS "core_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "rut" varchar(10) NOT NULL, "edad" integer unsigned NOT NULL CHECK ("edad" >= 0), "fecha_nacimiento" date NOT NULL, "telefono" varchar(9) NOT NULL, "email" varchar(50) NOT NULL, "direccion" varchar(50) NOT NULL, "is_apoderado" bool NOT NULL, "is_parvularia" bool NOT NULL, "is_niño" bool NOT NULL, "apellido" varchar(50) NOT NULL, "nombre" varchar(50) NOT NULL);
CREATE TABLE IF NOT EXISTS "core_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "core_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "core_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "core_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "core_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_contenttype','Can add content type'),
 (14,4,'change_contenttype','Can change content type'),
 (15,4,'delete_contenttype','Can delete content type'),
 (16,4,'view_contenttype','Can view content type'),
 (17,5,'add_session','Can add session'),
 (18,5,'change_session','Can change session'),
 (19,5,'delete_session','Can delete session'),
 (20,5,'view_session','Can view session'),
 (21,6,'add_user','Can add user'),
 (22,6,'change_user','Can change user'),
 (23,6,'delete_user','Can delete user'),
 (24,6,'view_user','Can view user'),
 (25,7,'add_apoderado','Can add apoderado'),
 (26,7,'change_apoderado','Can change apoderado'),
 (27,7,'delete_apoderado','Can delete apoderado'),
 (28,7,'view_apoderado','Can view apoderado'),
 (29,8,'add_niño','Can add niño'),
 (30,8,'change_niño','Can change niño'),
 (31,8,'delete_niño','Can delete niño'),
 (32,8,'view_niño','Can view niño'),
 (33,9,'add_planificacion','Can add planificacion'),
 (34,9,'change_planificacion','Can change planificacion'),
 (35,9,'delete_planificacion','Can delete planificacion'),
 (36,9,'view_planificacion','Can view planificacion');
INSERT INTO "core_user" ("id","password","last_login","is_superuser","username","first_name","last_name","is_staff","is_active","date_joined","rut","edad","fecha_nacimiento","telefono","email","direccion","is_apoderado","is_parvularia","is_niño","apellido","nombre") VALUES (1,'pbkdf2_sha256$870000$UVqqfnluQKxopthGuNTiSJ$EGI1qGNlEtVeMwcnMt/8a68dX9NBJyNTd2Hnso1PnfM=','2024-11-05 01:11:34.005408',1,'dirtyg','','',1,1,'2024-10-14 02:31:35.955186','11.111.111-1',1,'1950-01-01','','asd@asd.com','',0,0,0,'',''),
 (2,'pbkdf2_sha256$870000$kbc8ECNBMEvEnE1fO10Mx1$wE68tmr+6tQyb7QHXuXBciOUv+C8u/lgRi3W+CfeIs0=','2024-11-09 22:26:46.874561',0,'bvidal','','',0,1,'2024-10-15 11:57:32.068815','11.111.111-1',1,'1950-01-01','9123','bvidal@parvuloconnect.cl','',1,0,0,'Vidal','Brandon'),
 (3,'pbkdf2_sha256$870000$qH80ltmwiQmQdhmKgbEJID$0kcKNiAd41BMb/x9sdGW01BijFcg0R3Jx9DkexcLzPs=','2024-11-09 22:32:00.379386',0,'blagos','','',0,1,'2024-10-15 12:09:05.838156','11.111.111-1',1,'1950-01-01','9123','blagos@parvuloconnect.cl','',0,1,0,'Lagos','Bastián'),
 (4,'pbkdf2_sha256$870000$qYEr7rQgb41kIHnApNtChE$dZGKU4pq8uwPUlmJu9gtmQZFwG8OI6G0ESIwtmvZk6A=','2024-10-18 02:01:08.822638',0,'TestPC','','',0,1,'2024-10-18 01:39:26.221032','11.111.111-1',1,'1950-01-01','12345678','parvuloconnect_test@parvuloconnect.cl','',0,1,0,'PárvuloConnect','Testing');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'contenttypes','contenttype'),
 (5,'sessions','session'),
 (6,'core','user'),
 (7,'core','apoderado'),
 (8,'core','niño'),
 (9,'core','planificacion');
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2024-10-14 02:27:22.751750'),
 (2,'contenttypes','0002_remove_content_type_name','2024-10-14 02:27:22.765550'),
 (3,'auth','0001_initial','2024-10-14 02:27:22.792406'),
 (4,'auth','0002_alter_permission_name_max_length','2024-10-14 02:27:22.808987'),
 (5,'auth','0003_alter_user_email_max_length','2024-10-14 02:27:22.817660'),
 (6,'auth','0004_alter_user_username_opts','2024-10-14 02:27:22.830427'),
 (7,'auth','0005_alter_user_last_login_null','2024-10-14 02:27:22.840948'),
 (8,'auth','0006_require_contenttypes_0002','2024-10-14 02:27:22.847021'),
 (9,'auth','0007_alter_validators_add_error_messages','2024-10-14 02:27:22.857542'),
 (10,'auth','0008_alter_user_username_max_length','2024-10-14 02:27:22.869139'),
 (11,'auth','0009_alter_user_last_name_max_length','2024-10-14 02:27:22.877649'),
 (12,'auth','0010_alter_group_name_max_length','2024-10-14 02:27:22.893684'),
 (13,'auth','0011_update_proxy_permissions','2024-10-14 02:27:22.905371'),
 (14,'auth','0012_alter_user_first_name_max_length','2024-10-14 02:27:22.916413'),
 (15,'core','0001_initial','2024-10-14 02:27:22.938963'),
 (16,'admin','0001_initial','2024-10-14 02:27:22.957830'),
 (17,'admin','0002_logentry_remove_auto_add','2024-10-14 02:27:22.975370'),
 (18,'admin','0003_logentry_add_action_flag_choices','2024-10-14 02:27:22.987294'),
 (19,'core','0002_alter_user_fecha_nacimiento','2024-10-14 02:27:23.006405'),
 (20,'core','0003_remove_user_apellido_remove_user_nombre','2024-10-14 02:27:23.027460'),
 (21,'sessions','0001_initial','2024-10-14 02:27:23.040435'),
 (22,'core','0004_user_apellido_user_nombre','2024-10-14 02:32:35.836747'),
 (23,'core','0005_apoderado_niño_apoderado_niñodelapoderado','2024-10-15 12:01:25.916001'),
 (24,'core','0006_planificacion','2024-11-05 01:08:15.076244');
INSERT INTO "django_session" ("session_key","session_data","expire_date") VALUES ('qy05gunkhzic211iu374rzs51knh9by0','.eJxVjEEOgjAQRe_StWloZ2oZl-45AxnaGUFNSSisjHdXEha6_e-9_zI9b-vYb1WWfsrmYpw5_W4Dp4eUHeQ7l9ts01zWZRrsrtiDVtvNWZ7Xw_07GLmO3xq8Ni4jiBfAGJGDyNkpYUYKiRipJQ9NJvDYoIILECmIDqKtqo_m_QHBlDcv:1t1by2:d1tpwzs_QS-vB2PKvig7fparl2GJdC8nzQnOW7oCJLI','2024-11-01 01:39:50.955032'),
 ('eg1ive8cuqupvgqzrrayzuhg8w170uab','.eJxVjDsOwjAQBe_iGlnxZ9cLJT1nsHZtgwPIkeKkQtwdIqWA9s3Me6nI61Lj2sscx6xOyqvD7yacHqVtIN-53SadprbMo-hN0Tvt-jLl8jzv7t9B5V6_NXlAZwu4NHjPQsQyJAeZ0QAXsBKIErlwBA8GxV5NMAgOJCD5jE69P7_cNo0:1t1cIe:joGV4YrOoQiXHxWD1Oo28nx-_1N_RiHM6WuAdCVnV8U','2024-11-01 02:01:08.831723'),
 ('290916pm8pt4krru8rcrykcg0sipxu6d','.eJxVjEEOwiAQRe_C2hBHSgGX7j0DmWEGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVWRh1-N8L0kLoBvmO9NZ1aXeaJ9KbonXZ9bSzPy-7-HRTs5VsnGqwlDzlLcsk4ouDIs_cwEudAIR0zECKf_CDGujwIALLwaMQggHp_ABdyOSU:1t1cKa:Z-fc2a5CEhL-kGC6BRlvWEq1R-h_selYKXNc4IE7rUA','2024-11-01 02:03:08.573182'),
 ('sc956zs2y0d7knlwkwzcnl2f7htainlx','.eJxVjDsOwjAQBe_iGln-fyjpOYO1Xq9xADlSnFSIu0OkFNC-mXkvlmBbW9oGLWkq7MwUO_1uGfBBfQflDv02c5z7ukyZ7wo_6ODXudDzcrh_Bw1G-9agqaAWxWMEq4zTKH1UJLzyICgYJBNVzSBdldEYCsFq8uiy0VVLtOz9AeKwN6Y:1t1cMi:QWtxlLy8AK-WPo2RP-DSZ1adOqiFyXknWmeTjYWgkr4','2024-11-01 02:05:20.864686'),
 ('c9ndrcrj2lbcb4upeey57ukj9m3uv4yj','.eJxVjDsOwjAQBe_iGln-fyjpOYO1Xq9xADlSnFSIu0OkFNC-mXkvlmBbW9oGLWkq7MwUO_1uGfBBfQflDv02c5z7ukyZ7wo_6ODXudDzcrh_Bw1G-9agqaAWxWMEq4zTKH1UJLzyICgYJBNVzSBdldEYCsFq8uiy0VVLtOz9AeKwN6Y:1t1cNH:dQuclD7_mFolqlMyWbxO476pFCAdzjLKk4HqwltQF7E','2024-11-01 02:05:55.336460'),
 ('4yum1vf8lcef3dh6vhcp9hh5yvahhjv3','.eJxVjDsOwjAQBe_iGln-fyjpOYO1Xq9xADlSnFSIu0OkFNC-mXkvlmBbW9oGLWkq7MwUO_1uGfBBfQflDv02c5z7ukyZ7wo_6ODXudDzcrh_Bw1G-9agqaAWxWMEq4zTKH1UJLzyICgYJBNVzSBdldEYCsFq8uiy0VVLtOz9AeKwN6Y:1t1cOr:OZrJCUILTSLSh1WlIHLnHdYXp2l2sisR0UEmI19QpTQ','2024-11-01 02:07:33.953220'),
 ('q6b44bbtcwqnlpnlvtuopay0j8vi2odf','.eJxVjDsOwjAQBe_iGln-fyjpOYO1Xq9xADlSnFSIu0OkFNC-mXkvlmBbW9oGLWkq7MwUO_1uGfBBfQflDv02c5z7ukyZ7wo_6ODXudDzcrh_Bw1G-9agqaAWxWMEq4zTKH1UJLzyICgYJBNVzSBdldEYCsFq8uiy0VVLtOz9AeKwN6Y:1t1cPw:vaUq_DFLM22co0U7cynIw5YkuZdZ6cWMFbzwUaOJKac','2024-11-01 02:08:40.085577'),
 ('9qcdwfwd35xvksmwxgvuwtccmn8xsltt','.eJxVjDkOwjAQAP-yNbLiIz5S0vOGaL1e4wCypTipEH9HkVJAOzOaN8y4b2XeO6_zkmACBZdfFpGeXA-RHljvTVCr27pEcSTitF3cWuLX9Wz_BgV7gQlQcyI9JEcBR2WsJumC4sEphwN7Q2yCyhGlzTIYw96Pmh3ZaHTWkkb4fAHisDem:1t2KY3:8mStro03Q6HmtHqG8pGVV5hHZe9fq5gManx4L_r8xFE','2024-11-03 01:15:59.095335'),
 ('y6m0m8w6xcslv7d3nn5x8cef1dk8hm7q','.eJxVjDkOwjAQAP-yNbLiIz5S0vOGaL1e4wCypTipEH9HkVJAOzOaN8y4b2XeO6_zkmACBZdfFpGeXA-RHljvTVCr27pEcSTitF3cWuLX9Wz_BgV7gQlQcyI9JEcBR2WsJumC4sEphwN7Q2yCyhGlzTIYw96Pmh3ZaHTWkkb4fAHisDem:1t7lP2:KxhWl-klfXHJyYcQnCSPjuSihEAqkrip1Tr8w9r8k5c','2024-11-18 00:57:08.639945'),
 ('psqhrcsx2pt9nkqv6g83abw4rxfft90k','.eJxVjDkOwjAQAP-yNbLiIz5S0vOGaL1e4wCypTipEH9HkVJAOzOaN8y4b2XeO6_zkmACBZdfFpGeXA-RHljvTVCr27pEcSTitF3cWuLX9Wz_BgV7gQlQcyI9JEcBR2WsJumC4sEphwN7Q2yCyhGlzTIYw96Pmh3ZaHTWkkb4fAHisDem:1t88DE:9kAnUf64CcMf3q2W1WaoEhZHl-lM24NjBnHGq_W5fDA','2024-11-19 01:18:28.691719'),
 ('c1vdae56v2dim1azqitic784ftddvdcl','.eJxVjDEOwjAMAP_iGUWYJE3akZ03RHbskAJqpaadEH9HlTrAene6NyTa1pq2pksaBQawcPplTPmp0y7kQdN9Nnme1mVksyfmsM3cZtHX9Wj_BpVahQEyO-85YimaQ7aBuQ8cJUbsWErPfT4XZCK5RKfWh-IUkUSls2oJET5fF3I5JQ:1t88gp:keihF6eUVH1h757T2592ZJwAbHsK0SaBT5mDbhlgSuE','2024-11-19 01:49:03.579850'),
 ('u1lp3fikl28ust7119xg4largrl1bjia','.eJxVjEEOwiAQRe_C2hBHSgGX7j0DmWEGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVWRh1-N8L0kLoBvmO9NZ1aXeaJ9KbonXZ9bSzPy-7-HRTs5VsnGqwlDzlLcsk4ouDIs_cwEudAIR0zECKf_CDGujwIALLwaMQggHp_ABdyOSU:1t96h0:TmcSO_3yMENEzsy5hfLD1mpVKcu1X44IwgEE1beCVnA','2024-11-21 17:53:14.144707'),
 ('6xtgjlfhqftdd94bm4npkafyc2npty5w','.eJxVjEEOwiAQRe_C2hBHSgGX7j0DmWEGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVWRh1-N8L0kLoBvmO9NZ1aXeaJ9KbonXZ9bSzPy-7-HRTs5VsnGqwlDzlLcsk4ouDIs_cwEudAIR0zECKf_CDGujwIALLwaMQggHp_ABdyOSU:1t9rCr:z59DjS1YcuuNuBRfJ4U_ivBZeUBcXfJ6UrBjKabU5S8','2024-11-23 19:33:13.852463'),
 ('4ria84qugyp3zrbnofgi0vsdjiwazt9y','.eJxVjDEOwjAMAP_iGUWYJE3akZ03RHbskAJqpaadEH9HlTrAene6NyTa1pq2pksaBQawcPplTPmp0y7kQdN9Nnme1mVksyfmsM3cZtHX9Wj_BpVahQEyO-85YimaQ7aBuQ8cJUbsWErPfT4XZCK5RKfWh-IUkUSls2oJET5fF3I5JQ:1t9tzs:ieas4vLAu1La43nk1T1LQK5lH6K3D0SJTfUqoC47umU','2024-11-23 22:32:00.385597');
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "core_apoderado_niñodelApoderado_id_ef024c39" ON "core_apoderado" ("niñodelApoderado_id");
CREATE INDEX "core_niño_apoderadodelNiño_id_576d4c17" ON "core_niño" ("apoderadodelNiño_id");
CREATE INDEX "core_user_groups_group_id_fe8c697f" ON "core_user_groups" ("group_id");
CREATE INDEX "core_user_groups_user_id_70b4d9b8" ON "core_user_groups" ("user_id");
CREATE UNIQUE INDEX "core_user_groups_user_id_group_id_c82fcad1_uniq" ON "core_user_groups" ("user_id", "group_id");
CREATE INDEX "core_user_user_permissions_permission_id_35ccf601" ON "core_user_user_permissions" ("permission_id");
CREATE INDEX "core_user_user_permissions_user_id_085123d3" ON "core_user_user_permissions" ("user_id");
CREATE UNIQUE INDEX "core_user_user_permissions_user_id_permission_id_73ea0daa_uniq" ON "core_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
COMMIT;
