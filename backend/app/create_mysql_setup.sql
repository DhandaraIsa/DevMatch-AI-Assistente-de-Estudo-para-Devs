
CREATE DATABASE IF NOT EXISTS devmatch CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'devuser'@'localhost' IDENTIFIED BY 'devpass';
GRANT ALL PRIVILEGES ON devmatch.* TO 'devuser'@'localhost';
FLUSH PRIVILEGES;

