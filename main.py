import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Extract data from csv
df=pd.read_csv("data.csv", index_col=2)
df=df.transpose()
# Drop cols and rows for debugging
df=df.drop(df.index[range(3)])
df.drop(df.columns[2:], axis = 1, inplace = True)
df.drop(df.columns[0], axis = 1, inplace = True)
# Reset DF index
df=df.reset_index(drop=True)
print(df)
# Create Bokeh plot
sc=ColumnDataSource(df)
p=figure(y_range=(0,200))
p.line(x='index', y='Canada', source=sc, line_width=2)
#p.vbar(x='index', top='Canada', source=sc, width=0.7)
show(p)
