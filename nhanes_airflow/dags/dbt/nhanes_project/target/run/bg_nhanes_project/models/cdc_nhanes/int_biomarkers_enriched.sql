

  create or replace view `bg-gcp-biomarkers`.`raw`.`int_biomarkers_enriched`
  OPTIONS()
  as SELECT *,
  CASE
    WHEN cholesterol < 200 THEN 'Desirable'
    WHEN cholesterol < 240 THEN 'Borderline High'
    ELSE 'High'
  END AS cholesterol_category
FROM `bg-gcp-biomarkers`.`raw`.`stg_health_data`;

