import sys
sys.path.insert(0, '.')

try:
    from src.exception import CustomException
    print('exception ok')
except Exception as e:
    print('exception FAILED:', e)

try:
    from src.logger import logging
    print('logger ok')
except Exception as e:
    print('logger FAILED:', e)

try:
    from src.utils import load_object
    print('utils ok')
except Exception as e:
    print('utils FAILED:', e)

try:
    from src.pipeline.predict_pipeline import CustomData, PredictPipeline
    print('pipeline ok')
except Exception as e:
    print('pipeline FAILED:', e)

try:
    from flask import Flask
    print('flask ok')
except Exception as e:
    print('flask FAILED:', e)