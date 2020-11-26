###### datetime:2020/11/24 11:15
###### author:nzb

> docker-compose 的时候会经常超时，重新运行命令即可，不会影响前面已经拉取构建的镜像

- 配置文件
    - filebeat：[filebeat.yml](./compose/filebeat/config/filebeat.yml) 输出配置
    - logstash：[logstash.conf](./compose/logstash/pipeline/logstash.conf) 输入配置     
    - elasticsearch 账号密码：
        - [logstash.conf](./compose/logstash/pipeline/logstash.conf)    
        - [kibana.yml](./compose/kibana/config/kibana.yml)

- django 项目启动及数据库迁移命令
    docker exec -it container_name /bin/bash -c "start.sh"

- 安装成功检查
    - elasticsearch 安装成功检查：浏览器中访问端口 9200
    - kibana 安装成功检查：浏览器中访问端口 5601，账号密码[在这](./compose/kibana/config/kibana.yml)

    
- [Kafka](https://github.com/wurstmeister/kafka-docker.git)
    - [安装说明及使用](https://www.cnblogs.com/qa-freeroad/p/13780405.html)

- 架构图
    
    - 简易版
    ![](./imgs/elk-kafka1.png)
    - 标准版
    ![](./imgs/elk-kafka2.png)