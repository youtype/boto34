# boto34

[![PyPI - boto34](https://img.shields.io/pypi/v/boto34.svg?color=blue&label=boto34)](https://pypi.org/project/boto34)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/boto34.svg?color=blue)](https://pypi.org/project/boto34)

> There are type annotations for it. No exceptions.

Type annotated AWS SDK for Python.
Adds static type checking and code completions for your
[boto3](https://pypi.org/project/boto3/),
[aiobotocore](https://pypi.org/project/aiobotocore/),
and [aioboto3](https://pypi.org/project/aioboto3/)
code without affecting runtime.

This package is part of [mypy_boto3_builder](https://github.com/youtype/mypy_boto3_builder) project.

- [boto34](#boto34)
  - [Features](#features)
  - [What is not included](#what-is-not-included)
  - [Quickstart](#quickstart)
    - [boto3 / botocore](#boto3--botocore)
    - [aiobotocore](#aiobotocore)
    - [aioboto3](#aioboto3)
  - [How it works](#how-it-works)
    - [boto3 / botocore](#boto3--botocore-1)
    - [aioboto3 / aiobotocore](#aioboto3--aiobotocore)
  - [Versioning](#versioning)
  - [Latest changes](#latest-changes)

## Features

- Type safety for all [400+ AWS services](./services.md)
- Auto-completion for every client, resource, request, response, waiter, and paginator
- Support for `boto3`, `aiobotocore` and `aioboto3`

## What is not included

- No drop-in replacement, you need to rewrite your code a bit
- No wrappers around clients and resources
- No porn popup ads (?)

## Quickstart

### boto3 / botocore

Install `boto34` for `boto3`: `pip install 'boto34[boto3]'`

Then, rewrite your code:

```python
from boto34.boto3 import Session

# this is a wrapper for boto3.Session, arguments are the same
# all services are accessible as attributes
session = Session()

# this is botocore.BaseClient for s3 service
# no wrappers and fully type annotated
s3_client = session.s3.client(region_name="us-east-1")
put_object_response = s3_client.put_object(
  Bucket="bucket", Key="key", Body=b"message"
)
url = s3_client.generate_presigned_url(
    "get_object", {"Bucket": "bucket", "Key": "key"},
)

# same for boto3.ServiceResource
s3_resource = session.s3.resource(region_name="us-east-1")
s3_object = resource.Bucket("bucket").put_object(Key="key", Body=b"message")
```

Full list of supported AWS services can be found in [services.md](./services.md).

### aiobotocore

Install `boto34` for `aiobotocore`: `pip install 'boto34[aiobotocore]'`

Then, rewrite your code:

```python
from boto34.aiobotocore import get_session

# this is a wrapper for aiobotocore.Session/get_session, arguments are the same
# all services are accessible as attributes
session = get_session()

# this is aiobotocore.AioBaseClient for s3 service
# no wrappers and fully type annotated
async with session.s3.create_client(region_name="us-east-1") as s3_client:
    put_object_response = await s3_client.put_object(
      Bucket="bucket", Key="key", Body=b"message"
    )
    url = await s3_client.generate_presigned_url(
        "get_object", {"Bucket": "bucket", "Key": "key"}
    )
```

Full list of supported AWS services can be found in [services.md](./services.md).

### aioboto3

Install `boto34` for `aioboto3`: `pip install 'boto34[aioboto3]'`

Then, rewrite your code:

```python
from boto34.aioboto3 import Session

# this is a wrapper for aioboto3.Session, arguments are the same
# all services are accessible as attributes
session = Session()

# this is a aiobotocore.AioBaseClient for s3 service
# no wrappers and fully type annotated
async with session.s3.client(region_name="us-east-1") as s3_client:
    put_object_response = await s3_client.put_object(
      Bucket="bucket", Key="key", Body=b"message"
    )
    url = await s3_client.generate_presigned_url(
        "get_object", {"Bucket": "bucket", "Key": "key"}
    )

# same for aioboto3.AIOBoto3ServiceResource
async with session.s3.resource(region_name="us-east-1") as s3_resource:
    s3_bucket = await s3_resource.Bucket("bucket")
    s3_object = await s3_bucket.put_object(Key="key", Body=b"message")
```

Full list of supported AWS services can be found in [services.md](./services.md).

## How it works

### boto3 / botocore

`boto34` provides `boto34.boto3` wrapper for `boto3` and `botocore` session to add type annotations to all classes and methods.

Type annotations are powered by:
- [botocore-stubs](https://pypi.org/project/botocore-stubs/) - Static type annotations for `botocore`
- [types-boto3-lite](https://pypi.org/project/types-boto3-lite/) - Static type annotations for `boto3`
- [types-boto3-full](https://pypi.org/project/types-boto3-full/) - Generated type annotations for all AWS services

### aioboto3 / aiobotocore

`boto34` provides `boto34.aioboto3` wrapper for `aioboto3` session to add type annotations to all classes and methods.
If you use `aiobotocore` directly, you can use `boto34.aiobotocore` wrapper.

Type annotations are powered by:
- [types-aioboto3-lite](https://pypi.org/project/types-aioboto3-lite/) - Static type annotations for `aioboto3`
- [types-aiobotocore-lite](https://pypi.org/project/types-aiobotocore-lite/) - Static type annotations for `aiobotocore`
- [types-aiobotocore-full](https://pypi.org/project/types-aiobotocore-full/) - Generated type annotations for all AWS services

## Versioning

`boto34` version is not related to `boto3` version and follows
[Python Packaging version specifiers](https://packaging.python.org/en/latest/specifications/version-specifiers/).

## Latest changes

Full changelog can be found in [Releases](https://github.com/youtype/boto34/releases).
