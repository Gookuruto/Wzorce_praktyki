class WrittenText:
    """Represents a Written text"""

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class UnderlineWrapper(WrittenText):
    """Wraps a tag in <u>"""

    def __init__(self, wrapped: WrittenText):
        self._wrapped = wrapped

    def render(self):
        return "___{}___".format(self._wrapped.render())


class ItalicWrapper(WrittenText):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


class BoldWrapper(WrittenText):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    @property
    def wrapped(self):
        return self._wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


""" main method """

if __name__ == "__main__":
    before_gfg = WrittenText("Example Text")
    after_gfg = BoldWrapper(UnderlineWrapper(before_gfg))

    print(after_gfg.wrapped)
    print("before :", before_gfg.render())
    print("after :", after_gfg.render())
