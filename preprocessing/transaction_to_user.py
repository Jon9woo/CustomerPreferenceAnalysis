#######################################################################
# transaction_to_user.py
# - 트랜잭션 데이터를 유저 단위 데이터로 변경
#######################################################################

## 트랜잭션 단위 데이터를 유저 단위 데이터로 변경
import pandas as pd

# 경로설정
path = '../data'

data = pd.read_csv(f'{path}/2019-Oct_purchase_preprocessed.csv')

print('트랜잭션 단위 데이터를 불러왔습니다.')

# eventtime을 datetime으로 변환
data['event_time'] = pd.to_datetime(data['event_time'])

user_data = data.groupby('user_id').agg(purchase_count=('event_time', 'count'), # 구매 횟수
                                    total_spent=('price', 'sum'), # 총 구매액
                                    avg_spent=('price', 'mean'), # 평균 구매액
                                    max_spent=('price', 'max'), # 최대 구매액
                                    min_spent=('price', 'min'), # 최소 구매액
                                    first_purchase=('event_time', 'min'), # 첫 구매일
                                    last_purchase=('event_time', 'max'), # 마지막 구매일
                                    duration=('event_time', lambda x: x.max() - x.min()), # 구매 기간
                                    category_count=('category_code', 'nunique'), # 구매한 카테고리 수
                                    )

print('트랜잭션 단위 데이터를 유저 단위 데이터로 변경 완료하였습니다.')


user_data.to_csv(f'{path}/2019-Oct_user.csv', index=True)

# 경로에 저장하였다고 출력
print(f'유저 단위 데이터를 {path}에 저장완료하였습니다.')