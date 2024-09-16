import pandas as pd
import streamlit  as st

st.title("🦍PROJET_ALPHAS🦍")
st.header('PROJET_ALPHAS PAR  HOUNME HOUETO EMERICK GILLES')
st.title('TELECHARGEMENT DU PLAN ALIMENTAIRE')

ac=pd.read_csv(r'aliments3.txt', sep=';')

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
a2=gluc['aliments'].iloc[0]
a1=int(gluc.index[(gluc['aliments']==a['aliments'].iloc[0])][0])
crb_cal=a._get_value(a1, 'calories (100g)')
crb_name=a._get_value(a1, 'aliments')
crb_cat=a._get_value(a1, 'categorie')


b=prot.sample()
b1=int(prot.index[(prot['aliments']==b['aliments'].iloc[0])][0])
bcaa_cal=b._get_value(b1, 'calories (100g)')
bcaa_name=b._get_value(b1, 'aliments')

c=sauce.sample()
c1=int(sauce.index[(sauce['aliments']==c['aliments'].iloc[0])][0])
#bcaa_cal=b._get_value(b1, 'calories (100g)')
sauce_name=c._get_value(c1, 'aliments')
sauce_cat=c._get_value(c1, 'categorie')

arachide=ac[ac.categorie=='arachide']
sucre=ac[ac.categorie=='sucre']
lait=ac[ac.categorie=='lait']

fit=pd.read_csv(r'exo.txt', sep=',')

CARDIO=fit[fit.cibles=='cardio']
COURSE=fit[fit.cibles=='course']
abs1=fit[fit.cibles=='grand droit']
abs2=fit[fit.cibles=='obliques']
PL=fit[fit.cibles=='planche']
abs3=fit[fit.cibles=="abdos"]
SAT=fit[fit.cibles==' Squats']
QUA=fit[fit.cibles=='quadriceps']
SDT=fit[fit.cibles==' Soulevé de terre ']
QMI=fit[fit.cibles=='quadriceps mollets ischio-jambiers']
QUI=fit[fit.cibles=='quadriceps et ischio-jambiers']
FES=fit[fit.cibles=='fessiers']
BI=fit[fit.cibles=='Biceps']
TRI=fit[fit.cibles=='Triceps']
DAS=fit[fit.cibles=='delts antérieur et moyen']
DPT=fit[fit.cibles=='delts postérieur et Trapèzes']
TDR=fit[fit.cibles=='dorsaux et rhomboides et trapèzes']
TER=fit[fit.cibles=='Trapèzes et rhomboides']
DOX=fit[fit.cibles=='dorsaux']
PS=fit[fit.cibles=='grand pectoral partie supérieure']
GP=fit[fit.cibles=='grand pectoral']
FP=fit[fit.cibles=='fente des pectoraux']
PI=fit[fit.cibles=='grand pectoral partie inférieure']


cardio=CARDIO.sample(5)
course=COURSE.sample()
cours=course["exercices"].iloc[0]
cours=cours.upper()

CAR=[]
for i in range(len(cardio)):
    a=cardio["exercices"].iloc[i]
    a=a.upper()
    CAR.append(a)
        
    #print(f'Pour aujourd_ui,\n on va commencer avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
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
nom=st.text_input('Entrez votre nom et prénoms: ')

if type(nom) is not str:
    st.text('Valeur invalide!')
