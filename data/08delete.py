import pandas as pd

# 각 통합분류결과  주석처리 바꿔가며 처리

# file = 'D:\\2627\\randomData\\최종통합데이터\\tictok통합분류결과.csv'
# output = 'D:\\2627\\randomData\\최종통합데이터(처리)\\tictok통합분류결과.csv'
# file = 'D:\\2627\\randomData\\최종통합데이터\\youtube통합분류결과.csv'
# output = 'D:\\2627\\randomData\\최종통합데이터(처리)\\youtube통합분류결과.csv'
file = 'D:\\2627\\randomData\\최종통합데이터\\insta통합분류결과.csv'
output = 'D:\\2627\\randomData\\최종통합데이터(처리)\\insta통합분류결과.csv'

df = pd.read_csv(file)

df.drop('Category_Reason', axis=1, inplace=True)

df.to_csv(output, index=False)