import streamlit as st
st.title("🏋️‍♂️WELCOME TO THE BODYFAT ¨PREDICTION'S APP!🏋️‍♀️")
st.subheader('PREDICTIVE APP BY HOUNME HOUETO EMERICK GILLES')

st.text('Choose one language')
if(st.checkbox('English')):
    age=st.number_input('Enter your age :')
    poids=st.number_input("Enter your weight(in kg): ")
    taille=st.number_input('Enter your height (in m):', 1.0,3.0)

    t_taille=st.number_input('Enter your waist measurment: ',0.0)
    #t_taille=t_taille/2
    #neck=st.number_input('Entrez votre tour de cou en cm:',0.0)
    #POIDS IDEAUX MALE/FEMELLES




    imc=(poids/(taille*taille))
    gent=st.radio('What_s your birth gender?',('male', 'female'))


    if st.button('predict my bodyfat percentage'):
        with open('test.txt', 'w') as f:
                    pass
        if gent=='male':
            img=1.20*imc+0.23*age-10.8-5.4
            mg=poids*(img/100)
            mmg=poids-mg
            ffmi=(mmg/2.2)*2.20462/(taille*taille)
            ffmi_cor=ffmi+(6.1*(1.8-(taille/100)))
            w_idmen=(taille*100)-100-(taille*100-(150/4))
            #st.text(f'Votre ffmi est de {ffmi} .')
            if img>0:
                if img<15:
                    st.text(f'your bodyfat is {img}%. It_s litlle low.')
                    #st.write(f'\n\nVotre poids idéal est de {w_idmen}.')
                    with open('test.txt', "a") as f:
                        f.write(f'your bodyfat is {img}%. It_s litlle low.')
                        #f.write(f'Votre ffmi est de {ffmi} .')
                
                elif(15<img<20):
                    st.text(f"your bodyfat is {img} %.It is normal.")
                    #st.write(f'\n\nVotre poids idéal est de {w_idmen}.')
                    with open('test.txt', "a") as f:
                        f.write(f"your bodyfat is {img} %.It is normal.")
                        #f.write(f'Votre ffmi est de {ffmi} .')
                
                elif img>20:
                    st.text(f'Your bodyfat is {img}. Litlle more than the normal.')
                    #st.write(f'\n\nVotre poids idéal est de {w_idmen}.')
                    with open('test.txt', "a") as f:
                        f.write(f"Your bodyfat is {img}. Litlle more than the normal.")
                        #f.write(f'Votre ffmi est de {ffmi}.')
            #forme=st.radio('Voulez vous connaitre votre type de forme?',('oui','non'))
                
        
        else:
                
                img=1.20*imc+0.23*age-5.4

                mg=poids*(img/100)
                mmg=poids-mg
                ffmi=(mmg/2.2)*2.20462/(taille*taille)
                ffmi_cor=ffmi+(6.1*(1.8-(taille/100)))

                #st.text(f'Votre ffmi est de {ffmi} .')

                if img>0:
                    w_idwomen=(taille*100)-100-(taille*100-(150*5/2))
                    if img<25:
                        
                        st.text(f'"your bodyfat is {img}%.It is litlle low.')
                        #st.write(f'\n\nVotre poids idéal est de {w_idwomen}.')
                        with open('test.txt', "a") as f:
                            f.write(f"your bodyfat is {img}%.It is litlle low.")
                            #f.write(f'Votre ffmi est de {ffmi} .')
                    elif(25<img<30):
                        st.text(f"your bodyfat is {img}% . It's normal.")
                        #st.write(f'\n\nVotre poids idéal est de {w_idwomen}.')
                        with open('test.txt', "a") as f:
                            f.write(f"your bodyfat is {img}% . It's normal.")
                            #f.write(f'Votre ffmi est de {ffmi} .')
                    elif img>30:
                        st.text(f'Your bodyfat is {img}. Litlle more than the normal.')
                        #st.write(f'\n\nVotre poids idéal est de {w_idwomen}.')
                        with open('test.txt', "a") as f:
                            f.write(f"Your bodyfat is {img}. Litlle more than the normal.")
                            #f.write(f'Votre ffmi est de {ffmi} .')
        
    def download_file():
        with open (r'test.txt', 'r') as f:
            contenu=f.read()
        return contenu.encode()
    def main():
        st.title('File_s downloading')
        #st.write('cliquez sur le bouton suivant pour télécharger le fichier')
        down=st.radio('Do you want to download the results?',('no','yes'))

        if down=='yes':
            fichier=download_file()
            st.download_button(
                label="download",
                data=fichier,
                file_name=r'test.txt',
                mime='text/plain'
            )
        else:
            pass
    if __name__=="__main__":
        main()
