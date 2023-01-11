import Tkinter as tk 

root = tk.Tk()

WIDTH = 1340
HEIGHT = 1000

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

#Membuat Rectangle
canvas.create_rectangle(0,445.351,1346.143,0, fill="#78CDD3", outline="") #Biru Langit
canvas.create_rectangle(0,457.023,1343.895,712.141, fill="#8B8B8C", outline="") #Abu-Abu
canvas.create_rectangle(2.347,445.351,1343.825,457.023, fill="#603F20", outline="") #Coklat
canvas.create_rectangle(0,1000,1345.019,645.93, fill="#00A859", outline="") #Hijau

#Membuat Garis Jalan
canvas.create_polygon((60.096, 521.98),(238.611,521.98),(227.806,533.566),(49.29,533.81), fill="white", outline="")
canvas.create_polygon((322.796, 521.98),(501.311,521.98),(490.506,533.566),(311.99,533.81), fill="white", outline="")
canvas.create_polygon((592.164, 521.98),(770.68,521.98),(759.875,533.566),(581.359,533.81), fill="white", outline="")
canvas.create_polygon((854.371, 521.98),(1032.886,521.98),(1022.081,533.566),(843.565,533.81), fill="white", outline="")
canvas.create_polygon((1110.679, 521.98),(1300,521.98),(1289.195,533.566),(1110.679,533.81), fill="white", outline="")

#Batas Bawah
canvas.create_oval(837.194, 598.468, 1345.019, 693.392, fill="#00A859", outline="")
canvas.create_oval(640.362, 598.468, 1148.187, 693.392, fill="#00A859", outline="")
canvas.create_oval(299.61, 584.582, 807.435, 679.506, fill="#00A859", outline="")
canvas.create_oval(0, 594.315, 522.769, 684.571, fill="#00A859", outline="")

#Awan
canvas.create_rectangle(0,224,1350,443, fill="#CCE7D4", outline="") #Biru muda
canvas.create_oval(1159, 190, 1301, 295, fill="#CCE7D4", outline="")
canvas.create_oval(1029, 196, 1139, 277, fill="#CCE7D4", outline="")
canvas.create_oval(800, 131, 1071, 283, fill="#CCE7D4", outline="")
canvas.create_oval(637, 197, 833, 311, fill="#CCE7D4", outline="")
canvas.create_oval(484, 189, 680, 302, fill="#CCE7D4", outline="")
canvas.create_oval(196, 199, 386, 318, fill="#CCE7D4", outline="")
canvas.create_oval(118, 133, 308, 251, fill="#CCE7D4", outline="")
canvas.create_oval(47, 146, 159, 255, fill="#CCE7D4", outline="")
canvas.create_oval(0, 172, 79, 280, fill="#CCE7D4", outline="")

#Membuat Kereta Api (Gerbong-1)
ka9= canvas.create_rectangle(26.618, 408.081, 474.227, 398.338, fill="#5E1F1E", outline="black") #Coklat
ka1= canvas.create_rectangle(391.123, 308.665, 422.061, 294.976, fill="#001C56", outline="black") #Biru Tua
ka2= canvas.create_rectangle(395.731, 344.726, 422.061, 308.665, fill="#05BCFE", outline="black") #Biru Muda
ka3= canvas.create_rectangle(289.259, 279.604, 386.845, 263.924, fill="#001C56", outline="black") #Biru Tua
ka4= canvas.create_rectangle(294.278, 344.642, 381.826, 279.604, fill="#05BCFE", outline="black") #Biru Muda
ka5= canvas.create_rectangle(313.45, 335.711, 365.452, 290.468, fill="white", outline="black") #Putih
ka6= canvas.create_rectangle(294.278, 373.106, 445.1, 344.642, fill="#001C56", outline="black") #Biru Tua
ka7= canvas.create_rectangle(445.1, 373.106, 460.898, 333.707, fill="#05BCFE", outline="black") #Biru Muda
ka8= canvas.create_rectangle(294.278, 408.081, 474.227, 373.106, fill="#05BCFE", outline="black") #Biru Muda


