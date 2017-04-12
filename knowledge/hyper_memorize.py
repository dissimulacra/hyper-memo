import numpy as np
import time
import tinydb

def main():
	print "starting up..."
	dbs = map(lambda s: s.lower(), available_dbs())
	print "specify db or make [new] one: "
	for db in dbs:
		print db
	print '[new]'
	db_choice = raw_input('--> ').lower()

	# TODO: catch naming errors here, mention if existing or new one is being created
	db = TinyDB(db_choice+'.json')
	# TODO: print summary statistics about db

	# TODO: perpetuate db to tmp folder backup storage before closing program
	
	# TODO: proper directory structure

	# TODO: jupyter notebook to do direct db exploration



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
		# QUESTION: incremental changes, or big change?
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