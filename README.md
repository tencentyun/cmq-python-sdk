# Tencent TDMQ-CMQ Python3 SDK

Manage API: https://cloud.tencent.com/document/product/1496/62819

Data Flow API: https://cloud.tencent.com/document/product/1496/61039

Only support these data flow actions:

- Queue
    - QueryQueueRoute
    - SendMessage
    - BatchSendMessage
    - ReceiveMessage
    - BatchReceiveMessage
    - DeleteMessage
    - BatchDeleteMessage

- Topic
    - QueryTopicRoute
    - PublishMessage
    - BatchPublishMessage

Install from source:

```bash
python3 setup.py install
```

Example:

- [queue](sample/cmq_sample_queue.py)
- [topic](sample/cmq_sample_topic.py)

Python2 SDK:

https://github.com/tencentyun/cmq-python-sdk/tree/python2
