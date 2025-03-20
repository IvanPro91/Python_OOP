from unittest.mock import patch

import pytest

from config import ROOT_DIR
from src.read_products_file import read_products


def test_read_products() -> None:
    """
    [Тест] Функция чтения файла json.
    """
    with pytest.raises(FileNotFoundError):
        read_products("fake.json")

    with patch("src.read_products_file.open") as mock_file:
        mock_file.return_value = [{}]
        data = read_products("")
        assert data == []

    with patch("json.load") as mock_file:
        mock_file.return_value = None
        with pytest.raises(Exception):
            read_products(ROOT_DIR + "/data/products.json")
