-- Script that lists all bands with 'Glam rock' as their main style, ranked by their longevity

SELECT band_name,
  CASE
	WHEN split is NULL THEN 2022
	ELSE split
  END - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
