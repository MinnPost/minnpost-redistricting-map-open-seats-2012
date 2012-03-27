import csv

r1= csv.reader(open('../data/2010_general_results_cut.csv', 'rU'));
out = csv.writer(open('../data/2010_general_results_calculated.csv', 'wb'));

for line in r1:
    if line[0] == 'TOTALS':
        gov_votes_r_tot = int(line[24])
        gov_votes_d_tot = int(line[25])
        gov_votes_tot_tot = int(line[31])
        gov_spvi = round((1.0 * (gov_votes_r_tot - gov_votes_d_tot)) / gov_votes_tot_tot, 5)
        mn_leg_votes_r_tot = int(line[19])
        mn_leg_votes_d_tot = int(line[20])
        mn_leg_votes_tot_tot = int(line[22])
        mn_leg_spvi = round((1.0 * (mn_leg_votes_r_tot - mn_leg_votes_d_tot) / mn_leg_votes_tot_tot), 5)
        state_spvi = round((gov_spvi + mn_leg_spvi) / 2.0, 5)
        print state_spvi

r2= csv.reader(open('../data/2010_general_results_cut.csv', 'rU'));

# Write header row
out.writerow(r2.next() + ['CTUPRE', 'SPVI']);

for line in r2:
    if line[0] != 'TOTALS':
        try:
            ctupre = str(int(line[4])) + ':' + str(int(line[1]))
        except ValueError:
            break
    spvi = 1000
    has_gov = False
    has_mn_leg = False

    gov_votes_r = int(line[24])
    gov_votes_d = int(line[25])
    gov_votes_tot = int(line[31])
    gov_percent_r = -1
    gov_percent_d = -1
    if gov_votes_tot != 0:
        has_gov = True
        gov_percent_r = round( 100 * ((1.0 * gov_votes_r) / gov_votes_tot), 5)
        gov_percent_d = round( 100 * ((1.0 * gov_votes_d) / gov_votes_tot), 5)
        gov_spvi = gov_percent_r - gov_percent_d

    mn_leg_votes_r = int(line[19])
    mn_leg_votes_d = int(line[20])
    mn_leg_votes_tot = int(line[22])
    mn_leg_percent_r = -1
    mn_leg_percent_d = -1
    if mn_leg_votes_tot != 0:
        has_mn_leg = True
        mn_leg_percent_r = round( 100 * ((1.0 * mn_leg_votes_r) / mn_leg_votes_tot), 5)
        mn_leg_percent_d = round( 100 * ((1.0 * mn_leg_votes_d) / mn_leg_votes_tot), 5)
        mn_leg_spvi = mn_leg_percent_r - mn_leg_percent_d
        
    if has_gov and has_mn_leg:
        spvi = int(round(((gov_spvi + mn_leg_spvi) / 2.0), 5) - state_spvi)
 
    out.writerow(line + [ctupre, spvi])
