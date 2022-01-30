import mat2mat
import argparse

def cli():
        parser = argparse.ArgumentParser()
        parser.add_argument('rq', type=str, help='path to query region intervals (make sure the file is Tab separated')
        parser.add_argument('cq', type=str, help='path to query cell names (make sure the file is Tab separated')
        parser.add_argument('matq', type=str, help='path to query region x cell sparse count matrix (.mtx)')
        parser.add_argument('rt', type=str, help='path to target regions')
        parser.add_argument('-o', '--output', type=str, default="output/", help='path to output directory')
        parser.add_argument('-actual_rt', type=str, default="target.regions", help='path to the output actual regions')
        parser.add_argument('-actual_ct', type=str, default="target.cells", help='path to the output actual target cells')
        parser.add_argument('-matt', type=str, default="target.mtx", help='path to the output target region x cell sparse count matrix (.mtx)')

        parsed, _ = parser.parse_known_args()
        mat2mat.main(parsed.rq, parsed.cq, parsed.matq, parsed.rt, parsed.matt, parsed.actual_rt, parsed.actual_ct, parsed.output)
