def longestSubstring(input_string):
    longest = ""
    substring = ""
    for i in range(len(input_string)-1):
        if input_string[i] <= input_string[i+1]:
            substring += input_string[i]
        else:
            substring += input_string[i]
            if len(substring) > len(longest):
                longest = substring
            substring = ""

    substring += input_string[-1]
    if len(substring) > len(longest):
        longest = substring
    return longest

print(longestSubstring("abdulrhman"))
