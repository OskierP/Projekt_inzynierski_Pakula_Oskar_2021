from Cole_Cole_class import coleCole as CC
from file_functions_module import file_2_list

TCC = file_2_list(open('Cole-Cole_2.csv', 'r'), ",")  # 2-Cole-cole: czytanie watości z pliku csv

Skin = CC(TCC, 0, 2)

Fat = CC(TCC, 1, 2)

Muscle = CC(TCC, 2, 2)

Heart = CC(TCC, 3, 2)

Kidney = CC(TCC, 4, 2)

Liver = CC(TCC, 5, 2)

Lunge = CC(TCC, 6, 2)

Stomach = CC(TCC, 7, 2)

Colon = CC(TCC, 8, 2)

Small = CC(TCC, 9, 2)

Aort = CC(TCC, 10, 2)

Bladder = CC(TCC, 11, 2)

Esophagus = CC(TCC, 12, 2)

Fallopian = CC(TCC, 13, 2)

Gall_Bladder = CC(TCC, 14, 2)

Ovary = CC(TCC, 15, 2)

Pancears = CC(TCC, 16, 2)

Spleen = CC(TCC, 17, 2)

Uetrus = CC(TCC, 18, 2)


Two_Cole_Cole_Objects = [Skin, Fat, Muscle, Heart, Kidney, Liver, Lunge, Stomach, Colon, Small, Aort, Bladder, Esophagus, Fallopian, Gall_Bladder, Ovary, Pancears, Spleen, Uetrus]