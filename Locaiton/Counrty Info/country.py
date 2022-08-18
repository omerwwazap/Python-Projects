# If possible find a way to do this in javascript
# Add javascript version to my github page for daily use projects
#
from countryinfo import CountryInfo

# country_input = input("Enter country name: ")
country_input = "Turkey"

country = CountryInfo(country_input)

print("Capital: " + country.capital())
print(country.languages())
print("Population: " + str(country.population()))
print("Region: " + country.region())
print(country.timezones())
print(country.tld())
print(country.calling_codes())
print(country.borders())
print(country.demonym())
print("nativeName: " + country.native_name())
print(country.translations())
