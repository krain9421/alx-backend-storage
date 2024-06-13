-- Script that creates a stored procedure AddBonus that adds a new correction for a student

DELIMITER $$
CREATE PROCEDURE AddBonus
	@user_id INT,
	@project_name VARCHAR(255)
	@score INT
AS
BEGIN
	IF NOT EXISTS (SELECT name FROM projects WHERE name = @project_name)
	BEGIN
		INSERT INTO projects (name)
		VALUES (@project_name);
	END

	--DECLARE @p_id INT;
	--SET @p_id = (SELECT project_id FROM projects WHERE name = @project_name);
	INSERT INTO corrections (user_id, project_id, score)
	SELECT @user_id, p.id, @score
	FROM projects p
	WHERE p.name = @project_name;

END $$
