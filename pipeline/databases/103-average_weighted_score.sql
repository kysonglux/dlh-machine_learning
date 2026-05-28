-- creates a stored procedure
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_weighted FLOAT;

    SELECT SUM(score * weight) / SUM(weight)
    INTO avg_weighted
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    UPDATE users
    SET average_score = avg_weighted
    WHERE id = user_id;
END$$

DELIMITER ;