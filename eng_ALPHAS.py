import pandas as pd
import streamlit  as st

st.title("🦍PROJET_ALPHAS🦍")
st.header('PROJET_ALPHAS BY  HOUNME HOUETO EMERICK GILLES')
st.title('UPLOADING OF MEALS PLAN')

ac=pd.read_csv(r'meals.txt', sep=',')

gluc=ac[ac.accompagnement=='No']
#gluc['aliments']=gluc['aliments(en moyenne)']

prot=ac[ac.accompagnement=='Yes']
sauce=ac[ac.accompagnement=='maybe']

gluc=ac.drop(ac[ac['categorie']=='sauce to'].index)
gluc=gluc.drop(gluc[gluc['categorie']=='gésier'].index)
gluc=gluc.drop(gluc[gluc['categorie']=='saucisse'].index)
gluc=gluc.drop(gluc[gluc['aliments']=='sauce tomate'].index)
gluc=gluc[gluc.accompagnement=='No']



prot['calories']=prot['calories (100g)']

#sauce['aliments']=sauce['aliments(en moyenne)']
sauce['calories']=sauce['calories (100g)']

a=gluc.sample()
a2=gluc['meals'].iloc[0]
a1=int(gluc.index[(gluc['meals']==a['meals'].iloc[0])][0])
crb_cal=a._get_value(a1, 'calories (100g)')
crb_name=a._get_value(a1, 'meals')
crb_cat=a._get_value(a1, 'categorie')


b=prot.sample()
b1=int(prot.index[(prot['meals']==b['meals'].iloc[0])][0])
bcaa_cal=b._get_value(b1, 'calories (100g)')
bcaa_name=b._get_value(b1, 'meals')

c=sauce.sample()
c1=int(sauce.index[(sauce['meals']==c['meals'].iloc[0])][0])

#bcaa_cal=b._get_value(b1, 'calories (100g)')

sauce_name=c._get_value(c1, 'meals')
sauce_cat=c._get_value(c1, 'categorie')

arachide=ac[ac.categorie=='arachide']
sucre=ac[ac.categorie=='sucre']
lait=ac[ac.categorie=='lait']

fit=pd.read_csv(r'exo_eng.txt', sep=',')

CARDIO=fit[fit.cibles=='cardio']
COURSE=fit[fit.cibles=='course']
abs1=fit[fit.cibles=='abs']
abs2=fit[fit.cibles=='abs']
PL=fit[fit.cibles=='plank']
abs3=fit[fit.cibles=="abs"]
SAT=fit[fit.cibles==' Squats']
QUA=fit[fit.cibles=='quads']
SDT=fit[fit.cibles=='Deadlift']
QMI=fit[fit.cibles=='quads']
QUI=fit[fit.cibles=='quads']
FES=fit[fit.cibles=='glutes']
BI=fit[fit.cibles=='Biceps']
TRI=fit[fit.cibles=='Triceps']
DAS=fit[fit.cibles=='middle and anterior delts']
DPT=fit[fit.cibles=='posterior delts and Traps']
TDR=fit[fit.cibles=='dorsal and Traps']
TER=fit[fit.cibles=='Traps']
DOX=fit[fit.cibles=='dorsal']
PS=fit[fit.cibles=='upper chest']
GP=fit[fit.cibles=='chest']
FP=fit[fit.cibles=='middle chest']
PI=fit[fit.cibles=='lower chest']


cardio=CARDIO.sample(5)
course=COURSE.sample()
cours=course["exercices"].iloc[0]
cours=cours.upper()

CAR=[]
for i in range(len(cardio)):
    a=cardio["exercices"].iloc[i]
    a=a.upper()
    CAR.append(a)
        
    
bi=BI.sample(3)
tr=TRI.sample(3)

das=DAS.sample(2)
dpt=DPT.sample(2)

tdr=TDR.sample(2)
dox=DOX.sample()

gp=GP.sample()
fp=FP.sample()
pi=PI.sample()


qua=QUA.sample()
qui=QUI.sample()


DOS=[]
tdr1=tdr['exercices'].iloc[0]
DOS.append(tdr1)
tdr1_n=tdr['cibles'].iloc[0]
DOS.append(tdr1_n)
tdr2=tdr['exercices'].iloc[1]
DOS.append(tdr2)
tdr2_n=tdr['cibles'].iloc[1]
DOS.append(tdr2_n)
dox1=dox['exercices'].iloc[0]
DOS.append(dox1)
dox1_n=dox['cibles'].iloc[0]
DOS.append(dox1_n)

PECS=[]
gp1=gp['exercices'].iloc[0]
PECS.append(gp1)
gp1_n=gp['cibles'].iloc[0]
PECS.append(gp1_n)
fp1=fp['exercices'].iloc[0]
PECS.append(fp1)
fp1_n=fp['cibles'].iloc[0]
PECS.append(fp1_n)
pi1=pi['exercices'].iloc[0]
PECS.append(pi1)
pi1_n=pi['cibles'].iloc[0]
PECS.append(pi1_n)

JAMBES=[]
sq=SAT['exercices'].iloc[0]
JAMBES.append(sq)
sdt=SDT['exercices'].iloc[0]
JAMBES.append(sdt)
qua1=qua['exercices'].iloc[0]
JAMBES.append(qua1)
qua1_n=qua['cibles'].iloc[0]
JAMBES.append(qua1_n)
qui1=qui['exercices'].iloc[0]
JAMBES.append(qui1)
qui1_n=qui['cibles'].iloc[0]
JAMBES.append(qui1_n)
    
    
    
BRAS=[]
b1=bi['exercices'].iloc[0]
BRAS.append(b1)
b1_n=bi['cibles'].iloc[0]
BRAS.append(b1_n)
b2=bi['exercices'].iloc[1]
BRAS.append(b2)
b2_n=bi['cibles'].iloc[1]
BRAS.append(b2_n)
b3=bi['exercices'].iloc[2]
BRAS.append(b3)
b3_n=bi['cibles'].iloc[2]
BRAS.append(b3_n)

t1=tr["exercices"].iloc[0]
BRAS.append(t1)
t1_n=tr['cibles'].iloc[0]
BRAS.append(t1_n)
t2=tr["exercices"].iloc[1]
BRAS.append(t2)
t2_n=tr['cibles'].iloc[1]
BRAS.append(t2_n)
t3=tr["exercices"].iloc[2]
BRAS.append(t3)
t3_n=tr['cibles'].iloc[2]
BRAS.append(t2_n)



EPAULES=[]
das1=das['exercices'].iloc[0]
EPAULES.append(das1)
das_n=das['cibles'].iloc[0]
EPAULES.append(das_n)
das2=das['exercices'].iloc[1]
EPAULES.append(das2)
das2_n=das['cibles'].iloc[1]
EPAULES.append(das2_n)

dpt1=dpt['exercices'].iloc[0]
EPAULES.append(dpt1)
dpt1_n=dpt['cibles'].iloc[0]
EPAULES.append(dpt1_n)
dpt2=dpt['exercices'].iloc[1]
EPAULES.append(dpt2)
dpt2_n=dpt['cibles'].iloc[1]
EPAULES.append(dpt2_n)

FESS=[]
FEs=FES.sample(4)
fes=FEs['exercices'].iloc[0]
FESS.append(fes)
fes1=FEs['exercices'].iloc[1]
FESS.append(fes1)
fes2=FEs['exercices'].iloc[2]
FESS.append(fes2)
fes3=FEs['exercices'].iloc[3]
FESS.append(fes3)

GD=abs1.sample(2)
AB=abs2.sample()
OB=abs3.sample(2)

ABS=[]
for i in range(2):
    a=GD["exercices"].iloc[i]
    c=OB["exercices"].iloc[i]
    
    a=a.upper()
    c=c.upper()

    ABS.append(a)
    ABS.append(c)
b=AB["exercices"].iloc[0]
b=b.upper()
ABS.append(b)
d=PL['exercices'].iloc[0]
d=d.upper()
ABS.append(d)



#def depense_calorique():
nom=st.text_input('Please enter your first and last name: ')

if type(nom) is not str:
    st.text('Invalid Input!')
