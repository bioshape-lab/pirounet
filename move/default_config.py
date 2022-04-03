"""Default configuration parameters."""

batch_size = 8
learning_rate = 3e-4
epochs = 20
# TODO: check how seq_len is used: could be inconsistent
seq_len = 128
negative_slope = 0  # LeakyRelu
kl_weight = 0