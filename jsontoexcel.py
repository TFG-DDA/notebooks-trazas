f = open("E:\Descargas\hellfireponcho-desktop-default-rtdb-export (1).json", "r")
w = open("E:\Descargas\HPtrazasDesktopFinal_2.json", "x")
wForms = open("E:\Descargas\HPtrazasDesktopFinalFORMS_2.json", "x")

# Se deben copiar las sessionIDs de firebase en este array
# Permite que separemos el JSON por ids de usuario
sessionIDs = [
1126757909184086875,
1530393169260920597,
1947931233209809877,
3222661888180467937,
3848743437012212075,
4443867434743800590,
5116002334978996940,
6409546622230072682,
7405794501571521397,
7944648088642926644,
8905972887783645587,
975948956911856427
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