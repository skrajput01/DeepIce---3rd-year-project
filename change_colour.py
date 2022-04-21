color_list = []
# 5488 - Cubic, 5760 - Prism, Basal

#a = 0
#while a < 20:
#    print(a)
    
with open("C:\\Users\\shyam\\Documents\\KCL\\DeepIce\\Layer Thickness\\prediction_results_5760mols.dat", "r") as file: # output file of DeepIce--predict is taken as input 
    i = 0
    for line in file:
        i+=1
        if i==25: #i = 1 selects frame number 2
            line = str(line)
            color_list = line.split(",")
            color_list = [int(i) for i in color_list]

with open("C:\\Users\\shyam\Documents\\KCL\\DeepIce\\Models\\5760_Basalz_oxy.xyz", "r") as file: # open structure file
    line_list = []
    ss = file.readlines()
    newss = [ss[0], ss[1]]
    print(ss[4].replace("O", "A")) # replace the name of molecules from "name O" to "name A" whenever the molecule is liquid

    for i,c in enumerate(color_list):
        if c==1:
            newss.append(ss[i+2])
        elif c==0:
            newss.append((ss[i+2]).replace("O", "A"))
            print(newss[i])

with open("C:\\Users\\shyam\\Documents\\KCL\\DeepIce\\Layer Thickness\\5760_Basal_i=25.xyz", "w") as file:
    # save a new structure file with the update.
    file.write("".join(newss))
    
#a += 1

print("end")