PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2018-02-23 15:20:29.749748');
INSERT INTO django_migrations VALUES(2,'auth','0001_initial','2018-02-23 15:20:29.923885');
INSERT INTO django_migrations VALUES(3,'admin','0001_initial','2018-02-23 15:20:30.105010');
INSERT INTO django_migrations VALUES(4,'admin','0002_logentry_remove_auto_add','2018-02-23 15:20:30.255119');
INSERT INTO django_migrations VALUES(5,'contenttypes','0002_remove_content_type_name','2018-02-23 15:20:30.448242');
INSERT INTO django_migrations VALUES(6,'auth','0002_alter_permission_name_max_length','2018-02-23 15:20:30.640378');
INSERT INTO django_migrations VALUES(7,'auth','0003_alter_user_email_max_length','2018-02-23 15:20:30.815516');
INSERT INTO django_migrations VALUES(8,'auth','0004_alter_user_username_opts','2018-02-23 15:20:30.973614');
INSERT INTO django_migrations VALUES(9,'auth','0005_alter_user_last_login_null','2018-02-23 15:20:31.158746');
INSERT INTO django_migrations VALUES(10,'auth','0006_require_contenttypes_0002','2018-02-23 15:20:31.225807');
INSERT INTO django_migrations VALUES(11,'auth','0007_alter_validators_add_error_messages','2018-02-23 15:20:31.383906');
INSERT INTO django_migrations VALUES(12,'auth','0008_alter_user_username_max_length','2018-02-23 15:20:31.551023');
INSERT INTO django_migrations VALUES(13,'auth','0009_alter_user_last_name_max_length','2018-02-23 15:20:31.725148');
INSERT INTO django_migrations VALUES(14,'sessions','0001_initial','2018-02-23 15:20:31.883259');
INSERT INTO django_migrations VALUES(15,'testapp','0001_initial','2018-02-23 15:27:18.929846');
INSERT INTO django_migrations VALUES(16,'testapp','0002_blog_commemt_myuser_reply_test_test1','2018-02-23 15:27:19.153002');
INSERT INTO django_migrations VALUES(17,'testapp','0003_auto_20180223_2327','2018-02-23 15:27:33.812280');
INSERT INTO django_migrations VALUES(18,'testapp','0004_commemt_test','2018-02-24 13:58:09.816791');
INSERT INTO django_migrations VALUES(19,'testapp','0005_remove_commemt_test','2018-02-24 14:01:07.067760');
INSERT INTO django_migrations VALUES(20,'testapp','0006_auto_20180224_2318','2018-02-24 15:18:51.766571');
INSERT INTO django_migrations VALUES(21,'testapp','0007_auto_20180225_1429','2018-02-25 06:29:14.710279');
INSERT INTO django_migrations VALUES(22,'testapp','0008_auto_20180225_1609','2018-02-25 08:09:38.243994');
INSERT INTO django_migrations VALUES(23,'testapp','0009_auto_20180225_1610','2018-02-25 08:10:45.513382');
INSERT INTO django_migrations VALUES(24,'testapp','0010_auto_20180225_1611','2018-02-25 08:12:01.602289');
INSERT INTO django_migrations VALUES(25,'testapp','0011_auto_20180225_1614','2018-02-25 08:14:19.851685');
INSERT INTO django_migrations VALUES(26,'testapp','0002_comment_test','2018-02-25 09:06:04.427879');
INSERT INTO django_migrations VALUES(27,'testapp','0002_auto_20180225_2143','2018-02-25 13:43:11.903092');
INSERT INTO django_migrations VALUES(28,'testapp','0002_auto_20180225_2203','2018-02-25 14:04:37.666330');
INSERT INTO django_migrations VALUES(29,'testapp','0003_auto_20180225_2206','2018-02-25 14:06:40.829752');
INSERT INTO django_migrations VALUES(30,'testapp','0004_remove_comment_test','2018-02-25 14:11:31.646736');
INSERT INTO django_migrations VALUES(31,'testapp','0005_auto_20180225_2233','2018-02-25 14:33:11.687549');
INSERT INTO django_migrations VALUES(32,'testapp','0006_auto_20180225_2237','2018-02-25 14:37:36.004119');
INSERT INTO django_migrations VALUES(33,'testapp','0007_auto_20180225_2249','2018-02-25 14:49:44.978270');
INSERT INTO django_migrations VALUES(34,'testapp','0008_auto_20180225_2253','2018-02-25 14:53:50.376220');
INSERT INTO django_migrations VALUES(35,'testapp','0009_auto_20180225_2256','2018-02-25 14:56:05.074223');
INSERT INTO django_migrations VALUES(36,'testapp','0010_auto_20180225_2306','2018-02-25 15:06:13.881965');
INSERT INTO django_migrations VALUES(37,'testapp','0002_auto_20180225_2314','2018-02-25 15:15:54.542043');
INSERT INTO django_migrations VALUES(38,'testapp','0003_auto_20180225_2320','2018-02-25 15:20:09.084533');
INSERT INTO django_migrations VALUES(39,'testapp','0004_auto_20180226_2257','2018-02-26 14:57:43.283791');
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','group');
INSERT INTO django_content_type VALUES(3,'auth','user');
INSERT INTO django_content_type VALUES(4,'auth','permission');
INSERT INTO django_content_type VALUES(5,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(6,'sessions','session');
INSERT INTO django_content_type VALUES(7,'testapp','myuser');
INSERT INTO django_content_type VALUES(8,'testapp','blog');
INSERT INTO django_content_type VALUES(9,'testapp','commemt');
INSERT INTO django_content_type VALUES(10,'testapp','reply');
INSERT INTO django_content_type VALUES(11,'testapp','test');
INSERT INTO django_content_type VALUES(12,'testapp','test1');
INSERT INTO django_content_type VALUES(13,'testapp','comment');
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,2,'add_group','Can add group');
INSERT INTO auth_permission VALUES(5,2,'change_group','Can change group');
INSERT INTO auth_permission VALUES(6,2,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(7,3,'add_user','Can add user');
INSERT INTO auth_permission VALUES(8,3,'change_user','Can change user');
INSERT INTO auth_permission VALUES(9,3,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(10,4,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(11,4,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(12,4,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(13,5,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(14,5,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(15,5,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(16,6,'add_session','Can add session');
INSERT INTO auth_permission VALUES(17,6,'change_session','Can change session');
INSERT INTO auth_permission VALUES(18,6,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(19,7,'add_myuser','Can add my user');
INSERT INTO auth_permission VALUES(20,7,'change_myuser','Can change my user');
INSERT INTO auth_permission VALUES(21,7,'delete_myuser','Can delete my user');
INSERT INTO auth_permission VALUES(22,8,'add_blog','Can add blog');
INSERT INTO auth_permission VALUES(23,8,'change_blog','Can change blog');
INSERT INTO auth_permission VALUES(24,8,'delete_blog','Can delete blog');
INSERT INTO auth_permission VALUES(25,9,'add_commemt','Can add commemt');
INSERT INTO auth_permission VALUES(26,9,'change_commemt','Can change commemt');
INSERT INTO auth_permission VALUES(27,9,'delete_commemt','Can delete commemt');
INSERT INTO auth_permission VALUES(28,10,'add_reply','Can add reply');
INSERT INTO auth_permission VALUES(29,10,'change_reply','Can change reply');
INSERT INTO auth_permission VALUES(30,10,'delete_reply','Can delete reply');
INSERT INTO auth_permission VALUES(31,11,'add_test','Can add test');
INSERT INTO auth_permission VALUES(32,11,'change_test','Can change test');
INSERT INTO auth_permission VALUES(33,11,'delete_test','Can delete test');
INSERT INTO auth_permission VALUES(34,12,'add_test1','Can add test1');
INSERT INTO auth_permission VALUES(35,12,'change_test1','Can change test1');
INSERT INTO auth_permission VALUES(36,12,'delete_test1','Can delete test1');
INSERT INTO auth_permission VALUES(37,13,'add_comment','Can add comment');
INSERT INTO auth_permission VALUES(38,13,'change_comment','Can change comment');
INSERT INTO auth_permission VALUES(39,13,'delete_comment','Can delete comment');
CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "last_name" varchar(150) NOT NULL);
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO django_session VALUES('mv792sxzchlu7foxf1gkqmqwfams7ppd','MWE5MjQxOThlZWNhNWRjZjMzMjY5NjU4YTQ0NjkzZjMxNzZiYzhjNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkODA5YmUzZDcxYTg5OTA1Y2E5MzU2NTY0ZmNmOTAxNTg5N2JjYTI0In0=','2018-03-09 15:28:44.546433');
INSERT INTO django_session VALUES('v5vob2orwb47qgf7n45tb6b8j3ic87xt','MTI3NTEwYjI4Y2M5MjcyMTM2YWFmYjMyMWQxYzk3YzAyOWJhZDBhYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ4MDliZTNkNzFhODk5MDVjYTkzNTY1NjRmY2Y5MDE1ODk3YmNhMjQiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-03-10 14:02:08.284258');
INSERT INTO django_session VALUES('xmfu2av5jmskpax74u0mgueun1vws1t1','MTEyMjQ5MjdiZTMyZmJiNDc4ZmJmNDNiZTdhOTFlNjQwOTU0M2FjNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzYTJlY2UzNzI5Y2U1Yzk5OGI0MzkxZDViYjA2YmNjZTE5NWE0NDQ1In0=','2018-03-11 15:16:55.075855');
INSERT INTO django_session VALUES('c6yjzv2yux3mdjsmh91a2urrgsfnwc0m','YmY1YTExYzFhY2I0NTI4NzZmY2IyZGIzN2NiN2JhNDk1MjE5YzJkZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNWQ4YTZmZWFiOTg5NWYxN2MxMjI4Mjk5M2U0ZjBmMjYyYmQ1YjNhIn0=','2018-03-13 14:49:40.795565');
INSERT INTO django_session VALUES('uzo5rr690mvz49ozqaxsh9uv372zuqjh','YmY1YTExYzFhY2I0NTI4NzZmY2IyZGIzN2NiN2JhNDk1MjE5YzJkZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNWQ4YTZmZWFiOTg5NWYxN2MxMjI4Mjk5M2U0ZjBmMjYyYmQ1YjNhIn0=','2018-05-02 13:28:14.012800');
INSERT INTO django_session VALUES('cennen4z5z548rutdm4ek7ji7cfbw8wm','NmMzOWNlZDgyNDQ2MDJjNDE0YWY5MmM4OTk0MjlmNjhhY2JhMDRlZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjIiLCJfYXV0aF91c2VyX2hhc2giOiJiNWQ4YTZmZWFiOTg5NWYxN2MxMjI4Mjk5M2U0ZjBmMjYyYmQ1YjNhIn0=','2018-05-02 13:58:41.768620');
CREATE TABLE IF NOT EXISTS "testapp_blog" ("title" varchar(50) NOT NULL, "link" varchar(200) NOT NULL, "descript" varchar(100) NULL, "content" text NOT NULL, "blog_id" varchar(100) NOT NULL PRIMARY KEY);
INSERT INTO testapp_blog VALUES('dsdfsd','http://127.0.0.1:8000/blog?title=dsdfsd&id=-5627907445364614355','dfgdfgdfg','<p>dfgdfgdfg</p>','-5627907445364614355');
INSERT INTO testapp_blog VALUES('dsdfsd','http://127.0.0.1:8000/blog?title=dsdfsd&id=7482234273828271884','dfgdfgdfg','<p>dfgdfgdfg</p>','7482234273828271884');
INSERT INTO testapp_blog VALUES('yukyutk','http://127.0.0.1:8000/blog?title=yukyutk&id=-8508410932354782382','ytuitkyu','<p>ytuitkyu</p>','-8508410932354782382');
INSERT INTO testapp_blog VALUES('fghnfg','http://127.0.0.1:8000/blog?title=fghnfg&id=-5816925478739724666','therth','<p>therth</p>','-5816925478739724666');
CREATE TABLE IF NOT EXISTS "testapp_myuser_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "myuser_id" integer NOT NULL REFERENCES "testapp_myuser" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "testapp_myuser_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "myuser_id" integer NOT NULL REFERENCES "testapp_myuser" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "testapp_myuser" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "userid" integer NOT NULL UNIQUE, "headlink" varchar(50) NOT NULL);
INSERT INTO testapp_myuser VALUES(2,'pbkdf2_sha256$100000$44hTpBf1tnlM$0FHdB+BaLYZugUpxiksl10/oQfKXyvFQh0BgUWtOiQI=','2018-04-18 13:58:41.617513',1,'pan','','','asdasd@qq.com',1,1,'2018-02-27 14:48:49.345064',0,'/');
CREATE TABLE IF NOT EXISTS "testapp_reply" ("reply_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "to_commentId" integer NOT NULL, "to_username" varchar(20) NOT NULL, "content" text NOT NULL, "time" datetime NOT NULL, "userid" integer NOT NULL, "to_blogId" varchar(50) NOT NULL);
INSERT INTO testapp_reply VALUES(1,5,'pan','dfgefgrttr','2018-03-03 14:51:32.176152',0,'-8508410932354782382');
INSERT INTO testapp_reply VALUES(2,5,'pan','rtghrtghgrhrgh','2018-03-03 15:24:58.949071',0,'-8508410932354782382');
INSERT INTO testapp_reply VALUES(3,5,'pan','asddfggg','2018-03-03 15:46:58.676609',0,'-8508410932354782382');
INSERT INTO testapp_reply VALUES(4,5,'pan','asddfggg','2018-03-03 15:47:03.339923',0,'-8508410932354782382');
INSERT INTO testapp_reply VALUES(5,5,'pan','fuck you','2018-03-04 05:31:10.387233',0,'-8508410932354782382');
INSERT INTO testapp_reply VALUES(6,5,'pan','fuck','2018-03-04 05:31:41.611714',0,'-8508410932354782382');
INSERT INTO testapp_reply VALUES(7,10,'pan','sdfsdf','2018-04-18 13:28:33.666453',0,'-8508410932354782382');
CREATE TABLE IF NOT EXISTS "testapp_comment" ("comment_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "time" datetime NOT NULL, "content" text NOT NULL, "userid" integer NOT NULL, "to_blogId" varchar(50) NOT NULL);
INSERT INTO testapp_comment VALUES(5,'2018-02-27 14:50:22.960140','asdasdasd',0,'-8508410932354782382');
INSERT INTO testapp_comment VALUES(6,'2018-02-27 14:50:26.432924','asdasdasd',0,'-8508410932354782382');
INSERT INTO testapp_comment VALUES(7,'2018-03-03 06:31:26.993179','dfgdfbv',0,'-8508410932354782382');
INSERT INTO testapp_comment VALUES(8,'2018-03-03 06:31:40.370323','dfgrtrhnu74534',0,'-8508410932354782382');
INSERT INTO testapp_comment VALUES(9,'2018-03-03 06:36:24.868012','dfgfdgdfgdbu7867543233',0,'-8508410932354782382');
INSERT INTO testapp_comment VALUES(10,'2018-03-03 13:13:38.422536','sdfsdfdf456456',0,'-8508410932354782382');
INSERT INTO testapp_comment VALUES(11,'2018-03-03 13:14:07.527346','sdfsdfdf456456asdasdrgsfg',0,'-8508410932354782382');
INSERT INTO testapp_comment VALUES(12,'2018-03-03 13:43:22.546720','sdfgdgsfdg',0,'-8508410932354782382');
INSERT INTO testapp_comment VALUES(13,'2018-03-03 13:44:49.169849','ghjdchgjfth676786',0,'-8508410932354782382');
INSERT INTO testapp_comment VALUES(14,'2018-03-03 13:45:06.363625','dfgsrghhgjh655434jhg',0,'-8508410932354782382');
INSERT INTO testapp_comment VALUES(15,'2018-03-03 13:45:49.344276','dfgfsdgh56767',0,'-8508410932354782382');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',39);
INSERT INTO sqlite_sequence VALUES('django_admin_log',0);
INSERT INTO sqlite_sequence VALUES('django_content_type',13);
INSERT INTO sqlite_sequence VALUES('auth_permission',39);
INSERT INTO sqlite_sequence VALUES('auth_user',1);
INSERT INTO sqlite_sequence VALUES('testapp_myuser',2);
INSERT INTO sqlite_sequence VALUES('testapp_reply',7);
INSERT INTO sqlite_sequence VALUES('testapp_comment',15);
CREATE UNIQUE INDEX auth_group_permissions_group_id_permission_id_0cd325b0_uniq ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX auth_user_groups_user_id_group_id_94350c0c_uniq ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX auth_user_user_permissions_user_id_permission_id_14a6b632_uniq ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX django_content_type_app_label_model_76bd3d3b_uniq ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX auth_permission_content_type_id_codename_01ab375a_uniq ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE UNIQUE INDEX testapp_myuser_groups_myuser_id_group_id_a92556a2_uniq ON "testapp_myuser_groups" ("myuser_id", "group_id");
CREATE INDEX "testapp_myuser_groups_myuser_id_c53e6bcc" ON "testapp_myuser_groups" ("myuser_id");
CREATE INDEX "testapp_myuser_groups_group_id_0ea3b331" ON "testapp_myuser_groups" ("group_id");
CREATE UNIQUE INDEX testapp_myuser_user_permissions_myuser_id_permission_id_cb0f0a6e_uniq ON "testapp_myuser_user_permissions" ("myuser_id", "permission_id");
CREATE INDEX "testapp_myuser_user_permissions_myuser_id_24a7675b" ON "testapp_myuser_user_permissions" ("myuser_id");
CREATE INDEX "testapp_myuser_user_permissions_permission_id_67fd0a9c" ON "testapp_myuser_user_permissions" ("permission_id");
COMMIT;
