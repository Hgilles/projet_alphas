import pandas as pd
import streamlit as st 

st.header('🦍 KWABƆ ƉƆ PROJET_ALPHAS  HOUNME HOUETO EMERICK GILLES TON DJI !!!🦍')
st.image(['télécharger.jpg','th (1).jpg'])
ac=pd.read_csv(r'aliment-fon.txt', sep=';', encoding='utf-8')

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
a2=gluc['aliment-fon'].iloc[8]
a1=int(gluc.index[(gluc['aliment-fon']==a['aliment-fon'].iloc[0])][0])
crb_cal=a._get_value(a1, 'calories (100g)')
crb_name=a._get_value(a1, 'aliment-fon')
crb_cat=a._get_value(a1, 'categorie')


b=prot.sample()
b1=int(prot.index[(prot['aliment-fon']==b['aliment-fon'].iloc[0])][0])
bcaa_cal=b._get_value(b1, 'calories (100g)')
bcaa_name=b._get_value(b1, 'aliment-fon')

c=sauce.sample()
c1=int(sauce.index[(sauce['aliment-fon']==c['aliment-fon'].iloc[0])][0])
#bcaa_cal=b._get_value(b1, 'calories (100g)')
sauce_name=c._get_value(c1, 'aliment-fon')
sauce_cat=c._get_value(c1, 'categorie')

arachide=ac[ac.categorie=='arachide']
sucre=ac[ac.categorie=='sucre']
lait=ac[ac.categorie=='lait']


#def depense_calorique():
nom=st.text_input('Mi kɛnklɛn bo nan nyikɔ mitɔn: ')

#st.image()

if type(nom) is not str:
    st.text('Esso gbéa!!')
