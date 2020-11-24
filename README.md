###### datetime:2020/11/24 11:15
###### author:nzb

- ELK + filebeat 
    - 需修改的地方
        - filebeat：[filebeat.yml](./compose/filebeat/config/filebeat.yml) 输出配置
        - logstash：[logstash.conf](./compose/logstash/pipeline/logstash.conf) 输入配置     
    - docker-compose 的时候会经常超时，重新运行命令即可，不会影响前面已经拉取了的镜像
    
- [Kafka](https://github.com/wurstmeister/kafka-docker.git)

