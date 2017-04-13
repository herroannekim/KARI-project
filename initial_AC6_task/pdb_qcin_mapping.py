# Anne Kim
# Tidor Lab
# This file provides the mapping between 
# Molecular structures, PDB files, and generated qcin files 

label_dict {
C1   : carboxyl_carbon,        
O2   : carboxyl_oxygen_a,        
O3   : carboxyl_oxygen_b,        
C4   : alpha_carbon,        
C5   : TS_methyl_carbon,        
O6   : alpha_oxygen,        
C7   : beta_carbon,        
O8   : beta_oxygen,        
C9   : beta_methyl_carbon,        
H10  : beta_methyl_hydrogen_a,        
H11  : beta_methyl_hydrogen_b,        
H12  : beta_methyl_hydrogen_c,        
H13  : TS_methyl_hydrogen_a,        
H14  : TS_methyl_hydrogen_b,        
H15  : TS_methyl_hydrogen_c,        
O18  : water_a_oxygen,        
O19  : water_b_oxygen,        
O20  : water_c_oxygen,        
O21  : water_d_oxygen,        
O22  : water_e_oxygen,        
Mg16 : magnesium_a,        
Mg17 : magnesium_b,        
H23  : water_e_hydrogen_a,        
H24  : water_e_hydrogen_b,        
H25  : water_d_hydrogen_a,        
H26  : water_d_hydrogen_a,         
H27  : water_c_hydrogen_a,         
H28  : water_c_hydrogen_b,         
H29  : water_a_hydrogen_a,         
H30  : water_a_hydrogen_b,         
H31  : water_b_hydrogen_a,         
H32  : water_b_hydrogen_b, 
}

pdb_dict {
C1  :( 3.457,  -1.303,   2.639 ) ,        
O2  :( 4.585,  -1.568,   2.152 ) ,        
O3  :( 3.156,  -1.669,   3.838 ) ,        
C4  :( 2.431,  -0.611,   1.760 ) ,        
C5  :( 2.048,  -1.964,   0.324 ) ,        
O6  :( 1.323,  -0.391,   2.447 ) ,        
C7  :( 2.490,   0.068,   0.516 ) ,        
O8  :( 1.481,   0.694,   0.023 ) ,        
C9  :( 3.695,   0.184,  -0.328 ) ,        
H10 :( 3.485,  -0.146,  -1.481 ) ,        
H11 :( 4.489,  -0.484,   0.104 ) ,        
H12 :( 4.132,   1.211,  -0.539 ) ,        
H13 :( 1.160,  -1.639,  -0.299 ) ,        
H14 :( 1.810,  -2.780,   1.053 ) ,        
H15 :( 3.012,  -2.165,  -0.257 ) ,        
O18 :(-1.959,   1.488,   0.508 ) ,        
O19 :(-1.384,  -1.067,   1.277 ) ,        
O20 :( 0.976,   2.056,   2.737 ) ,        
O21 :( 2.241,  -0.074,   5.616 ) ,        
O22 :( 1.818,  -2.716,   5.917 ) ,        
Mg16:( 1.070,  -1.460,   4.371 ) ,        
Mg17:(-0.077,   0.829,   1.350 ) ,        
H23 :( 1.209,  -2.743,   6.694 ) ,        
H24 :( 2.636,  -2.243,   6.287 ) ,        
H25 :( 1.617,   0.431,   6.165 ) ,        
H26 :( 3.102,   0.101,   6.015 ) ,         
H27 :( 1.938,   2.339,   2.680 ) ,         
H28 :( 0.769,   1.458,   3.520 ) ,         
H29 :(-2.658,   1.141,   1.105 ) ,         
H30 :(-2.105,   1.177,  -0.410 ) ,         
H31 :(-2.295,  -0.767,   1.223 ) ,         
H32 :(-1.469,  -1.502,   2.155 ) ,
}

qcin_dict = {
   C1     :   ( 3.45700 , -1.30300 ,  2.63900),
   O2     :   ( 4.58500 , -1.56800 ,  2.15200),
   O3     :   ( 3.15600 , -1.66900 ,  3.83800),
   C4     :   ( 2.43100 , -0.61100 ,  1.76000),
   O6     :   ( 1.32300 , -0.39100 ,  2.44700),
   C7     :   ( 2.49000 ,  0.06800 ,  0.51600),
   O8     :   ( 1.48100 ,  0.69400 ,  0.02300),
   C9     :   ( 3.69500 ,  0.18400 , -0.32800),
   H10    :   ( 3.48500 , -0.14600 , -1.48100),
   H11    :   ( 4.48900 , -0.48400 ,  0.10400),
   H12    :   ( 4.13200 ,  1.21100 , -0.53900),
   C5     :   ( 2.04800 , -1.96400 ,  0.32400),
   H13    :   ( 1.16000 , -1.63900 , -0.29900),
   H14    :   ( 1.81000 , -2.78000 ,  1.05300),
   H15    :   ( 3.01200 , -2.16500 , -0.25700),
   O18    :   (-1.95900 ,  1.48800 ,  0.50800),
   H29    :   (-2.65800 ,  1.14100 ,  1.10500),
   H30    :   (-2.10500 ,  1.17700 , -0.41000),
   O19    :   (-1.38400 , -1.06700 ,  1.27700),
   H31    :   (-2.29500 , -0.76700 ,  1.22300),
   H32    :   (-1.46900 , -1.50200 ,  2.15500),
   O20    :   ( 0.97600 ,  2.05600 ,  2.73700),
   H27    :   ( 1.93800 ,  2.33900 ,  2.68000),
   H28    :   ( 0.76900 ,  1.45800 ,  3.52000),
   O21    :   ( 2.24100 , -0.07400 ,  5.61600),
   H25    :   ( 1.61700 ,  0.43100 ,  6.16500),
   H26    :   ( 3.10200 ,  0.10100 ,  6.01500),
   O22    :   ( 1.81800 , -2.71600 ,  5.91700),
   H23    :   ( 1.20900 , -2.74300 ,  6.69400),
   H24    :   ( 2.63600 , -2.24300 ,  6.28700),
  Mg16    :   ( 1.07000 , -1.46000 ,  4.37100),
  Mg17    :   (-0.07700 ,  0.82900 ,  1.35000),
 } 


