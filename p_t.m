% Parameters
A = 5;
Tb = 2;
alpha = rand(1)*Tb;
num_of_bits = 10;


% Time vector
t = 0:0.1:(Tb*num_of_bits);

% 10-bit signal
bits = randi([0 1],1,num_of_bits);

% NRZ signal
X = zeros(1, numel(t)); % Initialize signal with zeros
start_index = ceil(alpha*10); % Starting index of bit in P_rawpl

for i = 1:num_of_bits
    if bits(i) == 1
        X(start_index:start_index+(Tb/0.1)-1) = A;
    else
        X(start_index:start_index+(Tb/0.1)-1) = -A;
    end
    start_index = start_index+(Tb/0.1);
    % Ensure all bits stop at t = 20 
    if start_index+Tb/0.1 > numel(t)
        break;
    end
end

% Plot signal
plot(t,X);
xlabel('Time (s)');
ylabel('Voltage (V)');