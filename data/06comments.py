import pandas as pd
import os

# 수정될 수 있음
new_folder = 'D:\\2627\\randomData\\01원시데이터랜덤(좋아요)\\'

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

def convert_to_integer(value):
    if isinstance(value, str):
        if 'K' in value:
            return int(float(value.replace('K', '')) * 1000)
        elif 'M' in value:
            return int(float(value.replace('M', '')) * 1000000)
        elif '만' in value:
            return int(float(value.replace('만', '')) * 10000)
        elif '천' in value:
            return int(float(value.replace('천','')) * 1000)
        elif '좋아요' in value:
            return str(value.replace('좋아요','')) * 0
    return value

for file_name in os.listdir(new_folder):
    if file_name.endswith('.csv'):
        original_file_path = os.path.join(new_folder, file_name)
        new_file_path = os.path.join(new_folder, file_name)
        
        df = pd.read_csv(original_file_path)
        
        # 'Like' 열 값이 문자열일 때만 변환 함수를 적용
        df['Comments'] = df['Comments'].apply(convert_to_integer)
        
        # 정수로 변환한 데이터를 CSV로 저장하되, 소수점 이하 자릿수는 표현하지 않음
        df.to_csv(new_file_path, index=False, float_format='%.0f', encoding='utf-8-sig')