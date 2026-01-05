from kafka import KafkaProducer

# 브로커 목록을 정의
#   - 브로커가 한 개만 있어도 리스트 형식으로 조회
#   - 여러 개의 브로커가 띄워진 상태에서도 한 개의 브로커만 입력하는 것이 아닌, 모든 브로커의 목록을 입력

BROKER_SERVERS = ["172.31.36.132:9092"]
TOPIC_NAME = "sample-topic"

# producer 객체 생성
producer = KafkaProducer(bootstrap_servers=BROKER_SERVERS)

# 메시지를 토픽에 전송
producer.send(TOPIC_NAME,b'hello Kafka') # Kafka의 파티션에는 데이터가 바이너리화 되어서 저장

# 버퍼 플러싱
producer.flush()