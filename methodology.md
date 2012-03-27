Methodology

Our PVI is a Minnesota-specific version of the [Cook Partisan Index (CPVI)](http://en.wikipedia.org/wiki/Cook_Partisan_Voting_Index), which measures how strongly a geographic area leans toward one political party compared to the state as a whole.

Each district is assigned a PVI value, which shows its political leaning. R+12, for example, denotes that district leans Republican by 12 percentage points, whereas D+2 would represent a two percentage point leaning toward the Democratic party. EVEN means a political leaning of less than one percentage point.

Our calculations use four recent races:

- 2008 presidential
- 2008 state house
- 2010 governor
- 2010 state house

We calculated the PVI for each of these races at the precinct level, and then averaged these to find an overall PVI for each precinct. We also calculated the state's overall PVI using the same elctions, and subtracted this from each precinct to offset Minnesota's lean (which happened to be about zero percentage points).

We then matched these precincts geographically to the new district lines, averaging each precinct within each district. Many precinct lines fit exactly with the new district lines, but when they did not, our calculation includes any precincts that intersect with the district boundaries.

These numbers are then rounded to the nearest whole number and assigned a party for readability.

For the technical details, [check out our scripts and audit file](https://github.com/MinnPost/redistricting-map-open-seats-2012).
