"""
Wrapper for boto3 GlobalAccelerator service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_globalaccelerator/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_globalaccelerator.client import GlobalAcceleratorClient

from boto34.boto3.service_factory import ServiceFactory


class GlobalAcceleratorService(ServiceFactory[GlobalAcceleratorClient]):
    """
    GlobalAccelerator service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_globalaccelerator/)
    """
