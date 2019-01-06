import pandas as pd
from datetime import timedelta, date


baseurl = "https://promo.betfair.com/betfairsp/prices/dwbfpricesauswin"

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

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

start_date = date(2018, 1, 1)
end_date = date(2019, 1, 2)
for single_date in daterange(start_date, end_date):
    print("Processing " + str(single_date))
    try:
        url = str(baseurl) + str(single_date.strftime("%d%m%Y")) + ".csv"
        current_day_df = pd.read_csv(url)
        bsp_data_full = pd.concat([current_day_df, bsp_data_full], ignore_index=True, sort=False)
    except:
        pass