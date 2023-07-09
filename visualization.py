import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import math
import seaborn as sns
sns.set()
sns.set_style('white')
color1 = '#22A699'
color2 = '#17594A'
color3 = '#025464'

data = pd.read_csv('immobilieraVendre2023.csv')

figure, axes = plt.subplots(1, 2, figsize=(10,5))
axes[0].set_title('Average Price of Real Estate')
axes[0].set_xlabel('Euros per Square Meter')
axes[1].set_title('Average Size of Sale Property')
axes[1].set_xlabel('Size in Square Meters')
sns.histplot(data=data, x='pricem2', ax=axes[0], bins=30, color=color1)
sns.histplot(data=data, x='size', ax=axes[1], bins=50, color=color1)

left = data[(data['arrondissement']==5) | (data['arrondissement']==6) | (data['arrondissement']==7) |
            (data['arrondissement']==13) | (data['arrondissement']==14) | (data['arrondissement']==15)]
right = data[(data['arrondissement']==1) | (data['arrondissement']==2) | (data['arrondissement']==3) |
             (data['arrondissement']==4) | (data['arrondissement']==8) | (data['arrondissement']==9) |
             (data['arrondissement']==10) | (data['arrondissement']==11) | (data['arrondissement']==12) |
             (data['arrondissement']==16) | (data['arrondissement']==17) | (data['arrondissement']==18) |               (data['arrondissement']==19) | (data['arrondissement']==20)]
banks_df = pd.DataFrame()
banks_df['Bank'] = ['left','right']
banks_df['mean'] = [round(left['pricem2'].mean()),round(right['pricem2'].mean())]

sns.set_style('white')
figure, axes = plt.subplots(1, 2, figsize=(12,5), sharey=True)
axes[0].set_title('Average Price of Real Estate Based on Location')
axes[0].set_xlabel('Arrondissement')
axes[1].set_title('Average Price of Real State Based on Banks of the Seine')
axes[1].set_xlabel('Bank of the Seine')
sns.stripplot(data=data, x='arrondissement', y='pricem2', ax=axes[0], palette='viridis', jitter=0.3, edgecolor='white', linewidth=1)
ax = sns.barplot(data=banks_df, x='Bank', y='mean', color='#00DFA2', width=0.5, alpha=0.75)
ax.bar_label(ax.containers[0])

sns.set_style('whitegrid')
fibonnaci = sns.relplot(data=data, x='size', y='pricem2', col='arrondissement', color=color2, col_wrap=4, markers='o', s=200)
fibonnaci.set_ylabels("Price per Square Meter in Euros", clear_inner=True)

log_price = np.log(data["pricem2"])
data["log_price"] = log_price
data = data.drop(["rooms"], axis=1)
targets = data["log_price"]
inputs = data.drop(["log_price", "price", "pricem2", "size", "arrondissement"], axis=1)
sns.set_style('white')
scaler = StandardScaler()
scaler.fit(inputs)

inputs_scaled = scaler.transform(inputs)

x_train, x_test, y_train, y_test = train_test_split(inputs_scaled, targets, test_size=0.2, random_state=45)
reg = LinearRegression()
reg.fit(x_train, y_train)
yhat = reg.predict(x_train)

reg_summary = pd.DataFrame(inputs.columns.values, columns=["Features"])
reg_summary["Weights"] = reg.coef_

plt.plot(reg_summary['Weights'], color=color1)

yhat_test = reg.predict(x_test)
plt.scatter(y_test, yhat_test, color=color2, alpha=0.75, edgecolors='white', linewidths=1)
plt.xlabel("Targets", size=10)
plt.ylabel("Prediction", size=10)
plt.show()

df_pf = pd.DataFrame((yhat_test), columns=["Predictions"])
y_test = y_test.reset_index(drop=True)
df_pf["Target"] = (y_test)
df_pf["Residual"] = df_pf["Target"] - df_pf["Predictions"]
df_pf["Difference%"] = round(np.absolute(df_pf["Residual"]/df_pf["Target"]*100))

sns.countplot(data=df_pf, color='#00DFA2', x='Difference%')
plt.title('Measure of Model Precision')
plt.xlabel('Difference between predicted and actual values')
plt.ylabel('Number of predictions')

tree_data = pd.read_csv('arbresremarquablesparis.csv')

tree_list = []
for i in range(1, 21):
    count = tree_data[tree_data['arrondissement'] == i].count()
    tree_list.append(count['index'])
