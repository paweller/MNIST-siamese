IMAGE_WIDTH = 28
IMAGE_HEIGHT = 28
CHANNELS = 1
INPUT_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT, CHANNELS)

MARGIN = 1
EMBEDDING_SIZE = 30
LR = 0.0004
SEMI_HARD_IMG_COUNT = 500

NUM_CLASSES = 10
TRAIN_TRIPLES = NUM_CLASSES * (NUM_CLASSES - 1) * 64
EPOCHS = 15
EPOCHS_PER_BATCH = 10
BATCH_SIZE = 32