elif type(nom) is str :
    if len(nom)>0:
        st.text(f'Bienvenu {nom}!')
        gen=st.radio('quel est votre sexe de naissance?: ',('Homme','Femme'))

        if gen=='Homme':
            
            gender=0
        else:
            gender=1

        if gender==0:
            
            poid=st.number_input('Entrez votre poids(en kg): \n',1,1000)
            
            if (poid>0):

                taill=st.number_input('Entrez votre taille(en cm): \n',1,1000)
                
                if (taill >0):
            
                    age=st.number_input('Entrez votre age: \n',1,500)
        
            mba=(13.7516*poid) + (500.33*taill/100) - (6.7550*age) + 66.473
            mbb=(13.707*poid) + (492.3*taill/100) - (6.673*age) + 77.607
            
            
            MBh=(mba+mbb)/2
            
            if age>0:
                ap=st.radio('Avez vous eu une activité physique chaque semaine de manière régulière sur les 12 derniers mois ?', ('non','oui'))
                if ap=='non':
                    dep_cal=MBh*1.1
                else:
                    freq=st.selectbox('A quelle fréquence?',[ 'moins de 3 fois par semaine' , "3fois par semaine" , "plus de 3fois par semaine"])
                    if freq=='moins de 3 fois par semaine':
                        dep_cal=MBh*1.3
                    elif freq=='3fois par semaine':
                        dep_cal=MBh*1.5
                    elif freq=='plus de 3fois par semaine':
                        dep_cal=MBh*1.7
            #st.text(f'Votre métabolisme de base est de {MBh}')
                
    #        return (f'Votre metabolisme de base est d_environ {MBh} et votre dépense calorique est {dep_cal}')
        
        elif gender==1:
            poid=st.number_input('Entrez votre poids(en kg): \n',1,1000)
            
            if (poid>0):

                taill=st.number_input('Entrez votre taille(en cm): \n',1,1000)
            
                if (taill >0):
            
                    age=st.number_input('Entrez votre age: \n',1,500)
        
                
            mba=(9.5634*poid) + (184.96*taill/100) - (6.7556*age) + 655.0955
            mbb=(9.740*poid) + (172.9*taill/100) - (4.737*age) + 667.051
            
            MBf=(mba+mbb)/2
            
            if age>0:
                ap=st.radio('Avez vous eu une activité physique chaque semaine de manière régulière sur les 12 derniers mois ?', ('non','oui'))
                if ap=='non':
                    dep_cal=MBf*1.21
                else:
                    freq=st.selectbox('A quelle fréquence?',[ 'moins de 3 fois par semaine' , "3fois par semaine" , "plus de 3fois par semaine"])
                    if freq=='moins de 3 fois par semaine':
                        dep_cal=MBf*1.3
                    elif freq=='3fois par semaine':
                        dep_cal=MBf*1.5
                    elif freq=='plus de 3fois par semaine':
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
        c1=int(sauce.index[(sauce['aliments']==c['aliments'].iloc[0])][0])
        sauce_name=c._get_value(c1, 'aliments')
        sauce_cat=c._get_value(c1, 'categorie')
        
        
        #ARACHIDE, SUCRE , LAITS
        cacahuete=arachide[['aliments', 'calories (100g)', 'categorie']]
        ara=cacahuete.sample()
        ara1=int(ara.index[(ara['aliments']==ara['aliments'].iloc[0])][0])
        ara_cal=ara._get_value(ara1, 'calories (100g)')
        ara_name=ara._get_value(ara1, 'aliments')
        ara_cate=ara._get_value(ara1, 'categorie')

        laits=lait[['aliments', 'calories (100g)', 'categorie']]
        milk=laits.sample()
        milk1=int(milk.index[(milk['aliments']==milk['aliments'].iloc[0])][0])
        milk_cal=milk._get_value(milk1, 'calories (100g)')
        milk_name=milk._get_value(milk1, 'aliments')
        milk_cate=milk._get_value(milk1, 'categorie')
        
        suc=sucre[['aliments','calories (100g)', 'categorie']]
        suc1=int(suc.index[(suc['aliments']==suc['aliments'].iloc[0])][0])
        suc_cal=suc._get_value(suc1, 'calories (100g)')
        suc_name=suc._get_value(suc1, 'aliments')
        suc_cate=suc._get_value(suc1, 'categorie')
            

        if (st.button('générer le plan alimentaire')):
            st.subheader('A CHAQUE FOIS QU_UN PLAN ALIMENTAIRE NE VOUS PLAIT PAS, VEUILLEZ APPUYEZ A NOUVEAU SUR LE BOUTON GENERER UN PLAN ALIMENTAIRE, UN NOUVEAU PLAN VOUS SERA SUGGERE.')
        
            st.text(f'Votre  dépense calorique est de {dep_cal} calories et répartition moyenne journalière {brek} calories')
            with open('ALPHAS_meals.txt', 'w') as f:
                pass
            for i in range (1,8,1):
                a=gluc.sample()
                a2=a['aliments'].iloc[0]
                a1=int(gluc.index[(gluc['aliments']==a['aliments'].iloc[0])][0])
                crb_cal=a._get_value(a1, 'calories (100g)')
                crb_name=a._get_value(a1, 'aliments')
                crb_cate=a._get_value(a1, 'categorie')
                b=prot.sample()
                b1=int(prot.index[(prot['aliments']==b['aliments'].iloc[0])][0])
                bcaa_cal=b._get_value(b1, 'calories (100g)')
                bcaa_name=b._get_value(b1, 'aliments')

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
                    oe1=int(oe.index[(oe['aliments']==oe['aliments'].iloc[0])][0])
                    bcaa_cal=oe._get_value(oe1, 'calories (100g)')
                    bcaa_name=oe._get_value(oe1, 'aliments')
            
        
        
                a1=0.6*(brek)
                b1=0.4*(brek)
                brek1=a1*100/crb_cal
                brek2=b1*100/bcaa_cal
        
        
                a=gluc.sample()
                a2=a['aliments'].iloc[0]
                a1=int(gluc.index[(gluc['aliments']==a['aliments'].iloc[0])][0])
                crb_lun_cal=a._get_value(a1, 'calories (100g)')
                crb_lun_name=a._get_value(a1, 'aliments')
                crb_lun_cate=a._get_value(a1, 'categorie')

                b=prot.sample()
                b1=int(prot.index[(prot['aliments']==b['aliments'].iloc[0])][0])
                bcaa_lun_cal=b._get_value(b1, 'calories (100g)')
                bcaa_lun_name=b._get_value(b1, 'aliments')
        
                if (crb_lun_cate=='fruit'):
                    oe=prot[prot.aliments=='oeuf(en moyenne)']
                    oe1=(oe.index[(oe['aliments']==oe['aliments'].iloc[0])][0])
                    bcaa_lun_cal=oe._get_value(oe1, 'calories (100g)')
                    bcaa_lun_name=oe._get_value(oe1, 'aliments')
            
               

                a1=0.6*(lun)
                a=a1/crb_lun_cal
                b1=0.4*(lun)
                b=b1/bcaa_lun_cal
                lun1=a*100
                lun2=b*100
        
        
        #third
                a=gluc.sample()
                a2=a['aliments'].iloc[0]
                a1=int(gluc.index[(gluc['aliments']==a['aliments'].iloc[0])][0])
    #print(a2, a1)
                crb_t_cal=a._get_value(a1, 'calories (100g)')
                crb_t_name=a._get_value(a1, 'aliments')
                crb_t_cate=a._get_value(a1, 'categorie')

                b=prot.sample()
                b1=int(prot.index[(prot['aliments']==b['aliments'].iloc[0])][0])
                bcaa_t_cal=b._get_value(b1, 'calories (100g)')
                bcaa_t_name=b._get_value(b1, 'aliments')
        
                if (crb_t_cate=='fruit'):
                    oe=prot[prot.aliments=='oeuf(en moyenne)']
                    oe1=(oe.index[(oe['aliments']==oe['aliments'].iloc[0])][0])
                    bcaa_t_cal=oe._get_value(oe1, 'calories (100g)')
                    bcaa_t_name=oe._get_value(oe1, 'aliments')
            
            
        

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
            
                st.text(f'\n\n, Le petit dejeuner du jour {i} est {brek1} grammes de {crb_name} et {brek2} grammes de {bcaa_name},\n Le dejeuner est {lun1} grammes de {crb_lun_name} et {lun2} grammes de {bcaa_lun_name}, \n Le dernier est {t1} grammes de {crb_t_name} et {t2} grammes de {bcaa_t_name} \n')
                with open('ALPHAS_meals.txt', "a") as f:
                    f.write(f'Votre  dépense calorique est de {dep_cal} calories et répartition moyenne par repas de  {brek} calories')
            
                    f.write(f'\n\n, Le petit dejeuner du jour {i} est {brek1} grammes de {crb_name} et {brek2} grammes de {bcaa_name},\n Le dejeuner est {lun1} grammes de {crb_lun_name} et {lun2} grammes de {bcaa_lun_name}, \n Le dernier est {t1} grammes de {crb_t_name} et {t2} grammes de {bcaa_t_name} \n')
            
            def telecharger_fichier():
                    with open (r'ALPHAS_meals.txt', 'r') as f:
                        contenu=f.read()
                    return contenu.encode()
            def main():
                    st.subheader('TELECHARGER LE PLAN ALIMENTAIRE')
                    wish=st.radio('APPPUYEZ SUR TELECHARGER MON PLAN ',('oui','non'))
                    
                    if wish=='oui':
                        fichier=telecharger_fichier()
                        st.download_button(
                            label="TELECHARGER MON PLAN",
                            data=fichier,
                            file_name=r'ALPHAS_meals.txt',
                            mime='text/plain'
                        )
                    else:
                        pass
            if __name__=="__main__":
                    main()

