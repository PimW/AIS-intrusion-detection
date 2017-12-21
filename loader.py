import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, RobustScaler

data_file = "data-small.csv"

test_data_file = "data-test.csv"

print("Loading data..")
df = pd.read_csv(data_file)
df_test = pd.read_csv(test_data_file)
labels = df_test.loc[:, "label"]

print("Removing labels..")
df_no_labels = df.drop('label', 1)
df_test_no_labels = df_test.drop('label', 1)

print("OneHot for categorical data..")
df_total = pd.concat([df_no_labels, df_test_no_labels])
data = pd.get_dummies(df_total)

print("Making numpy matrix..")
np_array = data.as_matrix()


print("Min Max Normalization..")
rscaler = RobustScaler()
scaler = MinMaxScaler()
np_array = rscaler.fit_transform(np_array)
np_array = scaler.fit_transform(np_array)

print("Executing PCA..")
print(np_array.shape)
pca = PCA(n_components=5) # PCA(n_components=5)
pca_data = pca.fit_transform(np_array)
print(pca.explained_variance_ratio_.cumsum())



split_point = 494021
df1 = data.iloc[:split_point, :]
df2 = data.iloc[split_point:, :]

df_normal, df_intrusion = [x for _, x in df1.groupby(df['label'] != 'normal')]
print("Transforming normal dataset..")
normal_data = df_normal.as_matrix()
normal_data = rscaler.transform(normal_data)
normal_data = scaler.transform(normal_data)
normal_data = pca.transform(normal_data)

np.savetxt("data-self-kpca-robust.csv", normal_data, delimiter=",")

##################################################

print("Removing labels..")
df_test_no_labels = df_test.drop('label', 1)

print("OneHot for categorical data..")
test_data = df2

print("Making numpy matrix..")
np_array = test_data.as_matrix()
print(len(np_array[0]))

np_array = rscaler.transform(np_array)
np_array = scaler.transform(np_array)
np_array = pca.transform(np_array)


new_df = pd.DataFrame(data=np_array[0:, 0:])#, index=np_array[0:,0])
new_df = pd.concat([new_df, labels], axis=1)

new_df.to_csv("data-intrusion-kpca-robust.csv")
#np.savetxt("data-intrusion-test.csv", np_array, delimiter=",")

