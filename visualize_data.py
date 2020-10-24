import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv('iphone_price.csv')
plt.bar(data['version'], data['price'])
plt.show()