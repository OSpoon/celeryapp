### Celery+Redis+Flower+Supervisor

#### 一·Redis for Mac

##### Client [下载](http://www.pc6.com/mac/486661.html)
##### 安装
```
brew install redis
```
##### 启动
```
redis-server /usr/local/etc/redis.conf
```
##### 关闭
```
redis-cli shutdown
```
##### 检测服务器是否启动
```
redis-cli ping
```
#### 二·Celery

##### 安装
```
pip install celery[redis]
```
##### 简易Demo
```
import time
from celery import Celery


# 消息中间件 Broker
broker = 'redis://localhost:6379/1'
# 任务结果存储 Backend
backend = 'redis://localhost:6379/2'
myCelery = Celery('my_task', broker=broker, backend=backend)


@myCelery.task
def add(x, y):
    print('enter call func ...')
    time.sleep(5)
    return x, y
```
##### 运行 tasks Worker

```
celery worker -A tasks -l INFO
```
##### 外部配置
```
BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

```
##### 初始化Celery
```
from celery import Celery

app = Celery('celery_app')
app.config_from_object('celery_app.celeryconfig')
```

##### 运行 celery_app Worker

```
celery worker -A celery_app -l INFO
```
##### 调用任务
```
# 你可以用 delay() 方法来调用任务。
from tasks import add
add.delay(4, 4)

# 查看是否完成
result.ready()

# 获取结果
result.get(timeout=1)
```
##### Redis存储的结果信息
```
eg：
{"status": "SUCCESS", "result": 6, "traceback": null, "children": [], "task_id": "423d645d-86d9-4c91-a0e8-82a1ab997147", "date_done": "2019-08-17T14:54:43.189881"}
```
##### 配置定时任务

```
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (2, 8)
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=23, minute=15),
        'args': (4, 5)
    }
}
```
##### 发送定时任务
```
celery beat -A celery_app -l INFO
# 或
celery worker -A celery_app -l INFO -B
```

#### 三·Flower 监控任务
##### 安装
```
pip install flower
```
##### 启动
```
celery flower --broker=redis://localhost:6379/1 --address=127.0.0.1 --port=9999 --basic_auth=admin:123456
```

####  四·Supervisor 进程管理
##### 安装
```
 pip install supervisor
```
##### 增加配置
```
mkdir conf
echo_supervisord_conf > conf/supervisord.conf

[program:demo-celery-worker]
command=celery worker -A celery_app -l INFO -B
directory=/Users/zhangxin/PycharmProjects/flask_server
environment=PATH="/Users/zhangxin/PycharmProjects/flask_server/venv/bin"
stdout_logfile=/Users/zhangxin/PycharmProjects/flask_server/celery_app/log/work.log
stderr_logfile=/Users/zhangxin/PycharmProjects/flask_server/celery_app/log/err.log
autostart=true
priority=999
```

##### 启动进程 for mac
```
supervisord -c conf/supervisord.conf

ps -ef|grep supervisor
```

##### 查看进程
```
#进入命令行模式
supervisorctl

#更新进程组
update

# 进程状态
demo-celery-worker RUNNING pid 12711, uptime 0:02:26
```

##### WEB展示
```
http://127.0.0.1:9001/
```

#### 备注
##### 查看端口被哪个程序占用
```
sudo lsof -i tcp:port
如：sudo lsof -i tcp:9001
```
##### 看到进程的PID，可以将进程杀死
```
sudo kill -9 PID
如：sudo kill -9 750
```