
import datetime as dt
import matplotlib.pyplot as plot
import matplotlib.dates as mp_ds
import yfinance as yf
from mpl_finance import candlestick_ochl

# dateframes
start = dt.datetime(2025,5,1,)
end = dt.datetime.now()

# Load data
try :
    info = yf.Ticker(name).info

    print('fetching ..  ')
except:
    print('this does not exist')

data = yf.download('AAPL',start, end,auto_adjust=False)

# data preparation
data.reset_index(inplace=True)
data = data[['Date', 'Close', 'High', 'Low', 'Open',]]
data = data[1:]

data['Date'] = data['Date'].map(mp_ds.date2num)
cols = list(data.columns)
i, j = cols.index("Close"), cols.index("Open")
cols[i], cols[j] = cols[j], cols[i]
data = data[cols]

# values to vizualise
ohlc = data[['Date', 'Open', 'Close', 'High', 'Low']].values


# Matpotlib
ax = plot.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.xaxis_date()
candlestick_ochl(ax, ohlc, width=0.5, colorup='g', colordown='r')
plot.show()