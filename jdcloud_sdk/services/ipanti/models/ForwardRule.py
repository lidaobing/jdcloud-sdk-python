# coding=utf8

# Copyright 2018-2025 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class ForwardRule(object):

    def __init__(self, forwardRuleId=None, protocol=None, cname=None, originType=None, port=None, algorithm=None, originAddr=None, originDomain=None, originPort=None, status=None):
        """
        :param forwardRuleId: (Optional) 规则id
        :param protocol: (Optional) TCP或UDP
        :param cname: (Optional) 规则的cname
        :param originType: (Optional) 回源类型：ip或者domain
        :param port: (Optional) 端口号
        :param algorithm: (Optional) 转发规则：wrr-&gt;带权重的轮询，wlc-&gt;加权最小连接，rr-&gt;不带权重的轮询，sh-&gt;源地址hash
        :param originAddr: (Optional) 回源地址：originType为ip时为多个填多个ip，originType为domain时填一个域名
        :param originDomain: (Optional) 回源域名
        :param originPort: (Optional) 回源端口号
        :param status: (Optional) 0防御状态，1回源状态
        """

        self.forwardRuleId = forwardRuleId
        self.protocol = protocol
        self.cname = cname
        self.originType = originType
        self.port = port
        self.algorithm = algorithm
        self.originAddr = originAddr
        self.originDomain = originDomain
        self.originPort = originPort
        self.status = status