elif type(nom) is str :
    if len(nom)>0:
        st.text(f'MI KWABƆ {nom}!')
        gen=st.radio('nú a nyí sunnu hǔn, zǐn gbǎví nukɔntɔn ɔ, é ma nyí mɔ̌ ǎ ɔ, zǐn wegɔ ɔ: ',('Sunnu','Nyɔnu'))

        if gen=='Sunnu':
            
            gender=0
        else:
            gender=1

        if gender==0:
            
            poid=st.number_input('Mi kɛnklɛn bo wlan kilo mitɔn e mi ze ɖo dotooxwe ɔ: \n',0)
            
            if (poid >= 0):

                taill=st.number_input('Mi kɛnklɛn bo wlan ga mitɔn lěe e xlɛ gbɔn ɖo ID mitɔn ji e: \n',0)
                
                if (taill >= 0):
            
                    age=st.number_input('kɛnklɛn bo wlan xwe mitɔn din ɔ: \n',0)
        
            mba=(13.7516*poid) + (500.33*taill/100) - (6.7550*age) + 66.473
            mbb=(13.707*poid) + (492.3*taill/100) - (6.673*age) + 77.607
            
            
            MBh=(mba+mbb)/2
            
            if age>=0:
                ap=st.radio('a ka nɔ bló ayihun hwɛhwɛ ɖò sun 12 e wá yì lɛ é mɛ à, enyi é ma nyí mɔ̌ ǎ hǔn, zǐn ɖiɖe e ɖò aga é', ('éo','Ɛɛn'))
                if ap=='éo':
                    dep_cal=MBh*1.1
                else:
                    freq=st.selectbox('enyi mon hǔn, azɔn nabi ɖò aklunɔzán gbla ɖokpo mɛ?',[ 'é hwe hú azɔn aton ɖò aklunɔzán gbla ɖokpo mɛ' , "Azɔn aton ɖo azan ɖokpo mɛ" , "azɔn aton jɛji ɖò aklunɔzán gbla ɖokpo mɛ"])
                    if freq=='é hwe hú azɔn aton ɖò aklunɔzán gbla ɖokpo mɛ':
                        dep_cal=MBh*1.3
                    elif freq=="Azɔn aton ɖo azan ɖokpo mɛ":
                        dep_cal=MBh*1.5
                    elif freq=="azɔn aton jɛji ɖò aklunɔzán gbla ɖokpo mɛ":
                        dep_cal=MBh*1.7
            #st.text(f'Votre métabolisme de base est de {MBh}')
                
    #        return (f'Votre metabolisme de base est d_environ {MBh} et votre dépense calorique est {dep_cal}')
        
        elif gender==1:
            poid=st.number_input('Mi kɛnklɛn bo wlan kilo mitɔn e mi ze ɖo dotooxwe ɔ: \n',0)
            
            if (poid>=0):

                taill=st.number_input('Mi kɛnklɛn bo wlan ga mitɔn lěe e xlɛ gbɔn ɖo ID mitɔn ji e: \n',0)
                
                if (taill >=0):
            
                    age=st.number_input('kɛnklɛn bo wlan xwe mitɔn din ɔ: \n',0)
                
            mba=(9.5634*poid) + (184.96*taill/100) - (6.7556*age) + 655.0955
            mbb=(9.740*poid) + (172.9*taill/100) - (4.737*age) + 667.051
            
            MBf=(mba+mbb)/2
            
            if age>=0:
                ap=st.radio('a ka nɔ bló ayihun hwɛhwɛ ɖò sun 12 e wá yì lɛ é mɛ à, enyi é ma nyí mɔ̌ ǎ hǔn, zǐn ɖiɖe e ɖò aga é', ('éo','Ɛɛn'))
                if ap=='éo':
                    dep_cal=MBf*1.21
                else:
                    freq=st.selectbox('enyi mon hǔn, azɔn nabi ɖò aklunɔzán gbla ɖokpo mɛ?',[ 'é hwe hú azɔn aton ɖò aklunɔzán gbla ɖokpo mɛ' , "Azɔn aton ɖo azan ɖokpo mɛ" , "azɔn aton jɛji ɖò aklunɔzán gbla ɖokpo mɛ"])
                    if freq=='é hwe hú azɔn aton ɖò aklunɔzán gbla ɖokpo mɛ':
                        dep_cal=MBf*1.3
                    elif freq=="Azɔn aton ɖo azan ɖokpo mɛ":
                        dep_cal=MBf*1.5
                    elif freq=='azɔn aton jɛji ɖò aklunɔzán gbla ɖokpo mɛ':
                        dep_cal=MBf*1.7
            # st.text(f'Votre métabolisme de base est de {MBf}')
        brek=dep_cal/3
        

        deficit=dep_cal-500
        night=deficit/10
        rest=deficit-night
        brek=rest/3
        lun=rest/3
        third=rest/3

        dep_cal=round(dep_cal,2)
        brek=round(brek,2)

        c=sauce.sample()
        c1=int(sauce.index[(sauce['aliment-fon']==c['aliment-fon'].iloc[0])][0])
        sauce_name=c._get_value(c1, 'aliment-fon')
        sauce_cat=c._get_value(c1, 'categorie')
        
        
        #ARACHIDE, SUCRE , LAITS
        cacahuete=arachide[['aliment-fon', 'calories (100g)', 'categorie']]
        ara=cacahuete.sample()
        ara1=int(ara.index[(ara['aliment-fon']==ara['aliment-fon'].iloc[0])][0])
        ara_cal=ara._get_value(ara1, 'calories (100g)')
        ara_name=ara._get_value(ara1, 'aliment-fon')
        ara_cate=ara._get_value(ara1, 'categorie')

        laits=lait[['aliment-fon', 'calories (100g)', 'categorie']]
        milk=laits.sample()
        milk1=int(milk.index[(milk['aliment-fon']==milk['aliment-fon'].iloc[0])][0])
        milk_cal=milk._get_value(milk1, 'calories (100g)')
        milk_name=milk._get_value(milk1, 'aliment-fon')
        milk_cate=milk._get_value(milk1, 'categorie')
        
        suc=sucre[['aliment-fon','calories (100g)', 'categorie']]
        suc1=int(suc.index[(suc['aliment-fon']==suc['aliment-fon'].iloc[0])][0])
        suc_cal=suc._get_value(suc1, 'calories (100g)')
        suc_name=suc._get_value(suc1, 'aliment-fon')
        suc_cate=suc._get_value(suc1, 'categorie')
            

        if (st.button('bló tuto nùɖuɖu ce tɔn')):
            st.subheader('Hweɖebǔnu e a ma yí wǎn nú tuto nǔɖuɖu tɔn ɖé ǎ é ɔ, lɛ́vɔ zín butɔn "bló tuto nùɖuɖu ce tɔn" ɔ .')
            
            st.image(['OIP.jpg',"2.jpg"])
            #st.text(f'Votre  dépense calorique est de {dep_cal} calories et répartition moyenne journalière {brek} calories')
            with open('ALPHAS_meals.txt', 'w') as f:
                pass
            for i in range (1,8,1):
                a=gluc.sample()
                a2=a['aliment-fon'].iloc[0]
                a1=int(gluc.index[(gluc['aliment-fon']==a['aliment-fon'].iloc[0])][0])
                crb_cal=a._get_value(a1, 'calories (100g)')
                crb_name=a._get_value(a1, 'aliment-fon')
                crb_cate=a._get_value(a1, 'categorie')
                b=prot.sample()
                b1=int(prot.index[(prot['aliment-fon']==b['aliment-fon'].iloc[0])][0])
                bcaa_cal=b._get_value(b1, 'calories (100g)')
                bcaa_name=b._get_value(b1, 'aliment-fon')

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
                    oe1=int(oe.index[(oe['aliment-fon']==oe['aliment-fon'].iloc[0])][0])
                    bcaa_cal=oe._get_value(oe1, 'calories (100g)')
                    bcaa_name=oe._get_value(oe1, 'aliment-fon')
            
        
        
                a1=0.6*(brek)
                b1=0.4*(brek)
                brek1=a1*100/crb_cal
                brek2=b1*100/bcaa_cal
        
        
                a=gluc.sample()
                a2=a['aliment-fon'].iloc[0]
                a1=int(gluc.index[(gluc['aliment-fon']==a['aliment-fon'].iloc[0])][0])
                crb_lun_cal=a._get_value(a1, 'calories (100g)')
                crb_lun_name=a._get_value(a1, 'aliment-fon')
                crb_lun_cate=a._get_value(a1, 'categorie')

                b=prot.sample()
                b1=int(prot.index[(prot['aliment-fon']==b['aliment-fon'].iloc[0])][0])
                bcaa_lun_cal=b._get_value(b1, 'calories (100g)')
                bcaa_lun_name=b._get_value(b1, 'aliment-fon')
        
                if (crb_lun_cate=='fruit'):
                    oe=prot[prot.aliments=='oeuf(en moyenne)']
                    oe1=(oe.index[(oe['aliment-fon']==oe['aliment-fon'].iloc[0])][0])
                    bcaa_lun_cal=oe._get_value(oe1, 'calories (100g)')
                    bcaa_lun_name=oe._get_value(oe1, 'aliment-fon')
            
            

                a1=0.6*(lun)
                a=a1/crb_lun_cal
                b1=0.4*(lun)
                b=b1/bcaa_lun_cal
                lun1=a*100
                lun2=b*100
        
        
        #third
                a=gluc.sample()
                a2=a['aliment-fon'].iloc[0]
                a1=int(gluc.index[(gluc['aliment-fon']==a['aliment-fon'].iloc[0])][0])
    #print(a2, a1)
                crb_t_cal=a._get_value(a1, 'calories (100g)')
                crb_t_name=a._get_value(a1, 'aliment-fon')
                crb_t_cate=a._get_value(a1, 'categorie')

                b=prot.sample()
                b1=int(prot.index[(prot['aliment-fon']==b['aliment-fon'].iloc[0])][0])
                bcaa_t_cal=b._get_value(b1, 'calories (100g)')
                bcaa_t_name=b._get_value(b1, 'aliment-fon')
        
                if (crb_t_cate=='fruit'):
                    oe=prot[prot.aliments=='oeuf(en moyenne)']
                    oe1=(oe.index[(oe['aliment-fon']==oe['aliment-fon'].iloc[0])][0])
                    bcaa_t_cal=oe._get_value(oe1, 'calories (100g)')
                    bcaa_t_name=oe._get_value(oe1, 'aliment-fon')
            
            
        
                
                brek1=brek1/100
                brek1=int(brek1)
                brek2=brek2/100
                brek2=int(brek2)
                
                lun1=lun1/100
                lun1=int(lun1)
                lun2=lun2/100
                lun2=int(lun2)

                crb_cal=crb_cal/100
                crb_cal=int(crb_cal)
                crb_lun_cal=crb_lun_cal/100
                crb_lun_cal=int(crb_lun_cal)
                #crb_t_cal=crb_t_cal/100
                crb_t_cal=int(crb_t_cal)
                sug=sug/10
                sug=int(sug)
                la=la/10
                la=int(la)
                araki=araki/10
                araki=int(araki)
                


                a1=0.6*(third)
                a=a1/crb_t_cal
                b1=0.4*(third)
                b=b1/bcaa_t_cal
                t1=a*100
                t1=t1/100
                t1=int(t1)

                t2=b*100
                t2=t2/100
                t2=int(t2)

                

                crb_cal=str(crb_cal)
                crb_lun_cal=str(crb_lun_cal)
                crb_t_cal=str(crb_t_cal)
                sug=str(sug)
                la=str(la)
                araki=str(araki)

                if (crb_cate=='bouillie'):
                    ch={crb_name:crb_cal,suc_name:sug}
                    LM={milk_name:la,ara_name:araki}
                    
                    brek1=crb_cal+' gui gannu ɖò hun '+crb_name +', '+ sug
                    crb_name=' '+suc_name+', '
                    brek2=la+' tchivi '+milk_name+' kpô do '+araki
                    bcaa_name=' '+ara_name

                if (crb_lun_cate=='bouillie'):
                    ch={crb_lun_name:crb_lun_cal,suc_name:sug}
                    LM={milk_name:la,ara_name:araki}
                    lun1=crb_lun_cal+' gui gannu ɖò hun '+crb_lun_name +', '+ sug
                    crb_lun_name=' '+suc_name+', '
                    lun2=la+' tchivi '+milk_name+' kpô do '+araki
                    bcaa_lun_name=' '+ara_name
                
                if (crb_t_cate=='bouillie'):
                    ch={crb_t_name:crb_t_cal,suc_name:sug}
                    LM={milk_name:la,ara_name:araki}
                    
                    
                    
                    t1=crb_t_name+' gui gannu ɖò hun kpô do '+crb_t_cal+', '+ sug
                    crb_t_name=' '+suc_name+', '
                    t2=' tchivi '+milk_name+'  kpô do '+araki
                    bcaa_t_name=' '+ara_name
        
                if (crb_cate=='pâte'):
                    crb_name=crb_name+' kpô do '+sauce_name
                if (crb_lun_cate=='pâte'):
                    crb_lun_name=crb_lun_name+' kpô do '+sauce_name
                if (crb_t_cate=='pâte'):
                    crb_t_name=crb_t_name+' kpô do '+sauce_name
                

                st.text(f"\n\nZanzan nuɖuɖu azǎn {i} tɔ ɔ wɛ nyi gui gannu ɖò hun {brek1} {crb_name} ton, kpodo alɔ jlɛ̀n {brek2} ɖò hun nû {bcaa_name} ,\n Nuɖuɖu hwemɛ tɔn ɔ gui gannu ɖò hun {lun1} {crb_lun_name} ton, kpodo alɔ jlɛ̀n {lun2} ɖò hun nû {bcaa_lun_name} , \n Gudo tɔn ɔ wɛ nyi gui gannu ɖò hun {t1} {crb_t_name} ton, kpodo alɔ jlɛ̀n  {t2} ɖò hun nû {bcaa_t_name} \n\n\n")
                with open('ALPHAS_meals.txt', "a", encoding='utf-8') as f:
                    f.write(f"\n\n Zanzan nuɖuɖu azǎn {i} tɔ ɔ wɛ nyi gui gannu ɖò hun {brek1} {crb_name} ton, kpodo alɔ jlɛ̀n {brek2} ɖò hun nû {bcaa_name} ,\n Nuɖuɖu hwemɛ tɔn ɔ gui gannu ɖò hun {lun1} {crb_lun_name} ton, kpodo alɔ jlɛ̀n {lun2} ɖò hun nû {bcaa_lun_name} , \n Gudo tɔn ɔ wɛ nyi gui gannu ɖò hun {t1} {crb_t_name} ton, kpodo alɔ jlɛ̀n  {t2} ɖò hun nû {bcaa_t_name} \n\n\n")
               
                    #f.write(f'Votre  dépense calorique est de {dep_cal} calories et répartition moyenne par repas de  {brek} calories')
            
            def telecharger_fichier():
                    with open (r'ALPHAS_meals.txt', 'r',encoding='utf-8') as f:
                        contenu=f.read()
                    return contenu.encode()
            def main():
                    st.subheader('hɛn nùɖuɖu sín tuto ɔ')
                    wish=st.radio('hɛn nùɖuɖu sín tuto ɔ ',('Ɛɛn','éo'))
                    
                    if wish=='Ɛɛn':
                        fichier=telecharger_fichier()
                        st.download_button(
                            label="hɛn nùɖuɖu sín tuto ɔ",
                            data=fichier,
                            file_name=r'ALPHAS_meals.txt',
                            mime='text/plain'
                        )
                    else:
                        pass
            if __name__=="__main__":
                    main()

#st.title('TELECHARGEMENT DU PLAN D_ENTRAINEMENT')
