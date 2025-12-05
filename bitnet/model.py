from transformers import AutoTokenizer, AutoModelForCausalLM

class BitNetModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/bitnet-1.58b")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/bitnet-1.58b")

    def generate_text(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        output = self.model.generate(
            **inputs,
            max_new_tokens=150,
            do_sample=True,
            temperature=0.7
        )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
