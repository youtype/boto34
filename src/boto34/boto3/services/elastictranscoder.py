"""
Wrapper for boto3 ElasticTranscoder service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elastictranscoder/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_elastictranscoder.client import ElasticTranscoderClient

from boto34.boto3.service_factory import ServiceFactory


class ElasticTranscoderService(ServiceFactory[ElasticTranscoderClient]):
    """
    ElasticTranscoder service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_elastictranscoder/)
    """
