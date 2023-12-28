import os
import pandas as pd

# 입력 및 출력 폴더 경로 설정
folder_path = 'D:\\2627\\randomData\\최종통합데이터(유효데이터열삭제)'
output_file = 'D:\\2627\\randomData\\최종통합데이터(총)\\랜덤통합데이터.csv'

# 빈 DataFrame 생성 (데이터를 저장할 빈 공간을 만듭니다.)
combined_data = pd.DataFrame()

# 주어진 폴더 내의 모든 CSV 파일을 읽고 병합
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        data = pd.read_csv(file_path)
        combined_data = pd.concat([combined_data, data], ignore_index=True)

# 새로운 CSV 파일로 저장
combined_data.to_csv(output_file, index=False)
