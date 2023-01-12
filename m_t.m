% Define the number of bits
n = 10;

% Define the amplitude
A = 5;

% Define the bit period
Tb = 2;

% Define the initial time shift (alpha) with a uniform distribution
alpha = Tb * rand();

% Generate random binary data
data = randi([0 1], 1, n);

% Define the time step
dt = 0.1;

% Define the total time
T = 20;

% Initialize the time vector and the signal vector
t = 0:dt:T;
X = zeros(1, length(t));

% Generate the Manchester line code
manchester =[];

for i = 1:n
    if data(i) == 0
        manchester =[manchester , -A*ones(1,(Tb/2)/dt) , A*ones(1,(Tb/2)/dt)];
    else
        manchester =[manchester , A*ones(1,(Tb/2)/dt) , -A*ones(1,(Tb/2)/dt)];
    end
end

% Append zero values at the beginning of the signal to represent the alpha time shift
alpha_vector = A*linspace(0,0,ceil(alpha/dt)+1);
alpha_vector = alpha_vector(2:end);


% Append
alpha_length = length(alpha_vector);
manchester_length = ceil(T/dt) - alpha_length;
X(alpha_length+1: alpha_length+manchester_length) = manchester(1:manchester_length);
size(X)
size(t)
plot(t,X)
xlabel('Time (s)')
ylabel('Amplitude (V)')
title('Manchester Code')