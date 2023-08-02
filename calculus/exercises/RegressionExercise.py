import torch
import matplotlib.pyplot as plt

print("Defining x")
x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7.]) # E.g.: Dosage of drug for treating Alzheimer's disease
print(x)
print("")


print("Defining y sample vector")
y = -0.5*x + 2 + torch.normal(mean=torch.zeros(8), std=0.8)
print(y)


print("Showing points corresponding according to our actual data")
fig, ax = plt.subplots()
plt.title("Clinical Trial")
plt.xlabel("Drug dosage (mL)")
plt.ylabel("Forgetfulness")
_ = ax.scatter(x, y)

print("")


print("-------------------------------------")
print("Defining random entries for m and b so that the system "
      "can find the more aproximate value to real data")
print("")

print("Defining slope m")
m = torch.tensor([0.9]).requires_grad_()
print(m)

print("Defining slope y-intercept b")
b = torch.tensor([0.1]).requires_grad_()
print(b)

print("Defining function for finding y for every ocurrence")
def regression(my_x, my_m, my_b):
    return my_m*my_x + my_b

def regression_plot(my_x, my_y, my_m, my_b):   
    fig, ax = plt.subplots()

    ax.scatter(my_x, my_y)
    
    x_min, x_max = ax.get_xlim()
    y_min = regression(x_min, my_m, my_b).detach().item()
    y_max = regression(x_max, my_m, my_b).detach().item()
    
    ax.set_xlim([x_min, x_max])
    _ = ax.plot([x_min, x_max], [y_min, y_max])
    
yhat = regression(x, m, b)
yhat    

def mse(my_yhat, my_y): 
    sigma = torch.sum((my_yhat - my_y)**2)
    return sigma/len(my_y)
    
print("Calculating MSE (Cost)")    
C = mse(yhat, y)
print(C)
print("")
C.backward()

print("m.grad")
print(m.grad)

print("b.grad")
print(b.grad)
print("")
optimizer = torch.optim.SGD([m, b], lr=0.01)
optimizer.step()

print("Confirming that values already changed sensibly")
print("m:")
print(m)
print("b:")
print(b)
print("")

print("Plotting new line")
regression_plot(x, y, m, b)




print("Put the 4 steps in a loop to iteratively minimize cost toward zero:")
epochs = 1000
for epoch in range(epochs):
    
    optimizer.zero_grad() # Reset gradients to zero; else they accumulate
    
    yhat = regression(x, m, b) # Step 1
    C = mse(yhat, y) # Step 2
    
    C.backward() # Step 3
    optimizer.step() # Step 4
    
    print('Epoch {}, cost {}, m grad {}, b grad {}'.format(epoch, '%.3g' % C.item(), '%.3g' % m.grad.item(), '%.3g' % b.grad.item()))
    
    
    
print("Print final result")

regression_plot(x, y, m, b)
plt.show()