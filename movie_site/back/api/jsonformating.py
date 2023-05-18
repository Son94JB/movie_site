import json

# JSON 파일 열기
with open('movies.json', 'r') as f:
    # JSON 데이터 로드
    data = json.load(f)

# JSON 데이터 다시 인코딩
formatted_data = json.dumps(data, indent=4)

# JSON 파일에 쓰기
with open('movies.json', 'w') as f:
    f.write(formatted_data)

# 파일 닫기
f.close()
