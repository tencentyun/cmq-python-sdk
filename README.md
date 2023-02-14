# Tencent TDMQ-CMQ Python2 SDK

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

Install by pip:

```bash
# https://pypi.org/project/qcloud-cmq-sdk/
pip install qcloud-cmq-sdk
```

Install from source:

```bash
python2 setup.py install
```

Example:

- [queue](sample/cmq_sample_queue.py)
- [topic](sample/cmq_sample_topic.py)

Python3 SDK:

https://github.com/tencentyun/cmq-python-sdk/tree/python3
