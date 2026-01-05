from kafka import KafkaProducer

import json
BROKER_SERVERS = ["172.31.36.132:9092"]
TOPIC_NAME = "json-example"

producer = KafkaProducer(bootstrap_servers=BROKER_SERVERS)

sample_json = {
    "name" : "정유진",
    "age" : 25
    
}

# 반드시 json.dumps를 이용해 프로듀싱한다.
producer.send(TOPIC_NAME,json.dumps(sample_json).encode("utf-8"))

producer.flush()