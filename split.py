val_pct = 0.2
def split_indices(n, val_pct):
  # Determine the size of validation set
  n_val = int(n*val_pct)
  # Create the random permutation of 0 to n-1
  idxs = np.random.permutation(n)
  # Pick first n_val indices for validation set
  return idxs[n_val:], idxs[:n_val]