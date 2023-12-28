import pandas as pd

# 파일경로
file = 'D:\\2627\\randomData\\최종통합데이터(총)\\랜덤통합데이터.csv'

# 파일 읽기
df = pd.read_csv(file)

# 'gtag' 컬럼을 'gtags'로 이름 변경
df.rename(columns={'gtag': 'gtags'}, inplace=True)

# 변경된 데이터를 파일에 덮어씌우기
df.to_csv(file, index=False)