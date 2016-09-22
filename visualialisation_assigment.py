
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import dates
from matplotlib.patches import Rectangle
from matplotlib.dates import DayLocator


with open('C:/Users/Yulia/Desktop/fernstudium/datascientist/python/ds/ticket_price_range.csv') as csvfile:
    df = pd.read_csv(csvfile)
#formate time variable
time_format = '%Y-%m-%d'
df['crawled_date'] = [datetime.strptime(i, time_format) for i in df['crawled_date']]

 #create plot
fig, ax = plt.subplots()
ax.plot_date(df['crawled_date'],df['max_prices'], fmt="r-", c="lightslategrey", label='Maximum Ticketpreise')
ax.plot_date(df['crawled_date'],df['min_prices'], fmt="r-", c="darkkhaki", label='Minimum Ticketpreise')
ax.plot_date(df['crawled_date'],df['ATP'], fmt="r-",c="black", label='Angebotene Ticketpreise') 
#format axes
pd = dates.DateFormatter('%m/%d/%y')
ax.xaxis.set_major_locator(dates.DayLocator(bymonthday='2016-06-30',interval=18))
ax.set_ylim(0,140)
ax.xaxis.set_major_formatter(pd)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='lower left', bbox_to_anchor=(1,0), frameon=False)
ax.set_title('Die Spannbreite der Ticketpreise',size=18, horizontalalignment='left')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(axis='y', direction='out')
#add frames
autoAxis = ax.axis()
rec = Rectangle((autoAxis[0]-5,autoAxis[2]-10),(autoAxis[1]-autoAxis[0])+50,(autoAxis[3]-autoAxis[2])+30,fill=False,lw=1,edgecolor="darkkhaki")
rec = ax.add_patch(rec)
rec.set_clip_on(False)
rec2 = Rectangle((autoAxis[0]-5,autoAxis[2]+142),(autoAxis[1]-autoAxis[0])+50,(autoAxis[3]-autoAxis[2])-120,fill=True,lw=1,edgecolor="darkkhaki",facecolor="darkkhaki")
rec2 = ax.add_patch(rec2)
rec2.set_clip_on(False)
 #save the plot 
fig.savefig("plot.png")
