# import pandas as pd
# import os
# from datetime import datetime, timedelta
# import re

# def extract_date_from_filename(file_name):
#     # 파일 이름에서 날짜 정보 추출
#     date_matches = re.findall(r'\d{4}_\d{2}_\d{2}', file_name)  # 파일명에서 날짜 추출
#     if date_matches:
#         return datetime.strptime(date_matches[0], '%Y_%m_%d').date()
#     return None

# def adjust_date_based_on_offset(date, offset_str):
#     if '시간 전' in offset_str:
#         hours = int(re.search(r'\d+', offset_str).group())
#         if date:
#             return date - timedelta(hours=hours)
#     elif '일 전' in offset_str:
#         days = int(re.search(r'\d+', offset_str).group())
#         if date:
#             return date - timedelta(days=days)
#     elif '주 전' in offset_str:
#         weeks = int(re.search(r'\d+', offset_str).group())
#         if date:
#             return date - timedelta(weeks=weeks)
#     return None

# original_root_folder = 'D:\\randoms\\randomData\\01원시데이터랜덤(날짜)\\'

# new_root_folder = 'D:\\randoms\\randomData\\01원시데이터랜덤(시간)\\'

# for folder_name in os.listdir(original_root_folder):
#     original_folder = os.path.join(original_root_folder, folder_name)
#     new_folder = os.path.join(new_root_folder, folder_name)
    
#     if not os.path.exists(new_folder):
#         os.makedirs(new_folder)

#     for file_name in os.listdir(original_folder):
#         if file_name.endswith('.csv'):
#             original_file_path = os.path.join(original_folder, file_name)
#             new_file_path = os.path.join(new_folder, file_name)
            
#             df = pd.read_csv(original_file_path)
            
#             date_column = df['Date']
#             for idx, date_value in date_column.items():
#                 if isinstance(date_value, str):
#                     date_from_filename = extract_date_from_filename(file_name)
#                     adjusted_date = adjust_date_based_on_offset(date_from_filename, date_value)
#                     if adjusted_date:
#                         df.at[idx, 'Date'] = adjusted_date.strftime('%Y-%m-%d')
            
#             df.to_csv(new_file_path, index=False)

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

# 날짜를 조정하는 함수
def adjust_date_based_on_offset(date, offset_str):
    if '시간 전' in offset_str:
        hours = int(re.search(r'\d+', offset_str).group())
        if date:
            return date - timedelta(hours=hours)
    elif '일 전' in offset_str:
        days = int(re.search(r'\d+', offset_str).group())
        if date:
            return date - timedelta(days=days)
    elif '주 전' in offset_str:
        weeks = int(re.search(r'\d+', offset_str).group())
        if date:
            return date - timedelta(weeks=weeks)
    return None

# 문자열 날짜를 다시 날짜로 변환하는 함수
def convert_offset_to_date(date_str):
    if '시간 전' in date_str:
        hours = int(re.search(r'\d+', date_str).group())
        return datetime.now() - timedelta(hours=hours)
    # 날짜 형식으로 변환할 다른 조건들 추가

    return None

original_root_folder = 'D:\\2627\\randomData\\01원시데이터랜덤(날짜)\\'
new_root_folder = 'D:\\2627\\randomData\\01원시데이터랜덤(시간)\\'

for file_name in os.listdir(original_root_folder):
    if file_name.endswith('.csv'):
        original_file_path = os.path.join(original_root_folder, file_name)
        new_file_path = os.path.join(new_root_folder, file_name)
        
        df = pd.read_csv(original_file_path)
        
        date_column = df['Date']
        for idx, date_value in date_column.items():
            if pd.isnull(date_value):  # NaN 값 처리
                date_from_filename = extract_date_from_filename(file_name)
                df.at[idx, 'Date'] = date_from_filename.strftime('%Y-%m-%d') if date_from_filename else 'NaN 전'
            elif isinstance(date_value, str) and date_value.lower() != 'nan':  # 'nan' 문자열 제외
                date_from_filename = extract_date_from_filename(file_name)
                adjusted_date = adjust_date_based_on_offset(date_from_filename, date_value)
                if adjusted_date:
                    df.at[idx, 'Date'] = adjusted_date.strftime('%Y-%m-%d') if isinstance(adjusted_date, datetime) else adjusted_date
        
        df.to_csv(new_file_path, index=False, encoding='utf-8-sig')
