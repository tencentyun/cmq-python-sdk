#!/usr/bin/env python
# coding=utf8

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

import logging
from cmq.account import Account
from cmq.cmq_exception import *
from cmq.topic import *

# get your own secretId/secretKey: https://console.cloud.tencent.com/cam/capi
secretId = 'AKIDxxxxx'
secretKey = 'xxxxx'
# endpoint = 'http://cmq-queue-gz.api.tencentyun.com'
endpoint = 'https://cmq-gz.public.tencenttdmq.com'

try:
    # initialize my_account, my_topic
    # Account is not thread safe
    my_account = Account(endpoint, secretId, secretKey, debug=True)
    my_account.set_log_level(logging.DEBUG)
    topic_name = sys.argv[1] if len(sys.argv) > 1 else "Topic-test"
    my_topic = my_account.get_topic(topic_name)

    # public message without tags
    message = Message()
    message.msgBody = "this is a test message"
    my_topic.publish_message(message)
    # public message with tags
    message = Message("this is a test message", ["test", "york"])
    my_topic.publish_message(message)
    # batch publish message without tags
    vmsg = []
    for i in range(6):
        message = Message()
        message.msgBody = "this is a test message"
        vmsg.append(message)
    my_topic.batch_publish_message(vmsg)
    # batch publish message  with tags
    vmsg = []
    for i in range(6):
        message = Message("this  is a test message", ["test"])
        vmsg.append(message)
    my_topic.batch_publish_message(vmsg)

except CMQExceptionBase as e:
    print("Exception:%s\n" % e)
