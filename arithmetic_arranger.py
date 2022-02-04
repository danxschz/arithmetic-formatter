# Arithmetic Formatter -- Scientific Computing with Python Project #1 

## Main function
def arithmetic_arranger(problems, showresults = False):

  # Verify correct format of problems
  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    if "*" in problem or "/" in problem:
      return "Error: Operator must be '+' or '-'."

  for problem in problems:
    factors = problem.split()
    if factors[0].isdigit() is False or factors[2].isdigit() is False:
      return "Error: Numbers must only contain digits."
    if len(factors[0]) > 4 or len(factors[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

  # Arrange problems
  arrangedtop = None
  arrangedbottom = None
  dasheslist = list()
  for problem in problems:
    factors = problem.split()
    firstval = factors[0]
    sign = factors[1]
    secondval = factors[2]

    if len(firstval) > len(secondval):
      space = (len(firstval) - len(secondval)) * " "
      if arrangedtop is None:
        arrangedtop = f"  {firstval}" # 2 spaces so it's arranged to the right
        arrangedbottom = f"{sign} {space}{secondval}" # Extra space considers the lenght difference so that both values are arranged to the right
      else:
        arrangedtop += f"      {firstval}" # 6 spaces so it's arranged to the right
        arrangedbottom += f"    {sign} {space}{secondval}"

    if len(secondval) > len(firstval):
      space = (len(secondval) - len(firstval)) * " "
      if arrangedtop is None:
        arrangedtop = f"  {space}{firstval}"
        arrangedbottom = f"{sign} {secondval}"
      else:
        arrangedtop += f"      {space}{firstval}"
        arrangedbottom += f"    {sign} {secondval}"

    if len(firstval) == len(secondval):
      if arrangedtop is None:
        arrangedtop = f"  {firstval}"
        arrangedbottom = f"{sign} {secondval}"
      else:
        arrangedtop += f"      {firstval}"
        arrangedbottom += f"    {sign} {secondval}"

    # Store the number of dashes for each problem
    longestval = max(len(firstval), len(secondval))
    dashnumber = longestval + 2
    dasheslist.append(dashnumber)

  # Arrange dashes string
  dashstr = None
  for dashnumber in dasheslist:
    dashes = dashnumber * "-"
    if dashstr is None:
      dashstr = dashes
    else:
      dashstr += f"    {dashes}"

  # Calculate results
  if showresults is True:
    resultlist = list()
    for problem in problems:
      factors = problem.split()
      firstval = int(factors[0])
      sign = factors[1]
      secondval = int(factors[2])
      if sign == "+":
        result = str(firstval + secondval)
      if sign == "-":
        result = str(firstval - secondval)
      resultlist.append(result)

    # Arrange results string
    n = 0
    resultstr = None
    for result in resultlist:
      if resultstr is None:
        resultstr = result.rjust(dasheslist[n])
      else:
        resultstr += f"    {result.rjust(dasheslist[n])}"
      n += 1

  # Assemble full string
  arrangedtop += "\n"
  arrangedbottom += "\n"

  if showresults is True:
    dashstr += "\n"
    arranged_problems = arrangedtop + arrangedbottom + dashstr + resultstr
    return arranged_problems

  arranged_problems = arrangedtop + arrangedbottom + dashstr
  return arranged_problems
