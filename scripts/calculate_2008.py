import csv

r1= csv.reader(open('../data/2008_general_results_cut.csv', 'rU'));
out = csv.writer(open('../data/2008_general_results_calculated.csv', 'wb'));

for line in r1:
    if line[0] == 'Statewide Totals':
        pres_votes_r_tot = int(line[6])
        pres_votes_d_tot = int(line[7])
        pres_votes_tot_tot = int(line[14])
        pres_spvi = round(1.0 * (pres_votes_r_tot - pres_votes_d_tot) / pres_votes_tot_tot, 5)
        mn_leg_votes_r_tot = int(line[25])
        mn_leg_votes_d_tot = int(line[26])
        mn_leg_votes_tot_tot = int(line[28])
        mn_leg_spvi = round((1.0 * (mn_leg_votes_r_tot - mn_leg_votes_d_tot) / mn_leg_votes_tot_tot), 5)
        state_spvi = round((pres_spvi + mn_leg_spvi) / 2.0, 5)
        print state_spvi

r2= csv.reader(open('../data/2008_general_results_cut.csv', 'rU'));

# Write header row
out.writerow(r2.next() + ['CTUPRE', 'SPVI']);

for line in r2:
    if line[0] != 'TOTALS':
        try:
            ctupre = str(int(line[4])) + ':' + str(int(line[1]))
        except ValueError:
            break
    spvi = 1000
    has_pres = False
    has_mn_leg = False

    pres_votes_r = int(line[6])
    pres_votes_d = int(line[7])
    pres_votes_tot = int(line[14])
    pres_percent_r = -1
    pres_percent_d = -1
    if pres_votes_tot != 0:
        has_pres = True
        pres_percent_r = round( 100 * ((1.0 * pres_votes_r) / pres_votes_tot), 5)
        pres_percent_d = round( 100 * ((1.0 * pres_votes_d) / pres_votes_tot), 5)
        pres_spvi = round(pres_percent_r - pres_percent_d)

    mn_leg_votes_r = int(line[25])
    mn_leg_votes_d = int(line[26])
    mn_leg_votes_tot = int(line[28])
    mn_leg_percent_r = -1
    mn_leg_percent_d = -1
    if mn_leg_votes_tot != 0:
        has_mn_leg = True
        mn_leg_percent_r = round( 100 * ((1.0 * mn_leg_votes_r) / mn_leg_votes_tot), 5)
        mn_leg_percent_d = round( 100 * ((1.0 * mn_leg_votes_d) / mn_leg_votes_tot), 5)
        mn_leg_spvi = round(mn_leg_percent_r - mn_leg_percent_d)
        
    if has_pres and has_mn_leg:
        spvi = int(round(((pres_spvi + mn_leg_spvi) / 2.0), 5) - state_spvi)

    out.writerow(line + [ctupre, spvi])
