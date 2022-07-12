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

        :param proof: hash current block
        :param previous_hash: hash previous block
        :return: new block created
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }

        return block
