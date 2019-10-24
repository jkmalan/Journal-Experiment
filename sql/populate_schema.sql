/* Generate some test users */
INSERT INTO user
    (username, password, fullname, email, created_on, updated_on)
    VALUES
        ('jmalandrakis', 'Password#1', 'John Malandrakis', 'john@malandrakis.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('alincoln', 'Password#1', 'Abraham Lincoln', 'abraham@lincoln.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('jbieber', 'Password#1', 'Justin Bieber', 'justin@bieber.com', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

/* Generate some test journals */
INSERT INTO journal
    (title, user_id, created_on, updated_on)
    VALUES
        ('John''s Journal', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Abraham''s Journal', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Justin''s Journal', 3, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

/* Generate some test entries */
INSERT INTO entry
    (title, body, journal_id, created_on, updated_on)
    VALUES
        ('Entry 1', 'Today, I woke up. It sucked.', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Entry 2', 'Today, I woke up again. How unfortunate.', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Entry 3', 'Im still breathing *depressed sigh*', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Entry 1', 'Fourscore and seven years ago, I crushed Bobby''s army mercilessly. It was fun.', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Entry 2', 'It would seem I have been shot. Hopefully Mary isn''t too upset', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Entry 1', 'Dear Diary, I am beautiful. The end.', 3, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);