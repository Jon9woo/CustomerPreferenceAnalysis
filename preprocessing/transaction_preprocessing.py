#######################################################################
# transaction_preprocessing.py
# - 트랜잭션 데이터 전처리
#######################################################################

import pandas as pd

# 경로설정
path = '../data'

data = pd.read_csv(f'{path}/2019-Oct_purchase.csv')

print("트랜잭션 단위 데이터를 불러왔습니다.")

# 결측치 제거
data = data.dropna(axis=0)

print("결측치 제거 완료")

data.reset_index(drop=True, inplace=True)

print("인덱스 초기화 완료")

# 카테고리 파싱
data[['ctg_1', 'ctg_2', 'ctg_3', 'ctg_4']] = data['category_code'].str.split('.', expand=True)

print("카테고리 파싱 완료")

# 데이터 저장
data.to_csv(f'{path}/2019-Oct_purchase_preprocessed.csv', index=False)

print(f"전처리된 데이터 {path} 위치에 저장 완료")