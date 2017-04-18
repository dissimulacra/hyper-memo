import numpy as np
import random
import re
import time
import tinydb

def main():
	print "starting up..."
	dbs = map(lambda s: s.lower(), available_dbs())
	print "specify [db] or make a new one by typing a new name: "
	for db in dbs:
		print db
	db_choice = raw_input('--> ').lower()
	db_string = None

	check = '[a-zA-Z_][a-zA-Z0-9_]*'
	if (len(re.findall(check, db_choice)) != 1) or (re.findall(check, db_choice) != db_choice):
		raise NameError('Not a valid name!')
	else: 
		db_string = db_choice + '.json'
		if db_string in os.listdir('.'):
			print 'Loading ' + db_string + ', coming right up!'
		else:
			print 'Creating a new db called ' + db_string + ', coming right up!'
	# FUTURE: this might be an opaque process automatically managed depending on knowledge type
	db = TinyDB(db_string)

	# TODO: print summary statistics about db

	# TODO: perpetuate db to tmp folder backup storage before closing program
	
	# TODO: proper directory structure

	# TODO: jupyter notebook to do direct db exploration

	# TODO: interleave different topics together for more random learning

	# TODO: multiple level review rotation? for instance multi example answers rotated each time, to prevent overfitting

	# TODO: convolutional neural net fed picture of text and spits out exact text, spaces, color?

	# TODO: system randomly and automatically surveys you, i.e. "is this card really useful?", to help with retirement

	# TODO: special format cards: in how to measure anything, we do confidence interval calibration
	# by having a bank of pre-known distributions (normal) and then the card asks to estimate the 
	# upper and lower bound (reminding of bet and other strategies), and keeps track of calibration 
	# over time; random distribution given each time; expected value of perfect information;
	# different special rules for small sized sampling

	# TODO: special format cards: for mental math, random problems generated for selected techniques 
	# with interactive hints given out when appropriate to remind of shortcut strategies

	# TODO: look into ways of storing time series data in databases, such as the following:
	# https://www.mongodb.com/blog/post/schema-design-for-time-series-data-in-mongodb

	# PRIORITY TODO: since developing different learning schemes and database ingestion will
	# take some time, focus on the (1) scheduling algorithm (2) factor calculation and disrupting 
	# learning interference and (3) the testing procedure and game playing process



def available_dbs(directory='.'):


def block_into_db(db, block):
	old_block = None
	new_block = block.inspect()

	redundid = new_block['redundid']

	Block = tinydb.Query()
	
	result = db.search(Block.redundid == redundid)

	if len(result) == 0:
		pass
	if len(result) == 1:
		old_block = result[0]
	if len(result) >= 2:
		pass # TODO: big error!

	if old_block:
		# insert_change + update
		for new_key, new_val in new_block.items():
			if old_block[new_key] not new_val:
				insert_change(db, redundid, new_key, old_block[new_key], new_val)
		db.update(new_block, Block.redundid == redundid)
	else:
		db.insert(record)

def block_for_now(db, ts):
	minimum_hr = 16
	dayseconds = 60 * 60 * 24
	hrsseconds = float(60 * 60)
	Block = Query()
	today_blocks = []
	valid_blocks = db.get(Block.start_ts > 0)
	for block_info in valid_blocks:
		start_ts = block_info['start_ts']
		interval = block_info['interval']

		if ((ts - start_ts) / hrsseconds) > minimum_hr:
			if (((ts - start_ts) / dayseconds) + 1) >= interval:
				memblock = MemoryBlock()
				memblock.initize(block_info)
				today_blocks.append(memblock)
	random.shuffle(today_blocks)
	return today_blocks

def insert_change(db, block_id, field, old_val, new_val):
	block_change = {'block_id' : block_id, 
			   		'field'    : field, 
			   		'old_val'  : old_val, 
			   		'new_val'  : new_val,
			   		'timestamp': int(time.time())}
	db.insert(block_change)

def insert_resp_q(db, block_id, qual):
	db.insert({'block_id': block_id, 'qual': qual, 'timestamp': int(time.time())})




if __name__ == '__main__':
	main()
	