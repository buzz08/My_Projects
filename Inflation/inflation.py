import requests

country_list = [
"Belarus",
"Brazil",
"Canada",
"European Union",
"Eurozone",
"France",
"Germany",
"Greece",
"India",
"Japan",
"Kazakhstan",
"Mexico",
"Russia",
"Spain",
"Turkey",
"Ukraine",
"United Kingdom",
"United States"
]

print("Enter the country name from below")
for tempname in country_list:
    print(tempname)

for name in range(0, len(country_list)):
    country_list[name] = country_list[name].lower()

print()

country_name = input().lower()

if(country_name in country_list):
    country_name = country_name.replace(" ","-")
    print("\nEnter the year of inflation")
    year = input()

    url = "https://www.statbureau.org/calculate-inflation-rate-json/?&country=" + country_name + "&start=" + year + "%2F1%2F1&end=" + year + "%2F12%2F1"

    source = requests.get(url)
    rate = source.content.decode("utf-8")
    rate = rate.replace("\"", "")

    if (rate=="0"):
        print("\nInflation for the year " +year+ " is not found" )
    else:
        print("\nInflation rate for the year " + year + " is " + rate + "%")

        print("\nEnter bitcoin price")
        bitcoin_price = input()

        actual_price = float(bitcoin_price) - ((float(bitcoin_price) * float(rate)) / 100)
        print("\nThe acutal price of bitcoin in " + country_name.upper().replace("-"," ") + " is " + str(actual_price))
else:
    print("Entered country name is incorrect. Please check and try again.")   
