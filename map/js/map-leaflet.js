/**
 * Redistricting map 2012
 */

// Global variables (because its just a little easier :)
var map = { "house": null, "senate": null };
var interaction;
var geocoder = new google.maps.Geocoder();
var marker;

// Namespace jQuery
(function($) {

/**
 * Document ready event.
 */
$(document).ready(function() {
  // Map, house legislating district.
  wax.tilejson('http://data.minnpost.s3.amazonaws.com/maps/leg_districts/redistricting_pvi_house.json',
    function(tilejson) {
      map.house = new L.Map('district-map-house')
        .addLayer(new wax.leaf.connector(tilejson))
        .setView(new L.LatLng(46.3, -94.2), 7);
        //.setMaxBounds(new L.LatLngBounds(new L.LatLng(-97.7124, 43.125), new L.LatLng(-89.165, 49.5466)));
        
      // Add wax interaction with UTFGrid data.
      interaction = wax.leaf.interaction(map.house, tilejson);
      
      // Map, senate legislating district.
      wax.tilejson('http://data.minnpost.s3.amazonaws.com/maps/leg_districts/redistricting_pvi_senate.json',
        function(tilejson) {
          map.senate = new L.Map('district-map-senate')
            .addLayer(new wax.leaf.connector(tilejson))
            .setView(new L.LatLng(46.3, -94.2), 7);
            //.setMaxBounds(new L.LatLngBounds(new L.LatLng(-97.7124, 43.125), new L.LatLng(-89.165, 49.5466)));
            
          // Add wax interaction with UTFGrid data.
          interaction = wax.leaf.interaction(map.senate, tilejson);
          
          // Tabs here to ensure all is loaded.
          $('#tabs').tabs();
        }
      );
    }
  );
    
  // Handle looking up address form.
  $("#redist-search-house").submit(function() {
    geocode($('#redist-query-house').val(), 'house');
    return false;
  });
  $("#redist-search-senate").submit(function() {
    geocode($('#redist-query-senate').val(), 'senate');
    return false;
  });
  
  // DataTable
  $('table').dataTable({
    'aaSorting': [[ 0, 'asc' ]]
  });
  
  // District selecting
  $.getJSON('data/L2012-shp-bounding_box.json', function(data) {
    // Add click events
    $('#tabs-house table tbody tr').live('click', function() {
      // Get districts
      var district = $('td.district', this).text();
      
      if (data[district] !== undefined) {
        district = data[district];
        
        // Zoom in
        var bounds = new L.LatLngBounds();
        for (var i in district.geom.coordinates[0]) {
          bounds.extend(new L.LatLng(district.geom.coordinates[0][i][1], district.geom.coordinates[0][i][0]));
        }
        map.house.fitBounds(bounds);
      }
    });
  });
  
  
  // Table making (remove for production)
  /*
  $.getJSON('data/open_seats_house.json', function(data) {
    var table = $('<table></table>');
    for (var i in data) {
      var row = '';
      row += '\n\n                <tr>';
      row += '\n                  <td class="district">' + data[i]['District'] + '</td>';
      if (data[i]["Retire?"] == "1") {
        row += '\n                  <td>' + data[i]["Retiree"];
        if (data[i]["Retiree party"] == 'DFL') {
          row += '<span class="inc-dfl"></span>';
        }
        else {
          row += '<span class="inc-r"></span>';
        }
        row += '</td>'
      }
      else {
        row += '\n                  <td>(open)</td>';
      }
      row += '\n                  <td class="leaning-';
      row += (data[i]["RPVI"].indexOf('R') >= 0) ? 'r' : '';
      row += (data[i]["RPVI"].indexOf('D') >= 0) ? 'dfl' : '';
      row += (data[i]["RPVI"].indexOf('EVE') >= 0) ? 'even' : '';
      row += '">' + data[i]["RPVI"] + '</td>\n';
      row += '\n                </tr>';
      
      table.append($(row));
    }
    $('body').append(table);
  });
  */
});

/**
 * Geocode address from form.
 */
function geocode(query, type) {
  // Check for minnesota or MN, and if not, add it.
  var gr = { 'location': query };
  if (typeof(query) == 'string') {
    var pattr = /\smn\s|\sminnesota\s/gi;
    var match = query.match(pattr);
    if (!match) {
      query = query + ' MN';
    }
    gr = { 'address': query };
  }
  
  // Geocode and fire callback.
  geocoder.geocode(gr, function(results, status) {
    var lat = results[0].geometry.location.lat();
    var lng = results[0].geometry.location.lng();
    var normalized_address = results[0].formatted_address;
    
    // Update form value with nice address.
    $('#redist-query-' + type).val(normalized_address)
  
    // Add marker and center
  	var point = new L.LatLng(lat, lng);
  	marker = new L.Marker(point);
  	map[type].addLayer(marker);
  	map[type].setView(point, 12);
  });
}

})(jQuery);
