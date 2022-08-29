import barcode
from barcode.writer import ImageWriter

input = input("Enter the barcode: ") 

# Set the barcode format
# https://python-barcode.readthedocs.io/en/stable/supported-formats.html
barcode_format = barcode.get_barcode_class("upc")

# Generate the barcode
my_barcode = barcode_format(input, writer=ImageWriter())

my_barcode.save("barcode.svg")
#open('barcode.png', 'wb')