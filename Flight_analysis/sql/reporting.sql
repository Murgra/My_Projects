
CREATE SCHEMA IF NOT EXISTS reporting;


CREATE OR REPLACE VIEW reporting.flight AS
SELECT 
    *,
    CASE 
        WHEN dep_delay_new > 0 THEN 1 
        ELSE 0 
    END AS is_delayed
FROM public.flight
WHERE cancelled = 0;

CREATE OR REPLACE VIEW reporting.top_reliability_roads AS
SELECT 
    f.origin_airport_id,
    al.display_airport_name AS origin_airport_name,
    f.dest_airport_id,
    al2.display_airport_name AS dest_airport_name,
    f.year,
    COUNT(*) AS cnt,
    AVG(CASE WHEN f.dep_delay_new > 0 THEN 1 ELSE 0 END) AS reliability,
    ROW_NUMBER() OVER (PARTITION BY f.origin_airport_id, f.dest_airport_id ORDER BY AVG(CASE WHEN f.dep_delay_new > 0 THEN 1 ELSE 0 END) DESC) AS nb
FROM public.flight f
JOIN public.airport_list al ON f.origin_airport_id = al.origin_airport_id
JOIN public.airport_list al2 ON f.dest_airport_id = al2.origin_airport_id
GROUP BY f.origin_airport_id, f.dest_airport_id, al.display_airport_name, al2.display_airport_name, f.year
HAVING COUNT(*) > 10000;

CREATE OR REPLACE VIEW reporting.year_to_year_comparision AS
SELECT 
    year,
    month,
    COUNT(*) AS flights_amount,
    AVG(CASE WHEN dep_delay_new > 0 THEN 1 ELSE 0 END) AS reliability
FROM public.flight
GROUP BY year, month;

CREATE OR REPLACE VIEW reporting.day_to_day_comparision AS
SELECT 
    year,
    day_of_week,
    COUNT(*) AS flights_amount
FROM public.flight
GROUP BY year, day_of_week;

CREATE OR REPLACE VIEW reporting.day_by_day_reliability AS
SELECT 
    TO_DATE(LPAD(year::text, 4, '0') || '-' || LPAD(month::text, 2, '0') || '-' || LPAD(day_of_month::text, 2, '0'), 'YYYY-MM-DD') AS date,
    AVG(CASE WHEN dep_delay_new > 0 THEN 1 ELSE 0 END) AS reliability
FROM public.flight
GROUP BY year, month, day_of_month