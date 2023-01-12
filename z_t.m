data1 = load('Sample_Process_2022.mat');
data2 = load('y_t.mat');
X1 = data1.X;
X2 = data2.X;
t1 = data1.t;
t2 = data2.t;

X1 = X1(:,1:21);

if size(X1) == size(X2)
    X = X1 .* X2;
else
    error('the size of X1 and X2 are not equal');
end
