from __future__ import annotations

import os
from typing import Any

from sitri.providers.base import ConfigProvider


class SystemConfigProvider(ConfigProvider):
    """Provider for get config from system environment."""

    provider_code = "system"
    _prefix = ""

    def __init__(self, prefix: str | None = None, *args: Any, **kwargs: Any) -> None:
        """
        :param prefix: prefix for create "namespace" for project variables in environment
        """
        super().__init__(*args, **kwargs)

        if prefix:
            self._prefix = prefix.upper()

    def prefixize(self, key: str) -> str:
        """Get key with prefix.

        :param key: varname without prefix
        """
        if self._prefix:
            return f"{self._prefix}_{key.upper()}"

        return key.upper()

    def unprefixize(self, var_name: str) -> str:
        """Remove prefix from variable name.

        :param var_name: variable name
        """
        if self._prefix:
            return var_name.replace(f"{self._prefix}_", "").lower()

        return var_name

    def get(self, key: str, **kwargs: Any) -> str | None:
        """Get value from system env.

        :param key: key without prefix from env
        """
        return os.getenv(self.prefixize(key), None)

    def keys(self, **kwargs: Any) -> list[str]:
        """Get keys list with prefix from system env."""
        var_list = []

        for var in os.environ:
            if var.upper().startswith(self._prefix):
                var_list.append(self.unprefixize(var))

        return var_list
