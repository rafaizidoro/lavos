# Lavos: A Pythonic Cron Expression Serializer with Fluent Syntax
![DALL·E 2023-11-19 15 06 51 - Logo design for an open source Python library named 'Lavos'  The logo should feature a stylized serpent or snake, representing Python, intertwined or ](https://github.com/rizidoro/lavos/assets/13101/6ce30f4b-bc35-477c-90d7-208ea5b4a870)


Lavos is an innovative Python library that simplifies working with cron expressions. It replaces the cryptic syntax of traditional cron expressions with a fluent, human-readable API. Lavos allows you to define cron schedules for your tasks intuitively, making schedule management in Python applications easier than ever.

## Features
- **Fluent Syntax**: Enjoy a fluent and expressive syntax for defining cron schedules, making your code more readable and maintainable.
- **AWS Cron Support**: Compatible with traditional Unix and AWS cron expressions, providing versatility for different environments.
- **Syntax Sugars**: Includes convenient syntax sugars for common scheduling patterns, allowing for more concise code.

## Installation

Install Lavos using pip:

```bash
pip install lavos
```

## Usage

Lavos offers a range of functionalities for scheduling tasks. Below are examples demonstrating its versatility:

### Basic Usage

```python
from lavos import Lavos, MON, JAN, FEB, MAR, WEEKDAYS

cron = Lavos()
```


- **Every 5 Minutes**:
  ```python
  # Cron: */5 * * * *
  cron.every(5).minutes
  ```
- **Every Hour**:
  ```python
  # Cron: 0 * * * *
  cron.every(1).hours
  ```
- **Daily at Specific Time**:
  ```python
  # Cron: 0 14 * * *
  cron.at("14:00").daily
  ```
- **Specific Weekday at Time**:
  ```python
  # Cron: 0 12 * * 5
  cron.at("12:00").on(THU)
  ```
- **First Day of Every Month**:
  ```python
  # Cron: 0 0 1 * *
  cron.on(1).monthly
  ```
- **Specific Days of Specific Months**:
  ```python
  # Cron: 0 0 15 1,2 *
  cron.on(15).of(JAN, FEB)
  ```
- **Every Weekday at Multiple Times**:
  ```python
  # Cron: 0 9,17 * * 1-5
  cron.at("09:00", "17:00").on(WEEKDAYS)
  ```

### Using AWS Format

You can also create schedules using the AWS cron format:

```python
cron = Lavos(format="aws")

# Every 5 minutes in AWS format
# */5 * * * ? *
cron.every(5).minutes

# Every weekday at 09:00 in AWS format
# 0 9 * * ? *
cron.at("09:00").on(WEEKDAYS)
```

## Advanced Features

## Contributing

We welcome contributions to Lavos! Whether it's adding new features, improving documentation, or fixing bugs, your input is valuable.

## License

Lavos is released under MIT. See the LICENSE file for more details.
