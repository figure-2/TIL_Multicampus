from kafka import KafkaProducer
from kafka import KafkaConsumer


import json

PAYMENT_TOPIC = 'payments'

FRAUD_TOPIC = "fraud_payment"
LEGIT_TOPIC = "legit_payments"

BROKER_SERVERS = ["172.31.36.132:9092"]

# 이상 결제 기준 정의
def is_suspicious(message): # message에 JSON 데이터가 들어옵니다.
    # stranger가 결제 or 결제 금액이 500만원 이상이면 이상 결제로 결정.
    #  메시지를 feature로 받는 머신러닝 모델의 predict
    if message["to"] == 'stranger' or message['amount'] >= 5000000:
        return True
    else:
        return False
    
if __name__ == "__main__": # __~~__ : 지금 이 파일이 내가 실제 실행한 파일이면 무언가를 해라(프로그램 진입점)

    # payments에서 데이터를 받아올 consumer
    consumer = KafkaConsumer(PAYMENT_TOPIC, bootstrap_servers=BROKER_SERVERS)
    
    # LEGIT_TOPIC 또는 FRAUD_TOPIC에 데이터를 전송할 producer 정의
    producer = KafkaProducer(bootstrap_servers=BROKER_SERVERS)
    
    for message in consumer:
        
        msg = json.loads(message.value.decode())
        
        if is_suspicious(msg):
            print("이상 결제 정보 발생!", msg)
            producer.send(FRAUD_TOPIC, json.dumps(msg).encode("utf-8"))
        else:
            print("정상 결제 정보 발생!", msg)
            producer.send(LEGIT_TOPIC, json.dumps(msg).encode("utf-8"))
            
        producer.flush()