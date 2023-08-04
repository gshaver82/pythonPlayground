print("hello world")

import torch
random_image_size_tensor = torch.rand(size=(224, 224, 3))
print(random_image_size_tensor)
print(random_image_size_tensor.shape), print(random_image_size_tensor.ndim)