ka10= canvas.create_oval(307.911, 367.415, 324.992, 350.333, fill="white", outline="") #bulat-bulat
ka11= canvas.create_oval(344.351, 367.415, 361.433, 350.333, fill="white", outline="")
ka12= canvas.create_oval(380.223, 367.415, 397.305, 350.333, fill="white", outline="")
ka13= canvas.create_oval(414.386, 367.415, 431.468, 350.333, fill="white", outline="")

ka14= canvas.create_oval(381.579, 442.805, 434.239, 389.383, fill="#FFCC9B", outline="black")
ka15= canvas.create_oval(306.538, 442.805, 359.2, 389.383, fill="#FFCC9B", outline="black")
ka16= canvas.create_oval(325, 424.108, 340.767, 408.081, fill="#450505", outline="black")
ka17= canvas.create_oval(400, 424.108, 415.108, 408.081, fill="#450505", outline="black") #Ban

#Membuat Kereta Api (Gerbong-2)
ka18= canvas.create_rectangle(164.85, 318.849, 288.519, 303.824, fill="#207F2A", outline="black") #Hijau Tua
ka19= canvas.create_rectangle(166.825, 373.607, 282.677, 318.819, fill="#87C743", outline="black") #Hijau Muda

ka20= canvas.create_rectangle(253.194, 362.839, 267.675, 329.804, fill="white", outline="black") #Jendela
ka21= canvas.create_rectangle(227.029, 362.839, 241.51, 329.804, fill="white", outline="black") #Jendela
ka22= canvas.create_rectangle(200.369, 362.839, 214.851, 329.804, fill="white", outline="black") #Jendela
ka23= canvas.create_rectangle(173.71, 362.839, 188.192, 329.804, fill="white", outline="black") #Jendela
ka24= canvas.create_rectangle(166.825, 408.081, 282.677, 373.607, fill="#207F2A", outline="black") #Hijau Tua

ka25= canvas.create_oval(164.686, 442.805, 217.346, 389.383, fill="#FFCC9B", outline="black")
ka26= canvas.create_oval(221.295, 442.805, 273.955, 389.383, fill="#FFCC9B", outline="black")
ka27= canvas.create_oval(239.726, 424.108, 255.524, 408.081, fill="#450505", outline="black") #Ban
ka28= canvas.create_oval(183.117, 424.108, 198.915, 408.081, fill="#450505", outline="black")

#Membuat Kereta Api (Gerbong-3)
ka29= canvas.create_rectangle(36.683, 318.849, 160.351, 303.824, fill="#4F1918", outline="black") #Coklat Tua
ka30= canvas.create_rectangle(36.657, 373.607, 154.509, 318.849, fill="#FA923A", outline="black") #Coklat Muda
ka31= canvas.create_rectangle(38.657, 408.081, 154.509, 373.607, fill="#4F1918", outline="black") #Coklat Tua

ka32= canvas.create_rectangle(125.026, 362.839, 139.508, 329.804, fill="white", outline="black") #Jendela
ka33= canvas.create_rectangle(98.861, 362.839, 113.342, 329.804, fill="white", outline="black") #Jendela
ka34= canvas.create_rectangle(72.202, 362.839, 86.683, 329.804, fill="white", outline="black") #Jendela
ka35= canvas.create_rectangle(45.543, 362.839, 60.024, 329.804, fill="white", outline="black") #Jendela

ka36= canvas.create_oval(93.127, 442.805, 145.787, 389.383, fill="#FFCC9B", outline="black")
ka37= canvas.create_oval(36.518, 442.805, 89.178, 389.383, fill="#FFCC9B", outline="black")
ka38= canvas.create_oval(111.558, 424.108, 127.356, 408.081, fill="#450505", outline="black")
ka39= canvas.create_oval(54.949, 424.108, 70.747, 408.081, fill="#450505", outline="black")

#Bendera
ka40= canvas.create_rectangle(28.233, 398.339, 34.188, 347.48, fill="#AA0000", outline="black") #Bendera
ka41= canvas.create_rectangle(23.903, 347.48, 34.188, 329.784, fill="#6E2C2A", outline="black") #Bendera

