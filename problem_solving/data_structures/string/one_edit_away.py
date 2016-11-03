class StringEditor:
    def one_edit_away(self, s1, s2):
        if len(s1) == len(s2):
            return self._one_edit_replace(s1, s2)
        elif len(s1) + 1 == len(s2):
            return self._one_edit_insert(s1, s2)
        elif len(s1) == len(s2) + 1:
            return self._one_edit_insert(s2, s1)
        else:
            return False

    def _one_edit_replace(self, s1, s2):
        edited = False
        for i in range(0, len(s1)):
            char1, char2 = s1[i], s2[i]
            if char1 != char2:
                if edited:
                    return False
                edited = True

        return True

    def _one_edit_insert(self, short_string, long_string):
        edited = False
        i, j = 0, 0
        while i < len(short_string) and j < len(long_string):
            char1, char2 = short_string[i], long_string[j]
            if char1 != char2:
                if edited:
                    return False
                edited = True
                j += 1
            else:
                i += 1
                j += 1

        return True


string_editor = StringEditor()
test_cases = [("pale", "ple"), ("pales", "pale"), ("pale", "bale"), ("pale", "bake")]
for s1, s2 in test_cases:
    is_one_edit_away = string_editor.one_edit_away(s1, s2)

    print(f"s1: {s1}, s2: {s2}, is_one_edit_away: {is_one_edit_away}")
