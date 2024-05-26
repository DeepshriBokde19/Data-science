import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('fdata.csv')

dates = data['Date']
close_prices = data['Close']

plt.plot(dates, close_prices, marker='o')

plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Prices of Alphabet Inc. (Oct 3, 2016 - Oct 7, 2016)')


plt.show()
