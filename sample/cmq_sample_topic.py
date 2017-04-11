#!/usr/bin/env python
# coding=utf8

'''
    CMQ V1.0.2 SDK PYTHON
    Tips:
    1 Account类对象不是线程安全的，如果多线程使用，需要每个线程单独初始化Account类对象
    2 Topic与Queue使用不同的endpoint, 因此需要需要分别初始化Account
    3 创建订阅的时候，需要设置订阅的属性，订阅属性参见SubscriptionMeta的定义
'''
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

import time
import logging
from cmq.account import Account
from cmq.cmq_exception import *
from cmq.topic import *
from cmq.subscription import *
# 从腾讯云官网查看云api的密钥信息
secretId = '您的secretId'
secretKey = '您的secretKey'
# 使用广州地域的消息服务
endpoint = 'http://cmq-queue-gz.api.tencentyun.com'

try:
# 初始化 my_account
# Account类对象不是线程安全的，如果多线程使用，需要每个线程单独初始化Account类对象
    my_account = Account(endpoint, secretId, secretKey, debug=True)
    my_account.set_log_level(logging.DEBUG)
    topic_name = sys.argv[1] if len(sys.argv) > 1 else "Topic-test"
    my_topic = my_account.get_topic(topic_name)


# create topic
    topic_meta = TopicMeta()
    my_topic.create(topic_meta)
# set and get topic meta
    topic_meta.maxMsgSize = 32768
    my_topic.set_attributes(topic_meta)
    topic_meta = my_topic.get_attributes();

# list topic
    totalCount, topicList, next_off = my_account.list_topic();



# public message without tags
    message = Message()
    message.msgBody = "this is a test message"
    my_topic.publish_message(message)
# public message with tags
    message = Message("this is a test message", ["test", "york"])
    my_topic.publish_message(message)


# batch publish messge without tags
    vmsg = []
    for i in range(6):
        message = Message()
        message.msgBody = "this is a test message"
        vmsg.append(message)

    my_topic.batch_publish_message(vmsg)


# batch publish messge  with tags
    vmsg = []
    for i in range(6):
        message = Message("this  is a test message", ["test"])
        vmsg.append(message)
    my_topic.batch_publish_message(vmsg)

# create subscription
    subscription_name = "subsc-test"
    my_sub = my_account.get_subscription(topic_name, subscription_name)
    subscription_meta = SubscriptionMeta()
# please set your endpoint protocal  here
    subscription_meta.Endpoint = "your endpoint "
    subscription_meta.Protocal = "http"

    my_sub.create(subscription_meta)
# list SubscriptionList
    totalCount, SubscriptionMetaiptionList, next_off = my_topic.list_subscription()
# set subscription meta

    subscription_meta = my_sub.get_attributes()
    my_sub.set_attributes(subscription_meta)
# delete sub and topic_name
    my_sub.delete()
    my_topic.delete
except CMQExceptionBase, e:
    print "Exception:%s\n" % e





