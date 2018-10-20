# initializing our blockchain list
MINING_REWARD = 10

gensis_block = {
    "previous_hash": '',
    "index": 0,
    "transactions": []
}
blockchain = [gensis_block]
open_transactions = []
owner = "Colin"
participants = {"Colin"}


def hash_block(block):
    return "-".join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx["amount"] for tx in block["transactions"]
                  if tx["sender"] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx["amount"] for tx in block["transactions"]
                     if tx["recipient"] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def get_last_blockchain_value():
    """Returns the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction['amount']


def add_data(recipient, sender=owner, amount=1.0):
    """Appned a new value as well as the last blockchain value in the blockchain

    Arguments:
     :sender: the sender of data
     :recipient:The recipient of the data
     :amount: The value of the data being passed

    """

    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": copied_transactions
    }
    blockchain.append(block)
    return True


def get_data_input():
    """Returns the input of the user (a new transaction amount) as a float """
    tx_recipient = input("Enter the recipent of the data: ")
    tx_amount = float(input('Data value being passed: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print("Outputting Block")
        print(block)
    else:
        print("-" * 20)


def verify_chain():
    # block_index = 0
    """Verify the current blockchain and return True if it's valid, False if not valid"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True


def verify_data():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    print("Please choose:")
    print("1: Add a new data point")
    print("2: Mine a new block")
    print("3: See a list of all data")
    print("4: Output participants")
    print("5: Check data validity")
    print("h: Manipulate chain")
    print("q: quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_data_input()
        recipient, amount = tx_data
        if add_data(recipient, amount=amount):
            print('Added data')
        else:
            print("Transaction failed")
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == '5':
        if verify_data():
            print('All Transactions are vailid')
        else:
            print('There are invalid transactions')
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": '',
                "index": 0,
                "transactions": [{"sender": "Morgan", "recipient": "Colin", "amount": 100}]
            }
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Input is invalid, please enter 1 or 2")
    if not verify_chain():
        print_blockchain_elements()
        print("invalid chain")
        break
    print(get_balance("Colin"))
print("Done")
