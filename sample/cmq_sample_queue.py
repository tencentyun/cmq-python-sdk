#!/usr/bin/env python
# coding=utf8

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

import logging
from cmq.account import Account
from cmq.queue import QueueMeta, Message
from cmq.cmq_exception import CMQExceptionBase

# get your own secretId/secretKey: https://console.cloud.tencent.com/cam/capi
secretId = 'AKIDxxxxx'
secretKey = 'xxxxx'
# endpoint = 'http://cmq-queue-gz.api.tencentyun.com'
endpoint = 'https://cmq-gz.public.tencenttdmq.com'

# initialize my_account, my_queue
# Account is not thread safe
my_account = Account(endpoint, secretId, secretKey, debug=True)
my_account.set_log_level(logging.DEBUG)
queue_name = sys.argv[1] if len(sys.argv) > 1 else "MySampleQueue"
my_queue = my_account.get_queue(queue_name)

queue_meta = QueueMeta()
queue_meta.queueName = queue_name
queue_meta.pollingWaitSeconds = 10
queue_meta.visibilityTimeout = 10
queue_meta.maxMsgSize = 1024
queue_meta.msgRetentionSeconds = 3600
try:
    msg_body = "I am test message."
    msg = Message(msg_body)
    re_msg = my_queue.send_message(msg)
    print "Send Message Succeed! MessageBody:%s MessageID:%s" % (msg_body, re_msg.msgId)

    wait_seconds = 3
    recv_msg = my_queue.receive_message(wait_seconds)
    print "Receive Message Succeed! ReceiptHandle:%s MessageBody:%s MessageID:%s" % (
        recv_msg.receiptHandle, recv_msg.msgBody, recv_msg.msgId)

    my_queue.delete_message(recv_msg.receiptHandle)

    msg_count = 3
    messages = []
    for i in range(msg_count):
        msg_body = "I am test message %s." % i
        msg = Message(msg_body)
        messages.append(msg)

    re_msg_list = my_queue.batch_send_message(messages)
    print "Batch Send Message Succeed! Messages\n%s" % (
        '\n'.join(['MessageBody:%s MessageID:%s' % (msg.msgBody, msg.msgId) for msg in re_msg_list]))

    wait_seconds = 3
    num_of_msg = 3
    sleep_time = 11
    recv_msg_list = my_queue.batch_receive_message(num_of_msg, wait_seconds)
    print "Batch Receive Message Succeed!\n%s" % ('\n'.join(
        ['ReceiptHandle:%s MessageBody:%s MessageID:%s' % (recv_msg.receiptHandle, recv_msg.msgBody, recv_msg.msgId) for
         recv_msg in recv_msg_list]))

except CMQExceptionBase, e:
    print "Queue Fail! Exception:%s\n" % e
