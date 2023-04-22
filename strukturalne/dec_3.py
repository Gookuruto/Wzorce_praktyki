class WrittenText:
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class UnderlineWrapper:
    """___text___"""

    def __init__(self, component):
        self._component = component

    def render(self):
        return f"___{self._component.render()}___"


class ItalicWrapper:
    """<i>text</i>"""

    def __init__(self, component):
        self._component = component

    def render(self):
        return f"<i>{self._component.render()}</i>"


class BoldWrapper:
    """<b>text</b>"""

    def __init__(self, component):
        self._component = component

    def render(self):
        return f"<b>{self._component.render()}</b>"


if __name__ == '__main__':
    before_gfg = WrittenText("Example Text")
    after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

    print("before :", before_gfg.render())
    print("after :", after_gfg.render())
