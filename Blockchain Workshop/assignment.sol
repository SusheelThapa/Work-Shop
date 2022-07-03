// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract EventTickets {
    struct Event {
        string name;
        string website_url;
        uint256 total_tickets;
        uint256 tickets_sold;
        address buyer;
        mapping(address => uint256) ticket_purchased;
        bool isOpen;
    }

    Event e;

    address public owner;
    address payable owner_wallet;

    uint256 TICKET_PRICE = 1 ether;

    /*Events*/
    event LogBuyTickets(address indexed _buyer, uint256 _ticket_purchased);

    event LogGetRefund(
        address indexed _refund_requested,
        uint256 _ticket_to_refund
    );

    event LogEndSale(address _owner, uint256 _transfer_balance);

    /*Modifier*/
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can access this function");
        _;
    }

    modifier onlyEventOpen() {
        require(e.isOpen == true, "Event hasn't started yet");
        _;
    }

    /*Constructor*/
    constructor(
        string memory _event_name,
        string memory _url,
        uint256 _total_tickets,
        address payable _wallet
    ) {
        e.name = _event_name;
        e.website_url = _url;
        e.total_tickets = _total_tickets;
        e.tickets_sold = 0;
        e.isOpen = true;

        owner = msg.sender;
        owner_wallet = _wallet;
    }

    function readEvent()
        public
        view
        returns (
            string memory name,
            string memory website,
            uint256 totalTickets,
            uint256 sales,
            bool isOpen
        )
    {
        return (
            e.name,
            e.website_url,
            e.total_tickets,
            e.tickets_sold,
            e.isOpen
        );
    }

    function getBuyerTicketCount(address buyer_address)
        public
        view
        returns (uint256)
    {
        return e.ticket_purchased[buyer_address];
    }

    function buyTicket(uint256 number_of_ticket) public payable onlyEventOpen {
        /*Checking enough number of tickets*/
        require(
            number_of_ticket <= (e.total_tickets - e.tickets_sold),
            "Not enough ticket to purchased"
        );

        /*Checking enough transaction value*/
        require(
            (number_of_ticket * TICKET_PRICE) <= msg.value,
            "Not enough ether for the transaction"
        );

        /*Purchaing the ticket*/
        e.ticket_purchased[msg.sender] += number_of_ticket;
        e.tickets_sold += number_of_ticket;

        /*Transfering ether to the owner wallet*/
        owner_wallet.transfer(TICKET_PRICE * number_of_ticket);

        /*Refunding the excess money*/
        payable(msg.sender).transfer(
            msg.value - TICKET_PRICE * number_of_ticket
        );

        /*Emiting the events*/
        emit LogBuyTickets(msg.sender, number_of_ticket);
    }

    function getRefund(
        uint256 _number_of_ticket_to_refund,
        address refund_requester,
        address payable refund_wallet_address
    ) public payable onlyOwner {
        /*Checking if s/he has purchased the ticket or not*/
        require(
            e.ticket_purchased[refund_requester] >= _number_of_ticket_to_refund,
            "You haven't purchased that much tickets"
        );

        /*Updating our state variable*/
        e.tickets_sold -= _number_of_ticket_to_refund;
        e.ticket_purchased[
            refund_requester
        ] -= _number_of_ticket_to_refund;

        /*Refunding ehther to the person who have asked refund*/
        payable(refund_wallet_address).transfer(
            _number_of_ticket_to_refund * TICKET_PRICE
        );

        /*Refunding excess money in owner_wallet*/
        owner_wallet.transfer(
            msg.value - _number_of_ticket_to_refund * TICKET_PRICE
        );

        /*Log messages*/
        emit LogGetRefund(msg.sender, _number_of_ticket_to_refund);
    }

    function endSale() public onlyOwner {
        /*Changing the isopen flag*/
        e.isOpen = false;

        /*Log messages*/
        emit LogEndSale(owner, TICKET_PRICE * e.tickets_sold);
    }
}
