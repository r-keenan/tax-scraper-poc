import tabula

tables = tabula.read_pdf("slstax_rates_7-1-2023.pdf",
                         pages="all")
df = tables[0].to_string(header=False)
print(df)
