class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        line = []
        line_length = 0

        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                if len(line) == 1:
                    output.append(line[0] + ' ' * (maxWidth - line_length))
                else:
                    total_spaces = maxWidth - line_length
                    extra_spaces = total_spaces % (len(line) - 1)
                    space_per_gap = total_spaces // (len(line) - 1)
                    line_text = ''
                    for i in range(len(line) - 1):
                        line_text += line[i]
                        line_text += ' ' * (space_per_gap + (1 if i < extra_spaces else 0))
                    line_text += line[-1]
                    output.append(line_text)
                line = [word]
                line_length = len(word)

        output.append(' '.join(line).ljust(maxWidth))
        return output