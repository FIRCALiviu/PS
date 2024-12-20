import torch.nn as nn
import torch

X = torch.linspace(0,10,1000)
trend = X*X+X-5

sezon = torch.sin(2*torch.pi*2*X)+torch.sin(2*torch.pi*40*X)

rezidual = torch.randn(1000)

serie = trend+sezon+rezidual/100

class AR(nn.Module):
    def __init__(self,p):
        super(AR, self).__init__()
        self.p = p
        self.params = nn.Parameter(torch.randn(p))
        

    def forward(self,y_serie):
        
        p= self.p
        Y = torch.zeros((len(y_serie)-p,p))

        for i in range(len(y_serie)-p):
            for j in range(p):
                Y[i][j] = y_serie[i+j]
        
        pred = Y@(self.params.T)
        
        loss = ((pred-y_serie[p:])**2).mean()+ torch.sum(torch.abs(self.params))
        return pred,loss
    
model = AR(50).to('cpu')

initial = model.params.detach().numpy()


optimizer = torch.optim.AdamW(params=model.parameters(),lr=0.01)

print(*model.parameters())

loss = torch.tensor([100])
___niter = 200

while loss.item()>10 and ___niter!=0:
    
    
    ___niter -=1
    optimizer.zero_grad()
    _,loss  = model(serie)
    loss.backward()

    
    with torch.no_grad():
        print(loss-torch.sum(torch.abs(model.params)))
    optimizer.step()
_,loss  = model(serie)
print(model.params)
print(loss) # loss final : 26 (fara eroarea de la l1)

import matplotlib.pyplot as plt

plt.imshow([model.params.detach().numpy()],cmap='gray')
plt.show()

