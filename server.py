from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # データのサイズを取得
        content_length = int(self.headers['Content-Length'])
        # データを読み取る
        post_data = self.rfile.read(content_length)
        # バイトデータをJSONに変換
        received_data = json.loads(post_data.decode('utf-8'))

        # レスポンスを準備（受信したJSONをそのまま返す）
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # 辞書をJSONに変換して返送
        self.wfile.write(json.dumps(received_data).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'ポート{port}でhttpdを起動中...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
