

  create or replace view `bg-gcp-biomarkers`.`raw`.`fct_longevity_summary`
  OPTIONS()
  as SELECT
  gender,
  AVG(age) AS avg_age,
  AVG(cholesterol) AS avg_cholesterol,
  COUNT(*) AS num_people
FROM `bg-gcp-biomarkers`.`raw`.`int_biomarkers_enriched`
GROUP BY gender;

