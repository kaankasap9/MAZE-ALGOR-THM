#GLOBALS
LİST_OF_PASS=[]
STUCK_PATH_LİST=[]
STARTİNG_I=0
STARTİNG_J=0
CRIT_POINTS=[]         #UYARI:: deneme.txt dosyasındaki labirentleri denerken ekstra satırlar olmamasına dikkat ediniz.
OPTİON=0               #UYARI:: deneme.txt dosyasındaki labirentleri denerken ekstra satırlar olmamasına dikkat ediniz.
BLOCK_LİST=[]          #UYARI:: deneme.txt dosyasındaki labirentleri denerken ekstra satırlar olmamasına dikkat ediniz.
STUCK_INDEX=0
CRIT_INDEX=0
END=[]
VALUE=-1
H=0
ON=True

#LABİTENTİMİZİ OKUYURUZ VE OLUŞTURUYORUZ
file = open("girdi", mode="r")
yol=file.readlines()
print("START\n")
print("LABİRENT:\n")
for value in yol:
    value = value.strip("\n")
    print(value)
print("-------------------")

#START NOKTASINI BULUYORUZ
def find():
    global STARTİNG_J,STARTİNG_I
    for i in range(0,len(yol)):
        for j in range(0,len(yol)):
            if yol[i][j].__contains__("S"):
                STARTİNG_I=i
                STARTİNG_J=j
                return (STARTİNG_I, STARTİNG_J)

#ETRAFININ KONTROL EDİLMESİ
def down():
    global STARTİNG_J,STARTİNG_I
    if STARTİNG_I+1>len(yol)-1:
        #print("LABİRENT DIŞI ALTA GİDEMEZ")
        return False
    elif yol[STARTİNG_I + 1][STARTİNG_J] == "W":
        #print("ALTI DOLU")
        return False
    else:
        if not (STARTİNG_I + 1, STARTİNG_J) in LİST_OF_PASS:
            #print("ALTI BOS")
            return True
        else:
            #print("ALTI BOS FAKAT DAHA ONCE GİTTİĞİ İÇİN GİDEMİYOR")
            return False
def up():
    global STARTİNG_J,STARTİNG_I
    if STARTİNG_I-1<0:
        #print("LABİRENT DIŞI ÜSTE GİDEMEZ")
        return False
    elif yol[STARTİNG_I - 1][STARTİNG_J] == "W":
        #print("ÜSTÜ DOLU")
        return False
    else:
        if not (STARTİNG_I - 1, STARTİNG_J) in LİST_OF_PASS:
            #print("ÜSTÜ BOS")
            return True
        else:
            #print("ÜSTÜ BOS FAKAT DAHA ONCE GİTTİĞİ İÇİN GİDEMİYOR")
            return False
def right():
    global STARTİNG_J,STARTİNG_I
    if STARTİNG_J+1>len(yol)-1:
        #print("LABİRENT DIŞI SAĞA GİDEMEZ")
        return False
    elif yol[STARTİNG_I][STARTİNG_J + 1] == "W":
        #print("SAĞI DOLU")
        return False
    else:
        if not (STARTİNG_I, STARTİNG_J + 1) in LİST_OF_PASS:
            #print("SAĞI BOS")
            return True
        else:
            #print("SAĞI BOS FAKAT DAHA ONCE GİTTİĞİ İÇİN GİDEMİYOR")
            return False
def left():
    global STARTİNG_J,STARTİNG_I
    if STARTİNG_J-1<0:
        #print("LABİRENT DIŞI SOLA GİDEMEZ")
        return False
    elif yol[STARTİNG_I][STARTİNG_J - 1] == "W":
        #print("SOLU DOLU")
        return False
    else:
        if not (STARTİNG_I, STARTİNG_J - 1) in LİST_OF_PASS:
            #print("SOLU BOS")
            return True
        else:
            #print("SOLU BOS FAKAT DAHA ONCE GİTTİĞİ İÇİN GİDEMİYOR")
            return False
def control():
    global STARTİNG_J,STARTİNG_I
    if up():
        STARTİNG_I = STARTİNG_I - 1
        LİST_OF_PASS.append((STARTİNG_I, STARTİNG_J))
    elif down():
       STARTİNG_I = STARTİNG_I + 1
       LİST_OF_PASS.append((STARTİNG_I, STARTİNG_J))
    elif right():
       STARTİNG_J = STARTİNG_J + 1
       LİST_OF_PASS.append((STARTİNG_I, STARTİNG_J))
    elif left():
       STARTİNG_J = STARTİNG_J - 1
       LİST_OF_PASS.append((STARTİNG_I, STARTİNG_J))
    else:
        return "STUCK"

