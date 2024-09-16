import streamlit as st 

import pandas as pd
import streamlit as st 
fit=pd.read_csv(r'exo.txt', sep=',')

PDC=fit[fit.cibles=='pdc']
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

pd_c=PDC.sample(7)
Pdc=[]
for i in range(len(pd_c)):
    z=pd_c['exercices'].iloc[i] 
    z=z.upper()
    Pdc.append(z) 


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

#
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

        p=st.radio('Quel programme préférez-vous?',('Aucun', 'Poids du corps','machine et haltères'))

        if p=='Aucun':
            pass
        elif p=='Poids du corps':
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

            exp=st.radio('Comment appréciez-vous votre niveau d_expérience?',('Néant','débutant', 'intermédiaire', 'avancé'))
                

            if(st.button('Générer le programme d_entrainement partie abdos:')):
                if (exp=='débutant'):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n\n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 1 minute.')
                    st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 1 minutes de repos.\n\n")
                    st.text("Vous prenez ensuite 5min de repos et vous commencez les exercices de musculation au poids du corps. \n\n")
                
                
                    st.text(f"On a à un rythme de 3 séries de 10 répétitions de {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n et de {Pdc[6]}")
                    st.text("Le temps de repos entre chaque série est de 45 secondes. Celui entre le changement d'exercices est de  2min.")
                elif (exp=='intermédiaire'):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n\n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 1 minute.')
                    st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 1 minutes de repos.\n\n")
                    st.text("Vous prenez ensuite 5min de repos et vous commencez les exercices de musculation au poids du corps. \n\n")
                

                    st.text(f"On a à un rythme de 5 séries de 10 répétitions de {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n et de {Pdc[6]}")
                    st.text("Le temps de repos entre chaque série est de 30 secondes. Celui entre le changement d'exercices est de  2min.")

                elif (exp=='avancé'):

                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'\nPour chacun de vos entrainements des 4 prochaines semaines chaque jour vous ferez:\n\n 3 séries de 30 secondes d_exercices et 30 secondes de récupération de: {CAR[0]},\n ensuite 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[1]},\n ensuite 3 séries de 30 secondes d_exerxices et 30 secondes de récupération de {CAR[2]}, \n après 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[3]},\n et pour finir 3 séries de 30 secondes d_exercices et 30 secondes de récupération de {CAR[4]}.\n Le repos entre le changement d_exercices est de 1 minute.')
                    st.text(f"\n\nAussi vous ferez:\n 4 séries de 10 répétitions de {ABS[0]},\n 4 séries de 10 répétitions de {ABS[1]}, \n 4 séries de 10 répétitions de {ABS[2]},\n 4 séries de 10 répétitions de {ABS[3]}, \n 4 séries de 10 répétitions de {ABS[4]},\n 3 séries de 30 secondes de {ABS[5]}.\n Entre chaque exercice prendre 1 minutes de repos.\n\n")
                    st.text("Vous prenez ensuite 5min de repos et vous commencez les exercices de musculation au poids du corps. \n\n")
                

                    st.text(f"On a à un rythme de 7 séries de 10 répétitions de {Pdc[0]}, \n {Pdc[1]} , \n{Pdc[2]} , \n{Pdc[3]},  \n{Pdc[4]}, \n{Pdc[5]}, \n et de {Pdc[6]}")
                    st.text("Le temps de repos entre chaque série est de 30 secondes. Celui entre le changement d'exercices est de  3min.")
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
                
            elif(nombre==5):
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'Pour les jours 1 , 3 et 5 des 4 prochaines semaines on va au programme le dos, les pectoraux et les épaules.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos, on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux, on a: {PECS[0]} pour travailler le {PECS[1]},\n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]}. Pour les épaules, on a : {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                    st.text(f'\n\n Pour le jour 2 et 4 des 4 prochaines semaines on démarre avec les biceps , les triceps et les jambes.Voici les exercices a faire suivant un rythme de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour les biceps et les Triceps on a, {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]},\n \n Pour les jambes , on a: {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.')
            elif (nombre==6):
                if(st.button('Générer le programme d_entrainement')):
                    st.text(f'Votre imc est de {imc} et voici ci-dessous votre programme:\n\n')
                    st.text(f'Pour les jours 1 et 4 on a: le dos et les épaules.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n Pour le dos, on a: {DOS[0]} pour travailler les {DOS[1]},\n ensuite {DOS[2]} pour les {DOS[3]}, \n et {d0} pour travailler les {d1}.\n\n Pour les pectoraux, on a:  {PECS[0]} pour travailler le {PECS[1]},\n\n \n Pour les épaules, on a : {a0} pour travailler le {a1},\n ensuite {EPAULES[2]} pour la {EPAULES[3]}, \n et {EPAULES[4]} pour travailler le {EPAULES[5]}, \n{EPAULES[6]} pour travailler le {EPAULES[7]}.')
                    st.text(f'\n\n Pour les jour 2 et 5 on démarre avec les pectoraux les biceps , les triceps.Voici les exercices a faire suivant un rythme minimal de 3 séries de 10 répétitions au moins pour chaque exercice :\n\n \n ensuite {PECS[2]} pour la {PECS[3]}, \n et {PECS[4]} pour travailler le {PECS[5]},\n\n pour les biceps,on a: {BRAS[0]} pour travailler le {BRAS[1]},\n ensuite {BRAS[2]} pour la {BRAS[3]}, \n et {BRAS[4]} pour travailler le {BRAS[5]}, \n\n{BRAS[6]} pour travailler le {BRAS[7]},\n ensuite {BRAS[8]} pour la {BRAS[9]}, \n et {BRAS[10]} pour travailler le {BRAS[11]}')
                    st.text(f'\n \n Pour les jours 3 et 6 jambes \n\n {JAMBES[0]},\n {JAMBES[1]},\n ensuite {JAMBES[2]} pour les {JAMBES[3]}, \n et {JAMBES[4]} pour travailler les {JAMBES[5]}.')
        