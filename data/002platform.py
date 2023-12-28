import pandas as pd
import os

file_path = 'D:\\2627\\randomData\\001원시데이터(크롤링날짜)'
new_file_path = 'D:\\2627\\randomData\\002원시데이터(플렛폼)'

def get_platform(file_name):
    if 'tiktok' in file_name.lower():
        return 't'
    elif 'insta' in file_name.lower():
        return 'i'
    elif 'youtube' in file_name.lower():
        return 'y'
    else:
        return 'Unknown'

for file_name in os.listdir(file_path):
    if file_name.endswith('.csv'):
        file_full_path = os.path.join(file_path, file_name)
        df = pd.read_csv(file_full_path)
        
        platform_value = get_platform(file_name)
        
        df['Platform'] = platform_value
        
        new_file_full_path = os.path.join(new_file_path, file_name)
        df.to_csv(new_file_full_path, index=False, encoding='utf-8-sig')
