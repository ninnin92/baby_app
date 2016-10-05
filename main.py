#!/usr/bin/env python
# coding:utf-8
# env python 3.4.4

from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
import datetime as dt

# PC用の設定
#Config.set('graphics', 'width', '800')  # 画面:横の大きさ
#Config.set('graphics', 'height', '1000')  # 画面:縦の大きさ
Config.set('graphics', 'show_cursor', '1')  # マウスカーソルの有無


# アプリデザイン（kvファイルでレイアウト指定）
class baby_app(Widget):
    pass


# アプリの挙動
class MyApp(App):
    title = 'Log_Time'  # ウィンドウのタイトル

    # Kivyアプリの構築（必須）
    def build(self):
        return baby_app()

    # 起動時に読み込まれる関数
    def on_start(self):
        pass

    # 終了時に読み込まれる関数
    def on_stop(self):
        pass

    # スマートフォンのポーズ機能をON（アプリを起動したまま画面を変えたりとか）
    def on_pause(self):
        return True

    # ポーズモードからの再開
    def on_resume(self):
        pass

if __name__ == '__main__':
    MyApp().run()
