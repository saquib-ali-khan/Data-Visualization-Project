import pandas as pd
data9 = pd.read_csv('static/spending_all_top100.csv')
data9.fillna(0,inplace = True)

def prepanda_stacked_bar(medicines):
        returning_dict = {}
        counter = 0
        print ("working on stacked bar ===================================================================================>")
        print ("working on stacked bar ===================================================================================>")

        for med_name in medicines:
                    temp = data9[data9["drugname_generic"]==med_name]
                    brands = set(temp["drugname_brand"].values)
                    
                    df_dict = {}
                    for yr in [2011,2012,2013,2014,2015]:                         
                        df_dict[yr] = {}
                        
                        for brand in brands:
                        
                            temp1= temp[temp["drugname_brand"]==brand]
                            temp1.fillna(0,inplace = True)   
                            aa =  temp1[temp1["year"]==yr]["total_spending"].values
                            print ("values extracted: ",aa)
                            if aa:                   
                                df_dict[yr][brand] = aa[-1]
                            else:
                                df_dict[yr][brand] = 0
                    returning_dict[med_name] = df_dict
                    counter = counter + 1
                    print (counter)
        return returning_dict

def prepanda_out_of_pocket_avg_lowincome(medicines):

        returning_dict = {}
        counter = 0
        print ("working on pocket_of_avg_lowincome =============================================================================>")
        print ("working on pocket_of_avg_lowincome =============================================================================>")

        for med_name in medicines:
                #print ("medicine name",med_name)
                temp = data9[data9["drugname_generic"]==med_name]
                brands = set(temp["drugname_brand"].values)
                df_dict = {}
                
                for yr in [2011,2012,2013,2014,2015]:
                    try:    
                            df_dict[yr] = {}
                
                            for brand in brands:
                              
                                temp1= temp[temp["drugname_brand"]==brand]
                                temp1.fillna(0,inplace = True)   

                                ################
                                aa = temp1[temp1["year"]==yr]["out_of_pocket_avg_lowincome"].values
                                print ("values extracted: ",aa)
                                if aa:                   
                                    df_dict[yr][brand] = aa[-1]
                                else:
                                    df_dict[yr][brand] = 0

                                #################                                                    
                    except:
                                print ("data could not be found from spreadsheet")

                returning_dict[med_name] = df_dict
                counter +=1

        return returning_dict


def prepanda_out_of_pocket_avg_non_lowincome(medicines):

        returning_dict = {}
        counter = 0
        print ("working on pocket_avg_non_lowincome ===========================================================================>")
        print ("working on pocket_avg_non_lowincome ===========================================================================>")

        for med_name in medicines:
                #print ("medicine name",med_name)
                temp = data9[data9["drugname_generic"]==med_name]
                brands = set(temp["drugname_brand"].values)
                df_dict = {}
                
                for yr in [2011,2012,2013,2014,2015]:
                    try:    
                            df_dict[yr] = {}
                    
                            for brand in brands:
 
                                temp1= temp[temp["drugname_brand"]==brand]

                                ################

                                aa = temp1[temp1["year"]==yr]["out_of_pocket_avg_non_lowincome"].values
                                print ("values extracted: ",aa)
                                if aa:                   
                                    df_dict[yr][brand] = aa[-1]
                                else:
                                    df_dict[yr][brand] = 0
                                #################                                                                                                                               
                    except:
                                print ("data could not be found from spreadsheet")

                returning_dict[med_name] = df_dict
                counter += 1 
        return returning_dict

def prepanda_total_spending(medicines):

        returning_dict = {}
        counter = 0
        print ("working on total_spending =======================================================================================>")
        print ("working on total_spending =======================================================================================>")

        for med_name in medicines:
                #print ("medicine name",med_name)
                temp = data9[data9["drugname_generic"]==med_name]
                brands = set(temp["drugname_brand"].values)
                df_dict = {}
                
                for yr in [2011,2012,2013,2014,2015]:
                    try:    
                            df_dict[yr] = {}
                
                            for brand in brands:
 
                                temp1= temp[temp["drugname_brand"]==brand]

                                ################
                                aa = temp1[temp1["year"]==yr]["total_spending"].values
                                print ("values extracted: ",aa)
                                if aa:                   
                                    df_dict[yr][brand] = aa[-1]
                                else:
                                    df_dict[yr][brand] = 0

                                #################                                               
                                                    
                    except:
                                print ("data could not be found from spreadsheet")

                returning_dict[med_name] = df_dict
                counter +=1
        return returning_dict



def prepanda_user_count(medicines):

        returning_dict = {}
        counter = 0
        print ("working on user_count =============================================================================================>")
        print ("working on user_count =============================================================================================>")

        for med_name in medicines:
                #print ("medicine name",med_name)
                temp = data9[data9["drugname_generic"]==med_name]
                brands = set(temp["drugname_brand"].values)
                df_dict = {}
                
                for yr in [2011,2012,2013,2014,2015]:
                    try:    
                            df_dict[yr] = {}
                
                            for brand in brands:

                                temp1= temp[temp["drugname_brand"]==brand]

                                ################
                                aa = temp1[temp1["year"]==yr]["user_count"].values
                                print ("extracted values",aa)
                                if aa:                   
                                    df_dict[yr][brand] = aa[-1]
                                else:
                                    df_dict[yr][brand] = 0

                                #################   
                                                    
                    except:
                                print ("data could not be found from spreadsheet")

                returning_dict[med_name] = df_dict
                counter+=1
        return returning_dict


def prepanda_claim_count(medicines):

        returning_dict = {}
        counter = 0
        print ("working on claim_count ============================================================================================>")
        print ("working on claim_count ============================================================================================>")

        for med_name in medicines:
                #print ("medicine name",med_name)
                temp = data9[data9["drugname_generic"]==med_name]
                brands = set(temp["drugname_brand"].values)
                df_dict = {}
                
                for yr in [2011,2012,2013,2014,2015]:
                    try:    
                            df_dict[yr] = {}
                            for brand in brands:

                                temp1= temp[temp["drugname_brand"]==brand]

                                ################

                                aa = temp1[temp1["year"]==yr]["claim_count"].values
                                print ("extracted value",aa)
                                if aa:                   
                                    df_dict[yr][brand] = aa[-1]
                                else:
                                    df_dict[yr][brand] = 0

                                #################   
                    except:
                                print ("data could not be found from spreadsheet")

                returning_dict[med_name] = df_dict
                counter+=1

        return returning_dict


        









