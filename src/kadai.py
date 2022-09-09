import pandas as pd

url_list = {'1':'https://uub.jp/cvd/cvd2w.html','2':'https://uub.jp/cvd/cvd6w.html','3':'https://uub.jp/cvd/cvd19w.html','4':'https://uub.jp/cvd/cvd21w.html'}
prefecture = ['北海道', '青森県', '岩手県','大阪府', '宮城県', '秋田県', '山形県', '福島県','京都府', '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県', '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野', '奈良県', '和歌山県', '鳥取県', '島根県', '岡山県', '広島県', '山口県', '徳島県', '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県', '全国']

def case1(url, area): 
    url = url
    table = pd.read_html(url, match='＃')[0]
    table = table.drop(index=47)
    table = table.iloc[:, [1, 2]]
    table = table.loc[table.都道府県 == area]
    table = table.to_csv(index=False,header=False)
    return table

def case2(url): 
    url = url
    table = pd.read_html(url, match='＃')[0]
    table = table.drop(index=47)
    table = table.drop(index=48)
    table = table.iloc[:, [1, 2]]
    table = table.to_csv(index=False,header=False)
    return table

def bye():
    print('\n     bye     \n')

def select_number():
    while True:
        print('\n1 : 累計感染者数, 2 : 何人に1人, 3 : 累計死亡者数, 4 : 死亡率')
        num = input('1から4を選択してください  ')
        if num == '' or not num in url_list:    
            print('\n1から4の中の一つを選んでください。')
            continue
        if num == '3' or num == '4':
            print('\n本当に見ますか?')
            print('見る    →    enterキー')
            res = input('見ない   →   n  ')
            if res == 'n':
                print()
                continue
        url = url_list[num]
        return url

def select_prefecture():
    while True:
        print('\n1 : 都道府県を選んで見る, 2 : 都道府県別で見る')
        num2 = input('\n1から2を選択してください。')
        if num2 == '' or num2 not in ['1', '2']:
            print('\n1から2の中の一つを選んでください。')
            continue
        elif num2 == '1':
            area = input('\n見たい都道府県を入力してください  ')
            if area == '' or not area in prefecture:
                print('\n47都道府県でお願いします。')
                continue
            return area
        elif num2 == '2':
            return  num2

def output():
    while True:
        url = select_number()
        while True:
            ans = select_prefecture()
            if ans == '2':
                print(case2(url))
            else:
                print(case1(url, ans))
            print('\n他の都道府県も見る  →  enterキー')
            res = input('終了する       →       n  ')
            if res == 'n':
                print('\nこのアプリケーションを終了しますか?')
                print('続ける   →   enterキー')
                res = input('終了する  →  n  ')
                if res == 'n':
                    bye()
                    exit()
                else:
                    break

output()