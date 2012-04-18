Data analysis and interactive map for Minnesota's 2012 districts

## Methodology

Our PVI is a Minnesota-specific version of the [Cook Partisan Index (CPVI)](http://en.wikipedia.org/wiki/Cook_Partisan_Voting_Index), which measures how strongly a geographic area leans toward one political party.

Each district is assigned a PVI value, which shows its political leaning. R+12, for example, denotes that district leans Republican by 12 percentage points, whereas D+2 would represent a two percentage point leaning toward the Democratic party. EVEN means a political leaning of less than one percentage point.

Our calculations use three recent races:

- 2006 state house
- 2008 state house
- 2010 state house

Using a spatial database process, we matched up each precinct to its newly assigned district. For example, a precinct with a [geometric centroid](http://postgis.refractions.net/docs/ST_Centroid.html) in district 21A would be considered part of that district.

We then add up the total votes for each party per 2012 district, for each race. These numbers are turned into a PVI index as follows:

```
100 * ((Votes for a republican candidate / Total number of votes) - (Votes for a democratic candidate / Total number of votes))
```

This is calculated for each race. The average of these gives the overall PVI used in our visualization. These numbers are then rounded to the nearest whole number and assigned a party for readability.

For the technical details, [check out our scripts](https://github.com/MinnPost/redistricting-map-open-seats-2012/tree/master/data/scripts).

## Data

- 2002/2012 district plans from [Minnesota GIS](http://www.gis.leg.mn/redist2010/plans.html)
- Voting results from [Minnesota Secretary of State](http://www.sos.state.mn.us/index.aspx?page=137)

### Data Manipulation

#### Bounding Box

Import L2012-shp.zip into PostGIS: ```shp2pgsql -d data/L2012-shp/L2012 redistricting_map | psql -U postgres -h localhost -d minnpost```

Query to get Bounding Box (Enveloper): ```
SELECT 
	district,
	ST_AsGeoJSON(BOX2D(ST_Transform(ST_SetSRID(the_geom, 26915), 4326)), 4) as geom
FROM
	redistricting_map;
```

Converted this output to CSV, then to JSON with csvjson (csvkit).

#### Pvi calculations
Get data in line:

```
mkdir -p originals
cp *.xls originals
in2csv 2006_general_results.xls > 2006_results.csv
in2csv 2008_general_results.xls > 2008_results.csv
in2csv 2010_General_Results_Final.xls > 2010_results.csv
python prep.py
python calculate.py
```

Use fabfile.py functions:

```fab setup_shapefiles``` 

```fab enter_precincts_shapefile:{2002,2002_sen,2010,2012_sen}```

```fab calculate_shapefile:{2002,2002_sen,2010,2012_sen}```
