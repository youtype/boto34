"""
Wrapper for boto3 DevOpsGuru service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_devops_guru/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_devops_guru.client import DevOpsGuruClient

from boto34.boto3.service_factory import ServiceFactory


class DevOpsGuruService(ServiceFactory[DevOpsGuruClient]):
    """
    DevOpsGuru service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_devops_guru/)
    """
