"""
Wrapper for aiobotocore ACM 2.20.1 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_acm/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore ACM client
    async with session.acm.create_client() as acm_client:
        acm_client: types_aiobotocore_acm.client.ACMClient```
"""

from __future__ import annotations

from types_aiobotocore_acm.client import ACMClient
from types_aiobotocore_acm.paginator import ListCertificatesPaginator
from types_aiobotocore_acm.waiter import CertificateValidatedWaiter

from boto34.aiobotocore.client_factory import ClientFactory
from boto34.aiobotocore.service_factory import ServiceFactory


class ACMWaiterFactory(ClientFactory[ACMClient]):
    @property
    def certificate_validated(self) -> CertificateValidatedWaiter:
        return self._client.get_waiter("certificate_validated")


class ACMPaginatorFactory(ClientFactory[ACMClient]):
    @property
    def list_certificates(self) -> ListCertificatesPaginator:
        return self._client.get_paginator("list_certificates")


class ACMService(
    ServiceFactory[
        ACMClient,
        ACMWaiterFactory,
        ACMPaginatorFactory,
    ]
):
    SERVICE_NAME = "acm"
    _SERVICE_PROP = "acm"
    _WAITER_FACTORY_CLS = ACMWaiterFactory
    _PAGINATOR_FACTORY_CLS = ACMPaginatorFactory

    def get_waiters(self, client: ACMClient) -> ACMWaiterFactory:
        return self._get_waiter_factory(client)

    def get_paginators(self, client: ACMClient) -> ACMPaginatorFactory:
        return self._get_paginator_factory(client)
