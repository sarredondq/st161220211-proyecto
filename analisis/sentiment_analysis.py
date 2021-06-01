from textblob import TextBlob
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
import re

import settings

def stream_preprocessing(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub('@\w+', '', text)
    text = text.replace('#', '')
    text = text.replace('RT', '')
    text = text.replace(':', '')
    return text


def calculate_text_polarity(text) -> float:
    return TextBlob(text).sentiment.polarity

producer = KafkaProducer(bootstrap_servers=settings.KAFKA['HOST_PRODUCER'])
consumer = KafkaConsumer(settings.KAFKA['TOPIC'], bootstrap_servers=settings.KAFKA['HOST_CONSUMER'])
for message in consumer:
    try:
        # Decode the JSON from Twitter
        value = message.value
        value = value.decode()
        datajson = json.loads(value)
        if "extended_tweet" in datajson:
            twit = datajson["extended_tweet"]
            twit = str(twit["full_text"])
            twit = stream_preprocessing(twit)
            print(twit)
            polaridad = calculate_text_polarity(twit)
            if polaridad > 0.2:
                polaridad = 1
            elif polaridad < -0.2:
                polaridad = -1
            else:
                polaridad = 0

            datajson["polaridad"] = polaridad
            datajson = json.dumps(datajson)
            datajson = datajson.encode()
            producer.send(settings.KAFKA['TOPIC'],datajson)
            producer.flush()
            
            
    except Exception as e:
        print(e)
