from Cole_Cole_class import coleCole as CC
from file_2_list import file_2_list

FCC = file_2_list(open('Cole-Cole_4.csv', 'r'), ",")  # 4-Cole-cole: czytanie watości z pliku csv

Dry_Skin = CC(FCC, 0, 4)

Wet_Skin = CC(FCC, 1, 4)

Fat = CC(FCC, 2, 4)

Muscle = CC(FCC, 3, 4)

Spounge_Bone = CC(FCC, 4, 4)

Condense_Bone = CC(FCC, 5, 4)

Marrow = CC(FCC, 6, 4)

Grey_Brain = CC(FCC, 7, 4)

White_Brain = CC(FCC, 8, 4)

Eye = CC(FCC, 9, 4)

Blood = CC(FCC, 10, 4)

Heart = CC(FCC, 11, 4)

Kidney = CC(FCC, 12, 4)

Liver = CC(FCC, 13, 4)

Lunge_nO2 = CC(FCC, 14, 4)

Lunge_O2 = CC(FCC, 15, 4)

Stomach = CC(FCC, 16, 4)

Colon = CC(FCC, 17, 4)

Small = CC(FCC, 18, 4)

Four_Cole_Cole_Objects = [Dry_Skin, Wet_Skin, Fat, Muscle, Spounge_Bone, Condense_Bone, Marrow, Grey_Brain, White_Brain,
                          Eye, Blood, Heart,Kidney, Liver, Lunge_nO2, Lunge_O2, Stomach, Colon, Small, Dry_Skin, Wet_Skin, Fat,
                          Muscle]