tree_df = pd.DataFrame()
tree_df['arrondissement'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
tree_df['count'] = tree_list
sns.barplot(data=tree_df, x='arrondissement', y='count', palette='viridis')
plt.title('Number of Trees per Arrondissement')
plt.xlabel('Arrondissement')
plt.ylabel('')

ilots = pd.read_csv('ilots-de-fraicheur-espaces-verts-frais.csv')
ilots['coverage'] = ilots['percent_veg']*100

sns.kdeplot(data=ilots, x='coverage', y='arrondissement', cmap='Greens', fill=True)
sns.despine(left=True, bottom=True)
plt.title('Vegetation Desntiy of Paris by Arrondissement')
plt.xlabel('Percentage of plant coverage')
plt.ylabel('Arrondissement')

data = pd.read_csv('immoVenduFinal.csv')

figure, axes = plt.subplots(1, 2, figsize=(12,5))
axes[0].set_title('Location of Historical Trees')
axes[0].set_xlabel('Arrondissement')
axes[0].set_ylabel('Height in meters')
axes[1].set_title('Location of Green Spaces')
axes[1].set_xlabel('Arrondissement')
axes[1].set_ylabel('Percent or vegetation coverage')
sns.stripplot(data=tree_data, x='arrondissement', y='hauteur_m', ax=axes[0], palette='mako', jitter=0.3, edgecolor='white', linewidth=1)
sns.stripplot(data=ilots, x='arrondissement', y='coverage', ax=axes[1], palette='mako', jitter=0.3, edgecolor='white', linewidth=1)

figure, axes = plt.subplots(1, 2, figsize=(12,5), sharey=True)
axes[0].set_title('Price of Real Estate Relative to the Nearest Tree')
axes[0].set_xlabel('Distance to nearest tree in meters')
axes[0].set_ylabel('Price per square meter in euros')
axes[1].set_title('Price of Real Estate Relative to the Nearest Green Space')
axes[1].set_xlabel('Distance to nearest green space in meters')
sns.kdeplot(data=data, x='tree_dist', y='pricem2', ax=axes[0], cmap='Greens', fill=True)
sns.despine(left=True, bottom=True)
sns.kdeplot(data=data, x='ilot_dist', y='pricem2', ax=axes[1], cmap='Greens', fill=True)

twentyfive_tree = data[data['tree_dist'] <= 25]
twentyfive_ilot = data[data['ilot_dist'] <= 25]
twentyfive_aire = data[data['aire_dist'] <= 25]
fifty_tree = data[data['tree_dist'] <= 50]
fifty_ilot = data[data['ilot_dist'] <= 50]
fifty_aire = data[data['aire_dist'] <= 50]
hundred_tree = data[data['tree_dist'] <= 100]
hundred_ilot = data[data['ilot_dist'] <= 100]
hundred_aire = data[data['aire_dist'] <= 100]
twohundred_tree = data[data['tree_dist'] <= 200]
twohundred_ilot = data[data['ilot_dist'] <= 200]
twohundred_aire = data[data['aire_dist'] <= 200]
far_tree = data[data['tree_dist'] > 200]
far_ilot = data[data['ilot_dist'] > 200]
far_aire = data[data['aire_dist'] > 200]

tree25 = twentyfive_tree['pricem2'].mean()
tree50 = fifty_tree['pricem2'].mean()
tree100 = hundred_tree['pricem2'].mean()
tree200 = twohundred_tree['pricem2'].mean()
treefar = far_tree['pricem2'].mean()
ilot25 = twentyfive_ilot['pricem2'].mean()
ilot50 = fifty_ilot['pricem2'].mean()
ilot100 = hundred_ilot['pricem2'].mean()
ilot200 = twohundred_ilot['pricem2'].mean()
ilotfar = far_ilot['pricem2'].mean()
aire25 = twentyfive_aire['pricem2'].mean()
aire50 = fifty_aire['pricem2'].mean()
aire100 = hundred_aire['pricem2'].mean()
aire200 = twohundred_aire['pricem2'].mean()
airefar = far_aire['pricem2'].mean()

averages = pd.DataFrame()

averages['distance']=[25,50,100,200]
averages['tree_ave']=[tree25, tree50, tree100, tree200]
averages['ilot_ave']=[ilot25, ilot50, ilot100, ilot200]
averages['aire_ave']=[aire25, aire50, aire100, ilot200]

sns.lineplot(x='distance', y='value', hue='variable', data=pd.melt(averages, ['distance']), linewidth=3)
plt.title('Price of Real Estate Relative to Euclidean Distance')
plt.ylabel('Price per square meter in euros')
plt.xlabel('Distance in meters')
plt.legend(labels=['Trees','Carfree Zones','Parks'])

immos = pd.read_csv('immoVenduFinal.csv')
log_price = np.log(immos["pricem2"])
immos["log_price"] = log_price
targets = immos['pricem2']
inputs = immos.drop(['pricem2', 'index', 'price', 'adress', 'm2', 'rooms', 'lat', 'long', 'tree_num', 'wrong_num', 'ilot_num', 'aire_num', 'log_price'], axis=1)
scaler = StandardScaler()
scaler.fit(inputs)
inputs_scaled = scaler.transform(inputs)
x_train, x_test, y_train, y_test = train_test_split(inputs_scaled, targets, test_size=0.2, random_state=365)
reg = LinearRegression()
reg.fit(x_train, y_train)
yhat = reg.predict(x_train)

sns.displot(y_train - yhat, color=color1)
plt.title("Difference Between Actual and Predicted Values", size=10)
plt.xlabel('')
plt.ylabel('')

print(f"Score: {reg.score(x_train, y_train)}")

data = pd.read_csv('immobilieraVendre2023.csv')
chat = pd.read_csv('chat_immo.csv')

targets = data["pricem2"]
inputs = data.drop(["rooms", "price", "pricem2", "size", "arrondissement"], axis=1)
chat = chat.drop(["rooms", "price", "pricem2", "size", "arrondissement"], axis=1)
sns.set_style('white')
scaler = StandardScaler()
scaler.fit(inputs)
inputs_scaled = scaler.transform(inputs)
chat = scaler.transform(chat)
x_train, x_test, y_train, y_test = train_test_split(inputs_scaled, targets, test_size=0.2, random_state=45)
reg = LinearRegression()
reg.fit(x_train, y_train)
yhat = reg.predict(x_train)
chathat = reg.predict(chat)
print(chathat)