#BİR KONUMUN SAĞ SOL VS NE KADAR YERE GİTME ŞANSI OLDUĞUNU HESAPLAR
def option_counter():
    global OPTİON
    if up():
        OPTİON+=1
    if down():
        OPTİON += 1
    if right():
        OPTİON += 1
    if left():
        OPTİON += 1
    return OPTİON

#BİR METİNİN İÇİNDEKİ DEĞİŞTİRMEK İSTEDİĞİMİZ İNDİSTEKİ ELEMANI DEĞİŞTİRİR
def degistirici(degiscek_metin, yeni_str, index, x=False):
    if not x and index not in range(len(degiscek_metin)):
        raise ValueError("VAlUE ERROR")
    if index < 0:
        return yeni_str + degiscek_metin
    if index > len(degiscek_metin):
        return degiscek_metin + yeni_str
    return degiscek_metin[:index] + yeni_str + degiscek_metin[index + 1:]

#SON CEVAP İÇİN UYGUN FORMA GETİRİR
def format():
    global END,yol
    for i in range(0, len(yol)):
            strs = yol[i]

            dic = {'W': '0,', 'P': '0,', 'F': 'F,', '1': '1,', 'S': 'S,'}
            strs = "".join((dic.get(x, x)  for x in strs))
            END.append(strs)

#GÜC NOKTASI BELİRLER
def guc_noktası_belirle():
    global yol
    print("'H' GÜÇ NOKTASI BELİRLİYORUZ (ÖRNEĞE GÖRE BELİRLENMİŞTİR.)\n")
    güc_noktalı_satır = degistirici(yol[3], "H", 2)
    yol[3] = güc_noktalı_satır
    file = open("cikti.txt", mode="w")
    file.writelines(yol)
    for value in yol:
        value = value.strip("\n")
        print(value)

    print("-------------------")

#ETRAF KONTROL EDİLDİKTEN SONRA YANLIS YOLLARIN DUVARLA DOLDURULMASI
def fill():

    global BLOCK_LİST,STUCK_INDEX,CRIT_INDEX,CRIT_POINTS,VALUE,STARTİNG_I,STARTİNG_J,H,OPTİON
    counter=0
    if H==3:
        VALUE-=1
    for i in STUCK_PATH_LİST[STUCK_INDEX]:
            if i==CRIT_POINTS[VALUE]:
                CRIT_INDEX= counter - 1
                break
            counter+=1

    BLOCK_LİST= STUCK_PATH_LİST[STUCK_INDEX][CRIT_INDEX + 2:]
    for i in range(0, len(BLOCK_LİST)):
        line=yol[BLOCK_LİST[i][0]]
        index=BLOCK_LİST[i][1]
        line=degistirici(line, "W", index)
        yol[BLOCK_LİST[i][0]] = line
        file=open("cikti.txt",mode="w")
        file.writelines(yol)
    H+=1
    STUCK_INDEX+=1

LİST_OF_PASS.append(find())
guc_noktası_belirle()

while ON:
    if option_counter()>=2 and  not (STARTİNG_I, STARTİNG_J) in CRIT_POINTS:
       CRIT_POINTS.append((STARTİNG_I, STARTİNG_J))
    OPTİON = 0
    if control()== "STUCK":
        STUCK_PATH_LİST.append(LİST_OF_PASS)
        fill()
        LİST_OF_PASS = []  # SIKIŞTIĞI İÇİN TEKRAR TENİ BİR YOL DENMESİ İÇİN RESET ATIYORUZ
        LİST_OF_PASS.append(find()) # EN BAŞA GÖNDERİYORUZ

    if yol[STARTİNG_I][STARTİNG_J]== "F":
        LİST_OF_PASS.pop(-1)
        for i in range(1, len(LİST_OF_PASS)):
            satır = yol[LİST_OF_PASS[i][0]]
            index = LİST_OF_PASS[i][1]
            satır = degistirici(satır, "1", index)
            yol[LİST_OF_PASS[i][0]] = satır
            file = open("cikti.txt", mode="w")
            file.writelines(yol)
        format()
        file = open("cikti.txt", mode="w")
        file.writelines(END)
        file.close()
        print("ÇÖZÜM:\n")
        for value in END:
            value=value.strip("\n")
            print(value)
        print("\nFİNİSH")
        ON=False

