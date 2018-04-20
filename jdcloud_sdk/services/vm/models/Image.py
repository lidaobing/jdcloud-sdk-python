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


class Image(object):

    def __init__(self, imageId=None, name=None, platform=None, osVersion=None, architecture=None, systemDiskSizeGB=None, imageSource=None, osType=None, status=None, createTime=None, sizeMB=None, desc=None, dataDisks=None):
        """
        :param imageId: (Optional) 镜像ID
        :param name: (Optional) 镜像名称
        :param platform: (Optional) 操作系统发行版，[suse, debian, ubuntu, centos, windows-server]
        :param osVersion: (Optional) 操作系统版本号
        :param architecture: (Optional) 镜像架构 i386, x86_64
        :param systemDiskSizeGB: (Optional) 镜像系统盘大小
        :param imageSource: (Optional) 镜像来源 jcloud：官方镜像 marketplace：镜像市场镜像 self：用户自己的镜像 shared：其他用户分享的镜像
        :param osType: (Optional) 镜像的操作系统类型，[windows, linux]
        :param status: (Optional) 镜像状态, [pending, ready, deleting, error]
        :param createTime: (Optional) 创建时间
        :param sizeMB: (Optional) 镜像本身大小
        :param desc: (Optional) 镜像描述
        :param dataDisks: (Optional) 打包镜像数据盘映射信息
        """

        self.imageId = imageId
        self.name = name
        self.platform = platform
        self.osVersion = osVersion
        self.architecture = architecture
        self.systemDiskSizeGB = systemDiskSizeGB
        self.imageSource = imageSource
        self.osType = osType
        self.status = status
        self.createTime = createTime
        self.sizeMB = sizeMB
        self.desc = desc
        self.dataDisks = dataDisks