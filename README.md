Map to show Minnesota Legislative Redistricting 2012.

## Data

- Original Data from: http://www.gis.leg.mn/redist2010/plans.php?plname=L2012&pltype=court

### Data Manipulation

#### Bounding Box

 - Import L2012-shp.zip into PostGIS: ```shp2pgsql -d data/L2012-shp/L2012 redistricting_map | psql -U postgres -h localhost -d minnpost```
 - Query to get Bounding Box (Enveloper): ```
SELECT 
	district,
	ST_AsGeoJSON(BOX2D(ST_Transform(ST_SetSRID(the_geom, 26915), 4326)), 4) as geom
FROM
	redistricting_map;
```