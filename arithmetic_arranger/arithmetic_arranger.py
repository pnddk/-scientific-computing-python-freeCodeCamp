MAXNUMPROB = 5
MAXDIGITS = 4

def arithmetic_arranger(problems, results = False):
  length = []
  dashes = []
  
  top_line = ""
  mid_line = ""
  dash_line = ""
  result_line = ""

  if len(problems) > MAXNUMPROB:
      return("Error: Too many problems.")

  for arithmetic in problems:
    values = arithmetic.split()

    num1 = values[0]
    op = values[1]
    num2 = values[2]

    if not (num1.isnumeric() and num2.isnumeric()):
        return("Error: Numbers must only contain digits.")

    if len(num1) > MAXDIGITS or len(num2) > MAXDIGITS:
        return("Error: Numbers cannot be more than four digits.")

    if op != "+" and op != "-":
        return("Error: Operator must be '+' or '-'.")
    
    # Calculates result
    if op == "+":
      result = str(int(num1) + int(num2))
    else:
      result = str(int(num1) - int(num2))

    # Calculate lengths and dashes
    longerNum = max(len(num1), len(num2))
    num_dashes = longerNum + 2
    dashes.append("-" * num_dashes)
    length.append(num_dashes)

    # Calculate spacers for alignment
    spacers = length[-1] - len(num1)

    # Build lines for arrangement
    top_line += " " * spacers + num1 + "    "
    mid_line += op + " " * (length[-1] - len(num2) - 1) + num2 + "    "
    dash_line += dashes[-1] + "    "
    result_line += " " * (length[-1] - len(str(result))) + result + "    "

  arranged_problems = top_line.rstrip() + "\n" + mid_line.rstrip() + "\n" + dash_line.rstrip()
  
  if results:
    arranged_problems += '\n' + result_line.rstrip()

  return arranged_problems
