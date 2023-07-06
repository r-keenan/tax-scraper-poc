import tabula
import pandas as pd
import urllib.request
import os

url = 'https://revenue.nebraska.gov/sites/revenue.nebraska.gov/files/doc/slstax_rates_7-1-2023.pdf'
write_file = 'Nebraska tax rates.pdf'

with urllib.request.urlopen(url) as response, open(write_file, 'wb') as write_file:
    data = response.read()
    write_file.write(data)

tables = tabula.read_pdf('Nebraska tax rates.pdf',
                         pages="all", multiple_tables=True)

for df in tables:
    df = df.iloc[1:].to_string(header=False)
    print(df)

os.remove('Nebraska tax rates.pdf')
