import pandas as pd

data = [[1, 62], [3, 54], [5, 76], [7, 88]]
data_frame = pd.DataFrame(data, columns=['No', 'score'])
print(data_frame)

mean_score = data_frame['score'].mean()
print(mean_score)

data_frame['score'] = data_frame['score'].astype('float')
print(data_frame)