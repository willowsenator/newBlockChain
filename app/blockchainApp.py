from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok

from model.blockchain import BlockChain

app = Flask(__name__)
run_with_ngrok(app)

blockchain = BlockChain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    """ Mining a block """
    previous_block = blockchain.get_last_block()
    previous_proof = previous_block['proof']
    current_proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    current_block = blockchain.create_block(current_proof, previous_hash)

    response = {
        'message': 'Congratulations!! You have mined a block',
        'index': current_block['index'],
        'timestamp': current_block['timestamp'],
        'proof': current_block['proof'],
        'previous_hash': current_block['previous_hash']
    }
    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    """Get blockchain"""
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    """ Check if the blockchain is valid"""
    if blockchain.is_chain_valid(blockchain.chain):
        response = {'message': 'THE BLOCKCHAIN IS VALID'}
    else:
        response = {'message': 'THE BLOCKCHAIN IS NOT VALID'}

    return jsonify(response), 200


app.run()
