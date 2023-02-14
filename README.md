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

Install by pip3:

```bash
# https://pypi.org/project/qcloud-cmq-sdk-py3/
pip3 install qcloud-cmq-sdk-py3
```

Install from source:

```bash
python3 setup.py install
```

Example:

- [queue](sample/cmq_sample_queue.py)
- [topic](sample/cmq_sample_topic.py)

Python2 SDK:

https://github.com/tencentyun/cmq-python-sdk/tree/python2
