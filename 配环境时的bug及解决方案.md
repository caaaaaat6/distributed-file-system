# 配置环境时的BUG及解决方案

### Docker配置
docker容器的时间要和主机设置成一样的，否则重启jenkins无法使插件生效



### requirements.txt

```
grpcio
grpcio-tools
# redis~=4.5.5
redis~=4.3.6
# ast # byDefault
pyyaml==6.0
# hashlib # byDefault
lru-dict
psutil~=5.9.5
pysyncobj~=0.3.12
protobuf==3.19.6
```



### 在Docker中安装python镜像
https://www.cnblogs.com/hq0202/p/16302742.html
1. 需要用豆瓣的镜像，清华的不行。还要信任豆瓣的主机。以下是Dockerfile
```dockerfile

------弃用，待更新-----
FROM python:3.7-alpine
WORKDIR /app
ADD ./requirements.txt /app
RUN apk add gcc python3-dev
RUN apk add build-base linux-headers
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
CMD ["python","SuperNode/superNode.py"]
```

### pycharm连接docker

遇到unexpected end of stream http://127.0.0.1 ...

https://stackoverflow.com/questions/21871479/docker-cant-connect-to-docker-daemon
