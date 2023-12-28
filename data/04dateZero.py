import pandas as pd
import os

# 폴더 경로 설정
new_root_folder = 'D:\\2627\\randomData\\01원시데이터랜덤(날짜)'

def adjust_date_format(date_str):
    try:
        # 날짜를 datetime 객체로 파싱하여 다시 원하는 형식으로 변환
        date = pd.to_datetime(date_str)
        return date.strftime('%Y-%m-%d')
    except ValueError:
        return date_str

# 폴더 내 모든 파일에 대해 작업 수행
for folder_name in os.listdir(new_root_folder):
    folder_path = os.path.join(new_root_folder, folder_name)
    
    if os.path.isdir(folder_path):
        # 폴더 내의 모든 CSV 파일에 대해 작업 수행
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.csv'):
                file_path = os.path.join(folder_path, file_name)
                
                # 파일 읽기
                df = pd.read_csv(file_path)
                
                # 'Date' 컬럼의 날짜 형식 조정
                df['Date'] = df['Date'].apply(adjust_date_format)
                
                # 변경된 데이터를 동일한 파일에 덮어쓰기
                df.to_csv(file_path, index=False)

