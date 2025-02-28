"""
Wrapper for boto3 ElasticBeanstalk service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elasticbeanstalk/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_elasticbeanstalk.client import ElasticBeanstalkClient

from boto34.boto3.service_factory import ServiceFactory


class ElasticBeanstalkService(ServiceFactory[ElasticBeanstalkClient]):
    """
    ElasticBeanstalk service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elasticbeanstalk/)
    """
