
# シンプルなPython HTTPサーバー

このプロジェクトには、HTTP POSTリクエストを処理し、JSONデータで応答するPythonで書かれたシンプルなHTTPサーバーが含まれています。

## 概要

`server.py`に実装されたサーバーは、ポート8000でPOSTリクエストを待ち受け、受信した任意のJSONデータをエコーバックします。これはREST APIが受信JSONリクエストをどのように扱うかを示す基本的な例で、教育目的で意図されています。

## セットアップ

1. システムにPython 3がインストールされていることを確認してください。
2. `server.py`を希望のディレクトリに配置します。

## サーバーの実行

ターミナルで次のコマンドを実行します：

```bash
python3 server.py
```

サーバーが起動し、ポート8000で待ち受けます。スクリプト内の`port`変数を変更することでポートを変更できます。

## APIの使用

サーバーにデータを送信するには、`curl`のようなツールを使用します。以下にコマンドの例を示します：

```bash
curl -d '{"key": "value"}' -H "Content-Type: application/json" -X POST http://localhost:8000
```

`'{"key": "value"}'`を任意のJSON形式の文字列に置き換えてください。サーバーは同じJSONペイロードで応答します。

## Linuxサービス

このサーバーをLinuxシステム上でサービスとして実行したい場合、`python_server.service`としてサンプルの`.service`ファイルが提供されています。ファイルパスをセットアップに合わせて更新し、`.service`ファイルを`/etc/systemd/system/`に配置してください。systemctlを使用してサービスを開始し、有効にします：

```bash
sudo systemctl start python_server.service
sudo systemctl enable python_server.service
```

## 注意

このサーバーはデモンストレーション目的であり、本番環境には適していません。
