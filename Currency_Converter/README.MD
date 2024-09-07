# Currency Converter

This script provides a command-line interface for converting currencies and getting exchange rates using the Free Currency Converter API.

## Dependencies

- `requests`: For making HTTP requests to the API
- `pprint`: For pretty-printing data (not used in the main functionality)

## Configuration

- `BASE_URL`: The base URL for the Free Currency Converter API
- `API_KEY`: Your API key for accessing the service

## Functions

### `get_currencies()`

Fetches a list of available currencies from the API.

Returns:

- A sorted list of tuples containing currency data

### `print_currencies(currencies)`

Prints a formatted list of currencies.

Parameters:

- `currencies`: A list of currency data tuples

### `exchange_rate(currency1, currency2)`

Fetches and displays the exchange rate between two currencies.

Parameters:

- `currency1`: The code for the base currency
- `currency2`: The code for the target currency

Returns:

- The exchange rate (float) or None if the request fails

### `convert(currency1, currency2, amount)`

Converts an amount from one currency to another and displays the result.

Parameters:

- `currency1`: The code for the base currency
- `currency2`: The code for the target currency
- `amount`: The amount to convert (as a string)

Returns:

- The converted amount (float) or None if the conversion fails

### `main()`

The main function that runs the command-line interface. It provides a loop for user interaction with the following commands:

- `list`: Display all available currencies
- `convert`: Convert an amount from one currency to another
- `rate`: Get the exchange rate between two currencies
- `q`: Quit the program

## Usage

Run the script and follow the prompts in the command-line interface. Enter commands as instructed to perform currency conversions, view exchange rates, or list available currencies.
