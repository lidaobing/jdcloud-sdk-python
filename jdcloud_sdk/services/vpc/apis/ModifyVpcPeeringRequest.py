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


class ModifyVpcPeeringRequest(JDCloudRequest):
    """
    修改VpcPeering接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyVpcPeeringRequest, self).__init__(
            '/regions/{regionId}/vpcPeerings/{vpcPeeringId}', 'PUT', header, version)
        self.parameters = parameters


class ModifyVpcPeeringParameters(object):

    def __init__(self, regionId, vpcPeeringId, ):
        """
        :param regionId: Region ID
        :param vpcPeeringId: vpcPeeringId ID
        """

        self.regionId = regionId
        self.vpcPeeringId = vpcPeeringId
        self.vpcPeeringName = None
        self.description = None

    def setVpcPeeringName(self, vpcPeeringName):
        """
        :param vpcPeeringName: (Optional) VpcPeering的名字,不为空。名称取值范围：1-32个中文、英文大小写的字母、数字和下划线分隔符
        """
        self.vpcPeeringName = vpcPeeringName

    def setDescription(self, description):
        """
        :param description: (Optional) VpcPeering 描述，取值范围：0-256个中文、英文大小写的字母、数字和下划线分隔符
        """
        self.description = description

