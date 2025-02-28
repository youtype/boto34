"""
Wrapper for boto3 SSMContacts service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_contacts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_ssm_contacts.client import SSMContactsClient

from boto34.boto3.service_factory import ServiceFactory


class SSMContactsService(ServiceFactory[SSMContactsClient]):
    """
    SSMContacts service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_contacts/)
    """
