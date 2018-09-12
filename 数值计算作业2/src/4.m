function ff = FFT()
x = []
tx = []
w=[]
w[1] = rand(1);
w[2]= rand(1);
w[3] = rand(1);
w[4] = rand(1);
w[5] = rand(1);
count = 1;
for i = 1: 2^10
    t = i + 2* pi / 1024;
    x(count) = sin(w[1] * t) + sin(w[2] * t) +sin(w[3]* t) + sin(w[4] * t) + sin(w[5] * t);
    tx(count) = t;
    count = count + 1;
end

A1 = []
A2 = []
w = []
n = size(x)
N = n(1, 2)
p = log2(N)
for k = 0:N - 1
    A1(k + 1) = x(k + 1)
end
for m = 0:(N/2 - 1)
    w(m + 1) = exp(-1i * 2 * pi * m / N);
end
for q = 1:p
    if mod(q, 2) == 1
        for k = 0:(2^(p-q)-1)
            for j = 0:(2^(q - 1) -1)
                A2(k * 2^q + j + 1) = A1(k * 2^(q-1) + j + 1) + A1(k*2^(q-1) + j + 2^(p-1) + 1);
                A2(k * 2^q + j + 2^(q-1) + 1) = [A1(k * 2^(q-1) + j + 1) - A1(k * 2^(q-1) + j + 2^(p-1) + 1)] * w(k*2^(q-1)+1);
            end
        end
    else
        for k = 0:(2^(p-q)-1)
            for j = 0:(2^(q - 1) -1)
                A1(k * 2^q + j + 1) = A2(k * 2^(q-1) + j + 1) + A2(k*2^(q-1) + j + 2^(p-1) + 1);
                A1(k * 2^q + j + 2^(q-1) + 1) = [A2(k * 2^(q-1) + j + 1) - A2(k * 2^(q-1) + j + 2^(p-1) + 1)] * w(k*2^(q-1)+1);
            end
        end
    end
end
if mod(p, 2) == 0
    for j = 1:N
        A2(j) = A1(j);
    end
end
figure(1)
plot(tx, x)
hold on
figure(2)
plot(tx, A2)
figure(3)
plot(tx, fft(x))