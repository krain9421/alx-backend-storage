-- Script that creates a trigger that resets the attribute 'valid_email' only when the email has changed.

CREATE TRIGGER UpdateOnEmailChange ON users
AFTER UPDATE
AS
BEGIN
	IF UPDATE(email)
	BEGIN
		UPDATE users
		SET valid_email =
		CASE
			WHEN inserted.email <> deleted.email
			THEN 0

			ELSE valid_email
		END;
	END;
END;
