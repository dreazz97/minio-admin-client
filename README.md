# MinIO Admin Client

**MinIO Admin Client** is a Python library for the MinIO client that provides admin operations and other functionalities not supported by the official Minio SDK. Please note that this library requires the MinIO client to be installed on the machine.

## Requirements

- Python and pip installed.
- MinIO client installed on the machine with the path environment added as `mc`.

## Usage Example

```python
from minio_admin_client import MinioAdminClient

# Initialize the MinIO Admin Client
client = MinioAdminClient('host:3000', 'access-key', 'secret-key')

# Example: Create a new user
client.create_user('new-access-key', 'new-secret-key')
```

## Source Code

The source code for this project is available on GitHub:

[GitHub Repository](https://github.com/dreazz97/minio-admin-client-lib)