from pylab import*
pix = 1000           # Image size (N x N)
Niters = 100 
x = linspace(-2,2,pix)
y = linspace(-2,2,pix)
X, Y = meshgrid(x, y)
c = X + 1j*Y
z = zeros((pix,pix))
mandel_set = zeros((pix,pix))

for i in range(Niters):
    z = z**2 + c
    mandel_set += abs(z) < 2

figure(figsize=(5, 5))
imshow(mandel_set, extent=(-2, 2, -2, 2),cmap='binary')
title("The Mandelbrot Set")
xlabel("Real")
ylabel("Imaginary")
#grid()
show()

