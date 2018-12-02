from urllib.request import urlopen
import json


def exchange(currency_from, currency_to, amount_from):
    """ Returns: a string decoded from the byte stream given by the url.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to."""

    url_inf = "http://cs1110.cs.cornell.edu/2016fa/a1server.php?"
    url_inf += "from=" + currency_from + "&to=" + \
        currency_to + "&amt=" + amount_from

    doc = urlopen(url_inf)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode("ascii")

    return jstr


def value(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange."""

    dic = exchange(currency_from, currency_to, amount_from)
    dic = json.loads(dic)
    value = dic["to"].split(" ")
    value[0] = "%.2f" % float(value[0])
    value = " ".join(value)

    return value


def test_exchange():
    """This function will test if the defined function value runs well."""

    assert("86.36 Euros" == value("USD", "EUR", "100"))
    assert("685.21 Chinese Yuan" == value("USD", "CNY", "100"))
    assert("100.00 United States Dollars" == value("USD", "USD", "100"))
    assert("84800.81 Euros" == value("XPD", "EUR", "100"))
    assert("4704.47 Zimbabwean Dollars" == value("CNY", "ZWL", "100"))


def test_currency_from(currency_from):
    """This function will test if the
        source currency input by user is valid."""

    assert("true" in exchange(currency_from, "USD", "100")), \
        "Source currency code is invalid."


def test_currency_to(currency_to):
    """This function will test if the
        exchange currency input by user is valid."""

    assert("true" in exchange("USD", currency_to, "100")), \
        "Exchange currency code is invalid."


def test_amount_from(amount_from):
    """This function will test if the
        currency amount input by user is valid."""

    assert("true" in exchange("USD", "EUR", amount_from)), \
        "Currency amount is invalid."


def testAll(currency_from, currency_to, amount_from):
    """We put all the test function here and create a new function:"""

    test_exchange()
    test_currency_from(currency_from)
    test_currency_to(currency_to)
    test_amount_from(amount_from)


def main():
    """This is the main module of this program."""

    currency_from = input("Please input the currency on hand:")
    currency_to = input("Please input the currency to convert to:")
    amount_from = input("Please input the amount of currency to convert:")
    testAll(currency_from, currency_to, amount_from)
    print(value(currency_from, currency_to, amount_from))


if __name__ == "__main__":
    main()
