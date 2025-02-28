"""
Wrapper for aiobotocore SSMContacts service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ssm_contacts.client import SSMContactsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SSMContactsService(ServiceFactory[SSMContactsClient]):
    """
    SSMContacts service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/)
    """
