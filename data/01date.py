# import pandas as pd
# import os
# from datetime import datetime

# original_folder = 'D:\\데이터폭파\\중간원시데이터\\12071210\\'
# # original_folder = 'D:\\데이터폭파\\중간원시데이터\\12111217\\'
# # original_folder = 'D:\\데이터폭파\\중간원시데이터\\12181224\\'

# new_folder = 'D:\\데이터폭파\\최종정리원시데이터\\12071210\\'
# # new_folder = 'D:\\데이터폭파\\최종정리원시데이터\\12111217\\'
# # new_folder = 'D:\\데이터폭파\\최종정리원시데이터\\12181224\\'

# if not os.path.exists(new_folder):
#     os.makedirs(new_folder)

# def convert_date_format(date_str):
#     try:
#         if '-' in date_str:
#             date = datetime.strptime(date_str, '%m-%d')
#             # 2023년으로 연도를 지정하여 날짜 포맷 변경
#             date = date.replace(year=2023)
#             return date.strftime('%Y-%m-%d')
#         else:
#             return date_str
#     except (ValueError, TypeError):
#         return date_str

# for file_name in os.listdir(original_folder):
#     if file_name.endswith('.csv'):
#         original_file_path = os.path.join(original_folder, file_name)
#         new_file_path = os.path.join(new_folder, file_name)
        
#         df = pd.read_csv(original_file_path)
        
#         # Date 컬럼에 대한 날짜 포맷 변환
#         df['Date'] = df['Date'].astype(str).apply(convert_date_format)
        
#         df.to_csv(new_file_path, index=False)

# import pandas as pd
# import os
# from datetime import datetime

# original_root_folder = 'D:\\randoms\\randomData\\01원시데이터(랜덤)'

# new_root_folder = 'D:\\randoms\\randomData\\01원시데이터랜덤(날짜)'

# for folder_name in os.listdir(original_root_folder):
#     original_folder = os.path.join(original_root_folder, folder_name)
#     new_folder = os.path.join(new_root_folder, folder_name)
    
#     if not os.path.exists(new_folder):
#         os.makedirs(new_folder)

#     def convert_date_format(date_str):
#         try:
#             if '-' in date_str:
#                 date = datetime.strptime(date_str, '%m-%d')
#                 # 2023년으로 연도를 지정하여 날짜 포맷 변경
#                 date = date.replace(year=2023)
#                 return date.strftime('%Y-%m-%d')
#             else:
#                 return date_str
#         except (ValueError, TypeError):
#             return date_str

#     for file_name in os.listdir(original_folder):
#         if file_name.endswith('.csv'):
#             original_file_path = os.path.join(original_folder, file_name)
#             new_file_path = os.path.join(new_folder, file_name)
            
#             df = pd.read_csv(original_file_path)
            
#             # Date 컬럼에 대한 날짜 포맷 변환
#             df['Date'] = df['Date'].astype(str).apply(convert_date_format)
            
#             df.to_csv(new_file_path, index=False)

import pandas as pd
import os
from datetime import datetime

original_root_folder = 'D:\\2627\\randomData\\002원시데이터(플렛폼)'
new_root_folder = 'D:\\2627\\randomData\\01원시데이터랜덤(날짜)'

def convert_date_format(date_str):
    try:
        if '-' in date_str:
            date = datetime.strptime(date_str, '%m-%d')
            # 2023년으로 연도를 지정하여 날짜 포맷 변경
            date = date.replace(year=2023)
            return date.strftime('%Y-%m-%d')
        else:
            return date_str
    except (ValueError, TypeError):
        return date_str

for file_name in os.listdir(original_root_folder):
    if file_name.endswith('.csv'):
        original_file_path = os.path.join(original_root_folder, file_name)
        new_file_path = os.path.join(new_root_folder, file_name)
        
        df = pd.read_csv(original_file_path)
        
        # Date 컬럼에 대한 날짜 포맷 변환
        df['Date'] = df['Date'].astype(str).apply(convert_date_format)
        
        df.to_csv(new_file_path, index=False)
