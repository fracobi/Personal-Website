close all
clear all
clc

yourID = 153497; 

%--- A-Priori Knowledge
Ts = 2; % Sampling time
N = 2000; % Number of samples
M = 350; % Saturation threshold

%% Question 1)

%--- Input
u = M*ones(N, 1); % Step input based on the saturation treshold value 

%--- Output
[y_u, w_u] = generate_exam(yourID, u); % Store the output vector y_u and the internal signal output w_u

Z1 = iddata(w_u, u, Ts); % Create the iddata object with step input

save SYSID_DATA.mat Z1

%% Question 2,3)

%--- Input 
warning off
U=M*idinput(N, 'PRBS', [0 1]); % Generate a PRBS (Pseudo Random Binary Sequence) input
warning on

%--- Output
[y w] = generate_exam(yourID, U);

Z2 = iddata(w, U, Ts); % Create the iddata object with PRBS input

save("SYSID_DATA.mat","Z2","-append")

%% Question 4)

Z4 = iddata(y, w, Ts); % Create the iddata object

save("SYSID_DATA.mat","Z4","-append")

