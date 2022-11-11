from copyreg import pickle
import copy
from pysmt.fnode import *
import pickle
import time
import sys
from btorparser import *


def main():


  btor_parser = BTOR2Parser()
  sts, _ = btor_parser.parse_file(Path("/data/wenjifang/WASIM/design/testcase1-simple_MAC/simple_MAC.btor2"))

  print(sts.input_var)
  print(sts.state_var)
  print(sts.sv_update)
  print(sts.trans.serialize())
  

if __name__ == '__main__':
  main()