elif type(nom) is str :
    if len(nom)>0:
        st.text(f'Welcome {nom}!')
        gen=st.radio("What's your birth's gender?: ",('Male','Female'))

        if gen=='Male':
            
            gender=0
        else:
            gender=1

        if gender==0:
            
            poid=st.number_input('Please enter your weight (in kg): \n',1,1000)
            
            if (poid>0):

                taill=st.number_input('Pleas enter your height (en cm): \n',1,1000)
                
                if (taill >0):
            
                    age=st.number_input('Please enter your age: \n',1,500)
        
            mba=(13.7516*poid) + (500.33*taill/100) - (6.7550*age) + 66.473
            mbb=(13.707*poid) + (492.3*taill/100) - (6.673*age) + 77.607
            
            
            MBh=(mba+mbb)/2
            
            if age>0:
                ap=st.radio("Did you have a regular sportive activity in the 12 last months?", ('no','yes'))
                if ap=='no':
                    dep_cal=MBh*1.1
                else:
                    freq=st.selectbox('What_s your regularity frequency?',[ 'less than 3 times per week' , "3 per week" , "more than 3 per week"])
                    if freq=='less than 3 times per week':
                        dep_cal=MBh*1.3
                    elif freq=='3 per week':
                        dep_cal=MBh*1.5
                    elif freq=='more than 3 per week':
                        dep_cal=MBh*1.7
            
        elif gender==1:
            poid=st.number_input('Please enter your weight(in kg): \n',1,1000)
            
            if (poid>0):

                taill=st.number_input('Please enter your height(in cm): \n',1,1000)
            
                if (taill >0):
            
                    age=st.number_input('Please enter your age: \n',1,500)
        
                
            mba=(9.5634*poid) + (184.96*taill/100) - (6.7556*age) + 655.0955
            mbb=(9.740*poid) + (172.9*taill/100) - (4.737*age) + 667.051
            
            MBf=(mba+mbb)/2
            
            if age>0:
                ap=st.radio("Did you have a regular sportive activity during the 12 last months?", ('no','yes'))
                if ap=='no':
                    dep_cal=MBf*1.21
                else:
                    freq=st.selectbox('What_s your physics activity frequency?',[ 'less than 3 times a week' , "3 times a week" , "more than 3 times a week"])
                    if freq=='less than 3 times a week':
                        dep_cal=MBf*1.3
                    elif freq=="3 times a week":
                        dep_cal=MBf*1.5
                    elif freq=='more than 3 times a week':
                        dep_cal=MBf*1.7
            # st.text(f'Votre métabolisme de base est de {MBf}')
        brek=dep_cal/3
        

        deficit=dep_cal-500
        night=deficit/10
        rest=deficit-night
        brek=rest/3
        lun=rest/3
        third=rest/3

        c=sauce.sample()
        c1=int(sauce.index[(sauce['meals']==c['meals'].iloc[0])][0])
        sauce_name=c._get_value(c1, 'meals')
        sauce_cat=c._get_value(c1, 'categorie')
        
        
        #ARACHIDE, SUCRE , LAITS
        cacahuete=arachide[['meals', 'calories (100g)', 'categorie']]
        ara=cacahuete.sample()
        ara1=int(ara.index[(ara['meals']==ara['meals'].iloc[0])][0])
        ara_cal=ara._get_value(ara1, 'calories (100g)')
        ara_name=ara._get_value(ara1, 'meals')
        ara_cate=ara._get_value(ara1, 'categorie')

        laits=lait[['meals', 'calories (100g)', 'categorie']]
        milk=laits.sample()
        milk1=int(milk.index[(milk['meals']==milk['meals'].iloc[0])][0])
        milk_cal=milk._get_value(milk1, 'calories (100g)')
        milk_name=milk._get_value(milk1, 'meals')
        milk_cate=milk._get_value(milk1, 'categorie')
        
        suc=sucre[['meals','calories (100g)', 'categorie']]
        suc1=int(suc.index[(suc['meals']==suc['meals'].iloc[0])][0])
        suc_cal=suc._get_value(suc1, 'calories (100g)')
        suc_name=suc._get_value(suc1, 'meals')
        suc_cate=suc._get_value(suc1, 'categorie')
            

        if (st.button('GENERATE MY MEAL PLAN')):
            st.subheader("IF YOU DON'T LIKE ONE MEAL PLAN, YOU CAN STILL GENERATE ANOTHER BY CLICKING ON GENERATE MY MEAL PLAN BUTTON. ANOTHER ONE WOULD BE GENERATE AUTOMATICALLY")
        
            st.text(f'Your daily_s calories expenditures are {dep_cal} calories and shared by a mean of {brek} calories per meals.')
            with open('ALPHAS_meals.txt', 'w') as f:
                pass
            for i in range (1,8,1):
                a=gluc.sample()
                a2=a['meals'].iloc[0]
                a1=int(gluc.index[(gluc['meals']==a['meals'].iloc[0])][0])
                crb_cal=a._get_value(a1, 'calories (100g)')
                crb_name=a._get_value(a1, 'meals')
                crb_cate=a._get_value(a1, 'categorie')
                b=prot.sample()
                b1=int(prot.index[(prot['meals']==b['meals'].iloc[0])][0])
                bcaa_cal=b._get_value(b1, 'calories (100g)')
                bcaa_name=b._get_value(b1, 'meals')

                bou=0.55*brek
                su=0.15*brek
                arak=0.15*brek
                laiti=0.15*brek
                p_cal=crb_cal
                p_name=crb_name
                bouil=bou*100/p_cal
                sug=su*100/suc_cal
                la=laiti*100/milk_cal
                araki=arak*100/ara_cal
        
        
                if (crb_cate=='fruit'):
                    oe=prot[prot.aliments=='oeuf(en moyenne)']
                    oe1=int(oe.index[(oe['meals']==oe['meals'].iloc[0])][0])
                    bcaa_cal=oe._get_value(oe1, 'calories (100g)')
                    bcaa_name=oe._get_value(oe1, 'meals')
            
        
        
                a1=0.6*(brek)
                b1=0.4*(brek)
                brek1=a1*100/crb_cal
                brek2=b1*100/bcaa_cal
        
        
                a=gluc.sample()
                a2=a['meals'].iloc[0]
                a1=int(gluc.index[(gluc['meals']==a['meals'].iloc[0])][0])
                crb_lun_cal=a._get_value(a1, 'calories (100g)')
                crb_lun_name=a._get_value(a1, 'meals')
                crb_lun_cate=a._get_value(a1, 'categorie')

                b=prot.sample()
                b1=int(prot.index[(prot['meals']==b['meals'].iloc[0])][0])
                bcaa_lun_cal=b._get_value(b1, 'calories (100g)')
                bcaa_lun_name=b._get_value(b1, 'meals')
        
                if (crb_lun_cate=='fruit'):
                    oe=prot[prot.aliments=='oeuf(en moyenne)']
                    oe1=(oe.index[(oe['meals']==oe['meals'].iloc[0])][0])
                    bcaa_lun_cal=oe._get_value(oe1, 'calories (100g)')
                    bcaa_lun_name=oe._get_value(oe1, 'meals')
            
               

                a1=0.6*(lun)
                a=a1/crb_lun_cal
                b1=0.4*(lun)
                b=b1/bcaa_lun_cal
                lun1=a*100
                lun2=b*100
        
        
        #third
                a=gluc.sample()
                a2=a['meals'].iloc[0]
                a1=int(gluc.index[(gluc['meals']==a['meals'].iloc[0])][0])
    #print(a2, a1)
                crb_t_cal=a._get_value(a1, 'calories (100g)')
                crb_t_name=a._get_value(a1, 'meals')
                crb_t_cate=a._get_value(a1, 'categorie')

                b=prot.sample()
                b1=int(prot.index[(prot['meals']==b['meals'].iloc[0])][0])
                bcaa_t_cal=b._get_value(b1, 'calories (100g)')
                bcaa_t_name=b._get_value(b1, 'aliments')
        
                if (crb_t_cate=='fruit'):
                    oe=prot[prot.aliments=='oeuf(en moyenne)']
                    oe1=(oe.index[(oe['meals']==oe['meals'].iloc[0])][0])
                    bcaa_t_cal=oe._get_value(oe1, 'calories (100g)')
                    bcaa_t_name=oe._get_value(oe1, 'meals')
            
            
        

                a1=0.6*(third)
                a=a1/crb_t_cal
                b1=0.4*(third)
                b=b1/bcaa_t_cal
                t1=a*100
                t2=b*100

                crb_cal=str(crb_cal)
                crb_lun_cal=str(crb_lun_cal)
                crb_t_cal=str(crb_t_cal)
                sug=str(sug)
                la=str(la)
                araki=str(araki)

                if (crb_cate=='bouillie'):
                    ch={crb_name:crb_cal,suc_name:sug}
                    LM={milk_name:la,ara_name:araki}
                    
                    brek1=crb_cal+' grammes de '+crb_name +', '+ sug
                    crb_name=' '+suc_name+', '
                    brek2=la+' grammes de '+milk_name+' et de '+araki
                    bcaa_name=' '+ara_name

                if (crb_lun_cate=='bouillie'):
                    ch={crb_lun_name:crb_lun_cal,suc_name:sug}
                    LM={milk_name:la,ara_name:araki}
                        
                    lun1=crb_lun_cal+' grammes de '+crb_lun_name+', '+sug
                    crb_lun_name=' '+suc_name+', '
                    lun2=la+' grammes de '+milk_name+' et de '+araki
                    bcaa_lun_name=' '+ara_name
                
                if (crb_t_cate=='bouillie'):
                    ch={crb_t_name:crb_t_cal,suc_name:sug}
                    LM={milk_name:la,ara_name:araki}
                    
                    t1=crb_t_cal+' grammes de '+crb_t_name+', '+sug
                    crb_t_name=' '+suc_name+', '
                    t2=la+' grammes de '+milk_name+' et de '+araki
                    bcaa_t_name=' '+ara_name
        
                if (crb_cate=='pâte'):
                    crb_name=crb_name+' et '+sauce_name
                if (crb_lun_cate=='pâte'):
                    crb_lun_name=crb_lun_name+' et '+sauce_name
                if (crb_t_cate=='pâte'):
                    crb_t_name=crb_t_name+' et '+sauce_name
            
                st.text(f'\n\n, The breakfast of day {i} is {brek1} grammes of {crb_name} and {brek2} grammes of {bcaa_name},\n The lunch is {lun1} grammes of {crb_lun_name} and {lun2} grammes of {bcaa_lun_name}, \n The third is {t1} grammes of {crb_t_name} and {t2} grammes of {bcaa_t_name} \n')
                with open('ALPHAS_meals.txt', "a") as f:
                    f.write(f'Your daily calories expenditures are {dep_cal} calories and the mean of a daily meal are {brek} calories')
            
                    f.write(f'\n\n, The breakfast of the day {i} is {brek1} grammes of {crb_name} and {brek2} grammes of {bcaa_name},\n The lunch is  {lun1} grammes of {crb_lun_name} and {lun2} grammes of {bcaa_lun_name}, \n The last is {t1} grammes of {crb_t_name} and {t2} grammes of {bcaa_t_name} \n')
            
            def telecharger_fichier():
                    with open (r'ALPHAS_meals.txt', 'r') as f:
                        contenu=f.read()
                    return contenu.encode()
            def main():
                    st.subheader('DOWNLOAD MY MEAL PLAN')
                    wish=st.radio( "AGREE AND WANNA DOWNLOAD THIS MEAL PLAN?",('yes','no'))
                    
                    if wish=='yes':
                        fichier=telecharger_fichier()
                        st.download_button(
                            label="DOWNLOAD MY PLAN",
                            data=fichier,
                            file_name=r'ALPHAS_meals.txt',
                            mime='text/plain'
                        )
                    else:
                        pass
            if __name__=="__main__":
                    main()

