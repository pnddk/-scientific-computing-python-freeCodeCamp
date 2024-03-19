class Category:
  # Initialize Object and Create Ledger List
  def __init__(self, category):
    self.category = category
    self.ledger = []
  
  # Create Outline for Category and Print out Amounts and Balance  
  def __str__(self):
    output = self.category.center(30, "*") + "\n"
    for entry in self.ledger:
      output += f"{entry['description'][:23]:23}{entry['amount']:>7.2f}\n"
    output += f"Total: {self.get_balance():.2f}"
    return output  
  
  # Deposit Method  
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

  # Withdraw Method
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  # Get Balance Method
  def get_balance(self):
     return sum(entry["amount"] for entry in self.ledger)

  # Transfer Method
  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category.category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
      return True
    return False

  # Check Funds Method
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True

# Create Spend Chart Function    
def create_spend_chart(categories):
  spend = []
  for category in categories:
    spend.append(sum(entry["amount"] for entry in category.ledger if entry["amount"] < 0))
  total = sum(spend)
  percentages = [int(100 * amount / total) for amount in spend]
  output = "Percentage spent by category\n"

  # Create Bar Chart
  for i in range(100, -1, -10):
    output += f"{i:3}| "
    for percentage in percentages:
      output += "o  " if percentage >= i else "   "
    output += "\n"
  output += "    ----------"

  # Create Category Names (X-Axis) and add Necessary Spaces
  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  for index_1 in range(max_length):
    output += "\n    "
    for index_2 in range(len(categories)):
      if index_1 < cat_length[index_2]:
        output += " " + categories[index_2].category[index_1] + " "
      else:
        output += "   "
    output += " "

  return output
