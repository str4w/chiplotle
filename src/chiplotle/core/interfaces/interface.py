from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library

standard_library.install_aliases()


class _Interface(object):
    def __init__(self, client):
        self._client = client
