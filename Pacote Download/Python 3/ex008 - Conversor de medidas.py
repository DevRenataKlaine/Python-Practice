m = float (input('Uma distância em metros: '))
km = m*0.001
hm = m*0.01
dam = m*0.1
dm = m*10
cm = m*100
mm = m*1000
print('A medida de {}m corresponde a \n {:.3f} km \n {:.2f} hm \n {:.1f} dam \n {:.0f} dm \n {:.0f} cm \n {:.0f} mm'.format( m, km, hm, dam, dm, cm, mm))
#print ('A medida de {}m corresponde a \n {:.3f} km \n {:.2f} hm \n {:.1f} dam \n {:.0f} dm \n {:.0f} cm \n {:.0f} mm'.format( m, m*0.001, m*0.01, m*0.1, m*10, m*100, m*1000))
