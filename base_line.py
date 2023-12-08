from transformers import pipeline, set_seed

#model_name = 'gpt2'
model_name = "EleutherAI/pythia-410m"
generator = pipeline('text-generation', model=model_name)
set_seed(42)
#print(generator("Oil price", max_length=20, num_return_sequences=5)[0])
print(generator("Oil price", max_length=20)[0])


