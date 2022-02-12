CREATE DATABASE expense_tracker;
CREATE USER expense_tracker_user WITH PASSWORD 'expense_tracker';
GRANT ALL PRIVILEGES ON DATABASE expense_tracker TO expense_tracker_user;