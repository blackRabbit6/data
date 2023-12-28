import pandas as pd

file = 'D:\\2627\\randomData\\최종통합데이터(처리)\\tictok통합분류결과.csv'
output = 'D:\\2627\\randomData\\최종통합데이터(변경)\\tictok통합분류결과.csv'
# file = 'D:\\2627\\randomData\\최종통합데이터(처리)\\youtube통합분류결과.csv'
# output = 'D:\\2627\\randomData\\최종통합데이터(변경)\\youtube통합분류결과.csv'
# file = 'D:\\2627\\randomData\\최종통합데이터(처리)\\insta통합분류결과.csv'
# output = 'D:\\2627\\randomData\\최종통합데이터(변경)\\insta통합분류결과.csv'

# 새로운 컬럼 이름
new_columns = [
            'writer', 'content', 'date', 'likes', 'gtag', 'comments', 
            'url', 'crawlingdate', 'platformid', 'categoryid', 'valid_tags'
            ]

# 파일 읽기
data = pd.read_csv(file)

# 컬럼 이름 변경
data.columns = new_columns

# 새 파일로 저장
data.to_csv(output, index=False)