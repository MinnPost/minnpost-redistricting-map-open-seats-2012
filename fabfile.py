#!/usr/bin/env python
"""
This fabfile will allow us to style, render and deploy our map tiles for the redistricting project.
"""

import sys
import warnings

from fabric.api import local

try:
    exec(open('project_dirs.py'))
except IOError:
    warnings.warn('Using default variables - please create a project_dirs.py file')
    MAPS_LIST = ['redistricting_pvi_house', 'redistricting_pvi_senate']
    MAPBOX_PROJECTS_DIRECTORY = '/Users/minnpostproduction/Documents/MapBox/project/'
    MAPBOX_EXPORT_DIRECTORY = '/Users/minnpostproduction/Documents/MapBox/export/'
    PROJECT_DIRECTORY = '/Users/minnpostproduction/data_projects/redistricting-map-open-seats-2012/'
    S3_DIRECTORY_S3CMD = 's3://data.minnpost/maps/leg_districts/'
    S3_DIRECTORY = 'data.minnpost/maps/leg_districts/'

# #
# When making changes, update this and in map/data/{MAPS_LIST}.json
VERSION = 0.3

# #
# Functions
def deploy_all():
    """
    Copies the .mbtils file from exported MapBox projects, runs mb-util, deploys to s3
    Use this when all maps have changed.
    """

    for map in MAPS_LIST:
        copy_map_dirs(map)
        extract_tiles(map)
        deploy_map(map)
        deploy_json(map)

def setup_shapefiles():
    local('data/setup_data')

def calculate_shapefile(year):
    join_shapefiles(year)
    pivot_pvi(year)

def enter_precincts_shapefile():
    local('shp2pgsql -s 4326 -d data/shapefiles/precincts_pvi_mnleg_060810/vtd_20101029.shp precincts | psql -d minnpost_redistricting_2012')

def enter_district_shapefiles(year):

    if year == '2002':
        inFile = 'data/shapefiles/2002_leg/reprojected/tl_2010_27_sldl10.shp'
        local('shp2pgsql -s 4326 -d ' + inFile + ' districts_' + year + ' | psql -d minnpost_redistricting_2012')
    elif year == '2002_sen':
        inFile = 'data/shapefiles/2002_sen/reprojected/tl_2010_27_sldu10.shp'
        local('shp2pgsql -s 4326 -d ' + inFile + ' districts_sen_2002 | psql -d minnpost_redistricting_2012')
    elif year == '2012':
        inFile = 'data/shapefiles/2012_leg/L2012.shp'
        local('shp2pgsql -s 4326 -d ' + inFile + ' districts_' + year + ' | psql -d minnpost_redistricting_2012')
    elif year == '2012_sen':
        inFile = 'data/shapefiles/2012_sen/S2012.shp'
        local('shp2pgsql -s 4326 -d ' + inFile + ' districts_sen_2012 | psql -d minnpost_redistricting_2012')
    else:
        print 'Year not supported'
        sys.exit(2)
    

def join_shapefiles(year):
    if year == '2002':
        local('mkdir -p data/shapefiles/precincts_pvi_2002')
        local('pgsql2shp -f data/shapefiles/precincts_pvi_2002/precincts_pvi_2002.shp minnpost_redistricting_2012 "SELECT districts_2002.the_geom, districts_2002.sldlst10, precincts.ltr06, precincts.ltd06, precincts.lot06, precincts.ltr08, precincts.ltd08, precincts.lot08, precincts.ltr10, precincts.ltd10, precincts.lot10 FROM districts_2002 INNER JOIN precincts ON ST_Intersects(districts_2002.the_geom, ST_Centroid(precincts.the_geom));"')

    elif year == '2002_sen':
        local('mkdir -p data/shapefiles/precincts_pvi_sen_2002')
        local('pgsql2shp -f data/shapefiles/precincts_pvi_sen_2002/precincts_pvi_sen_2002.shp minnpost_redistricting_2012 "SELECT districts_sen_2002.the_geom, districts_sen_2002.sldust10, precincts.ltr06, precincts.ltd06, precincts.lot06, precincts.ltr08, precincts.ltd08, precincts.lot08, precincts.ltr10, precincts.ltd10, precincts.lot10 FROM districts_sen_2002 INNER JOIN precincts ON ST_Intersects(districts_sen_2002.the_geom, ST_Centroid(precincts.the_geom));"')

    elif year == '2012':
        local('mkdir -p data/shapefiles/precincts_pvi_2012')
        local('pgsql2shp -f data/shapefiles/precincts_pvi_2012/precincts_pvi_2012.shp minnpost_redistricting_2012 "SELECT districts_2012.the_geom, districts_2012.district, precincts.ltr06, precincts.ltd06, precincts.lot06, precincts.ltr08, precincts.ltd08, precincts.lot08, precincts.ltr10, precincts.ltd10, precincts.lot10 FROM districts_2012 INNER JOIN precincts ON ST_Intersects(districts_2012.the_geom, ST_Centroid(precincts.the_geom));"')

    elif year == '2012_sen':
        local('mkdir -p data/shapefiles/precincts_pvi_sen_2012')
        local('pgsql2shp -f data/shapefiles/precincts_pvi_sen_2012/precincts_pvi_sen_2012.shp minnpost_redistricting_2012 "SELECT districts_sen_2012.the_geom, districts_sen_2012.district, precincts.ltr06, precincts.ltd06, precincts.lot06, precincts.ltr08, precincts.ltd08, precincts.lot08, precincts.ltr10, precincts.ltd10, precincts.lot10 FROM districts_sen_2012 INNER JOIN precincts ON ST_Intersects(districts_sen_2012.the_geom, ST_Centroid(precincts.the_geom));"')

    else:
        print 'Year not supported'
        sys.exit(2)