#st.title('TELECHARGEMENT DU PLAN D_ENTRAINEMENT')
st.header('VOULEZ-VOUS EGALEMENT UN PLAN D_ENTRAINEMENT?')
plan= st.radio('CHOISSISEZ L_OPTION DE VOTRE CHOIX',('néant','non','oui'))
if plan=='néant':
    pass 
elif plan=='non':
    st.text('ok profitez de votre plan uniquement alors.')
else:
    st.title('TELECHARGEMENT DU PLAN D_ENTRAINEMENT')
    poids=st.number_input("Entrez votre poids en kg: ", 0)
    t=st.number_input('Entrez votre taille en cm:',1)
    taille=t/100
    imc=(poids/(taille*taille))


    sexe=st.radio('quel est votre sexe de naissance?: ',('Néant','Homme','Femme'))

    if sexe=='Homme':
        if (imc<16):
            st.error('Vous etes en sous-poids extreme.Faites attention!')
        elif(imc>=16 and imc<=18.5):
            st.warning('Vous etes en sous-poids')

        elif (imc>= 18.5 and imc<=25):
            st.text('Vous etes dans les normes!')
            p=st.radio('Quel programme préférez-vous?',('Aucun', 'Poids du corps','machine et haltères'))

            if p=='Aucun':
                pass
            elif p=='Poids du corps':
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

                exp=st.radio('Comment appréciez-vous votre niveau d_expérience?',('Néant','débutant', 'intermédiaire', 'avancé'))
                    

                if(st.button('Générer le programme d_entrainement:')):
                    if (exp=='débutant'):
                        st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n\n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 1 minute.')
                        st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 1 minutes de repos.\n\n")
                        st.text("Vous prenez ensuite 5min de repos et vous commencez les exercices de musculation au poids du corps. \n\n")
                    
                    
                        st.text(f"On a à un rythme de 3 séries de 10 répétitions de {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n et de {Pdc[6]}")
                        st.text("Le temps de repos entre chaque série est de 45 secondes. Celui entre le changement d'exercices est de  2min.")

                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n\n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 1 minute.')
                            f.write(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 1 minutes de repos.\n\n")
                            f.write("Vous prenez ensuite 5min de repos et vous commencez les exercices de musculation au poids du corps. \n\n")
                        
                        
                            f.write(f"On a à un rythme de 3 séries de 10 répétitions de {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n et de {Pdc[6]}")
                            f.write("Le temps de repos entre chaque série est de 45 secondes. Celui entre le changement d'exercices est de  2min.")


                    elif (exp=='intermédiaire'):
                        st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n\n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 1 minute.')
                        st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 1 minutes de repos.\n\n")
                        st.text("Vous prenez ensuite 5min de repos et vous commencez les exercices de musculation au poids du corps. \n\n")
                    

                        st.text(f"On a à un rythme de 5 séries de 10 répétitions de {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n et de {Pdc[6]}")
                        st.text("Le temps de repos entre chaque série est de 30 secondes. Celui entre le changement d'exercices est de  2min.")
                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n\n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 1 minute.')
                            f.write(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 1 minutes de repos.\n\n")
                            f.write("Vous prenez ensuite 5min de repos et vous commencez les exercices de musculation au poids du corps. \n\n")
                        

                            f.write(f"On a à un rythme de 5 séries de 10 répétitions de {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n et de {Pdc[6]}")
                            f.write("Le temps de repos entre chaque série est de 30 secondes. Celui entre le changement d'exercices est de  2min.")
                
                    elif (exp=='avancé'):

                        st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n\n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 1 minute.')
                        st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 1 minutes de repos.\n\n")
                        st.text("Vous prenez ensuite 5min de repos et vous commencez les exercices de musculation au poids du corps. \n\n")
                    

                        st.text(f"On a à un rythme de 7 séries de 10 répétitions de {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n et de {Pdc[6]}")
                        st.text("Le temps de repos entre chaque série est de 30 secondes. Celui entre le changement d'exercices est de  3min.")

                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n\n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 1 minute.')
                            f.write(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 1 minutes de repos.\n\n")
                            f.write("Vous prenez ensuite 5min de repos et vous commencez les exercices de musculation au poids du corps. \n\n")
                        

                            f.write(f"On a à un rythme de 7 séries de 10 répétitions de {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n et de {Pdc[6]}")
                            f.write("Le temps de repos entre chaque série est de 30 secondes. Celui entre le changement d'exercices est de  3min.")

                            
                        st.subheader('LE PROGRAMME DOIT ETRE EXECUTE AU MOINS 4 FOIS PAR SEMAINE AVEC 3JOURS DE REPOS A CONVENANCE.')
            elif p=='machine et haltères':
                a=fit[fit.exercices=='Elevations latérales aux haltères']
                a0=a['exercices'].iloc[0]
                a1=a['cibles'].iloc[0]
                d=fit[fit.exercices=='Tirage vertical poitrine']
                d0=d['exercices'].iloc[0]
                d1=d['cibles'].iloc[0]
                DAS=DAS.drop(DAS[DAS['exercices']=='Elevations latérales aux haltères'].index)
                DOX=DOX.drop(DOX[DOX['exercices']=='Tirage vertical poitrine'].index)
                nombre=st.number_input('Combien de fois pouvez-vous vous entrainer par semaine? Choissisez un nombre de fois entre 4 et 6: \n')    
                
                if (nombre<4 and nombre>6):
                    st.text('Valeur invalide')
                    if(nombre==4):
                        if(st.button('Générer le programme d_entrainement')):
                            st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme a suivre pour les 4 prochaines semaines:\n\n')
                            st.text(f'Pour les jours 1 et 3 on a au programme : le dos, les pectoraux et les épaules.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux on a: {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}.\n\n \n Et pour les épaules, on a: {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                            st.text(f'\n\n Pour les jour 2 et 4 on démarre avec les biceps , les triceps et les jambes.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour les biceps et les Triceps ,on a:  {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes, on a:  {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive. ')
                            with open('ALPHAS.txt', 'w') as f:
                                pass

                            with open('ALPHAS.txt', "a") as f:
                                f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme a suivre pour les 4 prochaines semaines:\n\n')
                                f.write(f'Pour les jours 1 et 3 on a au programme : le dos, les pectoraux et les épaules.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux on a: {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}.\n\n \n Et pour les épaules, on a: {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                                f.write(f'\n\n Pour les jour 2 et 4 on démarre avec les biceps , les triceps et les jambes.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour les biceps et les Triceps ,on a:  {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes, on a:  {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive. ')
                        


                    elif(nombre==5):
                        if(st.button('Générer le programme d_entrainement')):
                            st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            st.text(f'Pour les jours 1 , 3 et 5 des 4 prochaines semaines on va au programme le dos, les pectoraux et les épaules.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos, on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux, on a: {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}. Pour les épaules, on a : {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                            st.text(f'\n\n Pour le jour 2 et 4 des 4 prochaines semaines on démarre avec les biceps , les triceps et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour les biceps et les Triceps on a, {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes , on a: {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.')
                            
                            with open('ALPHAS.txt', 'w') as f:
                                pass

                            with open('ALPHAS.txt', "a") as f:
                                f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                                f.write(f'Pour les jours 1 , 3 et 5 des 4 prochaines semaines on va au programme le dos, les pectoraux et les épaules.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos, on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux, on a: {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}. Pour les épaules, on a : {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                                f.write(f'\n\n Pour le jour 2 et 4 des 4 prochaines semaines on démarre avec les biceps , les triceps et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour les biceps et les Triceps on a, {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes , on a: {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.')
                        
                    
                    
                    elif (nombre==6):
                        if(st.button('Générer le programme d_entrainement')):
                            st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            st.text(f'Pour les jours 1 et 4 on a: le dos et les épaules.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos, on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux, on a:  {PECS[0]} pour travailler le {PECS[1]},\n\n \n Pour les épaules, on a : {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                            st.text(f'\n\n Pour les jour 2 et 5 on démarre avec les pectoraux les biceps , les triceps.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n \n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]},\n\n pour les biceps,on a: {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]}')
                            st.text(f'\n \n Pour les jours 3 et 6 jambes \n\n {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.')
                            
                            with open('ALPHAS.txt', 'w') as f:
                                pass

                            with open('ALPHAS.txt', "a") as f:
                                f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                                f.write(f'Pour les jours 1 et 4 on a: le dos et les épaules.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos, on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux, on a:  {PECS[0]} pour travailler le {PECS[1]},\n\n \n Pour les épaules, on a : {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                                f.write(f'\n\n Pour les jour 2 et 5 on démarre avec les pectoraux les biceps , les triceps.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n \n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]},\n\n pour les biceps,on a: {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]}')
                                f.write(f'\n \n Pour les jours 3 et 6 jambes \n\n {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.')
                            
        



        
        elif (imc>=25 and imc<=30):
            if imc>=25 and imc<=30:

                a=fit[fit.exercices=='Elevations latérales aux haltères']
                a0=a['exercices'].iloc[0]
                a1=a['cibles'].iloc[0]
                d=fit[fit.exercices=='Tirage vertical poitrine']
                d0=d['exercices'].iloc[0]
                d1=d['cibles'].iloc[0]
                DAS=DAS.drop(DAS[DAS['exercices']=='Elevations latérales aux haltères'].index)
                DOX=DOX.drop(DOX[DOX['exercices']=='Tirage vertical poitrine'].index)
                nombre=st.number_input('Combien de fois pouvez-vous vous entrainer par semaine? Choissisez un nombre de fois entre 4 et 6: \n')    
                
                if (nombre<4 and nombre>6):
                    st.text('Valeur invalide')
                if(nombre==4):
                    if(st.button('Générer le programme d_entrainement')):
                        st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme a suivre pour les 4 prochaines semaines:\n\n')
                        st.text(f'Pour les jours 1 et 3 on a au programme : le dos, les pectoraux et les épaules.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux on a: {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}.\n\n \n Et pour les épaules, on a: {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                        st.text(f'\n\n Pour les jour 2 et 4 on démarre avec les biceps , les triceps et les jambes.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour les biceps et les Triceps ,on a:  {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes, on a:  {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive. ')
                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme a suivre pour les 4 prochaines semaines:\n\n')
                            f.write(f'Pour les jours 1 et 3 on a au programme : le dos, les pectoraux et les épaules.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux on a: {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}.\n\n \n Et pour les épaules, on a: {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                            f.write(f'\n\n Pour les jour 2 et 4 on démarre avec les biceps , les triceps et les jambes.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour les biceps et les Triceps ,on a:  {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes, on a:  {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive. ')
                       


                elif(nombre==5):
                    if(st.button('Générer le programme d_entrainement')):
                        st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        st.text(f'Pour les jours 1 , 3 et 5 des 4 prochaines semaines on va au programme le dos, les pectoraux et les épaules.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos, on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux, on a: {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}. Pour les épaules, on a : {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                        st.text(f'\n\n Pour le jour 2 et 4 des 4 prochaines semaines on démarre avec les biceps , les triceps et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour les biceps et les Triceps on a, {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes , on a: {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.')
                        
                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            f.write(f'Pour les jours 1 , 3 et 5 des 4 prochaines semaines on va au programme le dos, les pectoraux et les épaules.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos, on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux, on a: {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}. Pour les épaules, on a : {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                            f.write(f'\n\n Pour le jour 2 et 4 des 4 prochaines semaines on démarre avec les biceps , les triceps et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour les biceps et les Triceps on a, {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes , on a: {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.')
                       
                
                
                elif (nombre==6):
                    if(st.button('Générer le programme d_entrainement')):
                        st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        st.text(f'Pour les jours 1 et 4 on a: le dos et les épaules.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos, on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux, on a:  {PECS[0]} pour travailler le {PECS[1]},\n\n \n Pour les épaules, on a : {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                        st.text(f'\n\n Pour les jour 2 et 5 on démarre avec les pectoraux les biceps , les triceps.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n \n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]},\n\n pour les biceps,on a: {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]}')
                        st.text(f'\n \n Pour les jours 3 et 6 jambes \n\n {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.')
                        
                        with open('ALPHAS.txt', 'w') as f:
                            pass

                        with open('ALPHAS.txt', "a") as f:
                            f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            f.write(f'Pour les jours 1 et 4 on a: le dos et les épaules.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos, on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux, on a:  {PECS[0]} pour travailler le {PECS[1]},\n\n \n Pour les épaules, on a : {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                            f.write(f'\n\n Pour les jour 2 et 5 on démarre avec les pectoraux les biceps , les triceps.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n \n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]},\n\n pour les biceps,on a: {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]}')
                            f.write(f'\n \n Pour les jours 3 et 6 jambes \n\n {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.')
                        

        elif(imc>=30 and imc<35):
                nombre=st.number_input('Combien de fois pouvez-vous vous entrainer par semaine? Choissisez entre 3 et 5\n')
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')

                    if (nombre<3 and nombre>5):
                        st.text('Valeur invalide')
                    if (imc>=30 and imc<35):
                        if(nombre==3):
                            st.text(f'Pour les jours 1 et 3 on va commencer avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\n Ensuite on a le dos, les pectoraux et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {DOS[4]} pour travailler les {DOS[5]}.\n\n Pour les pectoraux on a :{PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}.\n\nPour les jambes on a, le {JAMBES[0]},\n le {JAMBES[1]},\n ensuite le/la {JAMBES[2]} pour les {JAMBES[3]}, \n et le/la {JAMBES[4]} pour travailler les {JAMBES[5]}')
                            st.text(f'\n\n Pour le jour 2 on démarre avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.  \n\nEnsuite les biceps , les triceps et les épaules.\nVoici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour le {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les épaules {EPAULES[0]} pour travailler le {EPAULES[1]},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]} ')
                            
                            with open('ALPHAS.txt', 'w') as f:
                                pass
                            
                            with open('ALPHAS.txt', 'a') as f:
                                f.write(f'Pour les jours 1 et 3 on va commencer avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\n Ensuite on a le dos, les pectoraux et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {DOS[4]} pour travailler les {DOS[5]}.\n\n Pour les pectoraux on a :{PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}.\n\nPour les jambes on a, le {JAMBES[0]},\n le {JAMBES[1]},\n ensuite le/la {JAMBES[2]} pour les {JAMBES[3]}, \n et le/la {JAMBES[4]} pour travailler les {JAMBES[5]}')
                                f.write(f'\n\n Pour le jour 2 on démarre avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.  \n\nEnsuite les biceps , les triceps et les épaules.\nVoici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour le {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les épaules {EPAULES[0]} pour travailler le {EPAULES[1]},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]} ')
                           

                        
                        elif(nombre==4):
                            st.text(f'Pour les jours 1 et 3 on va commencer avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\n Ensuite on a: le dos, les pectoraux et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {DOS[4]} pour travailler les {DOS[5]}.\n\n {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}.\n\n \n Pour les épaules {EPAULES[0]} pour travailler le {EPAULES[1]},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}')
                            st.text(f'\n\n Pour le jour 2 et 4 on démarre avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes. ensuite: \n\n les biceps , les triceps et les épaules.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes \n\n {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive. ')
                            
                            with open('ALPHAS.txt', 'w') as f:
                                pass
                            
                            with open('ALPHAS.txt', 'a') as f:
                               f.write(f'Pour les jours 1 et 3 on va commencer avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\n Ensuite on a: le dos, les pectoraux et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {DOS[4]} pour travailler les {DOS[5]}.\n\n {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}.\n\n \n Pour les épaules {EPAULES[0]} pour travailler le {EPAULES[1]},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}')
                               f.write(f'\n\n Pour le jour 2 et 4 on démarre avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes. ensuite: \n\n les biceps , les triceps et les épaules.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes \n\n {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive. ')
                           
                        
                        elif(nombre==5):
                            st.text(f'Pour les jours 1 et 3 et 5 des 4 prochaines semaines on va commencer avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\n Ensuite on a: le dos, les pectoraux et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {DOS[4]} pour travailler les {DOS[5]}.\n\n {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}.\n\n \n Pour les épaules {EPAULES[0]} pour travailler le {EPAULES[1]},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}')
                            st.text(f'\n\n Pour le jour 2 et 4 des 4 prochaines semaines on démarre avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes. ensuite: \n\n les biceps , les triceps et les épaules.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes \n\n {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}')
                            
                            with open('ALPHAS.txt', 'w') as f:
                                pass
                            
                            with open('ALPHAS.txt', 'a') as f:
                                f.write(f'Pour les jours 1 et 3 et 5 des 4 prochaines semaines on va commencer avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\n Ensuite on a: le dos, les pectoraux et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {DOS[4]} pour travailler les {DOS[5]}.\n\n {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}.\n\n \n Pour les épaules {EPAULES[0]} pour travailler le {EPAULES[1]},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}')
                                f.write(f'\n\n Pour le jour 2 et 4 des 4 prochaines semaines on démarre avec 10 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes. ensuite: \n\n les biceps , les triceps et les épaules.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes \n\n {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}')
                           

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
        
            nombre=st.number_input('Combien de fois pouvez-vous vous entrainer par semaine? Choissisez un nombre de fois entre 3 et 5: \n')
            
            if (nombre<3 and nombre>5):
                    st.text('Valeur invalide')
            if (nombre==3):
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                    st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\n Entre deux journées d_entrainement vous devez observer au moins une journeé de repos(sans entrainement). ")
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass

                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                        f.write(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\n Entre deux journées d_entrainement vous devez observer au moins une journeé de repos(sans entrainement). ")
            elif (nombre==4):
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                    st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive.  ")
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                        f.Write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                        f.Write(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive.  ")
                   
            
            
            elif(nombre==5):
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                    st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\nVous devez observer au moins deux journeés de repos(sans entrainement) par semaine. ")
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass

                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                        f.write(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\nVous devez observer au moins deux journeés de repos(sans entrainement) par semaine. ")
                    

        
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

            if(st.button('Générer le programme d_entrainement')):
                st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                st.text(f'Pour chacune de vos séances hebdomaires,on a:\n\n 15min de {z},15min de {z0} et de 15min de {z1} pour le cardio.\nLe repos entre le changement d_exercices est de 5 minutes.\n\n Pour les abdos,vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 4 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.')
                
                with open('ALPHAS.txt', 'w') as f:
                            pass
                
                with open('ALPHAS.txt', 'a') as f:
                    f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    f.write(f'Pour chacune de vos séances hebdomaires,on a:\n\n 15min de {z},15min de {z0} et de 15min de {z1} pour le cardio.\nLe repos entre le changement d_exercices est de 5 minutes.\n\n Pour les abdos,vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 4 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.')
               
    
    elif sexe=='Femme':
        if (imc<16):
            st.error('Vous etes en sous-poids extreme.Faites attention!')
        elif(imc>=16 and imc<=18.5):
            st.warning('Vous etes en sous-poids')

        elif (imc>= 18.5 and imc<=25):
            st.text('Vous etes dans les normes!')

        elif (imc>=25 and imc<=30):
            nombre=st.number_input('Combien de fois pouvez-vous vous entrainer par semaine? Choissisez un nombre de fois entre 3 et 5: \n',3,5)
            
            if (nombre<4 and nombre>6):
                    st.text('Valeur invalide')

            if (nombre==3):
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')

                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 1 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                    st.text(f"\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 séries de 10 répétitions de {JAMBES[1]}, \n 4 séries de 10 répétitions de {JAMBES[2]},\n 4 séries de 10 répétitions de {JAMBES[3]}.\n\n")
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\nPour travailler vos fessiers: \n4 séries de 10 répétitions de {FESS[0]},\n 4 séries de 10 répétitions de {FESS[1]}, \n 4 séries de 10 répétitions de {FESS[2]},\n 4 séries de 10 répétitions de {FESS[3]}.\n\n')
                    st.text(f"\n\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 3,\n Pour travailler vos fessiers: \n4 séries de 10 répétitions de {FESS[0]},\n 4 séries de 10 répétitions de {FESS[1]}, \n 4 séries de 10 répétitions de FESS{[2]},\n 4 séries de 10 répétitions de {FESS[3]}.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 séries de 10 répétitions de {JAMBES[1]}, \n 4 séries de 10 répétitions de {JAMBES[2]},\n 4 séries de 10 répétitions de {JAMBES[3]}.\n\n Entre deux journées d_entrainement vous devez observer au moins une journeé de repos(sans entrainement). ")
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 1 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                        f.write(f"\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 séries de 10 répétitions de {JAMBES[1]}, \n 4 séries de 10 répétitions de {JAMBES[2]},\n 4 séries de 10 répétitions de {JAMBES[3]}.\n\n")
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\nPour travailler vos fessiers: \n4 séries de 10 répétitions de {FESS[0]},\n 4 séries de 10 répétitions de {FESS[1]}, \n 4 séries de 10 répétitions de {FESS[2]},\n 4 séries de 10 répétitions de {FESS[3]}.\n\n')
                        f.write(f"\n\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 3,\n Pour travailler vos fessiers: \n4 séries de 10 répétitions de {FESS[0]},\n 4 séries de 10 répétitions de {FESS[1]}, \n 4 séries de 10 répétitions de FESS{[2]},\n 4 séries de 10 répétitions de {FESS[3]}.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 séries de 10 répétitions de {JAMBES[1]}, \n 4 séries de 10 répétitions de {JAMBES[2]},\n 4 séries de 10 répétitions de {JAMBES[3]}.\n\n Entre deux journées d_entrainement vous devez observer au moins une journeé de repos(sans entrainement). ")
                   




            elif (nombre==4):
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 1 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n')
                    st.text(f"\n\n Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 3 vous ferez:,\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\n")
                    st.text(f'Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 4 vous ferez:,\n\n Pour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\nPour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive. ')
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 1 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n')
                        f.write(f"\n\n Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 3 vous ferez:,\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\n")
                        f.write(f'Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 4 vous ferez:,\n\n Pour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\nPour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive. ')
                   

            
            
            elif(nombre==5):
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jours 1 et 3, vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n' )
                    st.text(f"\n\n Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 et 4 vous ferez:,\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n")
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 5 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\nPour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\nVous devez observer au moins deux journeés de repos(sans entrainement) par semaine.')
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jours 1 et 3, vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n' )
                        f.write(f"\n\n Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 et 4 vous ferez:,\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n")
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 5 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\nPour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\nVous devez observer au moins deux journeés de repos(sans entrainement) par semaine.')
                    



        elif (imc>=30 and imc<35):
            nombre=st.number_input('Combien de fois pouvez-vous vous entrainer par semaine? Choissisez un nombre de fois entre 3 et 5: \n')
            if (nombre<3 and nombre>5):
                    st.text('Valeur invalide')
            if (nombre==3):
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 1 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                    st.text(f"\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 séries de 10 répétitions de {JAMBES[1]}, \n 4 séries de 10 répétitions de {JAMBES[2]},\n 4 séries de 10 répétitions de {JAMBES[3]}.\n\n")
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\nPour travailler vos fessiers: \n4 séries de 10 répétitions de {FESS[0]},\n 4 séries de 10 répétitions de {FESS[1]}, \n 4 séries de 10 répétitions de {FESS[2]},\n 4 séries de 10 répétitions de {FESS[3]}.\n\n')
                    st.text(f"\n\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 3,\n Pour travailler vos fessiers: \n4 séries de 10 répétitions de {FESS[0]},\n 4 séries de 10 répétitions de {FESS[1]}, \n 4 séries de 10 répétitions de FESS{[2]},\n 4 séries de 10 répétitions de {FESS[3]}.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 séries de 10 répétitions de {JAMBES[1]}, \n 4 séries de 10 répétitions de {JAMBES[2]},\n 4 séries de 10 répétitions de {JAMBES[3]}.\n\n Entre deux journées d_entrainement vous devez observer au moins une journeé de repos(sans entrainement). ")
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 1 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                        f.write(f"\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 séries de 10 répétitions de {JAMBES[1]}, \n 4 séries de 10 répétitions de {JAMBES[2]},\n 4 séries de 10 répétitions de {JAMBES[3]}.\n\n")
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\nPour travailler vos fessiers: \n4 séries de 10 répétitions de {FESS[0]},\n 4 séries de 10 répétitions de {FESS[1]}, \n 4 séries de 10 répétitions de {FESS[2]},\n 4 séries de 10 répétitions de {FESS[3]}.\n\n')
                        f.write(f"\n\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 3,\n Pour travailler vos fessiers: \n4 séries de 10 répétitions de {FESS[0]},\n 4 séries de 10 répétitions de {FESS[1]}, \n 4 séries de 10 répétitions de FESS{[2]},\n 4 séries de 10 répétitions de {FESS[3]}.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n4 séries de 10 répétitions de {JAMBES[0]},\n 4 séries de 10 répétitions de {JAMBES[1]}, \n 4 séries de 10 répétitions de {JAMBES[2]},\n 4 séries de 10 répétitions de {JAMBES[3]}.\n\n Entre deux journées d_entrainement vous devez observer au moins une journeé de repos(sans entrainement). ")
                   




            elif (nombre==4):

                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 1 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n')
                    st.text(f"\n\n Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 3 vous ferez:,\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\n")
                    st.text(f'Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 4 vous ferez:,\n\n Pour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\nPour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive. ')
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 1 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n')
                        f.write(f"\n\n Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 3 vous ferez:,\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\n")
                        f.write(f'Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 4 vous ferez:,\n\n Pour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\nPour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive. ')
                    

            
            
            elif(nombre==5):
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jours 1 et 3, vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n' )
                    st.text(f"\n\n Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 et 4 vous ferez:,\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n")
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 5 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\nPour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\nVous devez observer au moins deux journeés de repos(sans entrainement) par semaine.')
                    
                    with open('ALPHAS.txt', 'w') as f:
                            pass
                    
                    with open('ALPHAS.txt', 'a') as f:
                        f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jours 1 et 3, vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n' )
                        f.write(f"\n\n Pour chacun de vos entrainements des 4 prochaines semaines chaque jour 2 et 4 vous ferez:,\n\n Pour les abdos vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n\n Pour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\nPour travailler vos fessiers: \n 5 séries de 10 répétitions de {FESS[0]},\n 5 séries de 10 répétitions de {FESS[1]}, \n 5 séries de 10 répétitions de {FESS[2]},\n 5 séries de 10 répétitions de {FESS[3]}.\n\n")
                        f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour 5 vous ferez:\n\n Pour le cardio 10 minutes de {cours}, \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.Le repos entre le changement d_exercices est de 2 minutes.\n\nPour travailler vos jambes: \n5 séries de 10 répétitions de {JAMBES[0]},\n 5 séries de 10 répétitions de {JAMBES[1]}, \n 5 séries de 10 répétitions de {JAMBES[2]},\n 5 séries de 10 répétitions de {JAMBES[3]}.\n\nVous devez observer au moins deux journeés de repos(sans entrainement) par semaine.')
                    

        
        
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
            nombre=st.number_input('Combien de fois pouvez-vous vous entrainer par semaine? Choissisez un nombre de fois entre 3 et 5: \n')
            if (nombre<3 or nombre>5):
                st.text("Valeur invalide!")
            else:
                #print('well')
                if (nombre==3):
                    if(st.button('Générer le programme d_entrainement')):
                        st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                        st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\n Entre deux journées d_entrainement vous devez observer au moins une journeé de repos(sans entrainement). ")
                        
                        with open('ALPHAS.txt', 'w') as f:
                            pass
                        
                        with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                            f.write(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\n Entre deux journées d_entrainement vous devez observer au moins une journeé de repos(sans entrainement). ")
                       
                
                
                elif (nombre==4):
                    if(st.button('Générer le programme d_entrainement')):
                        
                        st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                        st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive.  ")
                        
                        with open('ALPHAS.txt', 'w') as f:
                            pass
                        
                        with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                            f.write(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\n Vous devez observer au moins 3 journeés de repos(sans entrainement) par semaine et répartir les séances sur la semaine a votre convenance sans cumuler les 4jours d_entrainement de manière consécutive.  ")
                       


                elif(nombre==5):
                    if(st.button('Générer le programme d_entrainement')):
                        st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                        st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                        st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\nVous devez observer au moins deux journeés de repos(sans entrainement) par semaine. ")
                        
                        with open('ALPHAS.txt', 'w') as f:
                            pass
                        
                        with open('ALPHAS.txt', 'a') as f:
                            f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                            f.write(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n  15 minutes de {cours} et ensuite on a: \n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 2 minutes.')
                            f.write(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.\n\nVous devez observer au moins deux journeés de repos(sans entrainement) par semaine. ")
                        

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
            if(st.button('Générer le programme d_entrainement')):
                st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                st.text(f'Pour chacune de vos séances hebdomaires,on a:\n\n 15min de {z},15min de {z0} et de 15min de {z1} pour le cardio.\nLe repos entre le changement d_exercices est de 5 minutes.\n\n Pour les abdos,vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 4 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.')
                
                with open('ALPHAS.txt', 'w') as f:
                            pass
                
                with open('ALPHAS.txt', 'a') as f:
                    f.write(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    f.write(f'Pour chacune de vos séances hebdomaires,on a:\n\n 15min de {z},15min de {z0} et de 15min de {z1} pour le cardio.\nLe repos entre le changement d_exercices est de 5 minutes.\n\n Pour les abdos,vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 4 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 2 minutes de repos.')

#st.header('LA DEMONSTRATION, AINSI QUE L_EXECUTION DE TOUT LES EXERCICES SONT DISPONIBLES SUR LE SITE DOCTEURFITNESS.COM')
    st.subheader('A CHAQUE FOIS QU_UN PLAN D_ENTRAINEMENT NE VOUS PLAIT PAS, VEUILLEZ APPUYEZ A NOUVEAU SUR LE BOUTON GENERER LE PROGRAMME D_ENTRAINEMENT, UN NOUVEAU PLAN VOUS SERA SUGGERE.')
         

    def telecharger_fichier():
            with open (r'ALPHAS.txt', 'r') as f:
                contenu=f.read()
            return contenu.encode()
    def main():
            st.write('cliquez sur le bouton suivant pour télécharger le plan d_entrainement')
            wishes=st.radio("TELECHARGER LE PLAN D'ENTRAINEMENT",('néant','non','oui'))
            if wishes=='oui':
                fichier=telecharger_fichier()
                st.download_button(
                    label="telecharger",
                    data=fichier,
                    file_name=r'ALPHAS.txt',
                    mime='text/plain'
                    )
            else:
                pass
        
    if __name__=="__main__":
            main()
    st.markdown('LA DEMONSTRATION, AINSI QUE L_EXECUTION DE TOUT LES EXERCICES SONT DISPONIBLES SUR LE SITE [docteur-fitness.com](https://www.docteur-fitness.com).')
    #site=st.link_button('docteurfitness', 'https://www.docteur-fitness.com')
    