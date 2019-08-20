# Lesson 8 of Calculator Course


# Separates an input line using a list of separators
# Iterates over the input line character by character until an operator is found. At that point,
# the slice from the previous separator to the current one is appened to the output list,
# along with the current separator. After iteration is complete, the slice after the last operator is appended
# At every append operation, strip method is applied to get rid of whitespace
def separate_input(input_line, separators):
    output = []

    # Iterating over input line by index
    start = 0
    stop = 0
    while stop < len(input_line):
        # Checks to see if current character is operator
        if input_line[stop] in separators:
            # Appending proper terms
            output.append(input_line[start: stop].strip())
            output.append(input_line[stop].strip())
            # Incrementing counters
            stop += 1
            start = stop
        stop += 1

    # Appending final term
    output.append(input_line[start: stop + 1].strip())
    return output