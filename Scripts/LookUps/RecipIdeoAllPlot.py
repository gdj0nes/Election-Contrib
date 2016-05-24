import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd

output = [(-2.4, 392), (-2.3, 1472), (-2.2, 581), (-2.1, 619), (-2.0, 959), (-1.9, 2047), (-1.8, 7842), (-1.7, 43632), (-1.6, 355009), (-1.5, 459595), (-1.4, 577355), (-1.3, 508341), (-1.2, 350156), (-1.1, 318322), (-1.0, 243540), (-0.9, 248742), (-0.8, 256571), (-0.7, 289837), (-0.6, 247343), (-0.5, 190104), (-0.4, 163609), (-0.3, 151887), (-0.2, 146487), (-0.1, 151708), (-0.0, 172889), (0.1, 191980), (0.2, 248488), (0.3, 230281), (0.4, 207852), (0.5, 208604), (0.6, 232098), (0.7, 254168), (0.8, 295447), (0.9, 400978), (1.0, 405046), (1.1, 524672), (1.2, 415888), (1.3, 113807), (1.4, 53037), (1.5, 51127), (1.6, 8509), (1.7, 5103), (1.8, 9756), (1.9, 1254), (2.0, 1133), (2.1, 1210), (2.2, 975), (2.3, 1128), (2.4, 1103)]

output = sorted(output)
# ('', 3882045), 

output = [x for x in output if ((x[0] > -2.5) and (x[0] < 2.5))]
df = pd.DataFrame(output, columns=["Type", "Count"])
df.head()

sns.barplot(df.Type, df.Count)
plt.title("Recipient Political Leaning")
plt.xlim()
plt.show()
