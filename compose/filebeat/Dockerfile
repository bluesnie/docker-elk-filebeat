ARG ELK_VERSION

# https://www.docker.elastic.co/
FROM docker.elastic.co/beats/filebeat:${ELK_VERSION}

COPY /config/filebeat.yml /etc/filebeat/filebeat.yml

# Add your logstash plugins setup here
# Example: RUN logstash-plugin install logstash-filter-json