#Asap Kereta Api
ka42= canvas.create_oval(505, 151, 517, 171, fill="#606062", outline="")
ka43= canvas.create_oval(512, 159, 527, 176, fill="#606062", outline="")
ka44= canvas.create_oval(502, 168, 526, 196, fill="#606062", outline="")
ka45= canvas.create_oval(515, 168, 530, 187, fill="#606062", outline="")
ka46= canvas.create_oval(488, 178, 516, 201, fill="#606062", outline="")
ka47= canvas.create_oval(485, 160, 515, 185, fill="#606062", outline="")

ka48= canvas.create_oval(401, 242, 420, 260, fill="#606062", outline="")
ka49= canvas.create_oval(416, 239, 432, 258, fill="#606062", outline="")
ka50= canvas.create_oval(400, 220, 430, 247, fill="#606062", outline="")
ka51= canvas.create_oval(423, 225, 452, 247, fill="#606062", outline="")
ka52= canvas.create_oval(423, 199, 463, 235, fill="#606062", outline="")
ka53= canvas.create_oval(444, 217, 470, 236, fill="#606062", outline="")
ka54= canvas.create_oval(458, 202, 484, 227, fill="#606062", outline="")
ka55= canvas.create_oval(440, 179, 481, 225, fill="#606062", outline="")

#Membuat Matahari
canvas.create_oval(1230.484, 34.674, 1312.41, 117.787, fill="#C20022", outline="")

mt1=(1253.496 , 43.724); mt2=(1260.875,16.587); mt3=(1273.174,41.853); mt4=(1280.861,24.385); mt5=(1283.01,37.798); mt6=(1306.996,18.77); mt7=(1298.079,48.403); mt8=(1305.766,43.412); mt9=(1303.922,52.458); mt10=(1320.833,44.036);
mt11=(1305.459,60.88); mt12=(1326.367,62.44); mt13=(1308.841,72.421); mt14=(1325.444,78.66); mt15=(1316.221,81.155); mt16=(1327.29,94.256); mt17=(1302.692, 93.32); mt18=(1314.068,103.614); mt19=(1302.999,104.55); mt20=(1314.068,103.614);
mt21=(1302.999,104.55); mt22=(1306.074,122.017); mt23=(1288.24,106.733); mt24=(1287.625,120.77); mt25=(1281.476,112.348); mt26=(1271.637,129.816); mt27=(1266.102,111.724); mt28=(1252.266,127.944); mt29=(1252.881,117.65); mt30=(1240.274,129.816);
mt31=(1246.116,108.917); mt32=(1239.967,113.595); mt33=(1243.042,103.614); mt34=(1219.059,115.779); mt35=(1238.43,92.073); mt36=(1224.593,94.256); mt37=(1235.97,94.256); mt38=(1213.832,78.972); mt39=(1232.895,70.55); mt40=(1226.746,66.183);
mt41=(1236.585,66.183); mt42=(1216.599,52.458); mt43=(1239.045,54.954); mt44=(1218.136,28.752); mt45=(1248.269,47.155); mt46=(1246.116,35.302);
canvas.create_polygon(mt1,mt2,mt3,mt4,mt5,mt6,mt7,mt8,mt9,mt10,mt11,mt12,mt13,mt14,mt15,mt16,mt17,mt18,mt19,mt20,mt21,mt22,mt23,mt24,mt25,mt26,mt27,mt28,mt29,mt30,mt31,mt32,mt33,mt34,mt35,mt36,mt37,mt38,mt39,mt40,mt41,mt42,mt43,mt44,mt45,mt46, fill="#FE6400", outline="")

canvas.create_oval(1237.033, 41.763, 1304.985, 110.698, fill="#ED3237", outline="")
canvas.create_oval(1238.23, 42.977, 1303.788, 109.485, fill="#FEFE00", outline="")

