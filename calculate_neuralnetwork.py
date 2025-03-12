import matplotlib.pyplot as plt
import torch
from torchvision import datasets, transforms
import numpy as np
import time

# Transformation: Bild in Tensor umwandeln
transform = transforms.Compose([transforms.ToTensor()])
# Laden des Test-Datensatzes
test_dataset = datasets.MNIST(root="./data", train=False, transform=transform, download=True)
# Zugriff auf ein Testbild (z. B. das erste Bild)
test_image, test_label = test_dataset[123]  # test_image ist ein Tensor, test_label ist die Ziffer

# Bild als Vektor p
p_vec = test_image.view(784)
p_vec = p_vec.detach().cpu().numpy() if isinstance(p_vec, torch.Tensor) else np.array(p_vec)

# Bias und Weights erzeugen
v_vec = np.random.rand(784,10)
w_vec = np.random.rand(784,784)
a_vec = np.random.rand(784)
b_vec = np.random.rand(10)

start = time.time()

# Layer berechnen
h_vec = np.zeros(784)
h_vec = np.dot(p_vec, w_vec) + a_vec
h_vec = np.maximum(0, h_vec)  # ReLU
o_vec = np.dot(h_vec, v_vec) + b_vec

end = time.time()
print(o_vec)
print(end - start)
