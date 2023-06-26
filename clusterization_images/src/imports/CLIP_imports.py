
! pip install git+https://github.com/openai/CLIP.git

# импорт из clip нужного
import requests
from transformers import CLIPProcessor, CLIPModel
from transformers import AutoProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")
