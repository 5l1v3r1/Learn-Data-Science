import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

def encode_label(df):
    le = LabelEncoder()
    df2 = pd.DataFrame()
    for j in df.columns:
        le.fit(df[j].values)
        ## df.loc[:, j] = le.transform(df[j])
        df2[j] = le.transform(df[j])
    
    print(df2.head())
    return df2

df = pd.read_csv('mushrooms.csv')

y = df[df.columns[:1]]
X = df[df.columns[1:]]

from sklearn.preprocessing import LabelEncoder
X = encode_label(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=4)

#from sklearn.neural_network import MLPClassifier
#clf = MLPClassifier(
#    hidden_layer_sizes=(5,2),
#    activation='logistic',
#    max_iter=1000
#    )

# clf.fit(X_train, y_train.values.ravel())

# predicted_y = clf.predict(X_test)

#from sklearn.metrics import accuracy_score
#score = accuracy_score(predicted_y, y_test)

#print("Test Accuracy: %.2f%%" % (score * 100))

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
from IPython.display import Image
import pydotplus

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train.values.ravel())

dot_data = StringIO()
export_graphviz(clf.estimators_[0],
                out_file=dot_data,
                feature_names=X_train.columns,
                filled=True,
                rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())
