"""
Wrapper for aioboto3 SSMContacts service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ssm_contacts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ssm_contacts.client import SSMContactsClient

from boto34.aioboto3.service_factory import ServiceFactory


class SSMContactsService(ServiceFactory[SSMContactsClient]):
    """
    SSMContacts service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ssm_contacts/)
    """
