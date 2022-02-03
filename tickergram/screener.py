# using finwiz screener 
# https://finviz.com/screener.ashx?v=111&f=an_recom_holdbetter,cap_midover,fa_eps5years_pos,fa_grossmargin_pos,fa_netmargin_pos,fa_opermargin_pos,fa_sales5years_pos,geo_usa,ta_rsi_os30&ft=4&o=-marketcap&r=1
import requests 
import pandas as pd


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_screener(version):
    screen = requests.get(f'https://finviz.com/screener.ashx?v={version}&f=an_recom_holdbetter,cap_midover,fa_eps5years_pos,fa_grossmargin_pos,fa_netmargin_pos,fa_opermargin_pos,fa_sales5years_pos,geo_usa,ta_rsi_os30&ft=4&o=-marketcap&r=1', headers = headers).text

    tables = pd.read_html(screen)
    tables = tables[-2]
    tables.columns = tables.iloc[0]
    tables = tables[1:]

    return tables

tables111 = get_screener('111')
tables161 = get_screener('161')
tables121 = get_screener('121')

consolidatedtables = pd.merge(tables111,tables161,how='outer',left_on='Ticker',right_on='Ticker')
consolidatedtables = pd.merge(consolidatedtables,tables121,how='outer',left_on='Ticker',right_on='Ticker')

consolidatedtables.to_csv('test.csv')


csv_file = pd.read_csv('test.csv', usecols = ['Ticker','P/E_x'])
print(csv_file)
#df = pd.read_csv(io.StringIO(s), usecols=['Ticker', 'P/E', 'Fwd P/E'])
#print(df)