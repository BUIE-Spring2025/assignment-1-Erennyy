def int_to_roman(num):

    one = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundred = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousand = ["", "M", "MM", "MMM"]

    return thousands[num // 1000] + \
           hundreds[(num % 1000) // 100] + \
           tens[(num % 100) // 10] + \
           ones[num % 10]
