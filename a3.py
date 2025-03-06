import torch

def gradient_torch(x_val):
    x = torch.tensor([x_val], requires_grad=True)
    g = 0.01
    eps = 1e-5                                           # 1e-7 wird mit PyTorch nie erreicht...
    count = 1
    
    while(1):
        y = ((x**3)+(1 + x**2).sqrt())**2
        y.backward()                                     # Backward-Mode autodiff
        
        if abs(x.grad.item()) < eps or count > 100000:
            break

        # Variante 1:
        #with torch.no_grad():                            # In PyTorch best Praxis -> torch.no_grad() für Parameter-Updates zu verwenden!
                                                          # Ansonsten enthät computational graph auch diese Op und verfälscht Ergebnis
        #    x -= g * x.grad
        #x.grad.zero_()                                   # Gradient addiert sich sonst auf

        # Variante 2:
        x_val = x.item() - g * x.grad.item()    
        x.grad.zero_()                                   # Gradient addiert sich sonst auf
        x = torch.tensor([x_val], requires_grad=True)
        count += 1
    
    print(f"Found a minimum at Point p({x.item():.3f}, {y.item():.3f}) on iteration {count}")

gradient_torch(-0.5)
gradient_torch(0.0)
gradient_torch(-0.25)
