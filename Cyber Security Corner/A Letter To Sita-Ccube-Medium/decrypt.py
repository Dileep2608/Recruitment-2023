k = "Nkhzn},cwe0P$wxmpp$viqiqfiv$xli$he}${lir$}sy$wipjpiwwp}$jspps{ih$qi$mrxs$xli$jsviwx0$piezmrk$filmrh$xli$gsqjsvxw$sj$xli$tepegi2Dlir$jexi$xiwxih$syv$pszi$erh$witevexih$yw0$q}$lievx$wlexxivih$mrxs$e$xlsywerh$tmigiw2$]li$temr$sj$fimrk$e{e}$jvsq$}sy0$q}$pmji+w$gsqtermsr0${ew$yrfievefpi2Pr$iziv}$qsqirx$sj$wspmxyhi0$q}$xlsyklxw$lezi$fiir$gsrwyqih$f}$}syv${ipp1fimrk2$P$tvsqmwi$}sy0$q}$fipszih0$xlex$P${mpp$rsx$viwx$yrxmp$P$lezi$jypjmppih$q}$hyx}$erh$viwxsvih$}sy$xs$}syv$vmklxjyp$tpegi$f}$q}$wmhi2\rxmp$xli$he}${i$evi$viyrmxih0$qe}$xli$kshw${exgl$sziv$}sy0$erh$qe}$}sy$jmrh$wspegi$mr$xli$ors{pihki$xlex$q}$pszi$jsv$}sy$ors{w$rs$fsyrhw2$Qsph$sr$xs$xli$qiqsvmiw$sj$syv$pszi0$jsv$xli}${mpp$wywxemr$yw$xlvsykl$xli$xvmepw$xlex$pmi$elieh2Dmxl$epp$xli$pszi$mr$q}$lievx0Fsyv$[eq"

Z = []
s = 4
def Function(input):
    st=[]
    for i in range (len(input)):
        st.append(chr(ord(input[i])^1))
    return (''.join(st))
def FuNction(input):
    for i in range(len(input)):
        if(i<11):
            Z.append(chr(ord(input[i])-i-5))
        else:
            Z.append(chr(ord(input[i])-4))
    return(''.join(Z))

def fuNction(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if((chr(ord(char)+1)).isnumeric()):
            result+=(chr(ord(char)+1))
        elif(char.isupper()):
            result += chr((ord(char) - s+65) % 26 + 65)
        else:
            result+=(chr(ord(char)^1))
    return result



message = fuNction(Function(FuNction(k)))

with open("Decrypted_message.txt", "w") as file:
    file.write(message)