#st.title('TELECHARGEMENT DU PLAN D_ENTRAINEMENT')
st.header("DO YOU WANT A TRAINING PLAN TOO?")
plan= st.radio('MAKE ONE CHOICE',('None','no','yes'))
if plan=='None':
    pass 
elif plan=='no':
    st.text('Right! Enjoy your meal plan only.')
else:
    st.title("DOWNLOADING OF TRAINING PLAN")
    poids=st.number_input("Enter your weight in kg: ", 0)
    t=st.number_input('Enter your height in cm:',1)
    taille=t/100
    imc=(poids/(taille*taille))


    sexe=st.radio("What's your birth's gender?",('None','Male','Female'))

    if sexe=='Male':
        if (imc<16):
            st.text("Your plan will be available soon.We will notice you when it will be done.")
        elif(imc>=16 and imc<=18.5):
            st.warning("Your plan will be available soon.We will notice you when it will be done.")

        elif (imc>= 18.5 and imc<=25):
            
            p=st.radio('What program do you choose?',('None', 'bodyweight','machine and dumbells'))

            if p=="None":
                pass
            elif p=='bodyweight':
                cardio=CARDIO.sample(5)
                course=COURSE.sample()
                cours=course["exercices"].iloc[0]
                cours=cours.upper()


                PDC=fit[fit.cibles=='pdc']
                pd_c=PDC.sample(7)
                Pdc=[]
                for i in range(len(pd_c)):
                    z=pd_c['exercices'].iloc[i] 
                    z=z.upper()
                    Pdc.append(z)

                CAR=[]
                for i in range(len(cardio)):
                    a=cardio["exercices"].iloc[i]
                    a=a.upper()
                    CAR.append(a)
                GD=abs1.sample(2)
                AB=abs2.sample()
                OB=abs3.sample(2)

                ABS=[]
                for i in range(2):
                    a=GD["exercices"].iloc[i]
                    c=OB["exercices"].iloc[i]
                    
                    a=a.upper()
                    c=c.upper()

                    ABS.append(a)
                    ABS.append(c)
                b=AB["exercices"].iloc[0]
                b=b.upper()
                ABS.append(b)
                d=PL['exercices'].iloc[0]
                d=d.upper()
                ABS.append(d)

                exp=st.radio("How do you rate your physics activity's degree experience?",('None','beginner', 'intermediate', 'advanced'))
                    

                if(st.button('GENERATE MY TRAINING PROGRAMME:')):
                    if (exp=='beginner'):
                        st.text(f'Your bmi is {imc}. and below your program:\n\n')
                        st.text(f'Your bmi is  {imc} and below there is your program of training:\n\n')
                        st.text(f'\n For every training for the 4 next week we have :\n\n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n after 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and the for last 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between the exercise changement is 1 minute.')
                        st.text(f"\n\nAfter for train the abs you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 1 minute of rest between every exercise.\n\n")
                        st.text("Then you take 5mins of rest and you start body weight exercise. \n\n")
                    
                    
                        st.text(f"We have 3 sets of 10 reps of  {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n and of  {Pdc[6]}")
                        st.text("The rest time is 45 secondes. The rest time between every exercise is 2min.")

                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Your bmi is  {imc} and below there is your program of training:\n\n')
                            f.write(f'\n For every training for the 4 next week we have :\n\n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n after 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and the for last 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between the exercise changement is 1 minute.')
                            f.write(f"\n\nAfter for train the abs you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 1 minute of rest between every exercise.\n\n")
                            f.write("Then you take 5mins of rest and you start body weight exercise. \n\n")
                            f.write(f"We have 3 sets of 10 reps of  {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n and of  {Pdc[6]}")
                            f.write("The rest time is 45 secondes. The rest time between every exercise is 2min.")


                    elif (exp=='intermediate'):
                        st.text(f'Your bmi is  {imc} and below there is your program of training:\n\n')
                        st.text(f'\n For every training for the 4 next week we have :\n\n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n after 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and the for last 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between the exercise changement is 1 minute.')
                        st.text(f"\n\nAfter for train the abs you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 1 minute of rest between every exercise.\n\n")
                        st.text("Then you take 5mins of rest and you start body weight exercise. \n\n")

                        st.text(f"We have 5 sets of 10 reps of  {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n and of  {Pdc[6]}")
                        st.text("The rest time is 30 secondes. The rest time between every exercise is 2min.")
                        with open('ALPHAS.txt', 'w') as f:
                            pass  

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Your bmi is  {imc} and below there is your program of training:\n\n')
                            f.write(f'\n For every training for the 4 next week we have :\n\n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n after 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and the for last 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between the exercise changement is 1 minute.')
                            f.write(f"\n\nAfter for train the abs you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 1 minute of rest between every exercise.\n\n")
                            f.write("Then you take 5mins of rest and you start body weight exercise. \n\n")
                            f.write(f"We have 5 sets of 10 reps of  {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n and of  {Pdc[6]}")
                            f.write("The rest time is 30 secondes. The rest time between every exercise is 2min.")

                    elif (exp=='avdvanced'):

                        st.text(f'Your bmi is  {imc} and below there is your program of training:\n\n')
                        st.text(f'\n For every training for the 4 next week we have :\n\n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n after 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and the for last 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between the exercise changement is 1 minute.')
                        st.text(f"\n\nAfter for train the abs you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 1 minute of rest between every exercise.\n\n")
                        st.text("Then you take 5mins of rest and you start body weight exercise. \n\n")
                        st.text(f"We have 7 sets of 10 reps of  {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n and of  {Pdc[6]}")
                        st.text("The rest time is 30 secondes. The rest time between every exercise is 2min.")
                        with open('ALPHAS.txt', 'w') as f:
                            pass
          

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Your bmi is  {imc} and below there is your program of training:\n\n')
                            f.write(f'\n For every training for the 4 next week we have :\n\n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n then 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n after 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and the for last 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between the exercise changement is 1 minute.')
                            f.write(f"\n\nAfter for train the abs you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 1 minute of rest between every exercise.\n\n")
                            f.write("Then you take 5mins of rest and you start body weight exercise. \n\n")

                            f.write(f"We have 7 sets of 10 reps of  {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n and of  {Pdc[6]}")
                            f.write("The rest time is 30 secondes. The rest time between every exercise is 2min.")

                            
                        st.subheader('THE PROGRAM SHOULD BE DONE AT LEAST 4 TIMES A WEEK AVEC WITH 3 DAYS OF REST.')
            elif p=='machine and dumbells':
                nombre=st.number_input('How many times can you lift a week? Choose a number between 4 and 6: \n')    
                
                a=fit[fit.exercices=='Dumbbell Lateral Raises']
                a0=a['exercices'].iloc[0]
                a1=a['cibles'].iloc[0]
                d=fit[fit.exercices=='Vertical chest pull']
                d0=d['exercices'].iloc[0]
                d1=d['cibles'].iloc[0]
                DAS=DAS.drop(DAS[DAS['exercices']=='Dumbbell Lateral Raises'].index)
                DOX=DOX.drop(DOX[DOX['exercices']=='Vertical chest pull'].index)
                
                if (nombre<4 and nombre>6):
                    st.text('Invalid input!')
                if(nombre==4):
                    if nombre>1:
                        (st.button('GENERATE YOUR TRAINING PROGRAM'))
                        st.text(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                        st.text(f'For the days 1 and 3 we have : Back,chest and shoulders .Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after {DOS[2]} to train {DOS[3]}, \n and {d0} to train {d1}.\n\n For the chest we have: {PECS[0]} to train {PECS[1]},\n then {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} to train {PECS[5]}.\n\n \n For the shoulder, we have: {a0} to train {a1},\n then {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} to train {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                        st.text(f'\n\n For the days 2 and 4 we start with biceps ,triceps and legs.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the biceps and thr Triceps:  {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for {BRAS[3]}, \n and {BRAS[4]} for {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n then {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n For the legs:  {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for {JAMBES[3]}, \n and {JAMBES[4]} to train legs {JAMBES[5]}.\n\n You should observe 3 days of rest per week without train consecutively. ')
                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                            f.write(f'For the days 1 and 3 we have : Back,chest and shoulders .Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after {DOS[2]} to train {DOS[3]}, \n and {d0} to train {d1}.\n\n For the chest we have: {PECS[0]} to train {PECS[1]},\n then {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} to train {PECS[5]}.\n\n \n For the shoulder, we have: {a0} to train {a1},\n then {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} to train {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                            f.write(f'\n\n For the days 2 and 4 we start with biceps ,triceps and legs.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the biceps and thr Triceps:  {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for {BRAS[3]}, \n and {BRAS[4]} for {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n then {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n For the legs:  {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for {JAMBES[3]}, \n and {JAMBES[4]} to train legs {JAMBES[5]}.\n\n You should observe 3 days of rest per week without train consecutively. ')
                    
                elif(nombre==5):
                    if(st.button('GENERATE YOUR TRAINING PROGRAM')):
                        st.text(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                        st.text(f'For the days 1 , 3 and 5 of the 4 next weeks, we have back,chest and shoulders.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after {DOS[2]} to train {DOS[3]}, \n and {d0} to train {d1}.\n\n For the chest we have: {PECS[0]} to train {PECS[1]},\n then {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} to train {PECS[5]}.\n\n \n For the shoulder, we have: {a0} to train {a1},\n then {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} to train {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                        st.text(f'\n\n For the days 2 and 4 we start with biceps ,triceps and legs.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the biceps and thr Triceps:  {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for {BRAS[3]}, \n and {BRAS[4]} for {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n then {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n For the legs:  {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for {JAMBES[3]}, \n and {JAMBES[4]} to train legs {JAMBES[5]}.\n\n You should observe 3 days of rest per week without train consecutively. ')
                        
                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                            f.write(f'For the days 1 , 3 and 5 of the 4 next weeks, we have back,chest and shoulders.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after {DOS[2]} to train {DOS[3]}, \n and {d0} to train {d1}.\n\n For the chest we have: {PECS[0]} to train {PECS[1]},\n then {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} to train {PECS[5]}.\n\n \n For the shoulder, we have: {a0} to train {a1},\n then {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} to train {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                            f.write(f'\n\n For the days 2 and 4 we start with biceps ,triceps and legs.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the biceps and thr Triceps:  {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for {BRAS[3]}, \n and {BRAS[4]} for {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n then {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n For the legs:  {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for {JAMBES[3]}, \n and {JAMBES[4]} to train legs {JAMBES[5]}.\n\n You should observe 3 days of rest per week without train consecutively. ')

            
                elif (nombre==6):
                    if(st.button('GENERATE YOUR TRAINING PROGRAM')):
                        st.text(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                        st.text(f'For the days 1 and 4 we have on program: Back and shoulders.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back, we have: {DOS[0]} for train {DOS[1]},\n then {DOS[2]} to train {DOS[3]}, \n and {d0} for {d1}.\n\n For the chest, we have:  {PECS[0]} for train {PECS[1]},\n\n \n For the shoulders ,we have : {a0} for {a1},\n then {EPAULES[2]} for the {EPAULES[3]}, \n and {EPAULES[4]} for the {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                        st.text(f'\n\n For the days 2 and 5 we_ll train chest, biceps and triceps.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise:\n\n \n {PECS[0]} to train {PECS[1]}, {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} for the {PECS[5]},\n\n For the biceps,we have: {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for the {BRAS[3]}, \n and {BRAS[4]} to train {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n and {BRAS[8]} for training of  {BRAS[9]}, \n and {BRAS[10]} to train {BRAS[11]}')
                        st.text(f'\n \n For the days 3 and 6 we train legs.We start with: \n\n {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for the {JAMBES[3]}, \n and {JAMBES[4]} to train {JAMBES[5]}.')
                        
                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                            f.write(f'For the days 1 and 4 we have on program: Back and shoulders.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back, we have: {DOS[0]} for train {DOS[1]},\n then {DOS[2]} to train {DOS[3]}, \n and {d0} for {d1}.\n\n For the chest, we have:  {PECS[0]} for train {PECS[1]},\n\n \n For the shoulders ,we have : {a0} for {a1},\n then {EPAULES[2]} for the {EPAULES[3]}, \n and {EPAULES[4]} for the {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                            f.write(f'\n\n For the days 2 and 5 we_ll train chest, biceps and triceps.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise:\n\n \n {PECS[0]} to train {PECS[1]}, {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} for the {PECS[5]},\n\n For the biceps,we have: {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for the {BRAS[3]}, \n and {BRAS[4]} to train {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n and {BRAS[8]} for training of  {BRAS[9]}, \n and {BRAS[10]} to train {BRAS[11]}')
                            f.write(f'\n \n For the days 3 and 6 we train legs.We start with: \n\n {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for the {JAMBES[3]}, \n and {JAMBES[4]} to train {JAMBES[5]}.')
        elif (imc>=25 and imc<=30):
            if imc>=25 and imc<=30:

                a=fit[fit.exercices=='Incline Dumbbell Lateral Raises']
                a0=a['exercices'].iloc[0]
                a1=a['cibles'].iloc[0]
                d=fit[fit.exercices=='Vertical chest pull']
                d0=d['exercices'].iloc[0]
                d1=d['cibles'].iloc[0]
                DAS=DAS.drop(DAS[DAS['exercices']=='Incline Dumbbell Lateral Raises'].index)
                DOX=DOX.drop(DOX[DOX['exercices']=='Vertical chest pull'].index)
                nombre=st.number_input('How many times can you lift a week? Choose a number between 4 and 6: \n')    
                
                if (nombre<4 and nombre>6):
                    st.text('Invalid input!')
                if(nombre==4):
                    if(st.button('GENERATE YOUR TRAINING PROGRAM')):
                        st.text(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                        st.text(f'For the days 1 and 3 we have : Back,chest and shoulders .Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after {DOS[2]} to train {DOS[3]}, \n and {d0} to train {d1}.\n\n For the chest we have: {PECS[0]} to train {PECS[1]},\n then {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} to train {PECS[5]}.\n\n \n For the shoulder, we have: {a0} to train {a1},\n then {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} to train {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                        st.text(f'\n\n For the days 2 and 4 we start with biceps ,triceps and legs.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the biceps and thr Triceps:  {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for {BRAS[3]}, \n and {BRAS[4]} for {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n then {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n For the legs:  {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for {JAMBES[3]}, \n and {JAMBES[4]} to train legs {JAMBES[5]}.\n\n You should observe 3 days of rest per week without train consecutively. ')
                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                            f.write(f'For the days 1 and 3 we have : Back,chest and shoulders .Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after {DOS[2]} to train {DOS[3]}, \n and {d0} to train {d1}.\n\n For the chest we have: {PECS[0]} to train {PECS[1]},\n then {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} to train {PECS[5]}.\n\n \n For the shoulder, we have: {a0} to train {a1},\n then {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} to train {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                            f.write(f'\n\n For the days 2 and 4 we start with biceps ,triceps and legs.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the biceps and thr Triceps:  {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for {BRAS[3]}, \n and {BRAS[4]} for {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n then {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n For the legs:  {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for {JAMBES[3]}, \n and {JAMBES[4]} to train legs {JAMBES[5]}.\n\n You should observe 3 days of rest per week without train consecutively. ')
                



                elif(nombre==5):
                    if(st.button('GENERATE YOUR TRAINING PROGRAM')):
                        st.text(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                        st.text(f'For the days 1 , 3 and 5 of the 4 next weeks, we have back,chest and shoulders.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after {DOS[2]} to train {DOS[3]}, \n and {d0} to train {d1}.\n\n For the chest we have: {PECS[0]} to train {PECS[1]},\n then {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} to train {PECS[5]}.\n\n \n For the shoulder, we have: {a0} to train {a1},\n then {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} to train {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                        st.text(f'\n\n For the days 2 and 4 we start with biceps ,triceps and legs.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the biceps and thr Triceps:  {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for {BRAS[3]}, \n and {BRAS[4]} for {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n then {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n For the legs:  {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for {JAMBES[3]}, \n and {JAMBES[4]} to train legs {JAMBES[5]}.\n\n You should observe 3 days of rest per week without train consecutively. ')
                        
                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                            f.write(f'For the days 1 , 3 and 5 of the 4 next weeks, we have back,chest and shoulders.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after {DOS[2]} to train {DOS[3]}, \n and {d0} to train {d1}.\n\n For the chest we have: {PECS[0]} to train {PECS[1]},\n then {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} to train {PECS[5]}.\n\n \n For the shoulder, we have: {a0} to train {a1},\n then {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} to train {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                            f.write(f'\n\n For the days 2 and 4 we start with biceps ,triceps and legs.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the biceps and thr Triceps:  {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for {BRAS[3]}, \n and {BRAS[4]} for {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n then {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n For the legs:  {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for {JAMBES[3]}, \n and {JAMBES[4]} to train legs {JAMBES[5]}.\n\n You should observe 3 days of rest per week without train consecutively. ')
                            
            
                elif (nombre==6):
                    if(st.button('GENERATE YOUR TRAINING PROGRAM')):
                        st.text(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                        st.text(f'For the days 1 and 4 we have on program: Back and shoulders.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back, we have: {DOS[0]} for train {DOS[1]},\n then {DOS[2]} to train {DOS[3]}, \n and {d0} for {d1}.\n\n For the chest, we have:  {PECS[0]} for train {PECS[1]},\n\n \n For the shoulders ,we have : {a0} for {a1},\n then {EPAULES[2]} for the {EPAULES[3]}, \n and {EPAULES[4]} for the {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                        st.text(f'\n\n For the days 2 and 5 we_ll train chest, biceps and triceps.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise:\n\n \n {PECS[0]} to train {PECS[1]}, {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} for the {PECS[5]},\n\n For the biceps,we have: {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for the {BRAS[3]}, \n and {BRAS[4]} to train {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n and {BRAS[8]} for training of  {BRAS[9]}, \n and {BRAS[10]} to train {BRAS[11]}')
                        st.text(f'\n \n For the days 3 and 6 we train legs.We start with: \n\n {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for the {JAMBES[3]}, \n and {JAMBES[4]} to train {JAMBES[5]}.')
                        
                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Your bmi is {imc} and below your program for the 4 next weeks:\n\n')
                            f.write(f'For the days 1 and 4 we have on program: Back and shoulders.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise :\n\n For the back, we have: {DOS[0]} for train {DOS[1]},\n then {DOS[2]} to train {DOS[3]}, \n and {d0} for {d1}.\n\n For the chest, we have:  {PECS[0]} for train {PECS[1]},\n\n \n For the shoulders ,we have : {a0} for {a1},\n then {EPAULES[2]} for the {EPAULES[3]}, \n and {EPAULES[4]} for the {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}.')
                            f.write(f'\n\n For the days 2 and 5 we_ll train chest, biceps and triceps.Here we have the exercise that will be done at a 3 sets of 10 reps at least for every exercise:\n\n \n {PECS[0]} to train {PECS[1]}, {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} for the {PECS[5]},\n\n For the biceps,we have: {BRAS[0]} to train {BRAS[1]},\n after {BRAS[2]} for the {BRAS[3]}, \n and {BRAS[4]} to train {BRAS[5]}, \n\n{BRAS[6]} to train {BRAS[7]},\n and {BRAS[8]} for training of  {BRAS[9]}, \n and {BRAS[10]} to train {BRAS[11]}')
                            f.write(f'\n \n For the days 3 and 6 we train legs.We start with: \n\n {JAMBES[0]},\n {JAMBES[1]},\n and {JAMBES[2]} for the {JAMBES[3]}, \n and {JAMBES[4]} to train {JAMBES[5]}.')
                            

        elif(imc>=30 and imc<35):
                nombre=st.number_input('Combien de fois pouvez-vous vous entrainer par semaine? Choissisez entre 3 et 5\n')
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')

                    if (nombre<3 and nombre>5):
                        st.text('Valeur invalide')
                    nombre=st.number_input('How many times can you train a week? Choose a number between 3 and 5\n')
                if(st.button('GENERATE MY TRAINING PLAN')):
                    st.text(f'Your bmi is {imc} and that_s your program:\n\n')

                    if (nombre<3 and nombre>5):
                        st.text('Invalid input!')
                    if (imc>=30 and imc<35):
                        if(nombre==3):
                            st.text(f'For the days 1 and 3 let_s start with 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you_ll do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n After we_ll train back, chest and legs.For exercise you_ll do at least 3sets of 10 reps :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after we have {DOS[2]} to train {DOS[3]}, \n and {DOS[4]} to train {DOS[5]}.\n\n For chest we have:{PECS[0]} for the {PECS[1]},\n after {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} for the {PECS[5]}.\n\n To train legs we have, {JAMBES[0]},\n  {JAMBES[1]},\n and the {JAMBES[2]} for the {JAMBES[3]}, \n and the {JAMBES[4]} to train {JAMBES[5]}')
                            st.text(f'\n\nFor the day 2 let_s start with 10min of {cours} and then we have: \n 3 sets of 30 secs of exercise and 30 secs of rest of: {CAR[0]},\n after you have 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest time between the exercise changement is 2 minutes.  \n\n After we have to train the biceps , the triceps and the shoulders.\n You should do every exercise at least 3 sets of 10 reps.We have  :\n\n {BRAS[0]} to train {BRAS[1]},\n and {BRAS[2]} to train {BRAS[3]}, \n and {BRAS[4]} to train {BRAS[5]}, \n\n{BRAS[6]} for the {BRAS[7]},\n and {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n For the shoulders: {EPAULES[0]} to train {EPAULES[1]},\n and {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} for the {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]} ')
                            
                            with open('ALPHAS.txt', 'w') as f:
                                pass
                            
                            with open('ALPHAS.txt', 'a') as f:
                                f.write(f'For the days 1 and 3 let_s start with 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you_ll do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n After we_ll train back, chest and legs.For exercise you_ll do at least 3sets of 10 reps :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after we have {DOS[2]} to train {DOS[3]}, \n and {DOS[4]} to train {DOS[5]}.\n\n For chest we have:{PECS[0]} for the {PECS[1]},\n after {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} for the {PECS[5]}.\n\n To train legs we have, {JAMBES[0]},\n  {JAMBES[1]},\n and the {JAMBES[2]} for the {JAMBES[3]}, \n and the {JAMBES[4]} to train {JAMBES[5]}')
                                f.write(f'\n\nFor the day 2 let_s start with 10min of {cours} and then we have: \n 3 sets of 30 secs of exercise and 30 secs of rest of: {CAR[0]},\n after you have 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest time between the exercise changement is 2 minutes.  \n\n After we have to train the biceps , the triceps and the shoulders.\n You should do every exercise at least 3 sets of 10 reps.We have  :\n\n {BRAS[0]} to train {BRAS[1]},\n and {BRAS[2]} to train {BRAS[3]}, \n and {BRAS[4]} to train {BRAS[5]}, \n\n{BRAS[6]} for the {BRAS[7]},\n and {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n For the shoulders: {EPAULES[0]} to train {EPAULES[1]},\n and {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} for the {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]} ')

                        
                        elif(nombre==4):
                            st.text(f'For the days 1 and 3 let_s start with 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you_ll do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n After we_ll train back, chest and legs.For exercise you_ll do at least 3sets of 10 reps :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after we have {DOS[2]} to train {DOS[3]}, \n and {DOS[4]} to train {DOS[5]}.\n\n For chest we have:{PECS[0]} for the {PECS[1]},\n after {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} for the {PECS[5]}.\n\n \n For the shoulders we have {EPAULES[0]} to train {EPAULES[1]},\n and {EPAULES[2]} for the {EPAULES[3]}, \n and {EPAULES[4]} to train {EPAULES[5]}, \n{EPAULES[6]}for the {EPAULES[7]}')
                            st.text(f'\n\n For the days 2 and 4 let_s start with 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you_ll do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min. After you have : \n\n the biceps , the triceps and the shoulders.\n You should do every exercise at least 3 sets of 10 reps.We have  :\n\n {BRAS[0]} to train {BRAS[1]},\n and {BRAS[2]} to train {BRAS[3]}, \n and {BRAS[4]} to train {BRAS[5]}, \n\n{BRAS[6]} for the {BRAS[7]},\n and {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n To train legs we have, {JAMBES[0]},\n  {JAMBES[1]},\n and the {JAMBES[2]} for the {JAMBES[3]}, \n and the {JAMBES[4]} to train {JAMBES[5]}.\n\n You should observe 3 days of rest a week and train without train consecutively.')
                            
                            with open('ALPHAS.txt', 'w') as f:
                                pass
                            
                            with open('ALPHAS.txt', 'a') as f:
                                f.write(f'For the days 1 and 3 let_s start with 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you_ll do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n After we_ll train back, chest and legs.For exercise you_ll do at least 3sets of 10 reps :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after we have {DOS[2]} to train {DOS[3]}, \n and {DOS[4]} to train {DOS[5]}.\n\n For chest we have:{PECS[0]} for the {PECS[1]},\n after {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} for the {PECS[5]}.\n\n \n For the shoulders we have {EPAULES[0]} to train {EPAULES[1]},\n and {EPAULES[2]} for the {EPAULES[3]}, \n and {EPAULES[4]} to train {EPAULES[5]}, \n{EPAULES[6]}for the {EPAULES[7]}')
                                f.write(f'\n\n For the days 2 and 4 let_s start with 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you_ll do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min. After you have : \n\n the biceps , the triceps and the shoulders.\n You should do every exercise at least 3 sets of 10 reps.We have  :\n\n {BRAS[0]} to train {BRAS[1]},\n and {BRAS[2]} to train {BRAS[3]}, \n and {BRAS[4]} to train {BRAS[5]}, \n\n{BRAS[6]} for the {BRAS[7]},\n and {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n To train legs we have, {JAMBES[0]},\n  {JAMBES[1]},\n and the {JAMBES[2]} for the {JAMBES[3]}, \n and the {JAMBES[4]} to train {JAMBES[5]}.\n\n You should observe 3 days of rest a week and train without train consecutively.')
                            
                        elif(nombre==5):
                            st.text(f'For the days 1, 3 and 5 of 4 next weeks let_s start with 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you_ll do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n After we_ll train back, chest and legs.For exercise you_ll do at least 3sets of 10 reps :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after we have {DOS[2]} to train {DOS[3]}, \n and {DOS[4]} to train {DOS[5]}.\n\n For chest we have:{PECS[0]} for the {PECS[1]},\n after {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} for the {PECS[5]}.\n\n \n For the shoulders: {EPAULES[0]} to train {EPAULES[1]},\n and {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} for the {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}')
                            st.text(f'\n\n For the days 2 and 4 let_s start with 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you_ll do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min. After you have : \n\n the biceps , the triceps and the shoulders.\n You should do every exercise at least 3 sets of 10 reps.We have  :\n\n {BRAS[0]} to train {BRAS[1]},\n and {BRAS[2]} to train {BRAS[3]}, \n and {BRAS[4]} to train {BRAS[5]}, \n\n{BRAS[6]} for the {BRAS[7]},\n and {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n To train legs we have, {JAMBES[0]},\n  {JAMBES[1]},\n and the {JAMBES[2]} for the {JAMBES[3]}, \n and the {JAMBES[4]} to train {JAMBES[5]}.\n\n You should observe 3 days of rest a week and train without train consecutively')
                            
                            with open('ALPHAS.txt', 'w') as f:
                                pass
                            
                            with open('ALPHAS.txt', 'a') as f:
                                f.write(f'For the days 1, 3 and 5 of 4 next weeks let_s start with 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you_ll do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n After we_ll train back, chest and legs.For exercise you_ll do at least 3sets of 10 reps :\n\n For the back we have: {DOS[0]} to train {DOS[1]},\n after we have {DOS[2]} to train {DOS[3]}, \n and {DOS[4]} to train {DOS[5]}.\n\n For chest we have:{PECS[0]} for the {PECS[1]},\n after {PECS[2]} for the {PECS[3]}, \n and {PECS[4]} for the {PECS[5]}.\n\n \n For the shoulders: {EPAULES[0]} to train {EPAULES[1]},\n and {EPAULES[2]} to train {EPAULES[3]}, \n and {EPAULES[4]} for the {EPAULES[5]}, \n{EPAULES[6]} to train {EPAULES[7]}')
                                f.write(f'\n\n For the days 2 and 4 let_s start with 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you_ll do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min. After you have : \n\n the biceps , the triceps and the shoulders.\n You should do every exercise at least 3 sets of 10 reps.We have  :\n\n {BRAS[0]} to train {BRAS[1]},\n and {BRAS[2]} to train {BRAS[3]}, \n and {BRAS[4]} to train {BRAS[5]}, \n\n{BRAS[6]} for the {BRAS[7]},\n and {BRAS[8]} for the {BRAS[9]}, \n and {BRAS[10]} for the {BRAS[11]},\n \n To train legs we have, {JAMBES[0]},\n  {JAMBES[1]},\n and the {JAMBES[2]} for the {JAMBES[3]}, \n and the {JAMBES[4]} to train {JAMBES[5]}.\n\n You should observe 3 days of rest a week and train without train consecutively')

        elif(imc>=35 and imc<40):
            cardio=CARDIO.sample(5)
            course=COURSE.sample()
            cours=course["exercices"].iloc[0]
            cours=cours.upper()

            CAR=[]
            for i in range(len(cardio)):
                a=cardio["exercices"].iloc[i]
                a=a.upper()
                CAR.append(a)
            GD=abs1.sample(2)
            AB=abs2.sample()
            OB=abs3.sample(2)

            ABS=[]
            for i in range(2):
                a=GD["exercices"].iloc[i]
                c=OB["exercices"].iloc[i]
                
                a=a.upper()
                c=c.upper()

                ABS.append(a)
                ABS.append(c)
            b=AB["exercices"].iloc[0]
            b=b.upper()
            ABS.append(b)
            d=PL['exercices'].iloc[0]
            d=d.upper()
            ABS.append(d)
        
            nombre=st.number_input('How many times can you train a week? Choose a number between 3 and 5: \n')
            
            if (nombre<3 and nombre>5):
                    st.text('Valeur invalide')
            if (nombre==3):
                if(st.button('GENERATE MY TRAINING PLAN')):
                    st.text(f'Your bmi is {imc} and that_s your program:\n\n')
                    st.text(f'\nFor every training for the 4 next weeks we have 15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.')
                    st.text(f"\n\n In add, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n Between two days of training, observe one day of rest. ")
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass

                    with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Your bmi is {imc} and that_s your program:\n\n')
                            f.write(f'\nFor every training for the 4 next weeks we have 15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.')
                            f.write(f"\n\n In add, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n Between two days of training, observe one day of rest. ")
            elif (nombre==4):
                if(st.button('GENERATE MY TRAINING PLAN')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nFor every training for the 4 next weeks we have 15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.')
                    st.text(f"\n\n In add, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n You should have 3 days of rest per week without train consecutively.")
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Your bmi is {imc} and that_s your program:\n\n')
                            f.write(f'\nFor every training for the 4 next weeks we have 15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.')
                            f.write(f"\n\n In add, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n You should have 3 days of rest per week without train consecutively.")
                            
            
            
            elif(nombre==5):
                if(st.button('GENERATE TRAINING PLAN')):
                    st.text(f'Your bmi is {imc} and that_s your program:\n\n')
                    st.text(f'\nFor every training for the 4 next weeks we have 15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.')
                    st.text(f"\n\n In add, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n You should have 3 days of rest per week without train consecutively.")
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass

                    with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            f.write(f'\nFor every training for the 4 next weeks we have 15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.')
                            f.write(f"\n\n In add, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n You should have 3 days of rest per week without train consecutively.")
                            

        
        elif (imc>40):
            z=COURSE["exercices"].iloc[0]
            z=z.upper()
            z0=COURSE["exercices"].iloc[1]
            z0=z0.upper()
            z1=COURSE["exercices"].iloc[2]
            z1=z1.upper()
            GD=abs1.sample(2)
            AB=abs2.sample()
            OB=abs3.sample(2)
            ABS=[]
            for i in range(2):
                a=GD["exercices"].iloc[i]
                c=OB["exercices"].iloc[i]
                
                a=a.upper()
                c=c.upper()

                ABS.append(a)
                ABS.append(c)
            b=AB["exercices"].iloc[0]
            b=b.upper()
            ABS.append(b)
            d=PL['exercices'].iloc[0]
            d=d.upper()
            ABS.append(d)

            if(st.button('GENERATE MY TRAINING PLAN')):
                st.text(f'Your bmi is {imc} et and that_s your program:\n\n')
                st.text(f'For every training ,we have:\n\n 15min of {z},15min of {z0} and 15min of {z1} for the cardio.\n The rest between exercise is 5 minutes.\n\n To train abs, you will do:\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 4 sets of 30 secs of {ABS[5]}.\n Take 2min of rest between every exercise.')
                
                with open('ALPHAS.txt', 'w') as f:
                    pass
                
                with open('ALPHAS.txt', 'a') as f:
                    f.write(f'Your bmi is {imc} et and that_s your program:\n\n')
                    f.write(f'For every training ,we have:\n\n 15min of {z},15min of {z0} and 15min of {z1} for the cardio.\n The rest between exercise is 5 minutes.\n\n To train abs, you will do:\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 4 sets of 30 secs of {ABS[5]}.\n Take 2min of rest between every exercise.')
                    
    elif sexe=='Femme':
        if (imc<16):
            st.text('Your program will be available soon.We will notice it to you when it will be done.')
        elif(imc>=16 and imc<=18.5):
            st.text('Your program will be available soon.We will notice it to you when it will be done.')

        elif (imc>= 18.5 and imc<=25):
            st.text('Your program will be available soon.We will notice it to you when it will be done.')

        elif (imc>=25 and imc<=30):
            nombre=st.number_input('How many times can you train a week? Choose between 3 and 5: \n',3,5)
            
            if (nombre<4 and nombre>6):
                    st.text('Invalid input!')

            if (nombre==3):
                if(st.button('GENERATE MY TRAINING PLAN')):
                    st.text(f'Your bmi is {imc} and that_s your program:\n\n')

                    st.text(f'\n Let_s start with day 1 we have: 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.')
                    st.text(f"\n\n For the abs, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the legs: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 sets of 10 reps of {JAMBES[1]}, \n 4 sets of 10 reps of {JAMBES[2]},\n 4 sets of 10 reps of {JAMBES[3]}.\n\n")
                    st.text(f'\nFor every day 2:\n\n 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n For the abs, you will do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the glutes: \n4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n')
                    st.text(f"\n\nEvery day 3, you'll do: \n  \nFor the glutes: \n4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n For the abs, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the legs: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 sets of 10 reps of {JAMBES[1]}, \n 4 sets of 10 reps of {JAMBES[2]},\n 4 sets of 10 reps of {JAMBES[3]}.\n\n.\n\n Between two days of training you should have a day off for rest. ")
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Your bmi is {imc} and that_s your program:\n\n')

                            f.write(f'\n Let_s start with day 1 we have: 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.')
                            f.write(f"\n\n For the abs, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the legs: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 sets of 10 reps of {JAMBES[1]}, \n 4 sets of 10 reps of {JAMBES[2]},\n 4 sets of 10 reps of {JAMBES[3]}.\n\n")
                            f.write(f'\nFor every day 2:\n\n 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n For the abs, you will do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the glutes: \n4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n')
                            f.write(f"\n\nEvery day 3, you'll do: \n  \nFor the glutes: \n4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n For the abs, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the legs: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 sets of 10 reps of {JAMBES[1]}, \n 4 sets of 10 reps of {JAMBES[2]},\n 4 sets of 10 reps of {JAMBES[3]}.\n\n Between two days of training you should have a day off for rest. ")
                            




            elif (nombre==4):
                if(st.button('GENERATE MY TRAINING PLAN')):
                    st.text(f'Your bmi is {imc} and that_s your program:\n\n')
                    st.text(f'\n\nFor every day 1 we have:\n\n 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n For the abs, you will do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the glutes: \n4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n')
                    st.text(f'\n\nFor every day 2 we have:\n\n 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n For the glutes: \n4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n')
                    st.text(f"\n\nEvery day 3,For the abs, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the legs: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 sets of 10 reps of {JAMBES[1]}, \n 4 sets of 10 reps of {JAMBES[2]},\n 4 sets of 10 reps of {JAMBES[3]}.\n\n")
                    st.text(f'\n\nEvery day 4, you will do: \n  \nFor the glutes: \n 5 sets of 10 reps of {FESS[0]},\n 5 sets of 10 reps of {FESS[1]}, \n 5 sets of 10 reps of {FESS[2]},\n 5 sets of 10 reps of {FESS[3]}.\n\n For the abs, you will do :\n 5 sets of 10 reps of {ABS[0]},\n 5 sets of 10 reps of {ABS[1]}, \n 5 sets of 10 reps of {ABS[2]},\n 5 sets of 10 reps of {ABS[3]}, \n 5 sets of 10 reps of {ABS[4]},\n 5 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the legs: \n 5 séries de 10 répétitions de {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}.\n\n You should have 3 days of rest without traning. ')
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Your bmi is {imc} and that_s your program:\n\n')
                            f.write(f'\n\nFor every day 1 we have:\n\n 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n For the abs, you will do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the glutes: \n4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n')
                            f.write(f'\n\nFor every day 2 we have:\n\n 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n For the glutes: \n4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n')
                            f.write(f"\n\nEvery day 3,For the abs, you'll do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the legs: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 sets of 10 reps of {JAMBES[1]}, \n 4 sets of 10 reps of {JAMBES[2]},\n 4 sets of 10 reps of {JAMBES[3]}.\n\n")
                            f.write(f'\n\nEvery day 4, you will do: \n\n For the glutes: \n 5 sets of 10 reps of {FESS[0]},\n 5 sets of 10 reps of {FESS[1]}, \n 5 sets of 10 reps of {FESS[2]},\n 5 sets of 10 reps of {FESS[3]}.\n\n For the abs, you will do :\n 5 sets of 10 reps of {ABS[0]},\n 5 sets of 10 reps of {ABS[1]}, \n 5 sets of 10 reps of {ABS[2]},\n 5 sets of 10 reps of {ABS[3]}, \n 5 sets of 10 reps of {ABS[4]},\n 5 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the legs: \n 5 séries de 10 répétitions de {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}.\n\n You should have 3 days of rest without traning. ')
                            
            
            
            elif(nombre==5):
                if(st.button('GENERATE MY TRAINING PLAN')):
                    st.text(f'Your bmi is {imc} and that_s your program:\n\n')
                    st.text(f'\n\nFor every day 1 and 3 we have:\n\n 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n For the abs, you will do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the glutes: \n4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n')
                    st.text(f'\n\nEvery day 2 and 4, you will do: \n\n For the glutes: \n 5 sets of 10 reps of {FESS[0]},\n 5 sets of 10 reps of {FESS[1]}, \n 5 sets of 10 reps of {FESS[2]},\n 5 sets of 10 reps of {FESS[3]}.\n\n For the abs, you will do :\n 5 sets of 10 reps of {ABS[0]},\n 5 sets of 10 reps of {ABS[1]}, \n 5 sets of 10 reps of {ABS[2]},\n 5 sets of 10 reps of {ABS[3]}, \n 5 sets of 10 reps of {ABS[4]},\n 5 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the legs: \n 5 séries de 10 répétitions de {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}\n\n For the glutes: \n 5 sets of 10 reps of {FESS[0]},\n 5 sets of 10 reps of {FESS[1]}, \n 5 sets of 10 reps of {FESS[2]},\n 5 sets of 10 reps of {FESS[3]}.\n\n You should have 3 days of rest without traning. ')
                    st.text(f'\n\n Every day 5 :\n\n 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n For the legs: \n 5 séries de 10 répétitions de {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}.\n\n You should have 3 days of rest without traning.')
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Your bmi is {imc} and that_s your program:\n\n')
                            f.write(f'\n\nFor every day 1 and 3 we have:\n\n 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min.\n\n For the abs, you will do :\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the glutes: \n4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n')
                            f.write(f'\n\nEvery day 2 and 4, you will do: \n\n For the glutes: \n 5 sets of 10 reps of {FESS[0]},\n 5 sets of 10 reps of {FESS[1]}, \n 5 sets of 10 reps of {FESS[2]},\n 5 sets of 10 reps of {FESS[3]}.\n\n For the abs, you will do :\n 5 sets of 10 reps of {ABS[0]},\n 5 sets of 10 reps of {ABS[1]}, \n 5 sets of 10 reps of {ABS[2]},\n 5 sets of 10 reps of {ABS[3]}, \n 5 sets of 10 reps of {ABS[4]},\n 5 sets of 10 reps of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n For the legs: \n 5 séries de 10 répétitions de {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}\n\n For the glutes: \n 5 sets of 10 reps of {FESS[0]},\n 5 sets of 10 reps of {FESS[1]}, \n 5 sets of 10 reps of {FESS[2]},\n 5 sets of 10 reps of {FESS[3]}.\n\n You should have 3 days of rest without traning. ')
                            f.write(f'\n\n Every day 5 :\n\n 10 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n For the legs: \n 5 séries de 10 répétitions de {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}.\n\n You should have 3 days of rest without traning.')
                            
        elif (imc>=30 and imc<35):
            nombre=st.number_input('How many times can you train per week? Choose between 3 and 5: \n')
            if (nombre<3 and nombre>5):
                    st.text('Invalid input')
            if (nombre==3):
                if(st.button('GENERATE MY TRAINING PLAN')):
                    st.text(f'Your bmi is {imc} and there is your training program:\n\n')
                    st.text(f'\n For every next weeks day 1 of training you will do :\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.')
                    st.text(f"\n\n For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the legs: \n 4 sets of 10 reps of {JAMBES[0]},\n 4 sets of 10 reps of {JAMBES[1]}, \n 4 sets of 10 reps of {JAMBES[2]},\n 4 sets of 10 reps of {JAMBES[3]}.\n\n")
                    st.text(f'\n Every day 2 we have:\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n\n For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]} .\n\n For the glutes : \n 4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n')
                    st.text(f"\n\n For every day 3,\n For the glutes : \n 4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}..For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the legs: \n 4 sets of 10 reps of {JAMBES[0]},\n 4 sets of 10 reps of {JAMBES[1]}, \n 4 sets of 10 reps of {JAMBES[2]},\n 4 sets of 10 reps of {JAMBES[3]}.\n\n You should have one day of rest between two trainig days. ")
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Your bmi is {imc} and there is your training program:\n\n')
                        f.write(f'\n For every next weeks day 1 of training you will do :\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.')
                        f.write(f"\n\n For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the legs: \n 4 sets of 10 reps of {JAMBES[0]},\n 4 sets of 10 reps of {JAMBES[1]}, \n 4 sets of 10 reps of {JAMBES[2]},\n 4 sets of 10 reps of {JAMBES[3]}.\n\n")
                        f.write(f'\n Every day 2 we have:\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n\n For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]} .\n\n For the glutes : \n 4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.\n\n')
                        f.write(f"\n\n For every day 3,\n For the glutes : \n 4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the legs: \n 4 sets of 10 reps of {JAMBES[0]},\n 4 sets of 10 reps of {JAMBES[1]}, \n 4 sets of 10 reps of {JAMBES[2]},\n 4 sets of 10 reps of {JAMBES[3]}.\n\n You should have one day of rest between two trainig days. ")
                        




            elif (nombre==4):

                if(st.button('GENERATE MY TRAINING PLAN')):
                    st.text(f'Your bmi is {imc} and that_s your program:\n\n')
                    st.text(f'\nEvery day 1 we have:\n\n you will do :\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n\nFor the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]} .')
                    st.text(f'\nEvery day 2 we have:\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n\n For the glutes : \n 5 sets of 10 reps of {FESS[0]},\n 5 sets of 10 reps of {FESS[1]}, \n 5 sets of 10 reps of {FESS[2]},\n 5 sets of 10 reps of {FESS[3]} .\n\n')
                    st.text(f"\n\n Every day 3 we have:\n\n For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the legs: \n 5 sets of 10 reps of {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}\n\n")
                    st.text(f'Every day 4 we have:\n\n For the glutes : \n 4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the legs: \n 5 sets of 10 reps of {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}.Per week, have 3 days of rest without train 4days on a row.')
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Your bmi is {imc} and that_s your program:\n\n')
                        f.write(f'\nEvery day 1 we have:\n\n you will do :\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n\nFor the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]} .')
                        f.write(f'\nEvery day 2 we have:\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n\n For the glutes : \n 5 sets of 10 reps of {FESS[0]},\n 5 sets of 10 reps of {FESS[1]}, \n 5 sets of 10 reps of {FESS[2]},\n 5 sets of 10 reps of {FESS[3]} .\n\n')
                        f.write(f"\n\n Every day 3 we have:\n\n For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the legs: \n 5 sets of 10 reps of {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}\n\n")
                        f.write(f'Every day 4 we have:\n\n For the glutes : \n 4 sets of 10 reps of {FESS[0]},\n 4 sets of 10 reps of {FESS[1]}, \n 4 sets of 10 reps of {FESS[2]},\n 4 sets of 10 reps of {FESS[3]}.For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the legs: \n 5 sets of 10 reps of {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}.Per week, have 3 days of rest without train 4days on a row.')
                        

            
            
            elif(nombre==5):
                if(st.button('GENERATE MY TRAINING PLAN')):
                    st.text(f'Your bmi is {imc} et and there is your program:\n\n')
                    st.text(f'\n Every days 1 and 3, we have:\n\n For every next weeks day 1 of training you will do :\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n\nFor the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the glutes : \n 5 sets of 10 reps of {FESS[0]},\n 5 sets of 10 reps of {FESS[1]}, \n 5 sets of 10 reps of {FESS[2]},\n 5 sets of 10 reps of {FESS[3]}.\n\n' )
                    st.text(f"\n\n For days 2 and 4 vous ferez:\n\n For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the legs: \n 5 sets of 10 reps of {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}.\n\n")
                    st.text(f'\n Every 5 you have :\n\n you will do :\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n\nFor the legs: \n 5 sets of 10 reps of {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}.You should have two days of rest per week.')
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Your bmi is {imc} et and there is your program:\n\n')
                        f.write(f'\n Every days 1 and 3, we have:\n\n For every next weeks day 1 of training you will do :\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n\nFor the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the glutes : \n 5 sets of 10 reps of {FESS[0]},\n 5 sets of 10 reps of {FESS[1]}, \n 5 sets of 10 reps of {FESS[2]},\n 5 sets of 10 reps of {FESS[3]}.\n\n' )
                        f.write(f"\n\n For days 2 and 4 vous ferez:\n\n For the abs:\n 4 sets of 10 reps of  {ABS[0]},\n 4 4 sets of 10 reps of {ABS[1]}, \n 4 4 sets of 10 reps of {ABS[2]},\n 4 4 sets of 10 reps of {ABS[3]}, \n 4 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n\n For the legs: \n 5 sets of 10 reps of {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}.\n\n")
                        f.write(f'\n Every 5 you have :\n\n you will do :\n\n For the cardio, 10 mins of {cours}, \n 3 sets of 30 secs of exercises and 30 secs of rest of: {CAR[0]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[2]}, \n with 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[3]},\n and the last is 3 sets of 30 secs of exercises and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2min.\n\nFor the legs: \n 5 sets of 10 reps of {JAMBES[0]},\n 5 sets of 10 reps of {JAMBES[1]}, \n 5 sets of 10 reps of {JAMBES[2]},\n 5 sets of 10 reps of {JAMBES[3]}.You should have two days of rest per week.')
                            

        
        
        
        elif(imc>=35 and imc<40):
            cardio=CARDIO.sample(5)
            course=COURSE.sample()
            cours=course["exercices"].iloc[0]
            cours=cours.upper()

            CAR=[]
            for i in range(len(cardio)):
                a=cardio["exercices"].iloc[i]
                a=a.upper()
                CAR.append(a)
            GD=abs1.sample(2)
            AB=abs2.sample()
            OB=abs3.sample(2)

            ABS=[]
            for i in range(2):
                a=GD["exercices"].iloc[i]
                c=OB["exercices"].iloc[i]
                
                a=a.upper()
                c=c.upper()

                ABS.append(a)
                ABS.append(c)
            b=AB["exercices"].iloc[0]
            b=b.upper()
            ABS.append(b)
            d=PL['exercices'].iloc[0]
            d=d.upper()
            ABS.append(d)
            nombre=st.number_input('How many times can you train a week? Choose between 3 and 5: \n')
            if (nombre<3 and nombre>5):
                    st.text('Invalid input')
            if (nombre==3):
                    if(st.button('GENERATE MY TRAINING PLAN')):
                        st.text(f'Your bmi is {imc} and that_s your program:\n\n')
                        st.text(f'\n For every trainig you will do:\n  15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min')
                        st.text(f"\n\nFor abs training we have:\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n Take one day off between two traning days.")
                        
                        with open('ALPHAS.txt', 'w') as f:
                            pass
                        
                        with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Your bmi is {imc} and that_s your program:\n\n')
                            f.write(f'\n For every trainig you will do:\n  15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min')
                            f.write(f"\n\nFor abs training we have:\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n Take one day off between two traning days.")
                    
                
            elif (nombre==4):
                    if(st.button('GENERATE MY TRAINING PLAN')):
                        
                        st.text(f'Your bmi is {imc} and that_s your program:\n\n')
                        st.text(f'\n For every trainig you will do:\n  15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min')
                        st.text(f"\n\nFor abs training we have:\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n You should have 3 days off per week without train days a row.")
                        with open('ALPHAS.txt', 'w') as f:
                            pass
                        
                        with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Your bmi is {imc} and that_s your program:\n\n')
                            f.write(f'\n For every trainig you will do:\n  15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min')
                            f.write(f"\n\nFor abs training we have:\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n Take one day off between two traning days.")


            elif(nombre==5):
                    if(st.button('GENERATE MY TRAINING PLAN')):
                        st.text(f'Your bmi is {imc} and that_s your program:\n\n')
                        st.text(f'\n For every trainig you will do:\n  15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min')
                        st.text(f"\n\nFor abs training we have:\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n Take two days off per week.")
                        with open('ALPHAS.txt', 'w') as f:
                            pass
                        
                        with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Your bmi is {imc} and that_s your program:\n\n')
                            f.write(f'\n For every trainig you will do:\n  15 min of {cours} and: \n 3 sets of 30 secs of exercise and 30 secs of rest of : {CAR[0]},\n after you will do 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[1]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[2]}, \n 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[3]},\n and 3 sets of 30 secs of exercise and 30 secs of rest of {CAR[4]}.\n The rest between exercise is 2 min')
                            f.write(f"\n\nFor abs training we have:\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 3 sets of 30 secs of {ABS[5]}.\n Take 2 min of rest between every exercise.\n\n Take one day off between two traning days.")
        


        elif (imc>=40):
            z=COURSE["exercices"].iloc[0]
            z=z.upper()
            z0=COURSE["exercices"].iloc[1]
            z0=z0.upper()
            z1=COURSE["exercices"].iloc[2]
            z1=z1.upper()
            GD=abs1.sample(2)
            AB=abs2.sample()
            OB=abs3.sample(2)
            ABS=[]
            for i in range(2):
                a=GD["exercices"].iloc[i]
                c=OB["exercices"].iloc[i]
                
                a=a.upper()
                c=c.upper()

                ABS.append(a)
                ABS.append(c)
            b=AB["exercices"].iloc[0]
            b=b.upper()
            ABS.append(b)
            d=PL['exercices'].iloc[0]
            d=d.upper()
            ABS.append(d)
            if(st.button('GENERATE MY TRAINING PLAN')):
                st.text(f'Your bmi is {imc} and there is your program below:\n\n')
                st.text(f'Every week we have:\n\n 15min of {z},15min of {z0} and 15min of {z1} for the cardio.\n The rest between exercise is 5min .\n\n For abs:\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 4 sets of 30 secs of {ABS[5]}.\n Take 2 min of rest between every exercise.')
                
                with open('ALPHAS.txt', 'w') as f:
                     pass
                
                with open('ALPHAS.txt', 'a') as f:
                     st.text(f'Your bmi is {imc} and there is your program below:\n\n')
                     st.text(f'Every week we have:\n\n 15min of {z},15min of {z0} and 15min of {z1} for the cardio.\n The rest between exercise is 5min .\n\n For abs:\n 4 sets of 10 reps of {ABS[0]},\n 4 sets of 10 reps of {ABS[1]}, \n 4 sets of 10 reps of {ABS[2]},\n 4 sets of 10 reps of {ABS[3]}, \n 4 sets of 10 reps of {ABS[4]},\n 4 sets of 30 secs of {ABS[5]}.\n Take 2 min of rest between every exercise.')
                
#st.header('LA DEMONSTRATION, AINSI QUE L_EXECUTION DE TOUT LES EXERCICES SONT DISPONIBLES SUR LE SITE DOCTEURFITNESS.COM')
    st.subheader('AS FOR THE MEAL PLAN, IF YOU DO NOT LIKE A TRAINING PLAN RE-CLICK ON GENERATE MY TRAINING PLAN AGAIN. ANOTHER SHOULD BE AUTOMATICALLY GENERATED.')
         

    def DOWNLOAD():
            with open (r'ALPHAS.txt', 'r') as f:
                contenu=f.read()
            return contenu.encode()
    def main():
            st.write('CLICK ON BUTTON BELOW TO DOWNLOAD YOUR TRAINING PLAN')
            wishes=st.radio('DOWNLOAD MY TRAINING PLAN',('None','no','yes'))
            if wishes=='yes':
                fichier=DOWNLOAD()
                st.download_button(
                    label="DOWNLOAD",
                    data=fichier,
                    file_name=r'ALPHAS.txt',
                    mime='text/plain'
                    )
            else:
                pass
        
    if __name__=="__main__":
            main()
    st.markdown('EVERY EXERCISE_S APPLICATION ARE AVAILABLE ON [docteur-fitness.com](https://www.docteur-fitness.com).')
    #site=st.link_button('docteurfitness', 'https://www.docteur-fitness.com')