def pivot_pvi(year):
    if year == '2002':
        local('python data/dbf_to_csv.py -f data/shapefiles/precincts_pvi_2002/precincts_pvi_2002.dbf -o data/shapefiles/precincts_pvi_2002/precincts_pvi_2002.csv')
        local('python data/pivot.py -f data/shapefiles/precincts_pvi_2002/precincts_pvi_2002.csv -o data/shapefiles/pvi_2002_leg/pvi_2002_leg -y 2002')

    elif year == '2002_sen':
        local('python data/dbf_to_csv.py -f data/shapefiles/precincts_pvi_sen_2002/precincts_pvi_sen_2002.dbf -o data/shapefiles/precincts_pvi_sen_2002/precincts_pvi_sen_2002.csv')
        local('python data/pivot.py -f data/shapefiles/precincts_pvi_sen_2002/precincts_pvi_sen_2002.csv -o data/shapefiles/pvi_2002_sen/pvi_2002_sen -y 2002')

    elif year == '2012':
        local('python data/dbf_to_csv.py -f data/shapefiles/precincts_pvi_2012/precincts_pvi_2012.dbf -o data/shapefiles/precincts_pvi_2012/precincts_pvi_2012.csv')
        local('python data/pivot.py -f data/shapefiles/precincts_pvi_2012/precincts_pvi_2012.csv -o data/shapefiles/pvi_2012_leg/pvi_2012_leg -y 2012')

    elif year == '2012_sen':
        local('python data/dbf_to_csv.py -f data/shapefiles/precincts_pvi_sen_2012/precincts_pvi_sen_2012.dbf -o data/shapefiles/precincts_pvi_sen_2012/precincts_pvi_sen_2012.csv')
        local('python data/csvstrip.py -f data/shapefiles/precincts_pvi_sen_2012/precincts_pvi_sen_2012.csv -o data/shapefiles/precincts_pvi_sen_2012/precincts_pvi_sen_2012_strip.csv')
        local('python data/pivot.py -f data/shapefiles/precincts_pvi_sen_2012/precincts_pvi_sen_2012_strip.csv -o data/shapefiles/pvi_2012_sen/pvi_2012_sen -y 2012_sen')

    else:
        print 'Year not supported'
        sys.exit(2)

def setup_deploy_map(map):
    """
    Calls copy_map_dirs, extract_tiles, deploy_map and deploy_json.
    """
    copy_map_dirs(map)
    extract_tiles(map)
    deploy_map(map)
    deploy_json(map)

def deploy_json(map):
    """
    Sends json file to s3
    """
    command = 's3cmd put -P ' + PROJECT_DIRECTORY + 'map/data/' + map + '.json ' + S3_DIRECTORY_S3CMD
    local(command)

def copy_map_dirs(map):
    """
    Sets up dirs for map, copies .mbtiles file
    """
    print 'Making map directory: ' + map
    command = 'mkdir -p tiles_' + map
    local(command)

    print 'Copying .mbtiles file: ' + map
    command = 'cp ' + MAPBOX_EXPORT_DIRECTORY + map + '.mbtiles ' + PROJECT_DIRECTORY + 'tiles_' + map
    local(command)

def extract_tiles(map):
    """
    Removes previously rendered tiles, then runs mb-util on the .mbtiles file.
    """
    print 'Removing previously rendered tyles for map: ' + map
    command = 'rm -Rf ' + PROJECT_DIRECTORY + 'tiles_' + map + '/rendered_tiles'
    local(command)

    print 'Running mb-util for map: ' + map
    #command = 'mb-util ' + map + '.mbtiles ' + PROJECT_DIRECTORY + ' ' + PROJECT_DIRECTORY + 'tiles_' + map + '/rendered_tiles'
    command = 'mb-util ' + PROJECT_DIRECTORY + 'tiles_' + map + '/' + map + '.mbtiles rendered_tiles'
    local(command)

    print 'Moving json file into rendered_tiles'
    command = 'mv ' + PROJECT_DIRECTORY + map + '.json ' + 'rendered_tiles/'

    print 'Moving rendered_tiles into correct directory'
    command = 'mv ' + PROJECT_DIRECTORY + 'rendered_tiles ' + PROJECT_DIRECTORY + 'tiles_' + map + '/'
    local(command)

    print 'Fixing version number'
    command = 'mv ' + PROJECT_DIRECTORY + 'tiles_' + map + '/rendered_tiles/1.0.0 ' + PROJECT_DIRECTORY + 'tiles_' + map + '/rendered_tiles/' + VERSION
    local(command)

def deploy_map(map):
    """
    Deploys the rendered tiles to s3.
    """

    print 'Deploying map: ' + map
    #command = 's3cmd put --recursive -P ' + PROJECT_DIRECTORY + 'tiles_' + map + '/rendered_tiles/ ' + S3_DIRECTORY_S3CMD
    command = 'ivs3 --concurrency 32 -P ' + PROJECT_DIRECTORY + 'tiles_' + map + '/rendered_tiles/ ' + S3_DIRECTORY
    local(command)