elif st.checkbox('Français'):
    age=st.number_input('Entrez votre age :')
    poids=st.number_input("Entrez votre poids en kg: ")
    taille=st.number_input('Entrez votre taille en m:', 1.0,3.0)

    t_taille=st.number_input('Entrez votre tour de taille en cm: ',0.0)
    #t_taille=t_taille/2
    #neck=st.number_input('Entrez votre tour de cou en cm:',0.0)
    #POIDS IDEAUX MALE/FEMELLES




    imc=(poids/(taille*taille))
    gent=st.radio('Vous etes né homme ou femme?',('homme', 'femme'))


    if st.button('prédire mon pourcentage de masse grasse'):
        with open('test.txt', 'w') as f:
                    pass
        if gent=='homme':
            img=1.20*imc+0.23*age-10.8-5.4
            mg=poids*(img/100)
            mmg=poids-mg
            ffmi=(mmg/2.2)*2.20462/(taille*taille)
            ffmi_cor=ffmi+(6.1*(1.8-(taille/100)))
            w_idmen=(taille*100)-100-(taille*100-(150/4))
            #st.text(f'Votre ffmi est de {ffmi} .')
            if img>0:
                if img<15:
                    st.text(f'votre pourcentage de graisse corporelle est de {img}. C_est un peu bas.')
                    #st.write(f'\n\nVotre poids idéal est de {w_idmen}.')
                    with open('test.txt', "a") as f:
                        f.write(f'votre pourcentage de graisse corporelle est de {img}. C_est un peu bas.')
                        #f.write(f'Votre ffmi est de {ffmi} .')
                
                elif(15<img<20):
                    st.text(f"votre pourcentage de graisse corporelle est de {img} . C_est un taux normal.")
                    #st.write(f'\n\nVotre poids idéal est de {w_idmen}.')
                    with open('test.txt', "a") as f:
                        f.write(f"votre pourcentage de graisse corporelle est de {img} . C_est un taux normal.")
                        #f.write(f'Votre ffmi est de {ffmi} .')
                
                elif img>20:
                    st.text(f'Votre pourcentage de graisse corporelle est de {img}. Un peu supérieur a la normale.')
                    #st.write(f'\n\nVotre poids idéal est de {w_idmen}.')
                    with open('test.txt', "a") as f:
                        f.write(f"votre pourcentage de graisse corporelle est de {img} . Un peu supérieur a la normale.")
                        #f.write(f'Votre ffmi est de {ffmi}.')
            #forme=st.radio('Voulez vous connaitre votre type de forme?',('oui','non'))
                
        
        else:
                
                img=1.20*imc+0.23*age-5.4

                mg=poids*(img/100)
                mmg=poids-mg
                ffmi=(mmg/2.2)*2.20462/(taille*taille)
                ffmi_cor=ffmi+(6.1*(1.8-(taille/100)))

                #st.text(f'Votre ffmi est de {ffmi} .')

                if img>0:
                    w_idwomen=(taille*100)-100-(taille*100-(150*5/2))
                    if img<25:
                        
                        st.text(f'votre pourcentage de graisse corporelle est de {img}. C_est un peu bas.')
                        #st.write(f'\n\nVotre poids idéal est de {w_idwomen}.')
                        with open('test.txt', "a") as f:
                            f.write(f"votre pourcentage de graisse corporelle est de {img} .C_est un peu bas.")
                            #f.write(f'Votre ffmi est de {ffmi} .')
                    elif(25<img<30):
                        st.text(f"votre pourcentage de graisse corporelle est de {img} . C_est un taux normal.")
                        #st.write(f'\n\nVotre poids idéal est de {w_idwomen}.')
                        with open('test.txt', "a") as f:
                            f.write(f"votre pourcentage de graisse corporelle est de {img} . C_est un taux normal.")
                            #f.write(f'Votre ffmi est de {ffmi} .')
                    elif img>30:
                        st.text(f'Votre pourcentage de graisse corporelle est de {img}. Un peu supérieur a la normale.')
                        #st.write(f'\n\nVotre poids idéal est de {w_idwomen}.')
                        with open('test.txt', "a") as f:
                            f.write(f"votre pourcentage de graisse corporelle est de {img} . Un peu supérieur a la normale.")
                            #f.write(f'Votre ffmi est de {ffmi} .')
        def telecharger_fichier():
            with open (r'test.txt', 'r') as f:
                contenu=f.read()
            return contenu.encode()
        def main():
            st.title('telechargement du fichier')
            #st.write('cliquez sur le bouton suivant pour télécharger le fichier')
            down=st.radio('Voulez-vous télécharger les résultats?',('non','oui'))

            if down=='oui':
                fichier=telecharger_fichier()
                st.download_button(
                    label="telecharger",
                    data=fichier,
                    file_name=r'test.txt',
                    mime='text/plain'
                )
            else:
                pass
        if __name__=="__main__":
            main()
            
            