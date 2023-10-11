import pandas
# importing all Morse codes from csv found on GitHub
morse = pandas.read_csv("MORSE.csv")

letters = []
codes = []
for row in morse.iterrows():
    letters.append(row[1]["LETTER"])
    codes.append(row[1]["CODE"])

still_converting = True
print("Welcome to Morsify!")
print("We convert letters and numbers into Morse code for You :)\n")
while still_converting:
    text = input("Provide a text to be converted to morse code:\n")
    list_to_morsify = text.upper().split()
    for word in list_to_morsify:
        converted = ""
        for letter in word:
            try:
                converted += (codes[letters.index(letter)])
            except ValueError:
                converted += letter
            converted += "   "
        print("Here is your message in morse code - each word separated:")
        print(converted)

    next_text = input("Do you want to convert another text? y-yes n-no: ")
    if next_text.lower() != "y":
        still_converting = False
