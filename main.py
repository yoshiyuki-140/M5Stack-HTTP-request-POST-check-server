# main.py
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# --- リクエストボディのデータ形式を定義します ---
class M5StackRequest(BaseModel):
    uid: str

# FastAPIアプリケーションのインスタンスを作成します
app = FastAPI()

@app.post("/tap")
async def handle_tap_request(request_data: M5StackRequest):
    """
    /tap というURLへのPOSTリクエストを待ち受ける関数です。
    受け取ったリクエストのbodyが{"uid": "文字列"}の形式であることを検証し、
    コンソールに出力します。
    """
    # Pydanticモデルのおかげで、request_data.uid で安全にデータにアクセスできます
    received_uid = request_data.uid
    
    # ターミナル（コンソール）に受信内容を分かりやすく表示します
    print("="*20)
    print("M5StackからのPOSTリクエストを受信しました。")
    print(f"受信したUID: {received_uid}")
    print("="*20)
    
    # M5Stack側に、正しくデータを受け取ったことを知らせるための応答を返します
    return {"status": "success", "received_uid": received_uid}

if __name__ == "__main__":
    # uvicornサーバーを起動します
    # host="0.0.0.0" とすることで、同じネットワーク内の他のデバイス（M5Stackなど）から
    # このPCのIPアドレスでアクセスできるようになります。
    print("M5StackからのPOSTリクエストを http://<YOUR_PC_IP>:8000/tap で待機します...")
    uvicorn.run(app, host="0.0.0.0", port=8000)


