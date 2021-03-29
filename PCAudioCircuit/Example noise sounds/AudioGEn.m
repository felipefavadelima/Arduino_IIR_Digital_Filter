%Author: Felipe Fava de Lima
%Octave GNU Code
%Generate noise sound with specific frequencies content

clear all
pkg load signal
Fs = 44100;
te = 100;
dt = 1/Fs;
t = 0:dt:te-dt;
df = 1/te;
f = 0:df:Fs-df;

%Gen white Noise
y = randn(length(t),1);

%BP.wav filter
[b,a] = butter(3,[100 250]/(Fs/2),'stop');
y = filter(b,a,y);
plot(y);

%LP.wav filter
%[b,a] = butter(3,[100 250]/(Fs/2),'stop');
%y = filter(b,a,y);
%plot(y);

%Ress.wav filter
%Idx150 = find(f>148);
%Idx150 = intersect(Idx150,find(f<152));
%Absfft = abs(fft(y));
%Absfft = Absfft(1:(end/2)+1);
%Anglefft = angle(fft(y));
%Absfft(Idx150) = 0;
%Absfft = Absfft';
%Absfft = [Absfft fliplr(Absfft(2:end-1))];
%yfft = pol2cart(Anglefft',Absfft);
%yfft = yfft(:,1) + i*yfft(:,2);
%y = real(ifft(yfft));

%low pass 350Hz
[b,a] = butter(4,350/(Fs/2),'low');
y = filter(b,a,y);
plot(y);
y=y/max(abs(y));
audiowrite('BP.wav',y,44100);

%Plot FFT
ffty = 20*log10(abs(fft(y)));
ffty = ffty - max(ffty);
Nwindow = 100;
window = (1/Nwindow)*ones(Nwindow,1);
ffty = filtfilt(window,1,ffty);
plot(f(1:end/2),ffty(1:end/2));
ylabel('Amplitude (dB)');
xlabel('Frequency (Hz)');
