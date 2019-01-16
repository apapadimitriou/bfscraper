import pandas as pd
from datetime import timedelta, date, datetime

def daterange(start_date, end_date):
    for n in range(int(((end_date - start_date).days) + 1)):
        yield start_date + timedelta(n)

def scrape(start_date, end_date):
	start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
	end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
	base_url   = "https://promo.betfair.com/betfairsp/prices/dwbfpricesauswin"

	column_names = ['EVENT_ID',
	                'MENU_HINT',
	                'EVENT_NAME',
	                'EVENT_DT',
	                'SELECTION_ID',
	                'SELECTION_NAME',
	                'WIN_LOSE',
	                'BSP',
	                'PPWAP',
	                'MORNINGWAP',
	                'PPMAX',
	                'PPMIN',
	                'IPMAX',
	                'IPMIN',
	                'MORNINGTRADEDVOL',
	                'PPTRADEDVOL',
	                'IPTRADEDVOL']

	bsp_data_full = pd.DataFrame(columns=column_names)

	for single_date in daterange(start_date, end_date):
	    print("Processing " + str(single_date))
	    try:
	        url = str(base_url) + str(single_date.strftime("%d%m%Y")) + ".csv"
	        current_day_df = pd.read_csv(url)
	        bsp_data_full = pd.concat([current_day_df, bsp_data_full], ignore_index=True, sort=False)
	    except:
	        pass

	return bsp_data_full

if __name__ == '__main__':
	df = scrape("2018-01-01", "2018-01-02")
	print(df)