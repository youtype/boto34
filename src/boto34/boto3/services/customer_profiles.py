"""
Wrapper for boto3 CustomerProfiles service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_customer_profiles/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_customer_profiles.client import CustomerProfilesClient

from boto34.boto3.service_factory import ServiceFactory


class CustomerProfilesService(ServiceFactory[CustomerProfilesClient]):
    """
    CustomerProfiles service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_customer_profiles/)
    """
