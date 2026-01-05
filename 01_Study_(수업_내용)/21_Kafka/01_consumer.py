from kafka import KafkaConsumer


BROKER_SERVERS = ["172.31.36.132:9092"]
TOPIC_NAME = "sample-topic"

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=BROKER_SERVERS)

print("Wait.....")

# Consumer는 topic에 쌓여가는 메시지를 무제한으로 가져와야 한다. - 무한대기
#   - Consumer는 Python의 Generator로 구현되어 있다.
for message in consumer:
    print(message)