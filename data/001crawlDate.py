import pandas as pd
import os
from datetime import datetime, timedelta
import re

# 파일 이름에서 날짜 정보 추출
def extract_date_from_filename(file_name):
    date_matches = re.findall(r'\d{4}_\d{2}_\d{2}', file_name)  # 파일명에서 날짜 추출
    if date_matches:
        return datetime.strptime(date_matches[0], '%Y_%m_%d').date()
    return None

file_path = 'D:\\2627\\randomData\\00원시데이터(랜덤)\\'
new_root_folder = 'D:\\2627\\randomData\\001원시데이터(크롤링날짜)\\'  # 새로운 경로

for file_name in os.listdir(file_path):
    if file_name.endswith('.csv'):
        file_full_path = os.path.join(file_path, file_name)
        df = pd.read_csv(file_full_path)
        
        # 파일명에서 날짜 추출
        date_from_filename = extract_date_from_filename(file_name)
        
        # 'CrawlDate' 열 생성
        df['CrawlDate'] = date_from_filename.strftime('%Y-%m-%d') if date_from_filename else 'NaN'
        
        # 새로운 파일 경로 생성
        new_file_path = os.path.join(new_root_folder, file_name)
        
        # CSV 파일로 저장
        df.to_csv(new_file_path, index=False, encoding='utf-8-sig')
