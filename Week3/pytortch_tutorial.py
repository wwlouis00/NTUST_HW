import torch

x = torch.rand(2,2)
print(x.dtype)
print(x)
torch.cuda.is_available()