% Define the number of bits
n = 10;

% Define the amplitude
A = 5;

% Define the bit period
Tb = 2;

% Define the total time
T = 20;

% Define the time step
dt = 0.1;

% Initialize the time vector and the signal matrix
t = 0:dt:T;
X = zeros(100, length(t));

% Initialize the alpha matrix
alpha_matrix = zeros(100, 1);

% Initialize the bits matrix
bits_matrix = zeros(100, n);

for j = 1:100
    % Define the initial time shift (alpha) with a uniform distribution
    alpha = Tb * rand();

    % Generate random binary data
    data = randi([0 1], 1, n);
    bits_matrix(j,:) = data;
    % Initialize the manchester code
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

    alpha_length = length(alpha_vector);
    manchester_length = ceil(T/dt) - alpha_length;
    X(j, alpha_length+1: alpha_length+manchester_length) = manchester(1:manchester_length);
    alpha_matrix(j) = alpha;

end

% Plot the signal matrix
figure;
for j = 1:100
    plot(t,X(j,:));
    hold on;
    xlabel('Time (s)')
    ylabel('Amplitude (V)')
    title('Manchester Code')
end
