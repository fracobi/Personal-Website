close all 
clear all
clc

%% Final Homework for System Identification Exam

%--- Generate the .rtf file with the questions
yourID = 153497; 
generate_exam(yourID);

%--- A-Priori Knowledge
Ts = 2; % Sampling time
N = 2000; % Number of samples
M = 350; % Saturation threshold
k = 1.3; % Feedback gain

%--- Loading the .mat file containg Z1, Z2, Z4, that is the datasets needed
load SYSID_DATA.mat 

%% ---Question 1)

plot(Z1); title('Figure 1: Input-Output Data') % Draw the input-outup data
% print ('Figure1', '-depsc2')

SSG = mean(Z1.y(100:end))/M; % Estimate the S.S. gain of G. [0.3095]

%% ---Question 2)

figure; plot(Z2); % To see the inpout-output plot 

%--- Splitting the data set 
Z2 = detrend(Z2); % Remove mean from data
Z2e = Z2(1: 1000); % Data set for estimation
Z2v = Z2(1001:2000); % Data set for validation

%--- Model's order selection 
V = arxstruc(Z2e, Z2v, struc(1:5, 1:5, 1:5)); % Set the max order for polynomials to 5
% selstruc(V, 'PLOT') % To see the FIT of the various orders
nnopt_mdl = selstruc(V, 'mdl'); % Selects the optimal number of parameter for the model based to MDL criterion

%--- Arx Identification
arx_model = arx(Z2e, nnopt_mdl); % Arx model according to the MDL criterion
figure, resid(Z2v, arx_model); title('Figure 2: Residue Correlation Arx Model'); % Residual Analysis
% print ('Figure2', '-depsc2')
figure, compare (Z2v, arx_model, 10); title('Figure 3: 10 Step-Ahed prediction comparison') % Compare the 10 step_ahead prediction with the true output
% print ('Figure3', '-depsc2')

%% ---Question 3)

h = 5; % Prediction Horizon

%--- Armax idetification
armax2421 = armax(Z2e, [2 4 2 1]); % Fit = 86.31%, good residual [The best]
figure, compare (Z2v, armax2421, h); title('Figure 4: 5 Step-Ahead prediction Armax model');
title('Figure 6: 5 Step-Ahed prediction comparison (ARMAX)')
% print ('Figure6', '-depsc2')
figure, resid(Z2v, armax2421); title('Figure 5: Residue correlation Armax model');
title('Figure 5: Residue Correlation (ARMAX)')
% print ('Figure5', '-depsc2')

%--- OE identification
Opt=oeOptions;
Opt.InitialCondition='estimate';
oe551= oe(Z2e, [5 5 1], Opt); % FIT=77.35%, very bad residual
% figure, compare (Z2v, oe551, h);
% figure, resid(Z2v, oe551); 

%--- BJ identification
bj41221= bj(Z2e, [4 1 2 2 1]); % FIT=86.21%,  good residual
% figure, compare (Z2v, bj41221, h);
% figure, resid(Z2v, bj41221); 

% Comparison between the true output and the identified models
figure, compare(Z2v, arx_model, 'r', armax2421, 'g', oe551, '--m', bj41221, '--b', h); 
title('Figure 4: 5 Step-Ahed prediction comparison')
% print('Figure4', '-depsc2')

%--- Draw the zeros and poles 
% figure, iopzplot(arx_model, 'SD', 3); axis equal % Plot zeros/poles with confidence interval 3 sigma
% figure, iopzplot(armax2421, 'SD', 3); axis equal 
% figure, iopzplot(oe551, 'SD', 3); axis equal 
% figure, iopzplot(bj41221, 'SD', 3); axis equal 

% Based on the TF structure of the choosen model, obtain G(z), H(z)
G = tf(armax2421.B, armax2421.A, Ts);
H = tf(armax2421.C, armax2421.A, Ts);

% Compute the peak gain in dB
peak_gain_dB=20*log10(getPeakGain(armax2421)); % Peak gain in dB


%% ---Question 4)
H = inf; % Prediction Horizion

%--- Split the new data-set and remove the mean value 
Z4=detrend(Z4); % Remove the mean value
Z4e=Z4(1:1000); % Estimation data
Z4v=Z4(1001:2000); % Validation data

%--- OE 
Opt=oeOptions;
Opt.InitialCondition='estimate';
oe= oe(Z4e, [1 1 1], Opt); 
figure, compare (Z4v, oe, H);
title('Figure 7: Simulated response comparison (OE)')
% print ('Figure7', '-depsc2')
figure, resid(Z4v, oe); 
title('Figure 8: Residue Correlation (OE)')
% print ('Figure8', '-depsc2')

%--- Armax 
armax = armax(Z4e, [1 1 1 1]); 
% figure, compare (Z4v, armax, H); 
% figure, resid(Z4v, armax);

%--- BJ 
bj= bj(Z4e, [1 1 1 1 1]); 
% figure, compare (Z4v, bj, H);
% figure, resid(Z4v, bj); 

%--- Comparison between the true output and the identified models
figure, compare(Z4v, armax, 'g', oe, 'm', bj, '--b', H);

%--- Build the transfer function P(z)
P = tf(oe.B, oe.F, Ts);

%--- Solve for R(z)
num_R = oe.B; %% Define the numerator of R(z)
den_R = conv(oe.F, [1]) - k * conv(oe.B, [1]); % Compute the denominator of R(z) 

%--- Build the transfer function R(z)
R = tf(num_R, den_R, Ts); % Transfer function of R(z)

%--- Estimate the pole of R(z)
R_pole = pole(R);
















