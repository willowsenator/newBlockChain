import datetime
import hashlib
import json

from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok


# Blockchain creation

class BlockChain:
    def __init__(self):
        """
            Blockchain Contructor
        """
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        """
            Create a new block

        :param proof: nonce current block
        :param previous_hash: hash previous block
        :return: new block created
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }

        self.chain.append(block)
        return block

    def get_last_block(self):
        """
            Get last block of blockchain

        :return: last block of blockchain
        """

        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
            POW(Proof of works consensus protocol)

        :param previous_proof: previous nonce
        :return: new nonce
        """

        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof
