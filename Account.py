class bankAccount:
  def_init_(self,Account _number,account _holder_name,initial_balance=0.0):
    self._account _number =account_number
    self._account_holder_name=account _holder_name 
    self._account _balance =initial_balance 
  def deposit(self,account):
  if amount >0:
    self._account_balance +=amount 
    print ("deposited{}.New balance:₹{}".format(Account,self._account_balance ))
  else:
    print("invalid deposit amount. please deposit a positive amount.")
    def withdraw(self,amount):
    if amount >0and amount <=self._Account balance:
     self._account _balance-=amount 
     print ("withdraw₹{}.New balance:₹{}".format(amount,self._account _balance ))
  else:
  print ("invalid withdrawl amount  or insufficient balance.")
  def display _balance (self):
    print ("Account balance for{}(account #₹{}):₹{}".format(self. account_holder_name,self._accout_balance,self._accout_balance))
account =bankaccount(account _number="123456789",Account _holder_name ="hari prabu",initial_balance =5000.0)
account. display _balance ()
account. deposit (500.0)
account. withdraw (200.0)
account. withdraw (20000.0)
account. display _balance ()


                  

