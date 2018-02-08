pragma solidity ^0.4.18;

contract MyContract {

    uint public someNumber;
    bytes32 public someBytes;
    string private someString;

    struct User {
        uint joinedTime;
        bool isActive;
    }

    address[] public addrArray; 
    mapping(address => User) userMap;

    // constructor
    function MyContract(uint _someNumber, bytes32 _someBytes, string _someString) {
        someNumber = _someNumber;
        someBytes = _someBytes;
        someString = _someString;
    }
    
def __init__(_someNumber: num256, _someInt: timedelta):
    self.someNumber = _someNumber
    self.auction_end = self.auction_start + _someInt

    function newUser() public {
        User memory newUser;
        newUser.joinedTime = now;
        newUser.isActive = true;
        addrArray.push(msg.sender);
        userMap[msg.sender] = newUser;
    }

    function thingReturner(uint _thingNum) public returns(uint, bool) {
        address userAddr = addrArray[_thingNum];
        User memory user = userMap[userAddr];
        return (
            user.joinedTime,
            user.isActive
        );
    }

    function howLongSinceJoined(uint _thingNum) public returns(uint) {
        address userAddr = addrArray[_thingNum];
        User memory user = userMap[userAddr];
        return now - user.joinedTime; 
    }
}