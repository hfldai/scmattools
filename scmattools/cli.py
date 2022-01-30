import scmattools
import argparse

def cli():
        parser = argparse.ArgumentParser()
        parser.add_argument('rq', type=str, help='path to query region intervals (make sure the file is Tab separated)')
        parser.add_argument('cq', type=str, help='path to query cell names')
        parser.add_argument('matq', type=str, help='path to query rq x cq sparse count matrix (.mtx)')
        parser.add_argument('rt', type=str, help='path to target region intervals (make sure the file is Tab separated)')
        parser.add_argument('-o', '--output', type=str, default="output/", help='path to output directory')
        parser.add_argument('-ort', '--output_rt', type=str, default="target.regions", help='path to the output target region intervals')
        parser.add_argument('-oct', '--output_ct', type=str, default="target.cells", help='path to the output target cell names')
        parser.add_argument('-omatt', '--output_matt', type=str, default="target.mtx", help='path to the output target region x cell sparse count matrix (.mtx)')

        parsed, _ = parser.parse_known_args()
        scmattools.mat2mat(parsed.rq, parsed.cq, parsed.matq, parsed.rt, parsed.output_matt, parsed.output_rt, parsed.output_ct, parsed.output)
