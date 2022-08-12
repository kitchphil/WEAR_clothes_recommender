import streamlit as st

def userinput():
    ####################IMPORT LIBRARIES####################
    import pandas as pd
    from datetime import date
    import re
    import requests

    ####################STORE USER INFO####################
    
    #create df
    userinputdump = pd.read_csv('userinputdump.csv')
    
    
    #####CREATE USERID#####
    def useridcreate():
        import string
        import random
        from random import randint
        string.ascii_letters
        one = random.choice(string.ascii_letters)
        two = random.choice(string.ascii_letters)
        three = str(randint(0,9))
        four = str(randint(0,9))
        five = str(randint(0,9))
        six = str(randint(0,9))
        seven = random.choice(string.ascii_letters)
        eight = random.choice(string.ascii_letters)
        userid = one+two+three+four+five+six+seven+eight
        " ".join(random.sample(userid,len(userid)))
        for i in userinputdump['user']:
            if userid == i:
                one = random.choice(string.ascii_letters)
                two = random.choice(string.ascii_letters)
                three = str(randint(10,99))
                four = str(randint(0,9))
                five = str(randint(0,9))
                six = str(randint(0,9))
                seven = random.choice(string.ascii_letters)
                eight = random.choice(string.ascii_letters)
                userid = one+two+three+four+five+six+seven+eight
                " ".join(random.sample(userid,len(userid)))
                return userid
            else:
                " ".join(random.sample(userid,len(userid)))
                return userid
        return userid

    ###Determine Criteria for Multiple Choice###
    valid_gender = ['M', 'F']
    valid_sweat = ['Y', 'N']
    valid_coldhf = ['Y','N']
    valid_exercise = ['Never', '1 or 2 times per month', 'A couple of times per week', 'Every other day', 'Every day']
    
    userid = useridcreate()
    gender = st.radio("Please enter your gender: ",valid_gender, key = '1')
    dob = st.date_input("Please enter your date of birth: " , pd.to_datetime("2020/01/01") ,pd.to_datetime("1900/01/01"), key='2')
    dob = dob.strftime("%d/%m/%Y")
    dob = str(dob) 
    height = st.slider("Please enter your height (cm): ", 50, 230, key = '3')
    weight = st.slider("Please enter your weight (kg): ", 30, 200, key = '4')
    home = st.text_input("Where do you live? (format: City, Country)", key = '5')
    sweat = st.selectbox("Do you sweat easily? ",valid_sweat, key = '6')
    coldhf = st.selectbox("Do you often have cold hands and/or feet? ",valid_coldhf, key = '7')
    exercise = st.selectbox("How often do you exercise? ",valid_exercise, key = '8')
    destination = st.text_input("Where do you want to go out today? (format: City, Country)", key = '9')

    if st.button("What should I wear?"):    
        ####################TRANSFORM INPUT TO DATAFRAME####################
        userinfo = pd.DataFrame({'user' : userid
                           ,'gender':[gender]
                           ,'dob':[dob]
                           ,'height_cm':[height]
                           ,'weight_kg':[weight]
                           ,'currentlocation':[home]
                           ,'sweats':[sweat]
                           ,'coldhf':[coldhf]
                           ,'exercise':[exercise]}).reset_index(drop=True) 


        userinfo = userinfo.reset_index(drop = True)
        userinputdump = userinputdump.reset_index(drop = True)
        userinputdump = pd.concat([userinputdump,userinfo], axis=0).reset_index(drop = True)
        userinputdump.to_csv('userinputdump.csv',index = False)
        print(userinfo)
        print("Your ID is:",userid)

       # return userid
        #destination = st.text_input("Where do you want to go out today? (format: City, Country)", key = '9')
        #userid = userid

        #def clothesrecommender(destination):
        import pandas as pd
        from datetime import date
        import re
        import requests



        userinputdump = pd.read_csv('userinputdump.csv')


        ####################GET INPUT FROM USER####################
        user = userid
        user = str(user)
        #!!!!!DO NOT UNHASH!!!!! 


        #Find existing user
        userinputdump = userinputdump[userinputdump['user'] == user]



        ####################INPUT DESTINATION NAME - City, Country####################

        
    
        ####################CLEAN INPUT DATA####################

        #if height cm contains . , or ' <-- indicates feet' inches
        userinputdump = userinputdump.astype(str)
        for i in userinputdump['height_cm']:
            if '.' in i:
                    if "cm" in i:
                        userinputdump['height_cm'] = userinputdump['height_cm'].replace('cm',' ',regex = True)
                        userinputdump['height_cm'] = userinputdump['height_cm'].astype(float)
                        userinputdump['height_cm'] = userinputdump['height_cm'] * 100
                        userinputdump['height_cm'] = userinputdump['height_cm'].astype(int)
                    else:
                        userinputdump['height_cm'] = userinputdump['height_cm'].astype(float)
                        userinputdump['height_cm'] = userinputdump['height_cm'] * 100
                        userinputdump['height_cm'] = userinputdump['height_cm'].astype(int)

            elif ',' in i:
                    if "cm" in i:
                        userinputdump['height_cm'] = userinputdump['height_cm'].replace('cm',' ',regex = True)
                        userinputdump['height_cm'] = userinputdump['height_cm'].replace(",",'.', regex = True)
                        userinputdump['height_cm'] = userinputdump['height_cm'].astype(float)
                        userinputdump['height_cm'] = userinputdump['height_cm'] * 100
                        userinputdump['height_cm'] = userinputdump['height_cm'].astype(int)
                    else:
                        userinputdump['height_cm'] = userinputdump['height_cm'].replace(",",'.', regex = True)
                        userinputdump['height_cm'] = userinputdump['height_cm'].astype(float)
                        userinputdump['height_cm'] = userinputdump['height_cm'] * 100
                        userinputdump['height_cm'] = userinputdump['height_cm'].astype(int)

            #Convert feet and inches
            elif "'" in i:
                userinputdump['height_cm'] = round((userinputdump['height_cm'].str.split("'", n = 1, expand = True)[0].astype(int) * 30.48)+(userinputdump['height_cm'].str.split("'", n = 1, expand = True)[1].astype(int) * 2.54))
                userinputdump['height_cm'] = userinputdump['height_cm'].astype(int)



         ##Calculate age of person##
        for i in userinputdump['dob']:
            if '/' in i:
                userinputdump['dob'] = re.sub('/','',i)
                userinputdump['dob'] = (userinputdump['dob'].str[0:2]+'-'+userinputdump['dob'].str[2:4]+'-'+userinputdump['dob'].str[4:9])
                userinputdump['dob'] = pd.to_datetime(userinputdump['dob'], format = "%d-%m-%Y")
                userinputdump['now'] = pd.Timestamp("now")
                userinputdump['now'] = userinputdump['now'].astype(str).str[0:10]
                userinputdump['now'] = pd.to_datetime(userinputdump['now'])
                userinputdump['now'] = (userinputdump['now'] - userinputdump['dob'])/365.242199
                userinputdump['age'] = userinputdump['now'].astype(str).str[0:3]
                userinputdump['age'] = userinputdump['age'].astype(int)
                userinputdump = userinputdump.drop(columns='now')
            else:
                userinputdump['dob'] = (userinputdump['dob'].str[0:2]+'-'+userinputdump['dob'].str[2:4]+'-'+userinputdump['dob'].str[4:9])
                userinputdump['dob'] = pd.to_datetime(userinputdump['dob'], format = "%d-%m-%Y")
                userinputdump['now'] = pd.Timestamp("now")
                userinputdump['now'] = userinputdump['now'].astype(str).str[0:10]
                userinputdump['now'] = pd.to_datetime(userinputdump['now'])
                userinputdump['now'] = (userinputdump['now'] - userinputdump['dob'])/365.242199
                userinputdump['age'] = userinputdump['now'].astype(str).str[0:3]
                userinputdump['age'] = userinputdump['age'].astype(int)
                userinputdump = userinputdump.drop(columns='now')


        #####Calculate BMI#####
        userinputdump['height_cm'] = userinputdump['height_cm'].astype(float)
        userinputdump['weight_kg'] = userinputdump['weight_kg'].astype(float)
        userinputdump['bmi'] = round(userinputdump['weight_kg']/((userinputdump['height_cm']/100) ** 2),2)


        #####Separate Home Column into two Columns#####
        userinputdump['currentcity'] = userinputdump['currentlocation'].str.split(", ", n = 1, expand = True)[0]
        userinputdump['currentcountry'] = userinputdump['currentlocation'].str.split(", ", n = 1, expand = True)[1]



        ####################FIND REFERENCE FOR LAT & LONG COORDINATES TO FEED INTO API####################

        #load dataset
        geo = pd.read_csv('towns_latlong.csv', sep = ';')


        #convert titles to lower case, change spaces for _
        lower = []
        under = []
        for i in geo.columns:
            lower.append(i.lower())
        for j in lower:
            under.append(j.replace(' ','_'))
        geo.columns = under


        #filter columns in dataframe
        geo = geo[['geoname_id','name','alternate_names','country_name_en','country_code','timezone','label_en','coordinates','population' ]]


        #split geocode to isolate both latitude and longitude
        geo['latitude'] = geo['coordinates'].str.split(",", n=1, expand = True)[0]
        geo['longitude'] = geo['coordinates'].str.split(",", n=1, expand = True)[1]


        #split the searched location as two values: city and country
        city = destination.split(', ')[0]
        country = destination.split(', ')[1]


        #filter df to match searched location, then isolate the latitude and longitude as string 
        search = geo[(geo['name'] == city) & (geo['country_name_en'] == country)]

        if len(search) > 1:
            search = search.sort_values(by='population', ascending = False).reset_index(drop=True)
            search = search.loc[[0]]


        lat = search['latitude'].item()
        long = search['longitude'].item()



        ####################EXTRACT API####################


        #extract the api and change it into json format
        dest = requests.get("https://api.breezometer.com/weather/v1/forecast/hourly?lat="+lat+"&lon="+long+"&key="APIGOESHERE"&hours=24")
        print("Breezometer:",dest.status_code)

        import json
        dest = pd.DataFrame(dest.json())


        #extract the necessary information of times to define morning, afternoon and evening
        counter = 0
        ninem = []
        three = []
        ninen = []
        for i in dest['data']:
            if '09:00:00' in dest['data'][counter]['datetime'].split('T')[1]:
                ninem.append(dest['data'][counter])
                counter += 1
            elif '15:00:00' in dest['data'][counter]['datetime'].split('T')[1]:
                three.append(dest['data'][counter])
                counter += 1
            elif '21:00:00' in dest['data'][counter]['datetime'].split('T')[1]:
                ninen.append(dest['data'][counter])
                counter += 1
            else:
                counter +=1


        #Transform the information into dataframe to score the location's information at the specified times with geo info 
        def weatherinfo(x):
            date = x[0]['datetime'].split('T')[0]
            time = x[0]['datetime'].split('T')[1].replace('Z','')
            #morntime = morntime.replace('Z','')
            felt_temp_c = round(x[0]['feels_like_temperature']['value'])
            precipitation_prob = round(ninem[0]['precipitation']['precipitation_probability'])
            windspeed_km_h = round(x[0]['wind']['speed']['value'],1)
            isday = ninem[0]['is_day_time']

            return pd.DataFrame({'location': [destination]
                                ,'latitude':[lat]
                                ,'longitude':[long]
                                ,'date' : [date]
                                , 'time': [time]
                                , 'felt_temp_c' : [felt_temp_c]
                                , 'precipitation_prob' : [precipitation_prob]
                                , 'windspeed_km_h': [windspeed_km_h]
                                , 'day_time': [isday]})

        morndf = weatherinfo(ninem)
        morndf['time_of_day'] = 'morning'

        aftdf = weatherinfo(three)
        aftdf['time_of_day'] = 'afternoon'

        evedf = weatherinfo(ninen)
        evedf['time_of_day'] = 'evening'

        weatherinfo = pd.concat([morndf,aftdf,evedf], axis = 0)
        weatherinfo = weatherinfo.sort_values(['date','time'], ascending = [True,True]).reset_index(drop = True)


        ###########CREATE DATA DUMP FOR WEATHER###########
        weatherdump = pd.read_csv('weatherdump.csv')
        weatherinfo = weatherinfo.reset_index(drop = True)
        weatherdump = weatherdump.reset_index(drop = True)
        weatherdump = pd.concat([weatherdump,weatherinfo], axis = 0)
        weatherdump = weatherdump.reset_index(drop=True)
        weatherdump.to_csv('weatherdump.csv', index = False)


        #-----------------WE NOW MOVE ONTO SCORING THE DIFFERENT FACTORS TO DETERMINE THE mytemp© SCORE-----------------#



        #############SCORE GENDER#############

        for i in userinputdump['gender']:
            if 'M' in i:
                userinputdump['genscore'] = 1
            elif 'F' in i: 
                userinputdump['genscore'] = -2


        #############SCORE AGE#############       

        for i in userinputdump['gender']:
            if 'M' in i:
                for j in userinputdump['age']:
                    if j <= 59:
                        userinputdump['agescore'] = 0 
                    elif j <= 64:
                        userinputdump['agescore'] = -1
                    elif j <= 69:
                        userinputdump['agescore'] = -1     
                    elif j <= 74:
                        userinputdump['agescore'] = -2
                    elif j <= 79:
                        userinputdump['agescore'] = -2               
                    elif j >= 80:
                        userinputdump['agescore'] = -3               
            elif 'F' in i:
                for k in userinputdump['age']:  
                    if k <= 44:
                        userinputdump['agescore'] = 0
                    elif k <= 49:
                        userinputdump['agescore'] = 3    
                    elif k <= 54:
                        userinputdump['agescore'] = 3
                    elif k <= 59:
                        userinputdump['agescore'] = 0 
                    elif k <= 64:
                        userinputdump['agescore'] = -1
                    elif k <= 69:
                        userinputdump['agescore'] = -1     
                    elif k <= 74:
                        userinputdump['agescore'] = -2
                    elif k <= 79:
                        userinputdump['agescore'] = -2               
                    elif k >= 80:
                        userinputdump['agescore'] = -3  



        #############SCORE & LABEL BMI#############
        for i in userinputdump['bmi']:
            if i <= 18:
                userinputdump['bmi'] = 'underweight'
                userinputdump['bmiscore'] = -1
            elif i > 18:
                userinputdump['bmi'] = 'healthy'
                userinputdump['bmiscore'] = 0
            elif i > 24:
                userinputdump['bmi'] = 'overweight'
                userinputdump['bmiscore'] = 3
            elif i > 30:
                userinputdump['bmi'] = 'obese'
                userinputdump['bmiscore'] = 5



        #############SCORE CITY#############
        #if the city is the same - no difference in perceived temperature
        for i in userinputdump['currentlocation']:
            if i == destination:
                userinputdump['citymorningscore'] = ninem[0]['feels_like_temperature']['value']
                userinputdump['cityafternoonscore'] = three[0]['feels_like_temperature']['value']
                userinputdump['citynightscore'] = ninen[0]['feels_like_temperature']['value']

        #if the city is different - compare the two cities and find the difference in perceived temp.    
            elif i != destination:

                homecity = userinputdump['currentlocation'].str.split(', ', n=1, expand = True)[0]
                homecity = homecity.item()
                homecountry = userinputdump['currentlocation'].str.split(', ', n=1, expand = True)[1]
                homecountry = homecountry.item()

                searchhome = geo[(geo['name'] == homecity) & (geo['country_name_en'] == homecountry)]

                if len(searchhome) > 1:
                    searchhome = search.sort_values(by='population', ascending = False).reset_index(drop=True)
                    searchhome = search.loc[[0]]


                lathome = searchhome['latitude'].item()
                longhome = searchhome['longitude'].item()

                #extract the api and change it into json format
                homeloc = requests.get("https://api.breezometer.com/weather/v1/forecast/hourly?lat="+lathome+"&lon="+longhome+"&key="APIGOESHERE"&hours=24")
                print("Breezometer:",homeloc.status_code)

                homeloc = pd.DataFrame(homeloc.json())


                counterhome = 0
                homemor = []
                homeaft = []
                homenig = []
                for j in homeloc['data']:
                    if '09:00:00' in homeloc['data'][counterhome]['datetime'].split('T')[1]:
                        homemor.append(homeloc['data'][counterhome])
                        counterhome += 1
                    elif '15:00:00' in homeloc['data'][counterhome]['datetime'].split('T')[1]:
                        homeaft.append(homeloc['data'][counterhome])
                        counterhome += 1
                    elif '21:00:00' in homeloc['data'][counterhome]['datetime'].split('T')[1]:
                        homenig.append(homeloc['data'][counterhome])
                        counterhome += 1
                    else:
                        counterhome +=1

                hm = homemor[0]['feels_like_temperature']['value']
                ha = homeaft[0]['feels_like_temperature']['value']
                hn = homenig[0]['feels_like_temperature']['value']
                dm = ninem[0]['feels_like_temperature']['value']
                da = three[0]['temperature']['value']
                dn = ninen[0]['temperature']['value']
                if hm > dm:
                    tot = hm - dm
                    if (tot < 5)|(tot > -5):
                        userinputdump['citymorningscore'] = dm-3
                    elif (tot > 5)|(tot < -5):
                        userinputdump['citymorningscore'] = dm-5
                if dm > hm:
                    tot = dm - hm
                    if (tot < 5)|(tot > -5):
                        userinputdump['citymorningscore'] = dm+3
                    elif (tot > 5)|(tot < -5):
                        userinputdump['citymorningscore'] = dm+5
                if ha > da:
                    tot = ha - da
                    if (tot < 5)|(tot > -5):
                        userinputdump['cityafternoonscore'] = da-3
                    elif (tot > 5)|(tot < -5):
                        userinputdump['cityafternoonscore'] = da-5
                if da > ha:
                    tot = da - ha
                    if (tot < 5)|(tot > -5):
                        userinputdump['cityafternoonscore'] = da+3
                    elif (tot > 5)|(tot < -5):
                        userinputdump['cityafternoonscore'] = da+5 
                if hn > dn:
                    tot = hn - dn
                    if (tot < 5)|(tot > -5):
                        userinputdump['citynightscore'] = dn-3
                    elif (tot > 5)|(tot < -5):
                        userinputdump['citynightscore'] = dn-5
                if dn > hn:
                    tot = dn - hn
                    if (tot < 5)|(tot > -5):
                        userinputdump['citynightscore'] = dn+3
                    elif (tot > 5)|(tot < -5):
                        userinputdump['citynightscore'] = dn+5    

        #############SCORE SWEATS#############

        for i in userinputdump['sweats']:
            if 'Y' in i:
                userinputdump['sweatscore'] = 1
            elif 'N' in i:
                userinputdump['sweatscore'] = 0



        #############SCORE COLDHANDS&FEET#############

        for i in userinputdump['coldhf']:
            if 'Y' in i:
                userinputdump['coldhfscore'] = -2
            elif 'N' in i:
                userinputdump['coldhfscore'] = 0




        #############SCORE EXERCISE#############

        for i in userinputdump['exercise']:
            if 'Never' in i:
                userinputdump['exercisescore'] = 0
            elif '1 or 2 times per month' in i:
                userinputdump['exercisescore'] = 0      
            elif 'Once per week' in i:
                userinputdump['exercisescore'] = 0  
            elif 'A couple of times per week' in i:
                userinputdump['exercisescore'] = 0          
            elif 'Every other day' in i:
                userinputdump['exercisescore'] = 1          
            elif 'Every day' in i:
                userinputdump['exercisescore'] = 1  



        #############SCORE mytemp©#############

        userinputdump['mymorningtemp'] = round(userinputdump['genscore'] + userinputdump['agescore'] + userinputdump['bmiscore'] + userinputdump['citymorningscore'] + userinputdump['sweatscore'] + userinputdump['coldhfscore'] + userinputdump['exercisescore'])
        userinputdump['myafternoontemp'] = round(userinputdump['genscore'] + userinputdump['agescore'] + userinputdump['bmiscore'] + userinputdump['cityafternoonscore'] + userinputdump['sweatscore'] + userinputdump['coldhfscore'] + userinputdump['exercisescore'])
        userinputdump['mynighttemp'] = round(userinputdump['genscore'] + userinputdump['agescore'] + userinputdump['bmiscore'] + userinputdump['citynightscore'] + userinputdump['sweatscore'] + userinputdump['coldhfscore'] + userinputdump['exercisescore'])


        ############DEFINE DATAFRAME############
        userinputinformationmyscore = userinputdump[['user','gender','age','bmi','currentlocation','currentcity','currentcountry','sweats','coldhf','exercise','genscore', 'agescore','bmiscore', 'citymorningscore', 'cityafternoonscore', 'citynightscore', 'sweatscore', 'coldhfscore', 'exercisescore', 'mymorningtemp','myafternoontemp','mynighttemp']]



        ###########CREATE DATA DUMP FOR USER(NO mytemp) & USER(mytemp)###########

        #with mytemp
        usercleanmytemp = pd.read_csv('usercleanmytemp.csv')
        usercleanmytemp = usercleanmytemp.reset_index(drop = True)
        userinputdumpscore = userinputinformationmyscore.reset_index(drop = True)
        userdumpmytemp = pd.concat([usercleanmytemp,userinputdumpscore], axis = 0)
        userdumpmytemp = userdumpmytemp.reset_index(drop=True)
        userdumpmytemp.to_csv('usercleanmytemp.csv', index = False)

        #without mytemp
        usercleanwnotemp = pd.read_csv('usercleannotemp.csv')
        usercleanwnotemp = usercleanwnotemp.reset_index(drop=True)
        userdump = userinputdump[['user','gender','age','bmi','currentlocation','currentcity','currentcountry','sweats','coldhf','exercise','genscore', 'agescore','bmiscore', 'sweatscore', 'coldhfscore', 'exercisescore','dob','height_cm','weight_kg']].reset_index(drop = True)
        userdumpnotemp = pd.concat([usercleanwnotemp,userdump], axis = 0)
        userdumpnotemp = userdumpnotemp.reset_index(drop=True)
        userdumpnotemp.to_csv('usercleannotemp.csv', index = False)


        #############RECOMMEND CLOTHES#############

        #import df
        clothes = pd.read_excel('ClothesTemp.xlsx')


        #fill na values with .
        clothes = clothes.fillna('.')


        #############EXPORT THE CLOTHES TO A LIST#############


        for i in weatherinfo['time_of_day']:
            if 'afternoon' in i:
                ###finding the correct temperature
                corrtemp = 0
                for u in clothes['degrees_c']:
                    for h in userinputinformationmyscore['myafternoontemp']:
                        if u == h:
                            corrtemp += u


                #filter the rows to the correct temperature
                filtcloth = clothes[clothes['degrees_c'] == corrtemp]


                #filter column names to show only those columns with clothing
                colwear = ['jacket','sweater','top','bottom','other','shoes','underwear']
                colbring = ['accessories','comment']
                bringday = ['thinktobringday']
                bringnight = ['thinktobringnight'] 

                filtclothw = filtcloth[colwear]
                filtclothbring = filtcloth[colbring]
                filtclothbringday = filtcloth[bringday]
                filtclothbringnight = filtcloth[bringnight]

                towear = []
                for j in filtclothw.columns:
                    for k in filtclothw[j]:
                        if k != '.':
                            towear.append(k+", ")
                                
                tobring = []
                for j in filtclothbring.columns:
                    for k in filtclothbring[j]:
                        if k != '.':
                            tobring.append(k+", ")


                tobringd = []
                for j in filtclothbringday.columns:
                    for k in filtclothbringday[j]:
                        if k != '.':
                            tobringd.append(k+", ")

                st.markdown('### Afternoon: ')
                st.caption(" ".join(towear))
                if len(tobring) > 0:
                    st.markdown("##### Bring:")
                    print("Bring:"," ".join(tobring))
                    st.caption("".join(tobring))
                if len(tobringd) > 0:
                    st.caption("".join(tobringd))
                    
                #Take Rain Into account
                counter = 0
                for i in weatherinfo['precipitation_prob']:
                    counter = counter + i

                rainwarn = counter/3

                st.markdown('***Also, Take an Umbrella or Waterproof Clothing. It looks like it might rain!***')



            elif 'evening' in i:

                corrtemp = 0
                for u in clothes['degrees_c']:
                    for h in userinputinformationmyscore['mynighttemp']:
                        if u == h:
                            corrtemp += u


                #filter the rows to the correct temperature
                filtcloth = clothes[clothes['degrees_c'] == corrtemp]


                #filter column names to show only those columns with clothing
                colwear = ['jacket','sweater','top','bottom','other','shoes','underwear']
                colbring = ['accessories','comment']
                bringday = ['thinktobringday']
                bringnight = ['thinktobringnight'] 

                filtclothw = filtcloth[colwear]
                filtclothbring = filtcloth[colbring]
                filtclothbringday = filtcloth[bringday]
                filtclothbringnight = filtcloth[bringnight]        


                towear = []
                for j in filtclothw.columns:
                    for k in filtclothw[j]:
                        if k != '.':
                            towear.append(k+", ")

                tobring = []
                for j in filtclothbring.columns:
                    for k in filtclothbring[j]:
                        if k != '.':
                            tobring.append(k+", ")


                tobringn = []
                for j in filtclothbringnight.columns:
                    for k in filtclothbringnight[j]:
                        if k != '.':
                            tobringn.append(k+", ")

                st.markdown('### Evening: ')
                st.caption(" ".join(towear))
                if len(tobring) > 0:
                    st.markdown("##### Bring:")
                    print("Bring:"," ".join(tobring))
                    st.caption("".join(tobring))
                if len(tobringn) > 0:
                    st.caption("".join(tobringn))
                    
                #Take Rain Into account
                counter = 0
                for i in weatherinfo['precipitation_prob']:
                    counter = counter + i

                rainwarn = counter/3

                if rainwarn > 60:
                    st.markdown('***Also, Take an Umbrella or Waterproof Clothing. It looks like it might rain!***')

            elif 'morning' in i:
                corrtemp = 0
                for u in clothes['degrees_c']:
                    for h in userinputinformationmyscore['mymorningtemp']:
                        if u == h:
                            corrtemp += u


                #filter the rows to the correct temperature
                filtcloth = clothes[clothes['degrees_c'] == corrtemp]


                #filter column names to show only those columns with clothing
                colwear = ['jacket','sweater','top','bottom','other','shoes','underwear']
                colbring = ['accessories','comment']
                bringday = ['thinktobringday']
                bringnight = ['thinktobringnight'] 

                filtclothw = filtcloth[colwear]
                filtclothbring = filtcloth[colbring]
                filtclothbringday = filtcloth[bringday]
                filtclothbringnight = filtcloth[bringnight]
                towear = []

                for j in filtclothw.columns:
                    for k in filtclothw[j]:
                        if k != '.':
                            towear.append(k+", ")

                tobring = []
                for j in filtclothbring.columns:
                    for k in filtclothbring[j]:
                        if k != '.':
                            tobring.append(k+", ")


                tobringd = []
                for j in filtclothbringday.columns:
                    for k in filtclothbringday[j]:
                        if k != '.':
                            tobringd.append(k+", ")

                st.markdown('### Morning: ')
                print('Morning: ')
                st.caption(" ".join(towear))
                if len(tobring) > 0:
                    st.markdown("##### Bring:")
                    print("Bring:"," ".join(tobring))
                    st.caption("".join(tobring))
                if len(tobringd) > 0:
                    st.caption("".join(tobringd))

                #Take Rain Into account
                counter = 0
                for i in weatherinfo['precipitation_prob']:
                    counter = counter + i

                rainwarn = counter/3

                if rainwarn > 60:
                    st.markdown('**Also, Take an Umbrella or Waterproof Clothing. It looks like it might rain!**')
                    print('Also, Take an Umbrella or Waterproof Clothing. It looks like it might rain!')

