-- script that converts database hbtn_0c_0 to UTF8 --
-- (utf8mb4, collate utf8mb4_unicode_ci) on your MySQL server --
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
