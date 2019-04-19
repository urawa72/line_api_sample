# LINE MessagingAPI News Bot

## About
* Yahooスポナビから指定した単語を含むニュース記事を取得。
* プッシュ通知でLINEアカウントに記事のリンクを配信。

## How to use
* direnvを導入して.envrcを作成し、ENV_ACCESS_TOKENとENV_ACCESS_USER_IDにLINE MessageingAPI利用登録で取得したアクセストークンとユーザーIDを設定する。
* main.pyを実行すれば記事のリンクを取得して作成したLINEアカウントにプッシュ通知する。
```bash
$ python main.py
```