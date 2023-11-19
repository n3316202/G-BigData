data = {
    '이름':['김한국', '박대한', '홍길동'],
    '국어성적':[80, 75, 90],
    '영어성적':[90, 95, 75]
}
import pandas as pd
df = pd.DataFrame(data)
df.to_csv('csv.txt', sep=',')

import pandas as pd
df = pd.read_csv('csv.txt', index_col = 0)
print(df)