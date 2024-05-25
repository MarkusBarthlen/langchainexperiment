import transformers
import torch

with open('token') as file:
    token = file.read().rstrip()
    model_id = "meta-llama/Meta-Llama-3-8B"
    pipeline = transformers.pipeline(
        "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto", token=token
    )
    pipeline("Hey how are you doing today?")
