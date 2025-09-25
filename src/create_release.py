

import time

with open('src/proofs_of_concept.txt', 'a') as f:  # 'a' mode for appending
    f.write('\n# Release created at \n' + time.ctime())
