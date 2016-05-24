import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd

output = [('24E', 10541), ('24G', 3391), ('24F', 3030), ('24A', 5394), ('24C', 3661), ('24N', 291), ('24I', 9819), ('24H', 16), ('24K', 199846), ('24U', 1), ('24T', 8276), ('24P', 2), ('29 ', 266), ('24R', 30), ('24Z', 10399), ('17Z', 6), ('17Y', 19), ('17U', 64), ('17R', 118), ('22H', 15), ('22Z', 271), ('22Y', 21201), ('15T', 267), ('15Z', 340), ('15C', 36805), ('11', 1157), ('15E', 181493), ('10', 11804), ('15I', 11), ('15', 2329776), ('15J', 32207), ('19', 284), ('20R', 1), ('20Y', 5), ('20C', 434), ('20 ', 1), ('CNDT', 1748), ('19J', 8), ('011', 2), ('29', 11), ('18G', 3004), ('18J', 2038), ('18K', 16746), ('18U', 271), ('13 ', 931), ('527', 41554), ('   ', 1), ('16F', 1), ('16G', 374), ('16C', 12807), ('16R', 3)]
#('', 2181964), 


df = pd.DataFrame(output, columns=["Type", "Count"])
df.head()

sns.barplot(df.Type, df.Count)
plt.title("Contribution Types")
plt.show()
