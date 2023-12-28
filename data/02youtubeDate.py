import pandas as pd
import os
from datetime import datetime

# 22일짜 파일빼고 안됨 - 02_1파일쓰면됨
new_root_folder = 'D:\\2627\\randomData\\01원시데이터랜덤(날짜)'

# 주어진 날짜 형식을 변환하는 함수
def convert_date_format(date_str):
    if isinstance(date_str, str):
        try:
            date = datetime.strptime(date_str, '%Y. %m. %d.')
            return date.strftime('%Y-%m-%d')
        except ValueError:
            pass
    return date_str  # 문자열이 아니거나 변환이 실패한 경우 그대로 반환

for file_name in os.listdir(new_root_folder):
    if file_name.endswith('.csv'):
        file_path = os.path.join(new_root_folder, file_name)
        
        df = pd.read_csv(file_path)
        
        # Date 컬럼에 대한 날짜 형식 변환
        df['Date'] = df['Date'].apply(convert_date_format)
        
        # 변경된 데이터를 동일한 파일에 덮어쓰기
        df.to_csv(file_path, index=False)
