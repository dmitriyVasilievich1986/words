class TextInput(dict):
    def __init__(self, name, text=None):
        self["component"] = "textInput"
        self["text"] = text
        self["name"] = name
        self["data"] = ""


class BoolInput(dict):
    def __init__(self, name, text=None):
        self["component"] = "boolInput"
        self["data"] = False
        self["text"] = text
        self["name"] = name


class ChoiceInput(dict):
    def __init__(self, name, value, text=None, multiple=False):
        self["data"] = [] if multiple else value[0]["id"]
        self["component"] = "choiceInput"
        self["multiple"] = multiple
        self["value"] = value
        self["name"] = name
        self["text"] = text


class WordModel(dict):
    def __init__(self, word, url):
        self["word"] = word
        self["url"] = url
