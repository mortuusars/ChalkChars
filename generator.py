import string
import json
from pathlib import Path
import shutil
from PIL import Image

# -- Compose

# {id, group, en translation, ua translation}
entries = []

for letter in string.ascii_lowercase:
    entries.append([letter + "_uppercase", "letters", "Uppercase " + letter.capitalize(), "Велика літера " + letter.capitalize()])
    entries.append([letter + "_lowercase", "letters", "Lowercase " + letter.capitalize(), "Мала літера " + letter.capitalize()])

entries.append(["zero",   "numbers",   "Zero",     "Нуль"])
entries.append(["one",    "numbers",   "One",      "Один"])
entries.append(["two",    "numbers",   "Two",      "Два"])
entries.append(["three",  "numbers",   "Three",    "Три"])
entries.append(["four",   "numbers",   "Four",     "Чотири"])
entries.append(["five",   "numbers",   "Five",     "П’ять"])
entries.append(["six",    "numbers",   "Six",      "Шість"])
entries.append(["seven",  "numbers",   "Seven",    "Сім"])
entries.append(["eight",  "numbers",   "Eight",    "Вісім"])
entries.append(["nine",   "numbers",   "Nine",     "Дев’ять"])

entries.append(["period",                  "punctuation",      "Period",                "Крапка"])
entries.append(["comma",                   "punctuation",      "Comma",                 "Кома"])
entries.append(["semicolon",               "punctuation",      "Semicolon",             "Крапка з комою"])
entries.append(["colon",                   "punctuation",      "Colon",                 "Дві крапки"])
entries.append(["question",                "punctuation",      "Question",              "Знак питання"])
entries.append(["exclamation",             "punctuation",      "Exclamation",           "Знак оклику"])
entries.append(["hyphen",                  "punctuation",      "Hyphen",                "Дефіс"])
entries.append(["underscore",              "punctuation",      "Underscore",            "Підкреслення"])
entries.append(["tilde",                   "punctuation",      "Tilde",                 "Тильда"])
entries.append(["at",                      "punctuation",      "At",                    "Равлик"])
entries.append(["hash",                    "punctuation",      "Hash",                  "Октоторп"])
entries.append(["ampersand",               "punctuation",      "Ampersand",             "Амперсанд"])
entries.append(["left_angle_braket",       "punctuation",      "Left Angle Braket",     "Ліва кутова дужка"])
entries.append(["right_angle_braket",      "punctuation",      "Right Angle Braket",    "Права кутова дужка"])
entries.append(["left_parenthesis",        "punctuation",      "Left Parenthesis",      "Ліва дужка"])
entries.append(["right_parenthesis",       "punctuation",      "Right Parenthesis",     "Права дужка"])
entries.append(["left_square_braket",      "punctuation",      "Left Square Braket",    "Ліва квадратна дужка"])
entries.append(["right_square_braket",     "punctuation",      "Right Square Braket",   "Права квадратна дужка"])
entries.append(["left_brace",              "punctuation",      "Left Brace",            "Ліва фігурна дужка"])
entries.append(["right_brace",             "punctuation",      "Right Brace",           "Права фігурна дужка"])
entries.append(["caret",                   "punctuation",      "Caret",                 "Карет"])
entries.append(["slash",                   "punctuation",      "Slash",                 "Скісна риска"])
entries.append(["pipe",                    "punctuation",      "Pipe",                  "Вертикальна риска"])
entries.append(["backslash",               "punctuation",      "Backslash",             "Обернена скісна риска"])
entries.append(["plus",                    "punctuation",      "Plus",                  "Плюс"])
entries.append(["minus",                   "punctuation",      "Minus",                 "Мінус"])
entries.append(["equals",                  "punctuation",      "Equals",                "Дорівнює"])
entries.append(["asterisk",                "punctuation",      "Asterisk",              "Зірочка"])
entries.append(["percent",                 "punctuation",      "Percent",               "Відсоток"])
entries.append(["dollar",                  "punctuation",      "Dollar",                "Долар"])
entries.append(["apostrophe",              "punctuation",      "Apostrophe",            "Апостроф"])
entries.append(["quotation",               "punctuation",      "Quotation",             "Лапки"])

# -- Cleanup

generatedFolder = Path("generated")
if generatedFolder.exists():
    shutil.rmtree(generatedFolder)

# -- Data

dataOutput = Path("generated/data/chalk_chars/chalk/mark_symbol")
dataOutput.mkdir(parents=True, exist_ok=True)

index = 0
groupPriorities = {}

for entry in entries:
    id = entry[0]
    group = entry[1]

    if groupPriorities.__contains__(group) is False:
        groupPriorities[group] = 0

    groupPriority = groupPriorities[group]
    groupPriorities[group] = groupPriority + 1

    data = {
        "texture": "chalk_chars:block/mark/" + id,
        "group": group,
        "group_priority": groupPriority,
        "orientation_behavior": "up_down_cardinal"
    }

    index = index + 1

    print("Writing: " + id)

    with open(dataOutput / f"{id}.json", "w") as f:
        json.dump(data, f, indent=2)

# -- Lang

enLang = {}
uaLang = {}

langOutput = Path("generated/assets/chalk_chars/lang")
langOutput.mkdir(parents=True, exist_ok=True)

for entry in entries:
    id = entry[0]
    enName = entry[2]
    uaName = entry[3]
    enLang[f"mark_symbol.chalk_chars.{id}"] = enName
    uaLang[f"mark_symbol.chalk_chars.{id}"] = uaName

enLang["mark_symbol_group.chalk.letters"] = "Letters"
uaLang["mark_symbol_group.chalk.letters"] = "Букви"
enLang["mark_symbol_group.chalk.numbers"] = "Numbers"
uaLang["mark_symbol_group.chalk.numbers"] = "Цифри"
enLang["mark_symbol_group.chalk.punctuation"] = "Punctuation"
uaLang["mark_symbol_group.chalk.punctuation"] = "Пунктуація"

print("Writing en_us lang file")
with open(langOutput / "en_us.json", "w") as f:
    json.dump(enLang, f, indent=2, ensure_ascii=False)
print("Writing uk_ua lang file")
with open(langOutput / "uk_ua.json", "w", encoding="utf-8") as f:
    json.dump(uaLang, f, indent=2, ensure_ascii=False)

## -- Textures

textureSheet = Path("char_sheet.png")
textureOutput = Path("generated/assets/chalk_chars/textures/block/mark")
textureOutput.mkdir(parents=True,exist_ok=True)
imageSize = 16

image = Image.open(textureSheet)

for i, entry in enumerate(entries):
    id = entry[0]
    x = (i % (image.width // imageSize)) * imageSize
    y = (i // (image.width // imageSize)) * imageSize

    tile = image.crop((x, y, x + imageSize, y + imageSize))

    if tile.getbbox() is None:
        print(f"Image for {id} is empty!")
    else:
        tile.save(textureOutput / f"{id}.png")

## --

print("Done!")