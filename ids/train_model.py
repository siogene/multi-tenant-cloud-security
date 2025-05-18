from sklearn.ensemble import IsolationForest
import numpy as np
from sklearn.preprocessing import StandardScaler
X = np.random.rand(100, 4)  > train data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = IsolationForest(n_estimators=100, contamination=0.1)
model.fit(X_scaled)
print("Model trained and ready!")
