# given 1) a gene region a x cell count matrix and 2) a second region list b, 
# return: a new intersecting count matrix of region list b x cell

contigs = []

import os, re
from tqdm import tqdm
import pandas as pd
from pybedtools import BedTool

def split_region(region):
	region_split = re.split('[\W_+]', region)
	contig, start, end = region_split[:3] # ignore other fields. Overlapping ignoring strandness (TO DO: consider strandness?)
	start = int(start)
	end = int(end)
	return contig, start, end


def count_regions(counts_query, path_regions_query, path_regions_target):
	query = BedTool(path_regions_query)
	target = BedTool(path_regions_target)
	dict_reg_query_id = value2id(load_values(path_regions_query))
	dict_reg_target_id = value2id(load_values(path_regions_target))

	counts_target = {}
	cells_actual = []
	reg_cur = ''
	total = len(list(target.intersect(query, wa=True, wb=True)))
	for i, intersect in enumerate(tqdm(target.intersect(query, wa=True, wb=True), total=total, desc="calculating overlapped region counts for each cell")):
		reg_target = "\t".join(intersect.fields[:3])
		reg_query = "\t".join(intersect.fields[3:])
		rt_id = dict_reg_target_id[reg_target]
		rq_id = dict_reg_query_id[reg_query]

		if not reg_cur == reg_target:
			reg_cur = reg_target
			if not i==0:
				dic = dict(sorted(dic.items()))
				cells_actual += list(dic.keys())
				cells_actual = list(set(cells_actual))
				counts_target[rt_id] = dic
			dic = {}
		for cell in counts_query[rq_id].keys():
			if not (cell in dic.keys()):
				dic[cell] = counts_query[rq_id][cell]
			else:
				dic[cell] += counts_query[rq_id][cell]
	return cells_actual, counts_target
		
		

def id2value(values):
	return {(id+1):value for id, value in enumerate(values)}

def value2id(values):
        return {value:(id+1) for id, value in enumerate(values)}

def load_values(file):
	print("== loading: {} ==".format(file))
	with open(file,"r") as f:
		return [value.strip() for value in f.readlines()]

def load_count_mat(file):
	"""
	read sparse count matrix (row x col) into dict, with row ids as keys
	"""
	print("== loading sparse count matrix {} ==".format(file))
	with open(file, "r") as f:
		i_skip = 0
		for i, line in enumerate(f.readlines()):
			if line.startswith("%"):
				i_skip += 1
			elif i > i_skip:
				row_id, col_id, count = re.split('\W', line.strip())
				counts[int(row_id)][int(col_id)] = int(count)
			else:
				n_rows, n_cols, _ = re.split('\W', line.strip())
				counts = {(id+1):{} for id in range(int(n_rows))} # 1-indexed
	return counts
	
def reindex(actual, base=1):
	"""
	TODO: DOCUMENTATION
	Re-index a numeric list with missing values removed (assuming both are unique and sorted ascendingly):
	Ex: 
		input: original:[1,2,3,4,5], actual:[2,4];
		return: {2:1,4:2}
	"""
	reindex = {v:(i+base) for i,v in enumerate(actual)}
	return reindex	
	

def main(rq, cq, matq, rt, matt, actual_rt, actual_ct, output):
	dict_regions_target = id2value(load_values(rt))
	dict_cells_query = id2value(load_values(cq))
	counts_query = load_count_mat(matq)
	
	cells_actual, counts_target = count_regions(counts_query, rq, rt)
	cells_actual_keys = reindex(cells_actual)
	regions_actual_keys = reindex(list(counts_target.keys()))
	n_cells = len(cells_actual)
	n_regs_target = len(counts_target)
	# export actual cell ids and actual regions
	os.system("mkdir -p {}".format(output))
	print("== writing target regions ==".format(actual_rt))
	with open(os.path.join(output, actual_rt), "w") as f:
		f.write("\n".join([dict_regions_target[key] for key in regions_actual_keys.keys()]))
	print("== writing target sample names ==".format(actual_ct))
	with open(os.path.join(output, actual_ct), "w") as f:
		f.write("\n".join([dict_cells_query[key] for key in cells_actual]))
	# calculate sum of counts
	sum_counts_target = sum(sum(counts_target[reg].values()) for reg in counts_target.keys())
	print("== writing target sparse count matrix into {} ==".format(matt))
	with open(os.path.join(output, matt), "w") as f:
		f.write("%%MatrixMarket matrix coordinate integer general\n")
		f.write(f"{n_regs_target} {n_cells} {sum_counts_target}\n")
		for reg_ori in counts_target.keys():
			reg = regions_actual_keys[reg_ori]
			for cell_ori in counts_target[reg_ori].keys():
				count = counts_target[reg_ori][cell_ori]
				cell = cells_actual_keys[cell_ori]
				f.write(f"{reg} {cell} {count}\n")

