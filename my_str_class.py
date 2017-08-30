"Поздравляю!"

class Str2(object):
    def __init__(self, my_string):
        self.my_string = my_string

    def count(self, letter):
        counter = 0
        for x in self.my_string.lower():
            if x == letter:
                counter += 1
        return counter

    def lower(self):
        lower_list = []
        for x in self.my_string:
            if x.isupper():
                lower_list.append((chr(ord(x) + 32)))
            else:
                lower_list.append(x)
        return ''.join(lower_list)

    def upper(self):
        upper_list = []
        for x in self.my_string:
            if x.islower():
                upper_list.append((chr(ord(x) - 32)))
            else:
                upper_list.append(x)
        return ''.join(upper_list)

    def title(self):
        pass

    def rstrip(self):
        if self.my_string[len(self.my_string) - 1] == ' ':
            return self.my_string[:-1]

    def lstrip(self, symbols):
        if self.my_string[0] == ' ':
            return self.my_string[1:]

    def islower(self):
        counter = 0
        for letter in self.my_string:
            if ord(letter) >= 97 and ord(letter) <= 122:
                counter += 1
        return True if counter >= 1 else False

    def isupper(self):
        counter = 0
        for letter in self.my_string:
            if ord(letter) != (ord(letter) >= 97 and ord(letter) <= 122):
                counter += 1
        return True if counter == len(self.my_string) else False

    def isalnum(self):
        counter = 0
        if len(self.my_string) >= 1:
            for item in self.my_string:
                if ((ord(item) >= 97 and ord(item) <= 122) or (ord(item) >= 65 and ord(item) <= 90) or (ord(item) >= 48 and ord(item) <= 57)):
                    counter += 1
            if counter == len(self.my_string):
                return True
            else:
                return False
        else:
            return False
    def isalpha(self):
        counter = 0
        for item in self.my_string:
            if (ord(item) >= 97 and ord(item) <= 122) or (ord(item) >= 65 and ord(item) <= 90):
                counter += 1
        if counter == len(self.my_string):
            return True
        else:
            return False

    def isspace(self):
        counter = 0
        for item in self.my_string:
            if item == ' ' or item == '\n' or item == '\t' or item == '-':
                counter += 1
        if counter == len(self.my_string):
            return True
        else:
            return False

    def capitalize(self):
        capitalized_list = []
        if ord(self.my_string[0]) >= 97 and ord(self.my_string[0]) <= 122:
            capitalized_list.append(chr(ord(self.my_string[0]) - 32))
        else:
            capitalized_list.append(self.my_string[0])
        for x in self.my_string:
                capitalized_list.append(chr(ord(x) + 32))
        capitalized_list.pop(1)
        return ''.join(capitalized_list)

    def startswith(self, word):
        item_index = 0
        counter = 0
        len_word = len(word)
        while len_word != 0:
            if self.my_string[item_index] == word[item_index]:
                counter += 1
            len_word -= 1
        if counter == len(word):
            return True
        else:
            return False

    def endswith(self, word):
        pass

m_string = 'fsdfsdAAA'

my_string = Str2(m_string)
print "Roma: ", my_string.isalpha()

my_string = m_string
print "Test: ", my_string.isalpha()