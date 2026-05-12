import torch
from torchvision import transforms
from PIL import Image
import torch.nn as nn

# ----------- LOAD MODEL -----------
model_path = "alaska_optionA_efficientnet.pth"

class EfficientNetStego(nn.Module):
    def __init__(self):
        super().__init__()
        from torchvision.models import efficientnet_b0, EfficientNet_B0_Weights
        self.backbone = efficientnet_b0(weights=EfficientNet_B0_Weights.IMAGENET1K_V1)
        in_features = self.backbone.classifier[1].in_features
        self.backbone.classifier[1] = nn.Linear(in_features, 2)

    def forward(self, x):
        return self.backbone(x)

model = EfficientNetStego()
model.load_state_dict(torch.load(model_path, map_location="cpu"))
model.eval()

# ----------- TRANSFORM -----------
transform = transforms.Compose([
    transforms.Resize((256,256)),
    transforms.ToTensor(),
])

# ----------- TEST IMAGE -----------
img_path = "test.jpg"   # put any image here
img = Image.open(img_path).convert("RGB")
x = transform(img).unsqueeze(0)

with torch.no_grad():
    logits = model(x)
    pred = torch.argmax(logits, dim=1).item()

print("Prediction:", "STEGO" if pred==1 else "COVER")
