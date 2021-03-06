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


class ListThumbnailTaskRequest(JDCloudRequest):
    """
    查询截图任务
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ListThumbnailTaskRequest, self).__init__(
            '/regions/{regionId}/thumbnail', 'GET', header, version)
        self.parameters = parameters


class ListThumbnailTaskParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: region id
        """

        self.regionId = regionId
        self.status = None
        self.begin = None
        self.end = None
        self.marker = None
        self.limit = None

    def setStatus(self, status):
        """
        :param status: (Optional) task 状态 [PENDING, RUNNING, SUCCESS, FAILED]
        """
        self.status = status

    def setBegin(self, begin):
        """
        :param begin: (Optional) 开始时间 时间格式(GMT): yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;
        """
        self.begin = begin

    def setEnd(self, end):
        """
        :param end: (Optional) 结束时间 时间格式(GMT): yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;
        """
        self.end = end

    def setMarker(self, marker):
        """
        :param marker: (Optional) 查询标记
        """
        self.marker = marker

    def setLimit(self, limit):
        """
        :param limit: (Optional) 查询记录数
        """
        self.limit = limit

