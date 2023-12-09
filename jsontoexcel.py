f = open("E:\Descargas\hellfire-poncho-default-rtdb-export (3).json", "r")
w = open("E:\Descargas\HPtrazasDesktopWebFinal.json", "x")
wForms = open("E:\Descargas\HPtrazasDesktopWebFinalFORMS.json", "x")

# Se deben copiar las sessionIDs de firebase en este array
# Permite que separemos el JSON por ids de usuario
sessionIDs = [
1045560040136058036,
1088722923830231958,
1168129803860387891,
1267507278367725983,
1395763909340804219,
1538445874763309281,
157944069160053099,
1619366812132536978,
1809993702961660296,
1932672610123153558,
1984246957376655214,
2046253911411990718,
2063180268622913879,
2190702301670407137,
2490530026715395805,
2616183498576396450,
2707798156655514397,
2730937712664045593,
2788732078683563360,
2809462855172882374,
2883188744900435742,
2899760076836161003,
3007896395916945777,
3028517500769047673,
3108567711425957315,
3240999660248541886,
3365568272506603414,
3483298140389683341,
3704990574109784239,
3706859492818350796,
3741487149895369888,
374666576992521514,
3751794401808430801,
3858215830760853316,
3875563707110725317,
3929528011741992517,
4288731596789667052,
4508188291227463926,
4671740550322628655,
4848933432829190081,
5045398153499486808,
5233157276984910940,
5259363505039104955,
5306579675715248779,
5470214838606364060,
5523932241583497029,
5534641257637961746,
5615603050454732226,
6005218198949426372,
6076026726070860431,
6110964872882541941,
6120441850317779126,
622247180279702136,
6228396551229153993,
6346594997033955084,
6350943008401004876,
660344611267483099,
6615109153622399121,
6713325590405912600,
6921495534541474211,
7376718801858428027,
7421698782103601388,
746792246135835924,
7493229294646072814,
7787987802344267051,
789207802658492373,
8039639679257402388,
8099685567710576395,
8191282985395728588,
8211864454419133047,
8533893481328013180,
8579195801446396772,
8631649220093469435,
8789482585559465446,
8790335764012539502,
8894786196826590476,
8969406569146220590,
8993480018245408685,
9028204697655740339
]

lineRead = f.readline().strip()
count = 0
currentid = "0"

readingEvent = False
w.write("{\n")
wForms.write("{\n")

skillsSaved = []

# Se debe añadir "FIN" al final del JSON
while lineRead != "FIN" :
    if readingEvent:
        if "levelDifficulty" in lineRead:
            for i in range(len(skillsSaved)):
                if(i == 0):
                    wForms.write("\n{\n")
                else:
                    wForms.write(",\n{\n")
                
                wForms.write(skillsSaved[i])
                wForms.write("\n")
                wForms.write(lineRead)
                wForms.write("\n}")
                
            skillsSaved.clear()

        if "}" not in lineRead:
            w.write(lineRead)
            w.write("\n")
        else:
            readingEvent = False

    else:
        for sid in sessionIDs:
            if str(sid) in lineRead:
                currentid = str(sid)
                if(sid == sessionIDs[0]):
                    w.write("\"" + currentid + "\": [\n")
                    wForms.write("\"" + currentid + "\": [\n")
                else:
                    w.write("}\n],\n\"" + currentid + "\": [\n")
                    wForms.write("\n],\n\"" + currentid + "\": [\n")

        # Este script deshecha los eventos de formulario
        if "FormDataEvent" not in lineRead:
            if "EventType" in lineRead:

                if "InicioEvent" in lineRead:
                    count = 0
                else:
                    w.write("},\n")

                readingEvent = True
                w.write("{\n")
                w.write("\"EventCounter\": \"" + str(count) + "\",\n")
                count = count + 1
                w.write(lineRead)
                w.write("\n")
        else:
            lineRead = f.readline().strip()
            skillsSaved.append(lineRead)


    lineRead = f.readline().strip()


# En el archivo final
w.write("}]}")
wForms.write("]}")
f.close()
w.close()
wForms.close()