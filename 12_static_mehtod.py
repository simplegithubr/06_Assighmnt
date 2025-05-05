
"""12. Static Methods
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value."""
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

temp_celsius = 25
temp_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")