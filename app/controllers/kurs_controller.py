# Company     : PT. Arsytech Information Technology
# Owner       : Adi Surizal
# Email       : adisurizal.cyber@outlook.com

from flask import request
from app.services.exchange_api import get_exchange_rates
from app.utils.response import success_response, error_response

ALLOWED_CURRENCIES = {
    "IDR", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM",
    "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP",
    "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE", "CZK",
    "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP",
    "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG",
    "HUF", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES",
    "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD",
    "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR",
    "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB",
    "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR",
    "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SLL", "SOS", "SRD", "SSP", "STN",
    "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS",
    "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XCG",
    "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"
}

def convert_currency():
    if not request.is_json:
        return error_response("Content-Type harus 'application/json'", 415)

    data = request.get_json()
    currency_from = data.get('currency_from', '').upper()
    amount = data.get('amount', 0)

    if currency_from not in ALLOWED_CURRENCIES:
        return error_response("mata uang tidak diizinkan", 400)

    try:
        amount = float(amount)
    except ValueError:
        return error_response("format amount tidak valid", 422)

    result = get_exchange_rates(currency_from)
    if result is None:
        return error_response("Gagal mengambil kurs dari API", 502)

    rates = result.get('conversion_rates')
    converted = {k: round(v * amount, 3) for k, v in rates.items()}

    return success_response(data={
        "from": currency_from,
        "amount": amount,
        "converted": converted
    })
