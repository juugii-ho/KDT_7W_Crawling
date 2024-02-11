import pandas as pd


df = pd.read_csv('hollys_branches.csv')

a = 1
for i in range(df.shape[0]):
    print(f'[{a:>3}]: 매장이름: {df.iloc[i][0]}, 지역: {df.iloc[i][1]}, 주소: {df.iloc[i][2]}, 전화번호: {df.iloc[i][3]}')
    a+=1
print(f'전체 매장 수:{df.shape[0]}')
print('hollys_branches.csv 파일 저장 완료')

while True:
    try:
        inp1 = input('검색할 매장의 도시를 입력하세요: ')
        results = []
        if inp1 != 'quit':
            for i in range(df.shape[0]):
                if inp1 in df['위치(시,구)'][i]:
                    results.append(df.iloc[i])

            print('-'*20)
            print(f'검색된 매장 수: ', len(results))
            print('-'*20)
            a = 1
            for i in results:
                print(f"[{a:>3}]: ['{i[2]}', '{i[3]}']")
                a +=1
        else:
            break
    except Exception as e:
        print(e)