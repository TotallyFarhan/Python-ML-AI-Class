import pandas as pd
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale = 1.2)

recipes = pd.read_csv("Datasets/recipes_muffins_cupcakes.csv")

features = recipes[['Flour', 'Sugar']].to_numpy()
label = np.where(recipes['Type'] == 'Muffin', 0, 1)

model = svm.SVC(kernel='linear')
model.fit(features, label)

w = model.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(30, 60)
yy = a * xx - (model.intercept_[0]) / w[1]

b = model.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = model.support_vectors_[1]
yy_up = a * xx + (b[1] - a * b[0])

sns.lmplot(x="Flour", y="Sugar", data=recipes, hue='Type', palette='Set1', fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth = 2, color = 'black')

sns.lmplot(x="Flour", y="Sugar", data=recipes, hue='Type', palette='Set1', fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth = 2, color = 'black')
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=80, facecolors='none')

plt.axis([30, 60, 0, 35])

plt.show()

def muffin_or_cupcake(flour, sugar):
    if (model.predict([[flour, sugar]])) == 0:
        print("Muffin recipe")
    else:
        print("Cupcake recipe")
        
muffin_or_cupcake(50, 20)


