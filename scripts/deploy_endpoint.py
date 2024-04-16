import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel

role = 'arn:aws:iam::263358745544:role/service-role/AmazonSageMaker-ExecutionRole-20210616T105009'

hub = {
	'HF_MODEL_ID':'openai/whisper-large-v3',
	'HF_TASK':'automatic-speech-recognition'
}

# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	transformers_version='4.37.0',
	pytorch_version='2.1.0',
	py_version='py310',
	env=hub,
	role=role, 
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
	initial_instance_count=1, # number of instances
	instance_type='ml.g4dn.xlarge' # ec2 instance type
)