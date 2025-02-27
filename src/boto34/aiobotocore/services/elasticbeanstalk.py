"""
Wrapper for aiobotocore ElasticBeanstalk service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_elasticbeanstalk/)

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
    # Returns type annotated aiobotocore ElasticBeanstalk client
    async with session.elasticbeanstalk.create_client() as elasticbeanstalk_client:
        elasticbeanstalk_client: types_aiobotocore_elasticbeanstalk.client.ElasticBeanstalkClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_elasticbeanstalk.client import ElasticBeanstalkClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_elasticbeanstalk.client import ElasticBeanstalkClient
except ImportError:
    ElasticBeanstalkClient = object  # type: ignore[misc,assignment]


class ElasticBeanstalkService(
    ServiceFactory[ElasticBeanstalkClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elasticbeanstalk"
    _SERVICE_PROP = "elasticbeanstalk"
