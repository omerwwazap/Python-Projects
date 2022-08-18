# If possible find a way to do this in javascript
# Add javascript version to my github page for daily use projects
#

from langdetect import detect

text = input("Enter text: " + "\n")

print("Print Text: " + (text))
print("Print Detect: " + detect(text))