#Garis Rel
canvas.create_rectangle(1344.265 , 448.51, 1313.175, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(1245.138 , 448.51, 1276.227, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(1168.896 , 448.51, 1199.985, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(1106.717 , 448.51, 1075.628, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(1007.59 , 448.51, 1038.679, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(945.412 , 448.51, 914.332, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(821.055 , 448.51, 852.144, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(758.876 , 448.51, 789.965, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(696.698 , 448.51, 665.609, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(572.341 , 448.51, 603.43, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(501.162 , 448.51, 541.252, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(447.984 , 448.51, 416.895, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(385.805 , 448.51, 354.716, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(261.448 , 448.51, 292.538, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(199.27 , 448.51, 168.181, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(74.913 , 448.51, 106.002, 463.94, fill="#603F20", outline="")
canvas.create_rectangle(12.734 , 448.51, 43.824, 463.94, fill="#603F20", outline="")

#Membuat Lampu Lalu Lintas
canvas.create_polygon((938.553, 485.098),(954.429,485.098),(960.536,494.142),(954.429,500.832), (938.553,500.832), (932.446,494.142), fill="#605F54", outline="")
canvas.create_rectangle(938.553 , 414.353, 954.43, 485.097, fill="#605F54", outline="")
canvas.create_rectangle(923.776 , 414.353, 969.207, 295.413, fill="#605F54", outline="")

canvas.create_oval(932.08, 376.897, 961.714, 406.96, fill="#00A859", outline="") #Lampu
canvas.create_oval(932.08, 339.025, 961.714, 369.088, fill="#FEFE00", outline="") #Lampu
canvas.create_oval(932.08, 301.714, 961.714, 331.423, fill="#C20022", outline="") #Lampu

canvas.create_rectangle(941.789 , 284.263, 953.758, 295.413, fill="#605F54", outline="")
canvas.create_oval(935.188, 261.119, 959.369, 285.651, fill="#605F54", outline="")

#Membuat Burung-Burung
b1=(259.562,86.093); b2=(284.776,67.636); b3=(271.402,49.339); b4=(252.725,42.965)
b5=(234.177,37.204); b6=(223.315,23.054); b7=(277.243,46.124); b8=(288.834,64.611)
b9=(304.711,51.318); b10=(317.569,59.281); b11=(307.665,63.644); b12=(304.199,77.618)
burung0 = canvas.create_polygon(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12, fill="blue")

c1=(262.575,68.066); c2=(278.721,63.281); c3=(282.048,68.066); c4=(277.605,70.598); c5=(267.737,69.207)
burung1 = canvas.create_polygon(c1,c2,c3,c4,c5, fill="blue")

d1=(247.303,57.42); d2=(273.954,57.095); d3=(277.387,61.619); d4=(265.009,65.461); d5=(253.993,61.056)
burung2 = canvas.create_polygon(d1,d2,d3,d4,d5, fill="blue")

e1=(233.407,40.14); e2=(249.244,53.998); e3=(272.821,55.227); e4=(270.557,51.647); e5=(239.463,40.815)
burung3 = canvas.create_polygon(e1,e2,e3,e4,e5, fill="blue")

f1=(233.553, 97.965); f2=(255.489,88.559); f3=(269.15,85.71); f4=(263.379, 91.335); f5=(255.73,92.918)
burung4 = canvas.create_polygon(f1,f2,f3,f4,f5, fill="blue")

#Burung Kecil
br1=(184.605,69.259); br2=(201.694,56.75); br3=(192.63,44.349); br4=(179.972,40.029)
br5=(167.401,36.125); br6=(160.039,26.534); br7=(196.588,42.17); br8=(204.444,54.7)
br9=(215.205,45.69); br10=(223.919,51.087); br11=(217.207,54.044); br12=(214.858,63.515)
burung5 = canvas.create_polygon(br1,br2,br3,br4,br5,br6,br7,br8,br9,br10,br11,br12, fill="blue")

cr1=(186.647,57.041); cr2=(197.59,53.798); cr3=(199.843,57.041); cr4=(196.834,58.757); cr5=(190.146,57.814)
burung6 = canvas.create_polygon(cr1,cr2,cr3,cr4,cr5, fill="blue")

dr1=(176.297,49.826); dr2=(194.359,49.606); dr3=(196.686,52.672); dr4=(188.297,55.275); dr5=(188.297,55.29)
burung7 = canvas.create_polygon(dr1,dr2,dr3,dr4,dr5, fill="blue")

er1=(166.879,38.114); er2=(117.612,47.506); er3=(193.592,48.339); er4=(192.057,45.913); er5=(170.983,38.572)
burung8 = canvas.create_polygon(er1,er2,er3,er4,er5, fill="blue")

fr1=(166.978, 77.305); fr2=(181.845,70.93); fr3=(191.104,68.999); fr4=(187.192, 72.811); fr5=(182.008,73.884)
burung9 = canvas.create_polygon(fr1,fr2,fr3,fr4,fr5, fill="blue")

#Burung Kecil - 2
brt1=(198.032,136.874); brt2=(211.666,126.75); brt3=(204.434,116.714); brt4=(194.336,113.218)
brt5=(184.308,110.058); brt6=(178.435,102.296); brt7=(207.592,114.951); brt8=(213.86,125.091)
brt9=(222.444,117.799); brt10=(229.396,122.168); brt11=(224.042,124.561); brt12=(222.168,132.226)
burung10 = canvas.create_polygon(brt1,brt2,brt3,brt4,brt5,brt6,brt7,brt8,brt9,brt10,brt11,brt12, fill="blue")

crt1=(199.662,126.986); crt2=(208.392,124.362); crt3=(210.189,126.986); crt4=(207.789,128.375); crt5=(202.453,127.612)
burung11 = canvas.create_polygon(crt1,crt2,crt3,crt4,crt5, fill="blue")

drt1=(191.404,121.147); drt2=(205.814,120.969); drt3=(207.671,123.45); drt4=(200.978,125.557); drt5=(195.022,123.141)
burung12 = canvas.create_polygon(drt1,drt2,drt3,drt4,drt5, fill="blue")

ert1=(183.891,111.668); ert2=(192.454,119.269); ert3=(205.202,119.943); ert4=(203.977,117.98); ert5=(187.166,112.038)
burung13 = canvas.create_polygon(ert1,ert2,ert3,ert4,ert5, fill="blue")

frt1=(183.97,143.386); frt2=(195.83,138.227); frt3=(203.217,136.664); frt4=(200.096,139.749); frt5=(195.961,140.618)
burung14 = canvas.create_polygon(frt1,frt2,frt3,frt4,frt5, fill="blue")

#Pohon Kelapa
canvas.create_polygon((1150.088,631.144),(1180.612,640.796),(1208.361,634.764),(1208.361,679.403),(1173.873,682.621),(1138.592,674.577), fill="#5B2800") #Batang Pohon Kelapa
canvas.create_polygon((1163.963,591.331),(1151.674,627.123),(1180.612,633.155),(1207.965,629.134),(1208.361,591.733),(1187.748,598.972), fill="#5B2800")
canvas.create_polygon((1175.062,552.232),(1166.737,588.114),(1183.783,592.94),(1203.604,588.918),(1206.379,555.941),(1188.937,559.561), fill="#5B2800")
canvas.create_polygon((1184.973,527.388),(1179.026,547.094),(1191.712,553.528),(1209.551,552.323),(1212.326,527.388),(1198.847,518.943), fill="#5B2800")

#Buah Kelapa
canvas.create_oval(1193.682, 507.638, 1220.991, 539.25, fill="#A78E4E") #Warna Coklat Muda
canvas.create_oval(1179.423, 489.183, 1209.947, 514.519, fill="#A78E4E")
canvas.create_oval(1165.945, 506.074, 1196.865, 541.866, fill="#A78E4E")
canvas.create_oval(1205.923, 489.417, 1233.233, 521.029, fill="#A78E4E")

#Daun Pohon Kelapa
kl1=(1152.533,459.479); kl2=(1149.295,445.348); kl3=(1177.837,460.63); kl4=(1146.124,435.294); kl5=(1146.124,420.816); kl6=(1163.17,432.479); kl7=(1148.502,411.164); kl8=(1151.277,401.915); kl9=(1163.566,404.73); kl10=(1170.702,413.175);
kl11=(1171.098,402.317); kl12=(1184.18,409.958); kl13=(1187.748,426.849); kl14=(1193.298,413.175); kl15=(1204.397,432.077); kl16=(1198.451,450.576); kl17=(1209.551,438.913); kl18=(1217.479,454.597); kl19=(1194.487,483.955); kl20=(1165.494,463.619);
canvas.create_polygon(kl1, kl2, kl3, kl4, kl5, kl6, kl7, kl8, kl9, kl10, kl11, kl12, kl13, kl14, kl15, kl16, kl17, kl18, kl19, kl20, fill="#58E43B", outline="black")

qw1=(1195.28,478.727); qw2=(1223.822,450.575); qw3=(1272.185,429.664); qw4=(1307.466,429.262); qw5=(1332.837,451.38); qw6=(1290.024,441.728); qw7=(1300.727,459.021); qw8=(1290.42,465.021);
qw9=(1259.103,464.249); qw10=(1269.41,472.695); qw11=(1243.643,490.792); qw12=(1220.65,480.738); qw13=(1237.696,501.65); qw14=(1222.471,514.212); qw15=(1203.208,501.248);
canvas.create_polygon(qw1, qw2, qw3, qw4, qw5, qw6, qw7, qw8, qw9, qw10, qw11, qw12, qw13, qw14, qw15, fill="#58E43B", outline="black")

qwr1=(1194.487,483.955); qwr2=(1157.62,488.781); qwr3=(1109.257,506.476); qwr4=(1081.111,527.79); qwr5=(1077.543,545.083); qwr6=(1111.635,517.334);
qwr7=(1096.572,539.855); qwr8=(1129.078,535.855); qwr9=(1152.863,500.443); qwr10=(1136.61,534.225); qwr11=(1173.08,522.16)
canvas.create_polygon(qwr1, qwr2, qwr3, qwr4, qwr5, qwr6, qwr7, qwr8, qwr9, qwr10, qwr11, fill="#58E43B", outline="black")

qww1=(1065.254,461.434); qww2=(1079.922,448.967); qww3=(1117.185,448.163); qww4=(1168.72,464.651); qww5=(1194.487,483.955); qww6=(1160.689,488.379);
qww7=(1141.369,494.7272); qww8=(1118.771,485.966); qww9=(1157.223,471.488); qww10=(1114.014,483.151); qww11=(1083.49,469.879); qww12=(1106.086,460.63);
canvas.create_polygon(qww1, qww2, qww3, qww4, qww5, qww6, qww7, qww8, qww9, qww10, qww11, qww12, fill="#58E43B", outline="black")

qwrw1=(1215.798,518.793); qwrw2=(1230.762,499.271); qwrw3=(1280.481,539.552); qwrw4=(1296.282,572.304); qwrw5=(1291.831,595.132); qwrw6=(1275.076,552.34);
qwrw7=(1276.03, 580.73); qwrw8=(1249.608,560.885); qwrw9=(1240.072,522.544); qwrw10=(1240.142,559.686); qwrw11=(1212.722,531.828)
canvas.create_polygon(qwrw1, qwrw2, qwrw3, qwrw4, qwrw5, qwrw6, qwrw7, qwrw8, qwrw9, qwrw10, qwrw11, fill="#58E43B", outline="black")


def move(event):
	if event.char=='a': #Gerak burung ke kiri
		canvas.move( burung0,-10,0)
		canvas.move(burung1,-10,0)
		canvas.move(burung2,-10,0)
		canvas.move(burung3,-10,0)
		canvas.move(burung4,-10,0)
		canvas.move(burung5,-10,0)
		canvas.move(burung6,-10,0)
		canvas.move(burung7,-10,0)
		canvas.move(burung8,-10,0)
		canvas.move(burung9,-10,0)
		canvas.move(burung10,-10,0)
		canvas.move(burung11,-10,0)
		canvas.move(burung12,-10,0)
		canvas.move(burung13,-10,0)
		canvas.move(burung14,-10,0)
	elif event.char=='d': #Gerak burung ke kanan
		canvas.move(burung0,10,0)
		canvas.move(burung1,10,0)
		canvas.move(burung2,10,0)
		canvas.move(burung3,10,0)
		canvas.move(burung4,10,0)
		canvas.move(burung5,10,0)
		canvas.move(burung6,10,0)
		canvas.move(burung7,10,0)
		canvas.move(burung8,10,0)
		canvas.move(burung9,10,0)
		canvas.move(burung10,10,0)
		canvas.move(burung11,10,0)
		canvas.move(burung12,10,0)
		canvas.move(burung13,10,0)
		canvas.move(burung14,10,0)
	elif event.char=='w': #Gerak burung ke atas
		canvas.move(burung0,0,-10)
		canvas.move(burung1,0,-10)
		canvas.move(burung2,0,-10)
		canvas.move(burung3,0,-10)
		canvas.move(burung4,0,-10)
		canvas.move(burung5,0,-10)
		canvas.move(burung6,0,-10)
		canvas.move(burung7,0,-10)
		canvas.move(burung8,0,-10)
		canvas.move(burung9,0,-10)
		canvas.move(burung10,0,-10)
		canvas.move(burung11,0,-10)
		canvas.move(burung12,0,-10)
		canvas.move(burung13,0,-10)
		canvas.move(burung14,0,-10)
	elif event.char=='s': #Gerak burung ke bawah
		canvas.move(burung0,0,10)
		canvas.move(burung1,0,10)
		canvas.move(burung2,0,10)
		canvas.move(burung3,0,10)
		canvas.move(burung4,0,10)
		canvas.move(burung5,0,10)
		canvas.move(burung6,0,10)
		canvas.move(burung7,0,10)
		canvas.move(burung8,0,10)
		canvas.move(burung9,0,10)
		canvas.move(burung10,0,10)
		canvas.move(burung11,0,10)
		canvas.move(burung12,0,10)
		canvas.move(burung13,0,10)
		canvas.move(burung14,0,10)
	elif event.char=='l': #Gerak Kereta Api ke kanan
		canvas.move(ka1, 10, 0)
		canvas.move(ka2, 10, 0)
		canvas.move(ka3, 10, 0)
		canvas.move(ka4, 10, 0)
		canvas.move(ka5, 10, 0)
		canvas.move(ka6, 10, 0)
		canvas.move(ka7, 10, 0)
		canvas.move(ka8, 10, 0)
		canvas.move(ka9, 10, 0)
		canvas.move(ka10, 10, 0)
		canvas.move(ka11, 10, 0)
		canvas.move(ka12, 10, 0)
		canvas.move(ka13, 10, 0)
		canvas.move(ka14, 10, 0)
		canvas.move(ka15, 10, 0)
		canvas.move(ka16, 10, 0)
		canvas.move(ka17, 10, 0)
		canvas.move(ka18, 10, 0)
		canvas.move(ka19, 10, 0)
		canvas.move(ka20, 10, 0)
		canvas.move(ka21, 10, 0)
		canvas.move(ka22, 10, 0)
		canvas.move(ka23, 10, 0)
		canvas.move(ka24, 10, 0)
		canvas.move(ka25, 10, 0)
		canvas.move(ka26, 10, 0)
		canvas.move(ka27, 10, 0)
		canvas.move(ka28, 10, 0)
		canvas.move(ka29, 10, 0)
		canvas.move(ka30, 10, 0)
		canvas.move(ka31, 10, 0)
		canvas.move(ka32, 10, 0)
		canvas.move(ka33, 10, 0)
		canvas.move(ka34, 10, 0)
		canvas.move(ka35, 10, 0)
		canvas.move(ka36, 10, 0)
		canvas.move(ka37, 10, 0)
		canvas.move(ka38, 10, 0)
		canvas.move(ka39, 10, 0)
		canvas.move(ka40, 10, 0)
		canvas.move(ka41, 10, 0)
		canvas.move(ka42, 10, 0)
		canvas.move(ka43, 10, 0)
		canvas.move(ka44, 10, 0)
		canvas.move(ka45, 10, 0)
		canvas.move(ka46, 10, 0)
		canvas.move(ka47, 10, 0)
		canvas.move(ka48, 10, 0)
		canvas.move(ka49, 10, 0)
		canvas.move(ka50, 10, 0)
		canvas.move(ka51, 10, 0)
		canvas.move(ka52, 10, 0)
		canvas.move(ka53, 10, 0)
		canvas.move(ka54, 10, 0)
		canvas.move(ka55, 10, 0)
		
root.bind("<Key>",move)
root.mainloop()
