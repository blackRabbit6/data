import pandas as pd

youtube_file = 'D:\\2627\\randomData\\최종통합데이터(처리)\\youtube통합분류결과.csv'

# CSV 파일 읽기
youtube_data = pd.read_csv(youtube_file)

# 'Comments' 열에서 '사용 중지됨'을 0으로 변경
youtube_data['Comments'] = youtube_data['Comments'].replace('사용 중지됨', 0)

# 변경된 데이터를 기존 파일에 덮어씌우기
youtube_data.to_csv(youtube_file, index=False)
