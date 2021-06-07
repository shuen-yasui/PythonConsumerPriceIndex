import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Extract data from csv
df=pd.read_csv("data.csv", index_col=2)
print(df)
df=df.transpose()
# Drop cols and rows for debugging
df=df.drop(df.index[range(3)])
# Reset DF index
df=df.reset_index(drop=True)
print(df)
# Create Bokeh plot
sc=ColumnDataSource(df)
p=figure(y_range=(0,200))
p.line(x='index', y='Canada', line_color="blue", source=sc, line_width=2)
p.line(x='index', y='Switzerland', line_color="red", source=sc, line_width=2)
show(p)
