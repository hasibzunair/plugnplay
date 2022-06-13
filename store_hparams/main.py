from config import *

# See https://twitter.com/kagglingdieter/status/1531155343505489920 for details
# Also see https://github.com/DrSleep/light-weight-refinenet/blob/master/src/train.py
# And https://github.com/google/ml_collections

assert type(DATA_DIR) == str, f"Should be a path to dataset, got: {type(DATA_DIR)}"
assert type(LR) == float, f"Should be a float, got: {type(LR)}"

print(f"Path to data is at {DATA_DIR}.\n")
print(f"Pretraining is {PRETRAINED}.\n")
print(f"Optimizer is {OPTIM}.\n")


# TODO
# Add argparse