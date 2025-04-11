

  create or replace view `bg-gcp-biomarkers`.`raw`.`stg_health_data`
  OPTIONS()
  as SELECT
  SEQN,
  RIAGENDR AS gender,
  RIDAGEYR AS age,
  LBXTC AS cholesterol
FROM `bg-gcp-biomarkers`.`raw`.`raw_health_data`
WHERE RIDAGEYR IS NOT NULL AND LBXTC IS NOT NULL;

