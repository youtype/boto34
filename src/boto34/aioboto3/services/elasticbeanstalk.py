"""
Wrapper for aioboto3 ElasticBeanstalk service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_elasticbeanstalk/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_elasticbeanstalk.client import ElasticBeanstalkClient

from boto34.aioboto3.service_factory import ServiceFactory


class ElasticBeanstalkService(ServiceFactory[ElasticBeanstalkClient]):
    """
    ElasticBeanstalk service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_elasticbeanstalk/)
    """
