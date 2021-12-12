# part A


def matching_paren(inp):
    score = 0

    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

    for line in inp:
        stack = {"(": 0, "[": 0, "{": 0, "<": 0}
        opening_brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
        closing_brackets = {")": "(", "]": "[", "}": "{", ">": "<"}
        last_bracket = []
        for char in line:
            if char in opening_brackets:
                stack[char] += 1
                last_bracket.append(char)
            if char in closing_brackets:
                if stack[closing_brackets[char]] == 0:
                    score += scores[char]
                    break
                if char != opening_brackets[last_bracket[-1]]:
                    score += scores[char]
                    break
                else:
                    stack[closing_brackets[char]] -= 1
                    last_bracket.pop()

    return score


if __name__ == "__main__":
    with open("day10.txt") as file:
        inp = file.readlines()
        inp = [line.strip() for line in inp]
        print(matching_paren(inp))
