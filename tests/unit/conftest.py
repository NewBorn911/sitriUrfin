import pytest

from sitri import Sitri
from sitri.contrib.system import SystemConfigProvider


@pytest.fixture(scope="module")
def test_sitri():
    return Sitri(config_provider=SystemConfigProvider(prefix="test"))
