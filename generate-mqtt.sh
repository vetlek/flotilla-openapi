docker run --rm -v ${PWD}/mqtt_spec.yaml:/app/asyncapi.yaml -v ${PWD}/mqtt-output:/app/output asyncapi/generator -o /app/output /app/asyncapi.yaml @asyncapi/python-paho-template
