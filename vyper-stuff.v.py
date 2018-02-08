# Talk Plan:
# 1. Quick intro to design philosophy of Vyper
# 2. Explain basic solidity contract
# 3. Do it live (translation to Vyper) 


someUint: public(num256) # should be snake_case if we're trying to win style points
someInt: public(num) # !!! implicit
# someBytes: private(bytes32) # Base type with units can only be num, decimal
# exampleString = ""

# Defining a struct. 
User: {
    joinedTime: timestamp,
    isActive: bool,
}

addrArray: address[10]
addrCount: num
# userMap: public( User[address] ) # ????
# userArray: [timestamp,bool][10] # ???? 
userTimesArray: timestamp[10]
userBoolArray: bool[10]

@public
def __init__(_someUint: num256, _someInt: num):
    self.someUint = _someUint
    self.someInt = _someInt

@public 
def newUser():
    self.addrCount = self.addrCount + 1
    i = self.addrCount
    self.addrArray[i]       = msg.sender
    # self.userArray[i] = [block.timestamp,1] #  Typecasting from base type num(sec, positional) to num unavailable
    self.userTimesArray[i]  = block.timestamp
    self.userBoolArray[i]   = true
    
    
@public
def thingReturner(i: num) -> (address, timestamp, bool):
    addr = self.addrArray[i]
    # self.userArray[i] = [block.timestamp,1] # x` Typecasting from base type num(sec, positional) to num unavailable
    time = self.userTimesArray[i]  
    status = self.userBoolArray[i]
    return (addr, time, status)

@public
@constant
def howLongSinceJoined(i: num) -> (timedelta):
    delta = block.timestamp - self.userTimesArray[i]
    return delta




    
    
    
    
    
    