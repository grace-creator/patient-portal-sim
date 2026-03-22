CREATE USER patient_user WITH PASSWORD 'patient_pass';
CREATE DATABASE patient_db OWNER patient_user;

\c patient_db;

CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    note TEXT
);

INSERT INTO patients (first_name, last_name, dob, note) VALUES
('Alice', 'Rivera', '1985-03-12', 'Follow-up for lab results'),
('Bruno', 'Lopez', '1990-07-25', 'Annual checkup, no concerns'),
('Helena', 'Starling', '2021-11-05', 'Pediatrics visit: routine checkup');

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    hashed_password TEXT,
    role VARCHAR(20) -- 'admin', 'nurse', 'patient'
);


INSERT INTO users (username, hashed_password, role) VALUES
('admin_grace', 'hashed_pass_123', 'admin'),
('nurse_mark', 'hashed_pass_456', 'nurse'),
('patient_doe', 'hashed_pass_789', 'patient');


