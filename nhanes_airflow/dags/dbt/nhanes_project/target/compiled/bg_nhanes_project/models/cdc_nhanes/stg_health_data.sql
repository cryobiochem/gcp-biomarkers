SELECT
  SEQN,
  RIAGENDR AS gender,
  RIDAGEYR AS age,
  LBXTC AS cholesterol
FROM `bg-gcp-biomarkers`.`raw`.`raw_health_data`
WHERE RIDAGEYR IS NOT NULL AND LBXTC IS NOT NULL