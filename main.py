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
p=figure(y_range=(0,200), width=1500)
# arrays of colors and line styles
colors=['red','green','blue','purple','orange','lightblue','lightgreen','violet','black']
lineStyles=['solid','dashed','dotted']
iColor=0
iLine=0
# create years column
years=list(range(1960,2021))
sc.data['years']=years
# For each country create line plot using designated color and style
for country in df.columns:
    p.line(x='years', y=country, line_color=colors[iColor], line_dash=lineStyles[iLine], source=sc, line_width=2, legend_label=country)
    # cycle through colors and increment style one out of color
    iColor+=1
    if iColor>=len(colors):
        iColor=0
        iLine+=1
show(p)
