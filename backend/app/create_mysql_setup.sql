-- Cria banco e usuário para o projeto DevMatch
CREATE DATABASE IF NOT EXISTS devmatch CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'devuser'@'localhost' IDENTIFIED BY 'devpass';
GRANT ALL PRIVILEGES ON devmatch.* TO 'devuser'@'localhost';
FLUSH PRIVILEGES;

-- Se for necessário acesso remoto, execute (ajuste host/substitua '%'):
-- CREATE USER IF NOT EXISTS 'devuser'@'%' IDENTIFIED BY 'devpass';
-- GRANT ALL PRIVILEGES ON devmatch.* TO 'devuser'@'%';
-- FLUSH PRIVILEGES;
