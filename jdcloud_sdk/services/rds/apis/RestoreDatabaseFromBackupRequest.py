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


class RestoreDatabaseFromBackupRequest(JDCloudRequest):
    """
    从云数据库SQL Server备份中恢复单个数据库
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(RestoreDatabaseFromBackupRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/databases/{dbName}:restoreDatabaseFromBackup', 'POST', header, version)
        self.parameters = parameters


class RestoreDatabaseFromBackupParameters(object):

    def __init__(self, regionId, instanceId, dbName, ):
        """
        :param regionId: 区域代码
        :param instanceId: 实例ID
        :param dbName: 库名称
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.dbName = dbName
        self.backupId = None
        self.backupFileName = None

    def setBackupId(self, backupId):
        """
        :param backupId: (Optional) 备份ID
        """
        self.backupId = backupId

    def setBackupFileName(self, backupFileName):
        """
        :param backupFileName: (Optional) 指定该备份中用于恢复数据库的文件名称
        """
        self.backupFileName = backupFileName

