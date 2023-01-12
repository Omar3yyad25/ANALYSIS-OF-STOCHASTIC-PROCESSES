dt = 0.1; % time step
t = 0:dt:2; % time vector from 0 to 2 with time step 0.1

for i = 1:100
    beta = normrnd(0,1); % generate random variable from normal distribution N(0,1)
    X(i,:) = beta*sin(2*pi*t); % compute X(t)
end