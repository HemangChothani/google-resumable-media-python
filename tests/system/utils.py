# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import hashlib
import time


BUCKET_NAME = u'grpm-systest-{}'.format(int(1000 * time.time()))
BUCKET_POST_URL = u'https://www.googleapis.com/storage/v1/b/'
BUCKET_URL = u'https://www.googleapis.com/storage/v1/b/{}'.format(BUCKET_NAME)

_DOWNLOAD_BASE = u'https://www.googleapis.com/download/storage/v1/b/{}'.format(
    BUCKET_NAME)
DOWNLOAD_URL_TEMPLATE = _DOWNLOAD_BASE + u'/o/{blob_name}?alt=media'

_UPLOAD_BASE = u'https://www.googleapis.com/upload/storage/v1/b/{}'.format(
    BUCKET_NAME) + u'/o?uploadType='
SIMPLE_UPLOAD_TEMPLATE = _UPLOAD_BASE + u'media&name={blob_name}'
MULTIPART_UPLOAD = _UPLOAD_BASE + u'multipart'
RESUMABLE_UPLOAD = _UPLOAD_BASE + u'resumable'

METADATA_URL_TEMPLATE = BUCKET_URL + u'/o/{blob_name}'

GCS_RW_SCOPE = u'https://www.googleapis.com/auth/devstorage.read_write'
# Generated using random.choice() with all 256 byte choices.
ENCRYPTION_KEY = (
    b'R\xb8\x1b\x94T\xea_\xa8\x93\xae\xd1\xf6\xfca\x15\x0ekA'
    b'\x08 Y\x13\xe2\n\x02i\xadc\xe2\xd99x')


def get_encryption_headers(key=ENCRYPTION_KEY):
    """Builds customer-supplied encryption key headers

    See `Managing Data Encryption`_ for more details.

    Args:
        key (bytes): 32 byte key to build request key and hash.

    Returns:
        Dict[str, str]: The algorithm, key and key-SHA256 headers.

    .. _Managing Data Encryption:
        https://cloud.google.com/storage/docs/encryption
    """
    key_hash = hashlib.sha256(key).digest()
    key_hash_b64 = base64.b64encode(key_hash)
    key_b64 = base64.b64encode(key)

    return {
        u'x-goog-encryption-algorithm': u'AES256',
        u'x-goog-encryption-key': key_b64.decode(u'utf-8'),
        u'x-goog-encryption-key-sha256': key_hash_b64.decode(u'utf-8'),
    }
