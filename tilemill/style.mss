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

#l2012 {
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
  text-avoid-edges: true;
  text-placement-type: simple;
  text-allow-overlap: true;
} 
#l2012[MEANSPVI >= -100] { polygon-fill:@dem5; } 
#l2012[MEANSPVI >= -40] { polygon-fill:@dem4; } 
#l2012[MEANSPVI >= -20] { polygon-fill:@dem3; } 
#l2012[MEANSPVI >= -10] { polygon-fill:@dem2; } 
#l2012[MEANSPVI >= -5] { polygon-fill:@dem1; } 
#l2012[MEANSPVI >= -0.5] { polygon-fill:@neutral; } 
#l2012[MEANSPVI >= 0.5] { polygon-fill:@rep1; } 
#l2012[MEANSPVI >= 5] { polygon-fill:@rep2; } 
#l2012[MEANSPVI >= 10] { polygon-fill:@rep3; } 
#l2012[MEANSPVI >= 20] { polygon-fill:@rep4; } 
#l2012[MEANSPVI >= 40] { polygon-fill:@rep5; }
