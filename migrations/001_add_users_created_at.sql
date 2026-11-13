-- Bring existing users tables into alignment with app.model.User.
-- Existing users receive the migration time as their created_at value.
ALTER TABLE users
    ADD COLUMN IF NOT EXISTS created_at TIMESTAMP WITH TIME ZONE
    NOT NULL DEFAULT now();
