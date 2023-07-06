import tabula
import pandas as pd

tables = tabula.read_pdf("slstax_rates_7-1-2023.pdf",
                         pages="all", multiple_tables=True)

for df in tables:
    df = df.iloc[1:].to_string(header=False)
    print(df)
