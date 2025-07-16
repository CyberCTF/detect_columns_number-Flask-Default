CREATE DATABASE IF NOT EXISTS acme_research;
USE acme_research;

CREATE TABLE IF NOT EXISTS projects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    lead VARCHAR(255) NOT NULL,
    status VARCHAR(100) NOT NULL
);

INSERT INTO projects (title, lead, status) VALUES
('Quantum Computing Initiative', 'Dr. Alice Smith', 'Active'),
('AI for Healthcare', 'Dr. Bob Lee', 'Completed'),
('Renewable Energy Storage', 'Dr. Carol White', 'Active'),
('Mars Habitat Design', 'Dr. Dave Brown', 'Planning'); 