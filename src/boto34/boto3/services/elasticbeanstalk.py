"""
Wrapper for boto3 ElasticBeanstalk service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elasticbeanstalk/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 ElasticBeanstalk client
    elasticbeanstalk_client = session.elasticbeanstalk.client()
    elasticbeanstalk_client: types_boto3_elasticbeanstalk.client.ElasticBeanstalkClient
    ```
"""

from __future__ import annotations

from types_boto3_elasticbeanstalk.client import ElasticBeanstalkClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_elasticbeanstalk.client import ElasticBeanstalkClient
except ImportError:
    ElasticBeanstalkClient = object  # type: ignore[misc,assignment]


class ElasticBeanstalkService(
    ServiceFactory[ElasticBeanstalkClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "elasticbeanstalk"
    _SERVICE_PROP = "elasticbeanstalk"
