# Define number words for 1–19, tens, and others
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
         "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", 
        "sixty", "seventy", "eighty", "ninety"]

def number_to_words(n):
    if 1 <= n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 20 <= n < 100:
        return tens[n // 10] + ones[n % 10]
    elif 100 <= n < 1000:
        remainder = n % 100
        return ones[n // 100] + "hundred" + (("and" + number_to_words(remainder)) if remainder != 0 else "")
    elif n == 1000:
        return "onethousand"
    return ""

# Sum the lengths of number words from 1 to 1000
total_letters = sum(len(number_to_words(i)) for i in range(1, 1001))
total_letters
