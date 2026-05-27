-- creates a stored procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_weighted FLOAT;

    SELECT SUM(score * weight) / SUM(weight)
    INTO avg_weighted
    FROM corrections
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = avg_weighted
    WHERE id = user_id;
END$$

DELIMITER ;