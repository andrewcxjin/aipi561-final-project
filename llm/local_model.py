from llama_cpp import Llama

llm = Llama(model_path="models/mistral-7b.Q4_K_M.gguf")

def generate_content(prompt: str) -> str:
    result = llm(prompt, max_tokens=300)
    return result["choices"][0]["text"]