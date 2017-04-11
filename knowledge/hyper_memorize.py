import numpy as np
import time
import tinydb

def main():
	pass




# change record for each field change
# i.e. redundid, field, old_value, new_value

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
		# QUESTION: incremental changes, or big change?
		db.update(new_block, Block.redundid == redundid)
	else:
		db.insert(record)

def block_from_db(db, timestamp):
	# TODO: find all cards due today from start_ts and interval and timestamp
	dayseconds = 60 * 60 * 24
	pass

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