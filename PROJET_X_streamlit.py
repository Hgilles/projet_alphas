import pandas as pd
import streamlit  as st

st.title("PROJET_X")
st.header('Projet_X by HOUNME HOUETO EMERICK GILLES')


ac=pd.read_csv(r'aliments3.txt', sep=';')

gluc=ac[ac.accompagnement=='No']
#gluc['aliments']=gluc['aliments(en moyenne)']

prot=ac[ac.accompagnement=='Yes']
sauce=ac[ac.accompagnement=='maybe']

gluc=ac.drop(ac[ac['categorie']=='sauce to'].index)
gluc=gluc.drop(gluc[gluc['categorie']=='gésier'].index)
gluc=gluc.drop(gluc[gluc['categorie']=='saucisse'].index)
gluc=gluc.drop(gluc[gluc['categorie']=='bouillie'].index)
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


#def depense_calorique():
nom=st.text_input('Entrez votre nom et prénoms: ')
if type(nom) is not str:
    print('Valeur invalide!')
elif type(nom) is str :
    if len(nom)>0:

        gen=st.radio('quel est votre sexe de naissance?: ',('Homme','Femme'))

        if gen=='Homme':
            gender=0
        else:
            gender=1

        if gender==0:
            
            poids=st.number_input('Entrez votre poids(en kg): \n',1,1000)
            
            if (poids>0):

                taille=st.number_input('Entrez votre taille(en cm): \n',1,1000)
            
                if (taille >0):
            
                    age=st.number_input('Entrez votre age: \n',1,500)
        
            mba=(13.7516*poids) + (500.33*taille/100) - (6.7550*age) + 66.473
            mbb=(13.707*poids) + (492.3*taille/100) - (6.673*age) + 77.607
            
            
            MBh=(mba+mbb)/2
            
            if age>0:
                ap=st.radio('Avez vous une activité physique chaque semaine de manière régulière sur les 12 derniers mois ?', ('non','oui'))
                if ap=='non':
                    dep_cal=MBh*1.2
                else:
                    freq=st.selectbox('A quelle fréquence?',[ 'moins de 3 fois par semaine' , "3fois par semaine" , "plus de 3fois par semaine"])
                    if freq=='moins de 3 fois par semaine':
                        dep_cal=MBh*1.4
                    elif freq=='3fois par semaine':
                        dep_cal=MBh*1.6
                    elif freq=='plus de 3fois par semaine':
                        dep_cal=MBh*1.8
            #st.text(f'Votre métabolisme de base est de {MBh}')
                
    #        return (f'Votre metabolisme de base est d_environ {MBh} et votre dépense calorique est {dep_cal}')
        
        elif gender==1:
            poids=st.number_input('Entrez votre poids(en kg): \n',1,1000)
            
            if (poids>0):

                taille=st.number_input('Entrez votre taille(en cm): \n',1,1000)
            
                if (taille >0):
            
                    age=st.number_input('Entrez votre age: \n',1,500)
        
                
            mba=(9.5634*poids) + (184.96*taille/100) - (6.7556*age) + 655.0955
            mbb=(9.740*poids) + (172.9*taille/100) - (4.737*age) + 667.051
            
            MBf=(mba+mbb)/2
            
            if age>0:
                ap=st.radio('Avez vous une activité physique chaque semaine de manière régulière sur les 12 derniers mois ?', ('non','oui'))
                if ap=='non':
                    dep_cal=MBf*1.2
                else:
                    freq=st.selectbox('A quelle fréquence?',[ 'moins de 3 fois par semaine' , "3fois par semaine" , "plus de 3fois par semaine"])
                    if freq=='moins de 3 fois par semaine':
                        dep_cal=MBf*1.4
                    elif freq=='3fois par semaine':
                        dep_cal=MBf*1.6
                    elif freq=='plus de 3fois par semaine':
                        dep_cal=MBf*1.8
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
            st.text(f'Votre  dépense calorique est de {dep_cal} calories et répartition moyenne journalière {brek} calories')
            with open('text.txt', 'w') as f:
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
        
        
                if (crb_cate=='fruit'):
                    oe=prot[prot.aliments=='oeuf(en moyenne)']
                    oe1=int(oe.index[(oe['aliments']==oe['aliments'].iloc[0])][0])
                    bcaa_cal=oe._get_value(oe1, 'calories (100g)')
                    bcaa_name=oe._get_value(oe1, 'aliments')
            
                if (crb_cate=='bouillie'):
                    bou=0.7*brek
                    su=0.05*brek
                    arak=0.15*brek
                    laiti=0.1*brek

            # bouil=bou*100/p_cal
                    sug=su*100/suc_cal
                    la=laiti*100/milk_cal
                    araki=arak*100/ara_cal
            #  print (f'on a pour le petit_dej {bouil} g de {p_name}, avec {sug}g de {suc_name}, {la}g de {milk_name} et {araki}g de {ara_name}')
        
        
        
                a1=0.6*(brek)
        #a=a1/crb_cal
                b1=0.4*(brek)
        #b=b1/bcaa_cal
                brek1=a1*100/crb_cal
                brek2=b1*100/bcaa_cal
        
        #return print(f'on a {a1,b1} le petit dejeuner est {brek1} grammes de {crb_name} et {brek2} grammes de {bcaa_name} ')
        
        
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
            
                if (crb_lun_cate=='bouillie'):
                    bou=0.7*brek
                    su=0.05*brek
                    arak=0.15*brek
                    laiti=0.1*brek

            # bouil=bou*100/p_cal
                    sug=su*100/suc_cal
                    la=laiti*100/milk_cal
                    araki=arak*100/ara_cal
            #   return (f'on a pour le dej {bouil} g de {p_name}, avec {sug}g de {suc_name}, {la}g de {milk_name} et {araki}g de {ara_name}')


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
            
            
            #if (crb_t_cate=='bouillie'):
                    bou=0.7*brek
                    su=0.05*brek
                    arak=0.15*brek
                    laiti=0.1*brek

            #   bouil=bou*100/p_cal
                    sug=su*100/suc_cal
                    la=laiti*100/milk_cal
                    araki=arak*100/ara_cal
            #  return (f'on a pour le 3e {bouil} g de {p_name}, avec {sug}g de {suc_name}, {la}g de {milk_name} et {araki}g de {ara_name}')
            
        

                a1=0.6*(third)
                a=a1/crb_t_cal
                b1=0.4*(third)
                b=b1/bcaa_t_cal
                t1=a*100
                t2=b*100
        
                if (crb_cate=='pâte'):
                    crb_name=crb_name+' et '+sauce_name
                if (crb_lun_cate=='pâte'):
                    crb_lun_name=crb_lun_name+' et '+sauce_name
                if (crb_t_cate=='pâte'):
                    crb_t_name=crb_t_name+' et '+sauce_name
            
                
                st.text(f'\n\n, Le petit dejeuner du jour {i} est {brek1} grammes de {crb_name} et {brek2} grammes de {bcaa_name},\n Le dejeuner est {lun1} grammes de {crb_lun_name} et {lun2} grammes de {bcaa_lun_name}, \n Le dernier est {t1} grammes de {crb_t_name} et {t2} grammes de {bcaa_t_name} \n')
                
                

                with open('text.txt', "a") as f:
                    f.write(f'Votre  dépense calorique est de {dep_cal} calories et répartition moyenne journalière {brek} calories')
            
                    f.write(f'\n\n, Le petit dejeuner du jour {i} est {brek1} grammes de {crb_name} et {brek2} grammes de {bcaa_name},\n Le dejeuner est {lun1} grammes de {crb_lun_name} et {lun2} grammes de {bcaa_lun_name}, \n Le dernier est {t1} grammes de {crb_t_name} et {t2} grammes de {bcaa_t_name} \n')
                  
   
    saving=st.radio('Voulez-vous sauvegarder ce plan?',('non', 'oui'))
    
    if saving=='oui':
        def telecharger_fichier():
            with open (r'C:\Users\pc\Desktop\PROJET_X\text.txt', 'r') as f:
                contenu=f.read()
            return contenu.encode()
        def main():
            st.title('telechargement du fichier')
            st.write('cliquez sur le bouton suivant pour télécharger le fichier')

            if st.button('telecharger'):
                fichier=telecharger_fichier()
                st.download_button(
                    label="telecharger",
                    data=fichier,
                    file_name=r'text.txt',
                    mime='text/plain'
                )
        if __name__=="__main__":
            main()
        
        elif saving=='non':
            with open('text.txt', 'w') as f:
                pass





