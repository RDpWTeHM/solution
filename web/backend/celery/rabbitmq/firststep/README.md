# First Step

**Basic Environment**

```powershell
$ whereis rabbitmq-server
rabbitmq-server: /usr/sbin/rabbitmq-server

$ pip install celery
...

$ ls
README.md    tasks.py
```





\#### Terminal 1 ####

**Run It**

```powershell
$ celery -A tasks worker --loglevel=info

```

**Output/Runing**

```powershell
-------------- celery@hostmachine v4.3.0 (rhubarb)
---- **** -----
 --- * *** * -- Linux-4.15.0-45-generic-x86_64-with-Ubuntu-18.04-bionic 2019-04-04 15:43:16
-- * - **** ---
 - ** ---------- [config]
- ** ---------- .> app: tasks:0x7fe7d77a0898
- ** ---------- .> transport: amqp://guest:**@localhost:5672//
- ** ---------- .> results: disabled://
- *** --- * --- .> concurrency: 2 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** -----
 -------------- [queues]
 .> celery exchange=celery(direct) key=celery
  [tasks]
 . tasks.add
[2019-04-04 15:43:17,047: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
[2019-04-04 15:43:17,057: INFO/MainProcess] mingle: searching for neighbors
[2019-04-04 15:43:18,404: INFO/MainProcess] mingle: all alone
[2019-04-04 15:43:18,795: INFO/MainProcess] celery@hostmachine ready.
```



\#### Terminal 2 ####

**Producter**

```powershell
$ python
>>> from tasks import add
>>> add.delay(4, 4)
<AsyncResult: caf1badd-f1f7-4e5c-9397-24e5da50fb03>
>>>
```



\#### Terminal 1 ####

**Consumer**

```powershell
...
[2019-04-04 15:43:18,795: INFO/MainProcess] celery@hostmachine ready.
[2019-04-04 15:45:46,057: INFO/MainProcess] Received task: tasks.add[caf1badd-f1f7-4e5c-9397-24e5da50fb03]  
[2019-04-04 15:45:46,059: INFO/ForkPoolWorker-2] Task tasks.add[caf1badd-f1f7-4e5c-9397-24e5da50fb03] succeeded in 0.00033685099992908363s: 8
```








