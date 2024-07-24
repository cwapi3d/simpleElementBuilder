import unittest
from unittest.mock import patch

import mock_element_controller
import mock_attribute_controller
from mock_cadwork import point_3d


class TestCreateRectangularBeamVectors(unittest.TestCase):

    def setUp(self):
        self.width = 100.0
        self.height = 260.0
        self.length = 5_000.0
        self.p1 = point_3d(0, 0, 0)
        self.xl = point_3d(1, 0, 0)
        self.zl = point_3d(0, 0, 1)
        self.expected_name = "Beam 1"

    @patch('mock_element_controller.create_rectangular_beam_vectors')
    def test_create_rectangular_beam_vectors(self, mock_create):
        # Arrange
        mock_create.return_value = 62894811  # Mocked element ID

        # Act
        result = mock_element_controller.create_rectangular_beam_vectors(
            self.width, self.height, self.length, self.p1, self.xl, self.zl)
        name = mock_attribute_controller.get_name(result)

        # Assert
        mock_create.assert_called_once_with(self.width, self.height, self.length, self.p1, self.xl, self.zl)
        self.assertEqual(result, mock_create.return_value)
        self.assertEqual(name, self.expected_name)


if __name__ == '__main__':
    unittest.main()
