from colorama import Fore, Back, Style


def Colored(style):
    return ColoredText(style=style)


class ColoredText:
    def __init__(self, style=None, words=None):
        self.words = words.copy() if words else []
        self.style = style

    def __reset(self):
        return f'{Style.RESET_ALL}{Fore.RESET}{Back.RESET}'

    def __append_word(self, style, s):
        words = self.words.copy()
        words.append(f'{style}{s}{self.__reset()}')
        return ColoredText(style=self.style, words=words)

    def __get_style(self, method: str):
        return getattr(self.style, method)()

    # Define functions here to provide code completion hint
    def txt(self, s):
        return self.__append_word(self.__get_style('txt'), s)

    def kw(self, s):
        return self.__append_word(self.__get_style('kw'), s)

    def kw2(self, s):
        return self.__append_word(self.__get_style('kw2'), s)

    def newline(self):
        words = self.words.copy()
        words.append(f'\n')
        return ColoredText(style=self.style, words=words)

    def __to_str(self):
        words = []
        for w in self.words:
            if w[0] == '\n':
                pass
            if w[-1] == '\n':
                pass

        words = [w.replace('\n', f'{Style.RESET_ALL}\n') for w in self.words]
        return ''.join(words)

    def __repr__(self):
        return self.__to_str()

    def __str__(self):
        return self.__to_str()

    def __add__(self, other):
        words = self.words.copy()+other.words.copy()
        return ColoredText(style=other.style, words=words)
