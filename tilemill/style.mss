Map {
  background-color: #b8dee6;
}

#countries {
  ::outline {
    line-color: #85c5d3;
    line-width: 2;
    line-join: round;
  }
  polygon-fill: #fff;
}

@rep5: #330304; 
@rep4: #3B0304; 
@rep3: #4C0406; 
@rep2: #641a1b; 
@rep1: #7a2f30; 
@neutral: #343030; 
@dem1: #4B5B67; 
@dem2: #243746; 
@dem3: #20313F; 
@dem4: #1C2C38; 
@dem5: #192631; 

#states { 
  line-color:#074c71; 
  line-width:2; 
  polygon-opacity:1; 
  polygon-fill:#6d716d; 
} 

#roads { 
  line-width:0.5; 
  line-color:#b2c8d1; 
}

#l2012[zoom >= 7] {
  polygon-opacity:1;
  polygon-fill:#ae8;
  line-color:#464646;
  line-width:0.5;
  text-name: "[DISTRICT]";
  text-face-name: "Helvetica Light";
  text-size: 12;
  text-fill: #ccc;
  text-min-path-length: 80;
  text-vertical-alignment: bottom;
  //text-avoid-edges: true;
  text-placement-type: simple;
  text-allow-overlap: true;
}

// House district-level fixes
#l2012[DISTRICT = "24B"][zoom = 9] { text-dx: 30; }
#l2012[DISTRICT = "24B"][zoom = 8] { text-dx: 10; }
#l2012[DISTRICT = "24B"][zoom = 10] { text-dx: 60; }
#l2012[DISTRICT = "24B"][zoom = 11] { text-dx: 160; }
#l2012[DISTRICT = "24B"][zoom = 12] { text-dx: 300; }
#l2012[DISTRICT = "21B"][zoom = 9] { text-dy: -30; }
#l2012[DISTRICT = "21B"][zoom = 8] { text-dy: -15; }
#l2012[DISTRICT = "21B"][zoom = 7] { text-dy: -10; }
#l2012[DISTRICT = "66B"][zoom = 11] { text-dy: -15; }
#l2012[DISTRICT = "66B"][zoom = 12] { text-dy: -30; }
#l2012[DISTRICT = "03A"][zoom = 7] { text-dy: -15; }
#l2012[DISTRICT = "03B"][zoom = 8] { text-dy: -8; }
#l2012[DISTRICT = "07B"][zoom = 9] { text-dy: -13; }
#l2012[DISTRICT = "43A"][zoom = 10] { text-dx: -5; }
#l2012[DISTRICT = "46A"][zoom = 10] { text-dx: 5; }
#l2012[DISTRICT = "46A"][zoom = 10] { text-dy: 5; }
#l2012[DISTRICT = "57A"][zoom = 11] { text-dy: -5; }
#l2012[DISTRICT = "61A"][zoom = 11] { text-dx: -1; }
#l2012[DISTRICT = "64A"][zoom = 11] { text-dx: -5; }
#l2012[DISTRICT = "59B"][zoom = 11] { text-dy: -2; }
#l2012[DISTRICT = "43A"][zoom = 11] { text-dx: -8; }

// Senate district-level fixes
#l2012[DISTRICT = "62"][zoom = 11] { text-min-path-length: 0; }
#l2012[DISTRICT = "03"][zoom = 7] { text-dy: -15; }
#l2012[DISTRICT = "34"][zoom = 9] { text-dx: 5; }
#l2012[DISTRICT = "57"][zoom = 9] { text-dy: -5; }
#l2012[DISTRICT = "44"][zoom = 10] { text-dx: -5; }
#l2012[DISTRICT = "46"][zoom = 10] { text-dx: 5; }
#l2012[DISTRICT = "65"][zoom = 10] { text-dx: 5; }
#l2012[DISTRICT = "65"][zoom = 11] { text-dx: 10; }

#l2012[PVI >= -100] { polygon-fill:@dem5; } 
#l2012[PVI >= -50] { polygon-fill:@dem4; } 
#l2012[PVI >= -20] { polygon-fill:@dem3; } 
#l2012[PVI >= -10] { polygon-fill:@dem2; } 
#l2012[PVI >= -4] { polygon-fill:@dem1; } 
#l2012[PVI >= -0.5] { polygon-fill:@neutral; } 
#l2012[PVI >= 0.5] { polygon-fill:@rep1; } 
#l2012[PVI >= 4] { polygon-fill:@rep2; } 
#l2012[PVI >= 10] { polygon-fill:@rep3; } 
#l2012[PVI >= 20] { polygon-fill:@rep4; } 
#l2012[PVI >= 50] { polygon-fill:@rep5; }

