from math import radians,sin,cos,tan
ang = float(input('Digite o ângulo que você deseja:'))
sen = sin(radians(ang))
print('O ângulo de {} tem o SENO {:.2f}:'.format(ang,sen))
cos = cos(radians(ang))
print('O ângulo de {} tem o COSSENO {:.2f}:'.format(ang,cos))
tang = tan(radians(ang))
print('O ângulo de {} tem o TANGENTE {:.2f}:'.format(ang,tang))

