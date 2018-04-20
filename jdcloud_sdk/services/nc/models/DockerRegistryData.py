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


class DockerRegistryData(object):

    def __init__(self, server, username, password, email=None):
        """
        :param server:  registry服务器地址
        :param username:  用户名
        :param password:  密码
        :param email: (Optional) 邮件地址
        """

        self.server = server
        self.username = username
        self.password = password
        self.email = email
