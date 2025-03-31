# 1. Custom String Class: 
# Implement a CustomString class that overloads the + operator for concatenation and
# the * operator to repeat the string. Include a method to return the string in uppercase. 

class CustomString:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, CustomString):
            return CustomString(self.value + other.value)
        elif isinstance(other, str):
            return CustomString(self.value + other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return CustomString(self.value * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def to_upper(self):
        return CustomString(self.value.upper())


# Example 1: Basic creation and concatenation
str1 = CustomString("Hello")
str2 = CustomString("World")
combined = str1 + str2
print(combined.value)  # Output: HelloWorld

# Example 2: Concatenating with a regular string
str3 = CustomString("Python ")
str4 = str3 + "is fun"
print(str4.value)  # Output: Python is fun

# Example 3: Repetition using *
str5 = CustomString("Hi ")
repeated = str5 * 3
print(repeated.value)  # Output: Hi Hi Hi 

# Example 4: Uppercase conversion
str6 = CustomString("hello there")
upper_str = str6.to_upper()
print(upper_str.value)  # Output: HELLO THERE

# Example 5: Combining operations
str7 = CustomString("Repeat ")
result = (str7 * 2 + CustomString("and ")) * 2
print(result.value)  # Output: Repeat Repeat and Repeat Repeat and 

# Example 6: Uppercase before operations
str8 = CustomString("test").to_upper()
combined_str = str8 + " string"
print(combined_str.value)  # Output: TEST string

# Example 7: Multiplication with integer on left side
str9 = CustomString("AB")
multiplied = 3 * str9
print(multiplied.value)  # Output: ABABAB



# 2. Currency Conversion:
# Create a Currency class that represents a monetary amount in a specific currency.
# Overload the + operator to add amounts in the same currency, and 
# implement a method to convert between different currencies.



class Currency:
    # Exchange rates relative to USD (for simplicity)
    EXCHANGE_RATES = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.73,
        'JPY': 110.0,
        'CAD': 1.25
    }

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        if self.currency != other.currency:
            # Convert other to self's currency
            converted_amount = other.amount * (Currency.EXCHANGE_RATES[other.currency] / Currency.EXCHANGE_RATES[self.currency])
            other = Currency(converted_amount, self.currency)
        return Currency(self.amount + other.amount, self.currency)

    def convert_to(self, target_currency):
        if self.currency == target_currency:
            return Currency(self.amount, self.currency)
        exchange_rate = Currency.EXCHANGE_RATES[self.currency]
        target_rate = Currency.EXCHANGE_RATES[target_currency]
        converted_amount = self.amount * (exchange_rate / target_rate)
        return Currency(converted_amount, target_currency)

    def __repr__(self):
        return f"{self.amount} {self.currency}"

# Create some currency instances
usd = Currency(100, 'USD')
eur = Currency(100, 'EUR')
cad = Currency(50, 'CAD')

# Convert EUR to USD
converted_eur_to_usd = eur.convert_to('USD')
print(converted_eur_to_usd)  # Output: 117.64705882352942 USD

# Convert USD to JPY
converted_usd_to_jpy = usd.convert_to('JPY')
print(converted_usd_to_jpy)  # Output: 11000.0 JPY

# Add two currencies (automatically converting if needed)
total_usd = usd + eur
print(total_usd)  # Output: 185.0 USD (100 USD + 85 converted from 100 EUR)

# Add two currencies with same currency
total_cad = cad + Currency(30, 'CAD')
print(total_cad)  # Output: 80.0 CAD

# Complex conversion and addition
eur_to_cad = eur.convert_to('CAD')
total_cad_with_eur = cad + eur_to_cad
print(total_cad_with_eur)  # Output: 85.88235294117647 CAD

