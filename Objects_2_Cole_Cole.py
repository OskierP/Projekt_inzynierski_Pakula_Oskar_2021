from Cole_Cole_class import ColeCole as CC
from file_functions_module import file_2_list

TCC = file_2_list(open('Cole-Cole_2.csv', 'r'), ",")  # 2-Cole-cole: reading values from a file

Skin = CC(TCC, 0, 2)

Fat = CC(TCC, 1, 2)

Muscle = CC(TCC, 2, 2)

Blood = CC(TCC, 3, 2)

Heart = CC(TCC, 4, 2)

Kidney = CC(TCC, 5, 2)

Liver = CC(TCC, 6, 2)

Lunge = CC(TCC, 7, 2)

Stomach = CC(TCC, 8, 2)

Colon = CC(TCC, 9, 2)

Small = CC(TCC, 10, 2)

Aort = CC(TCC, 11, 2)

Bladder = CC(TCC, 12, 2)

Esophagus = CC(TCC, 13, 2)

Fallopian = CC(TCC, 14, 2)

Gall_Bladder = CC(TCC, 15, 2)

Ovary = CC(TCC, 16, 2)

Pancears = CC(TCC, 17, 2)

Spleen = CC(TCC, 18, 2)

Uetrus = CC(TCC, 19, 2)

two_Cole_Cole_Objects = [Skin, Fat, Muscle, Blood, Heart, Kidney, Liver, Lunge, Stomach, Colon, Small, Aort, Bladder,
                         Esophagus, Fallopian, Gall_Bladder, Ovary, Pancears, Spleen, Uetrus]
