import pandas as pd
from datetime import datetime

file = 'D:\\2627\\randomData\\01원시데이터랜덤(날짜)\\2023_12_22_youtubeShortsRandom.csv'

# 주어진 날짜 형식을 변환하는 함수
def convert_date_formats(date_str):
    if isinstance(date_str, str):
        try:
            date_parts = date_str.split('.')  # 날짜를 '.' 기준으로 분리
            if len(date_parts) == 3:
                date = datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
                return date.strftime('%Y-%m-%d')
        except ValueError:
            pass
    return date_str  # 문자열이 아니거나 변환이 실패한 경우 그대로 반환

df = pd.read_csv(file)

# Date 컬럼에 대한 날짜 형식 변환
df['Date'] = df['Date'].apply(convert_date_formats)

# 변경된 데이터를 동일한 파일에 덮어쓰기
df.to_csv(file, index=False)
