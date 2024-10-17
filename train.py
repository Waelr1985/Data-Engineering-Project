import os
import sys
from power.exception import PowerException
from power.pipeline.train_pipeline import TrainPipeline

from power.constants import *


def training():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

    except Exception as e:
        raise PowerException(e, sys) from e


if __name__ == "__main__":
    training()