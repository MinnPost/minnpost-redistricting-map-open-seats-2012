from ctupre import concatFields

# Add field CTUPRE to csv
concatFields('../2006_results.csv', '../2006_results_ctu.csv', 11, 9, 'CTUPRE')
concatFields('../2008_results.csv', '../2008_results_ctu.csv', 12, 1, 'CTUPRE')
concatFields('../2010_results.csv', '../2010_results_ctu.csv', 7, 1, 'CTUPRE')
