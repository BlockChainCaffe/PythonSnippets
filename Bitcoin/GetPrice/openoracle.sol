pragma solidity ^0.5.10

contract openoracle {
    
    address private smartContractOwner;

    string  public  description;    // What are we measuring? bitcoin? gold?
    uint    private value;          // Last recorded value
    uint    private decimals;       // number of decimals in the recorded value
    uint    private samples;        // number of sample values used in last measurement
    string  private mode;           // measuring mode
    uint    private timestamp;      // date supplied during write
    uint    private blocktime;      // date provided by blockchain 

    //-------------------------------------------------------------------------
    //    Modifiers
    //-------------------------------------------------------------------------

    // @dev Revert if the caller is not the owner.t
    modifier onlyOwner () {
        require (msg.sender == smartContractOwner, "Not contract owner");
        _;
    }

    //-------------------------------------------------------------------------
    //  Constructor
    //-------------------------------------------------------------------------

    // @param _contractId Id of the contract.
    // @param _mit main Item contract whose family will be tracked here
    constructor(string _description) public {
        smartContractOwner = msg.sender;
        description = _description;
    }

    //-------------------------------------------------------------------------
    //  Methods
    //-------------------------------------------------------------------------

    // Update the last value
    function update(uint _value, uint _decimals, string _mode, uint _saples, uint _timestamp) public onlyOwner {
        value = _value;    
        decimals = _decimals; 
        mode = _mode;     
        samples = _samples;  
        timestamp = _timestamp;
        blocktime = block.timestamp;
    }

    // Return the last stored value
    function read() public view returns (
        uint    _value,     
        uint    _decimals,  
        uint    _samples,   
        string  _mode,      
        uint    _timestamp, 
        uint    _blocktime
    )
    {
        _value    = value;   
        _decimals = decimals;
        _samples  = samples; 
        _mode     = mode;    
        _timestamp= timestamp;
        _blocktime= blocktime;
    }

    //-------------------------------------------------------------------------
    //  "Harakiri"
    //-------------------------------------------------------------------------

    function destroy() public onlyOwner {
        selfdestruct(smartContractOwner);
    }    
}


