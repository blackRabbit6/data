import pandas as pd

file = 'D:\\2627\\randomData\\최최종통합데이터(총)\\통합.csv'
output_file = 'D:\\2627\\randomData\\최최종통합데이터(총)\\통합순서.csv'

# CSV 파일 불러오기
data = pd.read_csv(file)

# 컬럼 순서 변경
data = data[['comments', 'content', 'crawlingdate', 'date', 'gtags', 'likes', 'platformid', 'url', 'writer', 'categoryid']]

# 새로운 파일로 저장
data.to_csv(output_file, index=False)
