import pandas as pd
import glob

# 파일 경로 설정
folder_path = r'D:\\2627\\randomData\\최종통합데이터(총)'
output_file = r'D:\\2627\\randomData\\최최종통합데이터(총)\\통합.csv'

# 해당 폴더 내의 모든 CSV 파일 가져오기
all_files = glob.glob(folder_path + "/*.csv")

# 모든 CSV 파일을 하나의 DataFrame으로 병합
combined_csv = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)

# 새로운 파일로 저장
combined_csv.to_csv(output_file, index=False,encoding='utf-8-sig')
