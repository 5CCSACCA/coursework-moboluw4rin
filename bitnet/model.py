from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class BitNetModel:
    def __init__(self):
        #load BitNet model
        model_name = "microsoft/bitnet-1.58b" #possibly replace with another BitNet model, can use to avoid re-writing too many times

        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/bitnet-1.58b")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/bitnet-1.58b", torch_dtype=torch.float32, device_map='cpu')


    def generate_feedback(self, cleanliness_score: int, detections: list) -> str:
        """
        Generates friendly feedback and study tips based on the YOLO detections and the desk cleanliness score.
        """
        items = [d.get("class_name", "unknown") for d in detections]
        prompt= f"""

        You are an academic productivity coach and online tutor.
        A student has taken a photo of their study desk.
        Detected items:{items}
        Desk Cleanliness Score:{cleanliness_score}/100

        Based on this:

        1. Tell the student what items they should remove or tidy.
        2. Explain how a tidy, clean desk affects study performance.
        3. Give 3 personalised study-habit tips.
        
        Keep the tone friendly and encouraging.
        """

        inputs = self.tokenizer(prompt, return_tensors="pt")
        output = self.model.generate(**inputs, max_new_tokens=100, temperature=0.7, do_sample=True)
        
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
