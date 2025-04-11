SELECT
  gender,
  AVG(age) AS avg_age,
  AVG(cholesterol) AS avg_cholesterol,
  COUNT(*) AS num_people
FROM {{ ref('int_biomarkers_enriched') }}
GROUP BY gender