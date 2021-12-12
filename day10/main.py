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


# part B


def autocomplete(inp):
    total_scores = []
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    opening_brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
    closing_brackets = {")": "(", "]": "[", "}": "{", ">": "<"}

    for line in inp:
        valid_line = True
        stack = {"(": 0, "[": 0, "{": 0, "<": 0}
        last_bracket = []
        for char in line:
            if char in opening_brackets:
                stack[char] += 1
                last_bracket.append(char)
            if char in closing_brackets:
                if (
                    stack[closing_brackets[char]] == 0
                    or char != opening_brackets[last_bracket[-1]]
                ):
                    valid_line = False
                else:
                    stack[closing_brackets[char]] -= 1
                    last_bracket.pop()

        # autocomplete
        if valid_line:
            line_score = 0
            for bracket in reversed(last_bracket):
                new_score = line_score * 5
                new_score += scores[opening_brackets[bracket]]
                last_bracket.pop()
                line_score = new_score
            total_scores.append(line_score)

    sorted_scores = sorted(total_scores)
    middleIndex = (len(sorted_scores) - 1) / 2
    return sorted_scores[int(middleIndex)]


if __name__ == "__main__":
    with open("day10.txt") as file:
        inp = file.readlines()
        inp = [line.strip() for line in inp]
        # print(matching_paren(inp))
        print(autocomplete(inp))
