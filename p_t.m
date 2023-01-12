% Parameters
A = 5;
Tb = 2;
num_of_bits = 10;
X = zeros(100, numel(t)); % Initialize signal with zeros
alphas = zeros(100,1);
bits_matrix = zeros(100,num_of_bits);

for k = 1:100
    % Generate random bits and alpha for each iteration
    bits = randi([0 1],1,num_of_bits);
    alpha = rand(1)*Tb;
    alphas(k) = alpha;
    bits_matrix(k,:) = bits;
    
    start_index = ceil(alpha*10); % Starting index of bit in P_rawpl

    for i = 1:num_of_bits
        if bits(i) == 1
            X(k, start_index:start_index+(Tb/0.1)-1) = A;
        else
            X(k, start_index:start_index+(Tb/0.1)-1) = -A;
        end
        start_index = start_index+(Tb/0.1);
        % Ensure all bits stop at t = 20 
        if start_index+Tb/0.1 > numel(t)
            break;
        end
    end
end
