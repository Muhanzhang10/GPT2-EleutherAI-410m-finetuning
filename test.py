from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import AutoTokenizer, AutoModelForCausalLM

import pandas as pd

# Load CSV file into a Pandas DataFrame
df = pd.read_csv('test_data/grid_search_result_gpt2.csv')

# Convert DataFrame to LaTeX
latex_code = df.to_latex(index=False)

# Print or save the LaTeX code
print(latex_code)