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


class InstanceTemplateDiskAttachmentSpec(object):

    def __init__(self, diskCategory=None, autoDelete=None, cloudDiskSpec=None, deviceName=None, noDevice=None):
        """
        :param diskCategory: (Optional) 磁盘分类，local或者cloud；系统盘仅支持local；数据盘仅支持cloud
        :param autoDelete: (Optional) 自动删除，删除主机时自动删除此磁盘，默认为True，本地盘不能更改此值
        :param cloudDiskSpec: (Optional) 云硬盘规格
        :param deviceName: (Optional) 数据盘逻辑挂载点vdb,vdc,vdd,vde,vdf,vdg,vdh
        :param noDevice: (Optional) 排除镜像数据盘映射中的逻辑挂载点
        """

        self.diskCategory = diskCategory
        self.autoDelete = autoDelete
        self.cloudDiskSpec = cloudDiskSpec
        self.deviceName = deviceName
        self.noDevice = noDevice
