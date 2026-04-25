# Currency Converter

A simple and interactive command-line application that converts currency amounts using real-time exchange rates from the Frankfurter API.

## Features

- **Real-time Exchange Rates**: Fetches current exchange rates from [Frankfurter](https://frankfurter.dev/)
- **Interactive Interface**: User-friendly command-line interface for entering conversion parameters
- **Multiple Currencies**: Supports conversion between various currency codes
- **Recursive Conversion**: Ability to perform multiple conversions in a single session
- **Error Handling**: Graceful error handling for invalid currency codes

## Requirements

- Python 3.x
- `requests` library (for API calls)

## Installation

1. Clone or download this repository to your local machine
2. Navigate to the project directory:
   ```bash
   cd Currency_converter
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application with:

```bash
python main.py
```

### Interactive Workflow

1. The application will display a welcome message
2. Enter the **base currency code** (e.g., `USD`, `EUR`, `GBP`)
3. Enter the **target currency code** (e.g., `EUR`, `JPY`, `CAD`)
4. Enter the **amount** you wish to convert
5. The application will display the conversion result
6. Choose whether to convert another currency or exit

### Example

```
================Welcome to the Currency Converter================

Enter the base currency code: USD
Enter the target currency code: EUR
Enter the amount you want to convert: 100

100 USD = 92.50 EUR


Do you want to convert another currency? (yes/no)
```

## Project Structure

```
Currency_converter/
├── converter.py
├── main.py
├── requirements.txt
└── README.md
```

## Author

[**Yoann N'dori**](https://github.com/yndori)
