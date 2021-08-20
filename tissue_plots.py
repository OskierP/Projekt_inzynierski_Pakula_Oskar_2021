from plot_module import plot

def tissue_plotting(x, epsilon_4cc, sigma_4cc, epsilon_2cc, sigma_2cc):

    #Skin
    skin_fcc_1 = [epsilon_4cc['Dry_Skin'], sigma_4cc['Dry_Skin']]
    skin_tcc = [epsilon_2cc['Skin'], sigma_2cc['Skin']]
    skin_fcc_2 = [epsilon_4cc['Wet_Skin'], sigma_4cc['Wet_Skin']]
    plot(x, skin_fcc_1, skin_tcc, skin_fcc_2, '4')

    #Fat
    fat_fcc = [epsilon_4cc['Fat'], sigma_4cc['Fat']]
    fat_tcc = [epsilon_2cc['Fat'], sigma_2cc['Fat']]
    plot(x, fat_fcc, fat_tcc)

    #Muscle
    muscle_fcc = [epsilon_4cc['Muscle'], sigma_4cc['Muscle']]
    muscle_tcc = [epsilon_2cc['Muscle'], sigma_2cc['Muscle']]
    plot(x, muscle_fcc, muscle_tcc)

    #Blood
    blood_fcc = [epsilon_4cc['Blood'], sigma_4cc['Blood']]
    blood_tcc = [epsilon_2cc['Blood'], sigma_2cc['Blood']]
    plot(x, blood_fcc, blood_tcc)

    #Heart
    heart_fcc = [epsilon_4cc['Heart'], sigma_4cc['Heart']]
    heart_tcc = [epsilon_2cc['Heart'], sigma_2cc['Heart']]
    plot(x, heart_fcc, heart_tcc)

    #Kidney
    kidney_fcc = [epsilon_4cc['Kidney'], sigma_4cc['Kidney']]
    kidney_tcc = [epsilon_2cc['Kidney'], sigma_2cc['Kidney']]
    plot(x, kidney_fcc, kidney_tcc)

    #Liver
    liver_fcc = [epsilon_4cc['Liver'], sigma_4cc['Liver']]
    liver_tcc = [epsilon_2cc['Liver'], sigma_2cc['Liver']]
    plot(x, liver_fcc, liver_tcc)

    #Lunge
    lunge_fcc1 = [epsilon_4cc['Lunge_nO2'], sigma_4cc['Lunge_nO2']]
    lunge_tcc = [epsilon_2cc['Lunge'], sigma_2cc['Lunge']]
    lunge_fcc2 = [epsilon_4cc['Lunge_O2'], sigma_4cc['Lunge_O2']]
    plot(x, lunge_fcc1, lunge_tcc, lunge_fcc2, '4')

    #Stomach
    stomach_fcc = [epsilon_4cc['Stomach'], sigma_4cc['Stomach']]
    stomach_tcc = [epsilon_2cc['Stomach'], sigma_2cc['Stomach']]
    plot(x, stomach_fcc, stomach_tcc)

    #Colon
    colon_fcc = [epsilon_4cc['Colon'], sigma_4cc['Colon']]
    colon_tcc = [epsilon_2cc['Colon'], sigma_2cc['Colon']]
    plot(x, colon_fcc, colon_tcc)

    #Small instestine
    small_fcc = [epsilon_4cc['Small_Instestine'], sigma_4cc['Small_Instestine']]
    small_tcc = [epsilon_2cc['Small_Instestine'], sigma_2cc['Small_Instestine']]
    plot(x, small_fcc, small_tcc)

    #Aort
    aort_tcc = [epsilon_2cc['Aort'], sigma_2cc['Aort']]
    plot(x,'', aort_tcc)

    #Brain
    brain_fcc1 = [epsilon_4cc['White_Matter'], sigma_4cc['White_Matter']]
    brain_fcc2 = [epsilon_4cc['Grey_Matter'], sigma_4cc['Grey_Matter']]
    plot(x, brain_fcc1,'', brain_fcc2, '4')

    #Bone
    bone_fcc1 = [epsilon_4cc['Cortex'], sigma_4cc['Cortex']]
    bone_fcc2 = [epsilon_4cc['Spongy_Bone'], sigma_4cc['Spongy_Bone']]
    marrow = [epsilon_4cc['Marrow'], sigma_4cc['Marrow']]
    plot(x, bone_fcc1, '', bone_fcc2, '4', marrow, '4')

    #Eye
    eye = [epsilon_4cc['Eye'], sigma_4cc['Eye']]
    plot(x, eye)

    #Genitals
    genitals_tcc1 = [epsilon_2cc['Fallopian'], sigma_2cc['Fallopian']]
    genitals_tcc2 = [epsilon_2cc['Ovary'], sigma_2cc['Ovary']]
    genitals_tcc3 = [epsilon_2cc['Uetrus'], sigma_2cc['Uetrus']]
    plot(x, '', genitals_tcc1, genitals_tcc2, '2', genitals_tcc3, '2')

    #Bladder
    bladder = [epsilon_2cc['Bladder'], sigma_2cc['Bladder']]
    plot(x, '', bladder)

    #Esophagus
    esophagus = [epsilon_2cc['Esophagus'], sigma_2cc['Esophagus']]
    plot(x, '', esophagus)

    #Gall_Bladder
    gall_bladder = [epsilon_2cc['Gall_Bladder'], sigma_2cc['Gall_Bladder']]
    plot(x, '' , gall_bladder)

    #Pancears
    pancears = [epsilon_2cc['Pancears'], sigma_2cc['Pancears']]
    plot(x, '', pancears)

    #Spleen
    spleen = [epsilon_2cc['Spleen'], sigma_2cc['Spleen']]
    plot(x, '', spleen)