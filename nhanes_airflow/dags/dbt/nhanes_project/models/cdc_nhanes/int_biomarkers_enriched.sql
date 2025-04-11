SELECT *,
  CASE
    WHEN cholesterol < 200 THEN 'Desirable'
    WHEN cholesterol < 240 THEN 'Borderline High'
    ELSE 'High'
  END AS cholesterol_category
FROM {{ ref('stg_health_data') }}