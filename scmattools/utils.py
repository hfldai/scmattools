# utils functions for file io
import re

def split_region(region):
        region_split = re.split('[\W_+]', region)
        contig, start, end = region_split[:3] # ignore other fields. Overlapping ignoring strandness (TO DO: consider strandness?)
        start = int(start)
        end = int(end)
        return contig, start, end

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
        Re-index a numeric list with missing values removed (assuming both are unique and sorted ascendingly):
        Ex:
                input: original:[1,2,3,4,5], actual:[2,4];
                return: {2:1,4:2}
        """
        reindex = {v:(i+base) for i,v in enumerate(actual)}
        return reindex
