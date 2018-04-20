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


class ElasticIp(object):

    def __init__(self, elasticIpId=None, elasticIpAddress=None, bandwidthMbps=None, provider=None, privateIpAddress=None, networkInterfaceId=None, instanceId=None, instanceType=None, charge=None, createdTime=None):
        """
        :param elasticIpId: (Optional) 弹性IP的Id
        :param elasticIpAddress: (Optional) 弹性IP地址
        :param bandwidthMbps: (Optional) 弹性ip的限速（单位：Mb)
        :param provider: (Optional) IP服务商，取值为bgp或no_bgp
        :param privateIpAddress: (Optional) 私有IP的IPV4地址
        :param networkInterfaceId: (Optional) 配置弹性网卡Id
        :param instanceId: (Optional) 实例Id
        :param instanceType: (Optional) 实例类型
        :param charge: (Optional) 计费配置
        :param createdTime: (Optional) 弹性ip创建时间
        """

        self.elasticIpId = elasticIpId
        self.elasticIpAddress = elasticIpAddress
        self.bandwidthMbps = bandwidthMbps
        self.provider = provider
        self.privateIpAddress = privateIpAddress
        self.networkInterfaceId = networkInterfaceId
        self.instanceId = instanceId
        self.instanceType = instanceType
        self.charge = charge
        self.createdTime = createdTime
