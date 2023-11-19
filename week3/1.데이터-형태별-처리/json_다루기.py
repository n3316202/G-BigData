data = {
    '이름':['김한국', '박대한', '홍길동'],
    '국어성적':[80, 75, 90],
    '영어성적':[90, 95, 75]
}

import pandas as pd
df = pd.DataFrame(data)

#https://jimmy-ai.tistory.com/194

#DataFrame을 JSON으로 변환하기
#한글 처리 필요할 경우 force_ascii=False 추가
#대표적으로 index, columns, records, split, values 등 종류의 변환 양식을 지원
json_data = df.to_json(orient='records', indent=4, force_ascii=False)
print(json_data)

#파일로 저장하기
df.to_json('data.json', orient='records', indent=4)