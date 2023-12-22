import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# エクセルファイルを作成
workbook = Workbook()
sheet = workbook.active

# 1から1000までのURLを処理
for i in range(1, 5):
    url = f'https://job-draft.jp/companies/{i}'  # URLを生成

    # ウェブサイトからデータを取得
    response = requests.get(url)
    web_content = response.text

    # ウェブサイトから取得したデータを解析
    local_soup = BeautifulSoup(web_content, 'html.parser')

    # ターゲットの要素を取得
    target_text = local_soup.find('h1', class_='p-profile-canopy__name')  # 正確なセレクタを使用

    # ターゲットの要素が存在するか確認
    if target_text:
        # セルにデータを書き込む
        sheet[f'A{i}'] = target_text.text  # セルAiに取得したテキストを書き込む
    else:
        # ターゲットの要素が見つからない場合のエラーメッセージ
        print(f'URL {url} からターゲットの要素が見つかりませんでした。')

# エクセルファイルを保存
workbook.save('output.xlsx')

print('データをエクセルに書き込みました。')
