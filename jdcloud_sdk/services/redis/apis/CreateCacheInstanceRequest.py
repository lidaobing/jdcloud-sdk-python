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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class CreateCacheInstanceRequest(JDCloudRequest):
    """
    创建一个指定配置的缓存Redis实例
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateCacheInstanceRequest, self).__init__(
            '/regions/{regionId}/cacheInstance', 'POST', header, version)
        self.parameters = parameters


class CreateCacheInstanceParameters(object):

    def __init__(self, regionId, cacheInstance, ):
        """
        :param regionId: 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2
        :param cacheInstance: 
        """

        self.regionId = regionId
        self.cacheInstance = cacheInstance
        self.charge = None

    def setCharge(self, charge):
        """
        :param charge: (Optional) 
        """
        self.charge = charge

