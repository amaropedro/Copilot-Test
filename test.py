# caramba que biblioteca massa.
# até sugestões de comentario ele faz, caraca.
import re
# importou uma biblioteca que eu não tinha, sem me avisar que eu não tinha... deveria?
import matplotlib.pyplot as plt

def plot_function(x, y, title):
    plt.axhline(0, color='black', linestyle='dotted')
    plt.axvline(0, color='black', linestyle='dotted')
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def parse_coef(coef):
    if coef == '':
        return 1
    return int(coef)

def parse_const(const):
    if const == '':
        return 0
    return int(const)

def handle_range(start, end):
    if start <= end:
        return list(range(start, end + 1))
    else:
        raise ValueError("Invalid range. Start value must be less or equal to end value.")

def parse_input(input_str: str, range: list):
    x = []
    y = []
    title = 'Plot of ' + input_str

    range = handle_range(range[0], range[1])

    # Extract coefficients and exponents using regular expressions
    match = re.match(r'y\s*=\s*(\d*)\s*x\s*\+\s*(\d*)', input_str)
    if match:
        coefficient = parse_coef(match.group(1))
        constant = parse_const(match.group(2))

        for i in range:
            x.append(i)
            y.append(coefficient * i + constant)
    else:
        match = re.match(r'y\s*=\s*(\d*)\s*x\s*-\s*(\d*)', input_str)
        if match:
            coefficient = parse_coef(match.group(1))
            constant = parse_const(match.group(2))

            for i in range:
                x.append(i)
                y.append(coefficient * i - constant)
        else:
            match = re.match(r'y\s*=\s*x\^(\d*)', input_str)
            if match:
                exponent = int(match.group(1))
                for i in range:
                    x.append(i)
                    y.append(i ** exponent)
            else:
                # add more regular expressions here, such as y = x, y = -x, y = mx^c, etc.
                # need to deal with flot values as well
                raise ValueError("Invalid input format. Please provide a valid function in the format 'y = mx + c' or 'y = x^c'.")

    print('match, type:', match)
    plot_function(x, y, title)

# Example usage
function_input = 'y = x^3'
function_range = [-10, 10]
parse_input(function_input, function_range)
