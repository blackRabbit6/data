import pandas as pd

# 파일 경로
tiktok_file = 'D:\\2627\\randomData\\최종통합데이터(처리)\\tictok통합분류결과.csv'

# TikTok 파일 처리
tiktok_data = pd.read_csv(tiktok_file)
tiktok_data['Like'] = tiktok_data['Like'].astype(int)  # 소수점을 없애기 위해 정수로 변환
# 기존 TikTok 파일 덮어쓰기
tiktok_data.to_csv(tiktok_file, index=False)

# youtube_file = 'D:\\2627\\randomData\\최종통합데이터(처리)\\youtube통합분류결과.csv'
# # YouTube 파일 처리
# youtube_data = pd.read_csv(youtube_file)
# youtube_data['Like'] = youtube_data['Like'].astype(int)  # 소수점을 없애기 위해 정수로 변환

# # 기존 YouTube 파일 덮어쓰기
# youtube_data.to_csv(youtube_file, index=False)
