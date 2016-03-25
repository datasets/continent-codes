#!/usr/bin/python

import os
import csv

CONTINENTS = {'AF': 'Africa',
				'AN':'Antarctica',
				'AS': 'Asia',
				'EU': 'Europe',
				'NA': 'North America',
				'OC': 'Oceania',
				'SA': 'South America'}
				

def process():
	'''
	
	'''
	filename = 'continent_codes'
	if not os.path.exists('data'):
		os.makedirs('data')
	with open('data/' + filename, 'w') as working_file:
		csvwriter = csv.writer(working_file)
		header = ['Code','Name']
		csvwriter.writerow(header)
		for continent in CONTINENTS:
			csvwriter.writerow([continent, CONTINENTS[continent]])
						
if __name__ == '__main__':
	process()
