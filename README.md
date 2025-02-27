# boto34

> There are type annotations for it. No exceptions.

Type annotated AWS SDK for Python. `boto3`, `aiobotocore`, and `aioboto3` clients included.

This package is part of [mypy_boto3_builder](https://github.com/youtype/mypy_boto3_builder) project.

## Features

- Type safety for all 400+ AWS services
- Auto-completion for every client, resource, waiter, and paginator
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

# this is not a boto3 Session, but arguments are the same
session = Session()

# this is a boto3 Client for s3 service
# no wrappers and fully type annotated
s3_client = session.s3.client(region_name="us-west-1")

# same for ServiceResource
s3_resource = session.s3.resource(region_name="us-west-1")

# oh, I almost forgot about waiters and paginators
object_exists_waiter = session.s3.waiter.object_exists
list_objects_paginator = session.s3.paginator.list_objects_v2
```

### aiobotocore

Install `boto34` for `aiobotocore`: `pip install 'boto34[aiobotocore]'`

Then, rewrite your code:

```python
from boto34.aiobotocore import get_session

# this is not an aiobotocore Session, but arguments are the same
session = get_session()

# this is a aiobotocore Client for s3 service
# no wrappers and fully type annotated
async with session.s3.create_client(region_name="us-west-1") as s3_client:
    ...
```

### aioboto3

Install `boto34` for `aioboto3`: `pip install 'boto34[aioboto3]'`

Then, rewrite your code:

```python
from boto34.aioboto3 import Session

# this is not an aioboto3 Session, but arguments are the same
session = Session()

# this is a aioboto3 Client for s3 service
# no wrappers and fully type annotated
async with session.s3.client(region_name="us-west-1") as s3_client:
    ...

# same for ServiceResource
async with session.s3.resource(region_name="us-west-1") as s3_resource:
    ...
```


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
