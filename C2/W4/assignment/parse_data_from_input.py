# GRADED FUNCTION: parse_data_from_input
def parse_data_from_input(filename):
  """
  Parses the images and labels from a CSV file
  
  Args:
    filename (string): path to the CSV file
    
  Returns:
    images, labels: tuple of numpy arrays containing the images and labels
  """
  with open(filename) as file:
    ### START CODE HERE

    # Use csv.reader, passing in the appropriate delimiter
    # Remember that csv.reader can be iterated and returns one line in each iteration

    '''
    a = np.loadtxt( filename, delimiter=',', skiprows=1 )
    num_rows, num_cols = a.shape
    labels = a[ :, 0  ]
    images = a[ :, 1: ]
    images = np.reshape( images, ( num_rows ,28, 28) )
    '''

    csv_reader = csv.reader(file, delimiter=',')

    labels = []
    images = []

    next( csv_reader )

    for row in csv_reader:
      lbl = row[ 0  ]
      img = row[ 1: ]
      img = np.reshape( img, (28, 28) )
      labels.append( lbl )
      images.append( img )


    labels = np.array( labels ).astype( np.float64 )
    images = np.array( images ).astype( np.float64 )
    
    
    ### END CODE HERE

    return images, labels
