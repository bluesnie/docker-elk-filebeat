###### datetime:2020/11/24 11:15
###### author:nzb

- ELK + filebeat 
    - 需修改的地方
        - filebeat：[filebeat.yml](./compose/filebeat/config/filebeat.yml) 输出配置
        - logstash：[logstash.conf](./compose/logstash/pipeline/logstash.conf) 输入配置     
- [Kafka](https://github.com/wurstmeister/kafka-docker.git)