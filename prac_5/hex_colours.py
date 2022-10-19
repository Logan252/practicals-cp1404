"""estimated time: 30 minutes
actual time: 12 minutes"""
# first 10 colours on the chart

COLOUR_CODES = {"Absolute Zero": "#0048ba", "Acid Green": "b0bf1a", "Alice Blue": "#f0f8ff", "Alizarin crimson":
                "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "9966cc",
                "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}
colour_name = input("Enter a colour name: ")
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")
