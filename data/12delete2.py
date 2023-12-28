import pandas as pd

# file = 'D:\\2627\\randomData\\최종통합데이터(변경)\\tictok통합분류결과.csv'
# output = 'D:\\2627\\randomData\\최종통합데이터(유효데이터열삭제)\\tictok통합분류결과.csv'
# file = 'D:\\2627\\randomData\\최종통합데이터(변경)\\youtube통합분류결과.csv'
# output = 'D:\\2627\\randomData\\최종통합데이터(유효데이터열삭제)\\youtube통합분류결과.csv'
file = 'D:\\2627\\randomData\\최종통합데이터(변경)\\insta통합분류결과.csv'
output = 'D:\\2627\\randomData\\최종통합데이터(유효데이터열삭제)\\insta통합분류결과.csv'

# 파일 읽기
data = pd.read_csv(file)

# 'valid_tags' 열 삭제
data.drop('valid_tags', axis=1, inplace=True)

# 변경된 데이터를 새 파일에 저장
data.to_csv(output, index=False)