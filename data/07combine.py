import pandas as pd
import os

# 파일이 있는 폴더 경로
folder_path = 'D:\\2627\\randomData\\01원시데이터랜덤(좋아요)\\'

# 모든 CSV 파일을 담을 빈 DataFrame 생성
combined_data = pd.DataFrame()

# 해당 폴더 내의 모든 파일에 대해 작업 수행
# 'tiktok' 'insta' 'youtube'
for file_name in os.listdir(folder_path):
    # if file_name.endswith('.csv') and 'tiktok' in file_name.lower():
    # if file_name.endswith('.csv') and 'youtube' in file_name.lower():
    if file_name.endswith('.csv') and 'insta' in file_name.lower():
        file_path = os.path.join(folder_path, file_name)
        
        # CSV 파일을 DataFrame으로 읽기
        df = pd.read_csv(file_path)
        
        # 데이터 통합
        combined_data = pd.concat([combined_data, df], ignore_index=True)

# 새로운 파일로 통합된 데이터 저장
# combined_data.to_csv('D:\\2627\\randomData\\통합데이터\\tiktok\\tiktok통합.csv', index=False, encoding='utf-8-sig')
# combined_data.to_csv('D:\\2627\\randomData\\통합데이터\\youtube\\youtube통합.csv', index=False, encoding='utf-8-sig')
combined_data.to_csv('D:\\2627\\randomData\\통합데이터\\insta\\insta통합.csv', index=False, encoding='utf-8-sig')
