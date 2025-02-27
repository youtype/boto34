"""
Wrapper for aioboto3 ElasticBeanstalk service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_elasticbeanstalk/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 ElasticBeanstalk client
    elasticbeanstalk_client = session.elasticbeanstalk.client()
    elasticbeanstalk_client: types_aiobotocore_elasticbeanstalk.client.ElasticBeanstalkClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_elasticbeanstalk.client import ElasticBeanstalkClient
except ImportError:
    ElasticBeanstalkClient = object  # type: ignore[misc,assignment]


class ElasticBeanstalkService(
    ServiceFactory[ElasticBeanstalkClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elasticbeanstalk"
    _SERVICE_PROP = "elasticbeanstalk"
