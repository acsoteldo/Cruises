-- Descriptive Analysis
SELECT
    COUNT(*) AS Num_Ships,
    AVG(Age) AS Avg_Age,
    MIN(Tonnage) AS Min_Tonnage,
    MAX(Passengers) AS Max_Passengers
FROM
    cruise_dataset_CLEANED;

-- Feature Importance Analysis
SELECT
    AVG(Tonnage) AS Avg_Tonnage,
    AVG(Passengers) AS Avg_Passengers,
    AVG(Length) AS Avg_Length
FROM
    cruise_dataset_CLEANED
GROUP BY
    Cruise_line
ORDER BY
    Avg_Tonnage DESC;

-- Segmentation Analysis
SELECT
    Cruise_line,
    AVG(Tonnage) AS Avg_Tonnage,
    AVG(Passengers) AS Avg_Passengers
FROM
    cruise_dataset_CLEANED
GROUP BY
    Cruise_line;

-- Correlation Analysis
SELECT
    CORR(Age, Tonnage) AS Age_Tonnage_Correlation,
    CORR(Passengers, Crew) AS Passengers_Crew_Correlation
FROM
    cruise_dataset_CLEANED;

-- Regression Analysis: linear regression
SELECT
    Ship_name,
    Age,
    Tonnage,
    Passengers,
    Crew,
    AVG(Total_Revenue) OVER (PARTITION BY Cruise_line ORDER BY Age) AS Avg_Revenue_By_Age
FROM
    cruise_dataset_CLEANED;
