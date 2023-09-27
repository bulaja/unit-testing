import pytest
from src.weather_service import generate_weather_report
from unittest.mock import patch


# Mock the get_weather function
@patch('src.weather_service.get_weather')
def test_generate_weather_report(mock_get_weather):
    # Configure the mock behavior
    mock_get_weather.return_value = {
        "temperature": 25,
        "condition": "Sunny"
    }

    # Test the function
    result = generate_weather_report("New York")

    # Assert the result
    assert result == "The weather in New York is Sunny with a temperature of 25°C."

    # Verify that get_weather was called with the correct argument
    mock_get_weather.assert_called_once_with("New York")