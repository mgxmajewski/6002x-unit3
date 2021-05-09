import pytest
from inferential_stat_lec7_exercise3 import std_dev_of_lengths
from assertpy import assert_that
import math
import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np


class TestClass:

    @pytest.fixture(autouse=True)
    def prepare_vat_service(self):
        self.std_dev_of_length = std_dev_of_lengths

    def test_std_dev_of_list_len_0(self):
        # Given
        L = []
        # When
        result = self.std_dev_of_length(L)
        # Then
        assert_that(result).is_nan()

    def test_std_dev_of_length_for_str_len_of_1(self):
        # Given
        L = ['a', 'z', 'p']
        # When
        result = self.std_dev_of_length(L)
        # Then
        assert_that(result).is_equal_to(0)

    def test_std_dev_of_length_for_str_various_len(self):
        # Given
        L = ['apples', 'oranges', 'kiwis', 'pineapples']
        # When
        result = self.std_dev_of_length(L)
        # Then
        assert_that(result).is_close_to(1.8708, 5)
