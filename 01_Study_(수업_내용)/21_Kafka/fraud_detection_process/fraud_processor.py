# 이상 데이터가 들어왔을 때의 처리
#   슬랙으로 메시지 보내기
import os
import requests
import json
from kafka import KafkaConsumer

FRAUD_TOPIC = 'fraud_payments'
BROKER_SERVERS = ["172.31.36.132:9092"]

def send_slack(msg):
    import requests
    WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')
    
    payloads = {
        "channel": "#이상탐지",
        "username": "홍길동",
        "text": msg
    }
    
    requests.post(WEBHOOK_URL, json.dumps(payloads))

if __name__ == "__main__":
    consumer = KafkaConsumer(FRAUD_TOPIC, bootstrap_servers=BROKER_SERVERS)
    
    for message in consumer:
        msg = json.loads(message.value.decode())
        
        payment_type = msg['payment_type']
        payment_date = msg['date']
        payment_time = msg['time']
        amount = msg['amount']
        to = msg['to']
        
        fraud_msg = f"[이상 결제 정보] : {payment_type} {payment_date} {payment_time} {amount}원 ({to})"
        
        send_slack(fraud_msg)
        print(fraud_msg)