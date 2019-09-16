NUM_THREADS = 12
parameterOutputPlaceHolder = 6

# Tensor related parameters, please use the same values for creating tensor, model training and variant calling
# Please change below value(s) in the dataPrepScripts at the same time
flankingBaseNum = 16
matrixRow = 8
matrixNum = 4
bloscBlockSize = 500

# Model hyperparameters
trainBatchSize = 10000
predictBatchSize = 10000
initialLearningRate = 0.001
learningRateDecay = 0.1
maxLearningRateSwitch = 3
trainingDatasetPercentage = 0.9

# Clair specific
l2RegularizationLambda = 0.005
l2RegularizationLambdaDecay = 1
dropoutRateFC4 = 0.5
dropoutRateFC5 = 0.0
dropoutRate = 0.05
default_optimizer = "Adam"  # Adam / SGDM
default_loss_function = "FocalLoss"  # CrossEntropy / FocalLoss

# Cyclical learning rate param(s)
clr_max_lr = 3e-2
clr_min_lr = 1e-4
stepsizeConstant = 1
clrGamma = 0.95
momentum = 0.9
maxEpoch = 30

# Cyclical learning rate finder param(s)
min_lr = 1e-6
max_lr = 1e-1
lr_finder_max_epoch = 1

# random seed (None to make it random for every run)
# set to None because cuDNN may introduce additional sources of randomness
# https://machinelearningmastery.com/reproducible-results-neural-networks-keras/
RANDOM_SEED = None
OPERATION_SEED = None


def get_model_parameters():
    return dict(
        flankingBaseNum=16,
        matrixNum=4,
        expandReferenceRegion=1000000,
    )


# Global functions
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        import sys
        raise sys.exit('Boolean value expected.')
