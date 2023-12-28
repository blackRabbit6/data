# import pandas as pd
# import os

# original_folder = 'D:\\데이터폭파\\12071210\\'
# new_folder = 'D:\\데이터폭파\\중간원시데이터\\12071210\\'

# if not os.path.exists(new_folder):
#     os.makedirs(new_folder)

# def convert_to_integer(value):
#     if isinstance(value, str):
#         if 'K' in value:
#             return int(float(value.replace('K', '')) * 1000)
#         elif 'M' in value:
#             return int(float(value.replace('M', '')) * 1000000)
#         elif '만' in value:
#             return int(float(value.replace('만', '')) * 10000)
#     return value

# for file_name in os.listdir(original_folder):
#     if file_name.endswith('.csv'):
#         original_file_path = os.path.join(original_folder, file_name)
#         new_file_path = os.path.join(new_folder, file_name)
        
#         df = pd.read_csv(original_file_path)
        
#         # 'Like' 열 값이 문자열일 때만 변환 함수를 적용
#         df['Like'] = df['Like'].apply(convert_to_integer)
        
#         # 정수로 변환한 데이터를 CSV로 저장하되, 소수점 이하 자릿수는 표현하지 않음
#         df.to_csv(new_file_path, index=False, float_format='%.0f')

# import pandas as pd
# import os

# # 수정될 수 있음
# original_folder = 'D:\\randoms\\randomData\\01원시데이터랜덤(시간)\\'  

# new_root_folder = 'D:\\randoms\\randomData\\01원시데이터랜덤(좋아요)\\'


# if not os.path.exists(new_root_folder):
#     os.makedirs(new_root_folder)

# def convert_to_integer(value):
#     if isinstance(value, str):
#         if 'K' in value:
#             return int(float(value.replace('K', '')) * 1000)
#         elif 'M' in value:
#             return int(float(value.replace('M', '')) * 1000000)
#         elif '만' in value:
#             return int(float(value.replace('만', '')) * 10000)
#     return value

# for folder_name in os.listdir(original_folder):
#     folder_path = os.path.join(original_folder, folder_name)
#     if os.path.isdir(folder_path):  # 폴더인 경우
#         new_folder = os.path.join(new_root_folder, folder_name)  # 새로운 폴더 생성
#         if not os.path.exists(new_folder):
#             os.makedirs(new_folder)
#         for file_name in os.listdir(folder_path):
#             if file_name.endswith('.csv'):
#                 original_file_path = os.path.join(folder_path, file_name)
#                 new_file_path = os.path.join(new_folder, file_name)
                
#                 df = pd.read_csv(original_file_path)
                
#                 # 'Like' 열 값이 문자열일 때만 변환 함수를 적용
#                 df['Like'] = df['Like'].apply(convert_to_integer)
                
#                 # 정수로 변환한 데이터를 CSV로 저장하되, 소수점 이하 자릿수는 표현하지 않음
#                 df.to_csv(new_file_path, index=False, float_format='%.0f')

import pandas as pd
import os

# 수정될 수 있음
original_folder = 'D:\\2627\\randomData\\01원시데이터랜덤(시간)\\'
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

for file_name in os.listdir(original_folder):
    if file_name.endswith('.csv'):
        original_file_path = os.path.join(original_folder, file_name)
        new_file_path = os.path.join(new_folder, file_name)
        
        df = pd.read_csv(original_file_path)
        
        # 'Like' 열 값이 문자열일 때만 변환 함수를 적용
        df['Like'] = df['Like'].apply(convert_to_integer)
        
        # 정수로 변환한 데이터를 CSV로 저장하되, 소수점 이하 자릿수는 표현하지 않음
        df.to_csv(new_file_path, index=False, float_format='%.0f', encoding='utf-8-sig')
