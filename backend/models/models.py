class TextInput(dict):
    def __init__(self, name, text=None):
        self["component"] = "textInput"
        self["text"] = text
        self["name"] = name
        self["data"] = ""


class ChoiceInput(dict):
    def __init__(self, name, value, text=None, multiple=False):
        self["component"] = "choiceInput"
        self["data"] = value[0]["id"]
        self["multiple"] = multiple
        self["value"] = value
        self["name"] = name
        self["text"] = text


class WordModel(dict):
    def __init__(self, name, url):
        self["name"] = name
        self["url"] = url
