import os, unittest
import scmattools

class Test(unittest.TestCase):
	def test_main(self):
		rq = "tests/test_data/test.query.regions"
		cq = "tests/test_data/test.query.cells"
		matq = "tests/test_data/test.query.mtx"
		rt = "tests/test_data/test.target.regions" 
		output = "tests/test_output/"
		output_rt = "target.regions"
		output_ct = "target.cells"
		output_matt = "target.mtx"
		scmattools.mat2mat(rq, cq, matq, rt, output_matt, output_rt, output_ct, output)

		target_rt = 'chr1\t10004036\t10005259\nchr1\t100102486\t100102490\nchr1\t100102510\t100102520\nchr1\t100102524\t100102600\nchr2\t10011487\t10011592\nchr7\t100155100\t100155230' 
		target_ct = 'cell1\ncell2\ncell3\ncell4\ncell5\ncell7\ncell9\ncell10\ncell11\ncell12\ncell13'
		target_matt = '%%MatrixMarket matrix coordinate integer general\n6 11 38\n1 2 1\n1 4 1\n1 8 1\n1 9 1\n2 2 1\n2 4 1\n2 8 1\n2 9 1\n3 3 2\n3 7 1\n3 10 5\n4 3 2\n4 7 1\n4 10 5\n5 3 2\n5 7 1\n5 10 5\n6 1 1\n6 5 2\n6 6 2\n6 11 1\n'
		with open(os.path.join(output, output_rt)) as f:
			actual = "".join(f.readlines())
			self.assertEqual(actual, target_rt)
		with open(os.path.join(output, output_ct)) as f:
			actual = "".join(f.readlines())
			self.assertEqual(actual, target_ct)
		with open(os.path.join(output, output_matt)) as f:
			actual = "".join(f.readlines())
			self.assertEqual(actual, target_matt)


if __name__ == '__main__':
	unittest.main()
