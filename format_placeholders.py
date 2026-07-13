text="We don't have {:<10} children"
print(text.format(7))
#:<() means lean left subsitituee the format index and then leave as much space as dummy number indicates
#:>() same but leans right
#:^() centers the index of format
#:+ mathematically indicates rahter the numbers are postive or negative
#:- mathematically indicates the negative numbers and naturally shows positive numbers
#:, helps us to seperate thousands. exp 13000 --> 13,000
info="The universe is {:,} years old"
print(info.format(13441243445123412345))
#:_ a thousand seperator but instead of a coma it uses underscores
#:b converts the number to its binary form
binary="The binary version of {0} is {0:b}."
print(binary.format(18))
#:c converts the number to its unicode form.
#:d converts the binary decrypt to decimal number.
#:e displays the number in scientific math
#:f fixes the amount of dispalyed number after the decimal
#:F same as f but displays the number in uppercase and involves the use of scientific notation for inf and nan.
#:o converts the number to its octal form.
#:x converts the number to its hexadecimal form.
#:X same as x but displays the number in uppercase.
#:n displays the number in a format that is appropriate for the current locale.
#:% displays the number as a percentage.(:.0%) 