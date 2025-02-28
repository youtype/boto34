"""
Wrapper for boto3 CloudHSM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudhsm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cloudhsm.client import CloudHSMClient

from boto34.boto3.service_factory import ServiceFactory


class CloudHSMService(ServiceFactory[CloudHSMClient]):
    """
    CloudHSM service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cloudhsm/)
    """
