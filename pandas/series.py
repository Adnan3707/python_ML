# %%
import pandas as pd

sales_2023 = {
	"United States": 1250000,
	"Canada": 480000,
	"United Kingdom": 620000,
	"Australia": 390000,
	"India": 810000,
}

sales_2024 = {
	"United States": 1380000,
	"Canada": 525000,
	"United Kingdom": 675000,
	"Australia": 430000,
	"India": 940000,
}

sales_y1 = pd.Series(sales_2023)
sales_y2 = pd.Series(sales_2024)
# %%
sales_y1
# %%
sales_y1.keys()
# %%
