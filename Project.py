# -*- coding: utf-8 -*-
"""
Project CRI
Moody's EDF Implied Rating and CRI Probability of default Implied Rating Comparison
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
import scipy.stats as ss
import seaborn as sns

#1. Implied Rating Mapping
financial_institutions = ["National Commercial Banks",
                              "Commercial Banks",
                              "Commercial Banks, NEC",
                              "State Commercial Banks",
                              "Investment Advice",
                              "Investors, NEC",                              
                              "Real estate",
                              "Real Estate Agents and Managers",
                              "Real Estate Operators and Lessors",
                              "Real Estate Investment Trusts",
                              "Real estate dealers",
                              "Short-Term Business Credit Institutions, Except Agricultural",
                              "Security Brokers, Dealers, and Flotation Companies",
                              "Security, commodity brokers, and services",
                              "Security and Commodity Exchanges",
                              "Services Allied With the Exchange of Securities or Commodities, NEC",
                              "Unit Investment Trusts, Face-Amount Certificate Offices, and Closed-End Management Investment Offices",
                              "Functions Related to Deposit Banking, NEC",
                              "Miscellaneous Business Credit Institutions",
                              "Loan Brokers",
                              "Lessors of Real Property, NEC",
                              "Life Insurance",
                              "Title Insurance",
                              "Insurance Agents, Brokers, and Service",
                              "Insurance Carriers, NEC",
                              "Savings Institutions, Federally Chartered",
                              "Savings institutions, Not Federally Chartered",
                              "Nondeposit Trust Facilities",
                              "Mortgage Bankers and Loan Correspondents",
                              "Foreign Trade and International Banking Institutions",
                              "Management Investment Offices, Open-End",
                              "Offices of Holding Companies, NEC",
                              "Offices of Bank Holding Companies",
                              "Finance services",
                              "Finance lessors",
                              "Federal and Federally-Sponsored Credit Agencies",]

def EDF_IR(data):
    entity_type = ["Financials","Corporates"]
    Min_Corporates = [0.0000,0.0126,0.0178,0.0214,0.0245,0.0280,0.0308,0.0325,0.0343,0.0434,0.0657,0.0995,0.1580,0.2631,0.4381,0.7828,1.5008,2.8772,4.9188,9.2582,26.5646]
    Max_Corporates = [0.0126,0.0178,0.0214,0.0245,0.0280,0.0308,0.0325,0.0343,0.0434,0.0657,0.0995,0.1580,0.2631,0.4381,0.7828,1.5008,2.8772,4.9188,9.2582,26.5646,50.0001]
    Min_Financials = [0.0000,0.0395,0.0558,0.0704,0.0886,0.1117,0.1407,0.1773,0.2234,0.2814,0.3545,0.4467,0.5628,0.7091,0.8934,1.1256,1.4182,1.7868,2.6221,5.8590,22.3764]
    Max_Financials = [0.0395,0.0558,0.0704,0.0886,0.1117,0.1407,0.1773,0.2234,0.2814,0.3545,0.4467,0.5628,0.7091,0.8934,1.1256,1.4182,1.7868,2.6221,5.8590,22.3764,50.0001]
    Rating = ['Aaa','Aa1','Aa2','Aa3','A1','A2','A3','Baa1','Baa2','Baa3','Ba1','Ba2','Ba3','B1','B2','B3','Caa1','Caa2','Caa3','Ca','C']
    
    for i in range(len(data.index)):
        if data.iloc[i,4] == entity_type[0]:
            for j in range(len(Min_Financials)):
                if Min_Financials[j]<=data.iloc[i,6]<=Max_Financials[j]:
                    data.iloc[i,5] = Rating[j]
        elif data.iloc[i,4] == entity_type[1]:
            for z in range(len(Min_Corporates)):
                if Min_Corporates[z]<=data.iloc[i,6]<=Max_Corporates[z]:
                    data.iloc[i,5] = Rating[z]
        else:
            data.iloc[i,5] = np.nan
    
    return data
            
#data_1209 = pd.read_excel("Project data_1209.xlsx", index_col = None, columns = 0)
#data_1031 = pd.read_excel("Project data_1031.xlsx", index_col = None, columns = 0)

#Output_1209 = EDF_IR(data_1209)
#Output_1031 = EDF_IR(data_1031)        


#Output_1209.to_csv('D:/实习&工作/NUS CRI/output_1209.csv')
#Output_1031.to_csv('D:/实习&工作/NUS CRI/output_1031.csv')


#2. Rating Score Mapping
def Lowest_Rating(data):
    Moody_rating = [["Aaa","Aaa *","Aaa *-"],
                    ["Aa1","Aa1 *+","Aa1 *","Aa1 *-"],
                    ["Aa2","Aa2 *+","Aa2 *","Aa2 *-"],
                    ["Aa3","Aa3 *+","Aa3 *","Aa3 *-"],
                    ["A1","A1 *+","A1 *","A1 *-"],
                    ["A2","A2 *+","A2 *","A2 *-"],
                    ["A3","A3 *+","A3 *","A3 *-"],
                    ["Baa1","Baa1 *+","Baa1 *","Baa1 *-"],
                    ["Baa2","Baa2 *+","Baa2 *","Baa2 *-"],
                    ["Baa3","Baa3 *+","Baa3 *","Baa3 *-"],
                    ["Ba1","Ba1 *+","Ba1 *","Ba1 *-"],
                    ["Ba2","Ba2 *+","Ba2 *","Ba2 *-"],
                    ["Ba3","Ba3 *+","Ba3 *","Ba3 *-"],
                    ["B1","B1 *+","B1 *","B1 *-"],
                    ["B2","B2 *+","B2 *","B2 *-"],
                    ["B3","B3 *+","B3 *","B3 *-"],
                    ["Caa1","Caa1 *+","Caa1 *","Caa1 *-"],
                    ["Caa2","Caa2 *+","Caa2 *","Caa2 *-"],
                    ["Caa3","Caa3 *+","Caa3 *","Caa3 *-"],
                    ["Ca","Ca *+","Ca *","Ca *-"],
                    ["C","C *+","C *","C *-"],
                    [],    #default level
                    ["WR","NR","#N/A N/A"]]
    
    SP_rating = [["AAA","AAA *","AAA *-"],
                 ["AA+","AA+ *+","AA+ *","AA+ *-"],
                 ["AA","AA *+","AA *","AA *-"],
                 ["AA-","AA- *+","AA- *","AA- *-"],
                 ["A+","A+ *+","A+ *","A+ *-"],
                 ["A","A *+","A *","A *-"],
                 ["A-","A- *+","A- *","A- *-"],
                 ["BBB+","BBB+ *+","BBB+ *","BBB+ *-","BBB+u"],
                 ["BBB","BBB *+","BBB *","BBB *-","BBBu"],
                 ["BBB-","BBB- *+","BBB- *","BBB- *-","BBB-u *+"],
                 ["BB+","BB+ *+","BB+ *","BB+ *-"],
                 ["BB","BB *+","BB *","BB *-","BBu"],
                 ["BB-","BB- *+","BB- *","BB- *-"],
                 ["B+","B+ *+","B+ *","B+ *-"],
                 ["B","B *+","B *","B *-"],
                 ["B-","B- *+","B- *","B- *-"],
                 ["CCC+","CCC+ *+","CCC+ *","CCC+ *-"],
                 ["CCC","CCC *+","CCC *","CCC *-"],
                 ["CCC-","CCC- *+","CCC- *","CCC- *-"],
                 ["CC","CC *+","CC *","CC *-"],
                 ["C","C *+","C *","C *-"],
                 ["D","SD"],    #default level
                 ["WD","NR","#N/A N/A"]]
    
    Fitch_rating = [["AAA","AAA *","AAA *-"],
                    ["AA+","AA+ *+","AA+ *","AA+ *-"],
                    ["AA","AA *+","AA *","AA *-"],
                    ["AA-","AA- *+","AA- *","AA- *-"],
                    ["A+","A+ *+","A+ *","A+ *-"],
                    ["A","A *+","A *","A *-"],
                    ["A-","A- *+","A- *","A- *-"],
                    ["BBB+","BBB+ *+","BBB+ *","BBB+ *-"],
                    ["BBB","BBB *+","BBB *","BBB *-"],
                    ["BBB-","BBB- *+","BBB- *","BBB- *-"],
                    ["BB+","BB+ *+","BB+ *","BB+ *-"],
                    ["BB","BB *+","BB *","BB *-"],
                    ["BB-","BB- *+","BB- *","BB- *-"],
                    ["B+","B+ *+","B+ *","B+ *-"],
                    ["B","B *+","B *","B *-"],
                    ["B-","B- *+","B- *","B- *-"],
                    ["CCC+","CCC+ *+","CCC+ *","CCC+ *-"],
                    ["CCC","CCC *+","CCC *","CCC *-"],
                    ["CCC-","CCC- *+","CCC- *","CCC- *-"],
                    ["CC","CC *+","CC *","CC *-"],
                    ["C","C *+","C *","C *-"],
                    ["DDD","DD","D"],    #default level
                    ["WD","NR","#N/A N/A"]]
    
    Score = [21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,np.nan]
    
    for i in range(len(data.index)):
        for j in range(len(Score)):
            if data.iloc[i,5] in Moody_rating[j]:
                data.iloc[i,5] = Score[j]
            if data.iloc[i,6] in SP_rating[j]:
                data.iloc[i,6] = Score[j]
            if data.iloc[i,7] in Fitch_rating[j]:
                data.iloc[i,7] = Score[j]
        data.iloc[i,8] = data.iloc[i,5:8].min()
    
    return data
    
#data_lr = pd.read_excel("Lowest Rating_input.xlsx", index_col = None, columns = 0)
#data_lr_output = Lowest_Rating(data_lr)
#data_lr_output.to_csv('D:/实习&工作/NUS CRI/Lowest Rating_output.csv')

#3. Rating Gap Distribution
def EDF_PD_IR_Gap(data):
    data_EDF_rgnn = data.dropna(subset=['EDF_LT Rating Gap'],inplace = False)
    data_PD_rgnn = data.dropna(subset=['PD_LT Rating Gap'],inplace = False)
# plot EDF LT Gap Distribution    
    plt.figure(figsize=(10,8))
    plt.style.use('ggplot')
    plt.hist(data_EDF_rgnn['EDF_LT Rating Gap'],
             bins = 22,  # number of bars in histogram
             color = sns.desaturate("indianred",0.8),
             density = True, # frequency or quantity
             edgecolor = 'k', # color of edge
             alpha = 0.4,
             label = 'Rating Gap Histogram')
    plt.title('Rating Gap between EDF Implied Rating and LT Issuer Rating')
    plt.xlabel('Rating Gap')
    plt.ylabel('Frequency of occurrence')
# plot normal distribution curve
    x1 = np.linspace(data_EDF_rgnn['EDF_LT Rating Gap'].min(),data_EDF_rgnn['EDF_LT Rating Gap'].max(),1000)
    normal = norm.pdf(x1,data_EDF_rgnn['EDF_LT Rating Gap'].mean(),data_EDF_rgnn['EDF_LT Rating Gap'].std())
    line1, = plt.plot(x1, normal, 'r-', linewidth = 2, label = 'Normal Distribution Curve')
# plot kernel density curve
    kde = mlab.GaussianKDE(data_EDF_rgnn['EDF_LT Rating Gap'])
    x2 = np.linspace(data_EDF_rgnn['EDF_LT Rating Gap'].min(),data_EDF_rgnn['EDF_LT Rating Gap'].max(),1000)
    line2, = plt.plot(x2, kde(x2), 'g-', linewidth = 2, label = 'Kernel Density Curve')

    plt.legend()
    plt.show()
# plot PDIR LT Gap Distribution    
    plt.figure(figsize=(10,8))
    plt.style.use('ggplot')
    plt.hist(data_PD_rgnn['PD_LT Rating Gap'],
             bins = 22,  # number of bars in histogram
             color = sns.desaturate("indianred",0.8),
             density = True, # frequency or quantity
             edgecolor = 'k', # color of edge
             alpha = 0.4,
             label = 'Rating Gap Histogram')
    plt.title('Rating Gap between CRI PD Implied Rating and LT Issuer Rating')
    plt.xlabel('Rating Gap')
    plt.ylabel('Frequency of occurrence')
# plot normal distribution curve
    x1 = np.linspace(data_PD_rgnn['PD_LT Rating Gap'].min(),data_PD_rgnn['PD_LT Rating Gap'].max(),1000)
    normal = norm.pdf(x1,data_PD_rgnn['PD_LT Rating Gap'].mean(),data_PD_rgnn['PD_LT Rating Gap'].std())
    line1, = plt.plot(x1, normal, 'r-', linewidth = 2, label = 'Normal Distribution Curve')
# plot kernel density curve
    kde = mlab.GaussianKDE(data_PD_rgnn['PD_LT Rating Gap'])
    x2 = np.linspace(data_PD_rgnn['PD_LT Rating Gap'].min(),data_PD_rgnn['PD_LT Rating Gap'].max(),1000)
    line2, = plt.plot(x2, kde(x2), 'g-', linewidth = 2, label = 'Kernel Density Curve')

    plt.legend()
    plt.show()

#data_rg = pd.read_excel("Rating Gap.xlsx", index_col = None, columns = 0)
#EDF_PD_IR_Gap(data_rg)

#4. PDIR Rating Mapping
def PDIR_IR(data):
    Min_PDIR = [0.0000,0.0099,0.0164,0.0198,0.0369,0.0613,0.0768,0.1272,0.2062,0.2597,0.5081,0.6479,1.0815,1.5509,3.0470,3.5227,6.8368,7.5806,13.6701,17.0572,23.3258]
    Max_PDIR = [0.0099,0.0164,0.0198,0.0369,0.0613,0.0768,0.1272,0.2062,0.2597,0.5081,0.6479,1.0815,1.5509,3.0470,3.5227,6.8368,7.5806,13.6701,17.0572,23.3258,100.0000]
    Rating = ['Aaa','Aa1','Aa2','Aa3','A1','A2','A3','Baa1','Baa2','Baa3','Ba1','Ba2','Ba3','B1','B2','B3','Caa1','Caa2','Caa3','Ca','C']
    
    for i in range(len(data.index)):
        for j in range(len(Rating)):
            if Min_PDIR[j] <= data.iloc[i,2] <= Max_PDIR[j]:
                data.iloc[i,4] = Rating[j]
        for z in range(len(Rating)):
            if Min_PDIR[z] <= data.iloc[i,3] <= Max_PDIR[z]:
                data.iloc[i,5] = Rating[z]
    
    return data

#data_CRIPD = pd.read_excel("CRI PDIR_input.xlsx", index_col = None, columns = 0)
#PDIR_output = PDIR_IR(data_CRIPD)
#PDIR_output.to_csv('D:/实习&工作/NUS CRI/CRI PDIR_output.csv')

#5. IR Rating Gap
def IR_Rating_Gap(data):
    Rating = ['Aaa','Aa1','Aa2','Aa3','A1','A2','A3','Baa1','Baa2','Baa3','Ba1','Ba2','Ba3','B1','B2','B3','Caa1','Caa2','Caa3','Ca','C']
    Score = [21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
    
    for i in range(len(data.index)):
        for j in range(2,6):
            for z in range(len(Rating)):
                if data.iloc[i,j] == Rating[z]:
                    data.iloc[i,j+4] = Score[z]
    
    return data

#data_IR_Gap = pd.read_excel("IR Rating Gap_input.xlsx", index_col = None, columns = 0)
#IR_Gap = IR_Rating_Gap(data_IR_Gap)
#IR_Gap.to_csv('D:/实习&工作/NUS CRI/IR Rating Gap_output.csv')
                
#6. IR Gap Distribution
def IR_Gap(data):
    data_1209_nn = data.dropna(subset = ['IR Gap (2019/12/09)'], inplace = False)
    data_1031_nn = data.dropna(subset=['IR Gap (2019/10/31)'], inplace = False)
# plot 20191209 IR Gap distribution    
    plt.figure(figsize=(10,8))
    plt.style.use('ggplot')
    plt.hist(data_1209_nn['IR Gap (2019/12/09)'],
             bins = 21,  # number of bars in histogram
             color = sns.desaturate("indianred",0.8),
             density = True, # frequency or quantity
             edgecolor = 'k', # color of edge
             alpha = 0.4,
             label = 'Implied Rating Gap Histogram')
    plt.title('Implied Rating Gap between EDF IR and CRI PD IR 2019-12-09')
    plt.xlabel('Implied Rating Gap')
    plt.ylabel('Frequency of occurrence')
# plot normal distribution curve
    x1 = np.linspace(data_1209_nn['IR Gap (2019/12/09)'].min(),data_1209_nn['IR Gap (2019/12/09)'].max(),1000)
    normal = norm.pdf(x1,data_1209_nn['IR Gap (2019/12/09)'].mean(),data_1209_nn['IR Gap (2019/12/09)'].std())
    line1, = plt.plot(x1, normal, 'r-', linewidth = 2, label = 'Normal Distribution Curve')
# plot kernel density curve
    kde = mlab.GaussianKDE(data_1209_nn['IR Gap (2019/12/09)'])
    x2 = np.linspace(data_1209_nn['IR Gap (2019/12/09)'].min(),data_1209_nn['IR Gap (2019/12/09)'].max(),1000)
    line2, = plt.plot(x2, kde(x2), 'g-', linewidth = 2, label = 'Kernel Density Curve')

    plt.legend()
    plt.show()
# plot 20191031 IR Gap Distribution    
    plt.figure(figsize=(10,8))
    plt.style.use('ggplot')
    plt.hist(data_1031_nn['IR Gap (2019/10/31)'],
             bins = 21,  # number of bars in histogram
             color = sns.desaturate("indianred",0.8),
             density = True, # frequency or quantity
             edgecolor = 'k', # color of edge
             alpha = 0.4,
             label = 'Implied Rating Gap Histogram')
    plt.title('Implied Rating Gap between EDF IR and CRI PD IR 2019-10-31')
    plt.xlabel('Implied Rating Gap')
    plt.ylabel('Frequency of occurrence')
# plot normal distribution curve
    x1 = np.linspace(data_1031_nn['IR Gap (2019/10/31)'].min(),data_1031_nn['IR Gap (2019/10/31)'].max(),1000)
    normal = norm.pdf(x1,data_1031_nn['IR Gap (2019/10/31)'].mean(),data_1031_nn['IR Gap (2019/10/31)'].std())
    line1, = plt.plot(x1, normal, 'r-', linewidth = 2, label = 'Normal Distribution Curve')
# plot kernel density curve
    kde = mlab.GaussianKDE(data_1031_nn['IR Gap (2019/10/31)'])
    x2 = np.linspace(data_1031_nn['IR Gap (2019/10/31)'].min(),data_1031_nn['IR Gap (2019/10/31)'].max(),1000)
    line2, = plt.plot(x2, kde(x2), 'g-', linewidth = 2, label = 'Kernel Density Curve')

    plt.legend()
    plt.show()

#data_IR_Gap_DB = pd.read_excel("IR Rating Gap Distribution_input.xlsx", index_col = None, columns = 0)
#IR_Gap(data_IR_Gap_DB)

#7. Implied Rating Distribution
def IR_Distribution(data):
    Rating = ['Aaa','Aa1','Aa2','Aa3','A1','A2','A3','Baa1','Baa2','Baa3','Ba1','Ba2','Ba3','B1','B2','B3','Caa1','Caa2','Caa3','Ca','C']
    RatingFrequency = pd.DataFrame(0, index = Rating, columns = ['number of occurrence (EDFIR 2019/12/09)', 'number of occurrence (EDFIR 2019/10/31)',
                                                             'number of occurrence (PDIR 2019/12/09)', 'number of occurrence (PDIR 2019/10/31)',                                                             
                                                             'frequency of occurrence (EDFIR 2019/12/09)', 'frequency of occurrence (EDFIR 2019/10/31)',
                                                             'frequency of occurrence (PDIR 2019/12/09)', 'frequency of occurrence (PDIR 2019/10/31)'])
    for i in range(len(data)):
        for j in range(4):
            for z in range(len(Rating)):
                if data.iloc[i,j+2] == Rating[z]:
                    RatingFrequency.iloc[z,j] += 1

    for i in range(len(Rating)):
        for j in range(4):
            RatingFrequency.iloc[i,j+4] = RatingFrequency.iloc[i,j]/(RatingFrequency.iloc[:,j].sum())

    plt.figure(figsize=(10,8))
    plt.style.use('ggplot')
    plt.bar(RatingFrequency.index,
            RatingFrequency['frequency of occurrence (EDFIR 2019/12/09)'],
            color = sns.desaturate("indianred",0.8),
            edgecolor = 'k', # color of edge
            width = 1.0,
            alpha = 0.4,
            label = "Moody's EDF Implied Rating Histogram")
    plt.bar(RatingFrequency.index,
            RatingFrequency['frequency of occurrence (PDIR 2019/12/09)'],
            color = sns.desaturate("lightskyblue",0.8),
            edgecolor = 'k', # color of edge
            width = 1.0,
            alpha = 0.4,
            label = "CRI PD Implied Rating Histogram")
    plt.title('Implied Rating Distribution 2019-12-09')
    plt.xlabel('Implied Rating')
    plt.xticks(RatingFrequency.index, rotation = 45)
    plt.ylabel('Frequency of occurrence')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10,8))
    plt.style.use('ggplot')
    plt.bar(RatingFrequency.index,
            RatingFrequency['frequency of occurrence (EDFIR 2019/10/31)'],
            color = sns.desaturate("indianred",0.8),
            edgecolor = 'k', # color of edge
            width = 1.0,
            alpha = 0.4,
            label = "Moody's EDF Implied Rating Histogram")
    plt.bar(RatingFrequency.index,
            RatingFrequency['frequency of occurrence (PDIR 2019/10/31)'],
            color = sns.desaturate("lightskyblue",0.8),
            edgecolor = 'k', # color of edge
            width = 1.0,
            alpha = 0.4,
            label = "CRI PD Implied Rating Histogram")
    plt.title('Implied Rating Distribution 2019-10-31')
    plt.xlabel('Implied Rating')
    plt.xticks(RatingFrequency.index, rotation = 45)
    plt.ylabel('Frequency of occurrence')
    plt.legend()
    plt.show()

#data_IR_Gap_DB = pd.read_excel("IR Rating Gap Distribution_input.xlsx", index_col = None, columns = 0)
#IR_Distribution(data_IR_Gap_DB)

#8. PD and EDF distribution histogram
def EDF_PD_Distribution(data):
    #drop the nan data and normalize the PD and EDF
    EDF_1209_nn = data.dropna(subset = ["Moody's EDF 1 year (%) (2019/12/09)"], inplace = False)
    EDF_1209_nn.iloc[:,5] = (EDF_1209_nn.iloc[:,5] - EDF_1209_nn.iloc[:,5].mean())/EDF_1209_nn.iloc[:,5].std()
    EDF_1209_percentile_90 = np.percentile(EDF_1209_nn.iloc[:,5], 90)
    EDF_1031_nn = data.dropna(subset = ["Moody's EDF 1 year (%) (2019/10/31)"], inplace = False)
    EDF_1031_nn.iloc[:,6] = (EDF_1031_nn.iloc[:,6] - EDF_1031_nn.iloc[:,6].mean())/EDF_1031_nn.iloc[:,6].std()
    EDF_1031_percentile_90 = np.percentile(EDF_1031_nn.iloc[:,6], 90)
    PD_1209_nn = data.dropna(subset = ["CRI PD 1 year (%) (2019/12/09)"], inplace = False)
    PD_1209_nn.iloc[:,7] = (PD_1209_nn.iloc[:,7] - PD_1209_nn.iloc[:,7].mean())/PD_1209_nn.iloc[:,7].std()
    PD_1209_percentile_90 = np.percentile(PD_1209_nn.iloc[:,7], 90)
    PD_1031_nn = data.dropna(subset = ["CRI PD 1 year (%) (2019/10/31)"], inplace = False)
    PD_1031_nn.iloc[:,8] = (PD_1031_nn.iloc[:,8] - PD_1031_nn.iloc[:,8].mean())/PD_1031_nn.iloc[:,8].std()
    PD_1031_percentile_90 = np.percentile(PD_1031_nn.iloc[:,8], 90)

    ub, lb = 3.00, -0.50
    #plot the 20191209 PD and EDF distribution
    plt.figure(figsize=(10,8))
    plt.style.use('ggplot')
    kde1 = mlab.GaussianKDE(EDF_1209_nn["Moody's EDF 1 year (%) (2019/12/09)"])
    x1 = np.linspace(EDF_1209_nn["Moody's EDF 1 year (%) (2019/12/09)"].min(),EDF_1209_nn["Moody's EDF 1 year (%) (2019/12/09)"].max(),1000)
    line, = plt.plot(x1, kde1(x1), 'g-', linewidth = 2, label = "Moody's EDF Kernel Density Curve")

    kde2 = mlab.GaussianKDE(PD_1209_nn["CRI PD 1 year (%) (2019/12/09)"])
    x2 = np.linspace(PD_1209_nn["CRI PD 1 year (%) (2019/12/09)"].min(),PD_1209_nn["CRI PD 1 year (%) (2019/12/09)"].max(),1000)
    line, = plt.plot(x2, kde2(x2), 'b-', linewidth = 2, label = "CRI PD Kernel Density Curve")

    plt.scatter(EDF_1209_percentile_90, kde1(EDF_1209_percentile_90), c = 'g', marker = 'o', label = "90% percentile of Moody's EDF")
    plt.vlines(EDF_1209_percentile_90, 0, kde1(EDF_1209_percentile_90), colors = 'g', linestyles = 'dashed')

    plt.scatter(PD_1209_percentile_90, kde2(PD_1209_percentile_90), c = 'b', marker = 'o', label = "90% percentile of CRI PD")
    plt.vlines(PD_1209_percentile_90, 0, kde2(PD_1209_percentile_90), colors = 'b', linestyles = 'dashed')

    plt.fill_between(np.linspace(EDF_1209_percentile_90, ub, 1000), kde1(np.linspace(EDF_1209_percentile_90, ub, 1000)) , 0, color = 'g', alpha = 0.2,
                     label = "Company whose EDF is greater than 90% of the sample's EDF")
    plt.fill_between(np.linspace(PD_1209_percentile_90, ub, 1000), kde2(np.linspace(PD_1209_percentile_90, ub, 1000)) , 0, color = 'b', alpha = 0.1,
                     label = "Company whose CRI PD is greater than 90% of the sample's PD")

    plt.title("Moody's EDF and CRI PD Distribution 2019-12-09")
    plt.xlabel('Normalized EDF | PD (%)')
    plt.ylabel('Density')
    plt.xlim(lb,ub)
    plt.xticks(np.arange(lb,ub,0.25))
    plt.ylim(0.00,2.50)
    plt.legend()
    plt.show()
    #plot the 20191031 PD and EDF distribution
    plt.figure(figsize=(10,8))
    plt.style.use('ggplot')
    kde1 = mlab.GaussianKDE(EDF_1031_nn["Moody's EDF 1 year (%) (2019/10/31)"])
    x1 = np.linspace(EDF_1031_nn["Moody's EDF 1 year (%) (2019/10/31)"].min(),EDF_1031_nn["Moody's EDF 1 year (%) (2019/10/31)"].max(),1000)
    line, = plt.plot(x1, kde1(x1), 'g-', linewidth = 2, label = "Moody's EDF Kernel Density Curve")

    kde2 = mlab.GaussianKDE(PD_1031_nn["CRI PD 1 year (%) (2019/10/31)"])
    x2 = np.linspace(PD_1031_nn["CRI PD 1 year (%) (2019/10/31)"].min(),PD_1031_nn["CRI PD 1 year (%) (2019/10/31)"].max(),1000)
    line, = plt.plot(x2, kde2(x2), 'b-', linewidth = 2, label = "CRI PD Kernel Density Curve")

    plt.scatter(EDF_1031_percentile_90, kde1(EDF_1031_percentile_90), c = 'g', marker = 'o', label = "90% percentile of Moody's EDF")
    plt.vlines(EDF_1031_percentile_90, 0, kde1(EDF_1031_percentile_90), colors = 'g', linestyles = 'dashed')

    plt.scatter(PD_1031_percentile_90, kde2(PD_1031_percentile_90), c = 'b', marker = 'o', label = "90% percentile of CRI PD")
    plt.vlines(PD_1031_percentile_90, 0, kde2(PD_1031_percentile_90), colors = 'b', linestyles = 'dashed')

    plt.fill_between(np.linspace(EDF_1031_percentile_90, ub, 1000), kde1(np.linspace(EDF_1031_percentile_90, ub, 1000)) , 0, color = 'g', alpha = 0.2,
                     label = "Company whose EDF is greater than 90% of the sample's EDF")
    plt.fill_between(np.linspace(PD_1031_percentile_90, ub, 1000), kde2(np.linspace(PD_1031_percentile_90, ub, 1000)) , 0, color = 'b', alpha = 0.1,
                     label = "Company whose CRI PD is greater than 90% of the sample's PD")

    plt.title("Moody's EDF and CRI PD Distribution 2019-10-31")
    plt.xlabel('Normalized EDF | PD (%)')
    plt.ylabel('Density')
    plt.xlim(lb,ub)
    plt.xticks(np.arange(lb,ub,0.25))
    plt.ylim(0.00,2.50)
    plt.legend()
    plt.show()


data_EDF_PD = pd.read_excel("EDF&PD data input.xlsx", index_col = None, columns = 0)
EDF_PD_Distribution(data_EDF_PD)

#9. Find the worst creditlessness company whose normalized PD & EDF is greater than 90% percentile
def Worst_Finding(data):
    #drop the company less than 90% percentile
    EDF_1209_nn = data.dropna(subset = ["Moody's EDF 1 year (%) (2019/12/09)"], inplace = False)
    EDF_1209_nn.iloc[:,5] = (EDF_1209_nn.iloc[:,5] - EDF_1209_nn.iloc[:,5].mean())/EDF_1209_nn.iloc[:,5].std()
    EDF_1209_percentile_90 = np.percentile(EDF_1209_nn.iloc[:,5], 90)
    IN_EDF_1209 = EDF_1209_nn[EDF_1209_nn["Moody's EDF 1 year (%) (2019/12/09)"] < EDF_1209_percentile_90].index
    EDF_1209_nn.drop(IN_EDF_1209, inplace = True)
        
    EDF_1031_nn = data.dropna(subset = ["Moody's EDF 1 year (%) (2019/10/31)"], inplace = False)
    EDF_1031_nn.iloc[:,6] = (EDF_1031_nn.iloc[:,6] - EDF_1031_nn.iloc[:,6].mean())/EDF_1031_nn.iloc[:,6].std()
    EDF_1031_percentile_90 = np.percentile(EDF_1031_nn.iloc[:,6], 90)
    IN_EDF_1031 = EDF_1031_nn[EDF_1031_nn["Moody's EDF 1 year (%) (2019/10/31)"] < EDF_1031_percentile_90].index
    EDF_1031_nn.drop(IN_EDF_1031, inplace = True)
    
    PD_1209_nn = data.dropna(subset = ["CRI PD 1 year (%) (2019/12/09)"], inplace = False)
    PD_1209_nn.iloc[:,7] = (PD_1209_nn.iloc[:,7] - PD_1209_nn.iloc[:,7].mean())/PD_1209_nn.iloc[:,7].std()
    PD_1209_percentile_90 = np.percentile(PD_1209_nn.iloc[:,7], 90)
    IN_PD_1209 = PD_1209_nn[PD_1209_nn["CRI PD 1 year (%) (2019/12/09)"] < PD_1209_percentile_90].index
    PD_1209_nn.drop(IN_PD_1209, inplace = True)
    
    PD_1031_nn = data.dropna(subset = ["CRI PD 1 year (%) (2019/10/31)"], inplace = False)
    PD_1031_nn.iloc[:,8] = (PD_1031_nn.iloc[:,8] - PD_1031_nn.iloc[:,8].mean())/PD_1031_nn.iloc[:,8].std()
    PD_1031_percentile_90 = np.percentile(PD_1031_nn.iloc[:,8], 90)
    IN_PD_1031 = PD_1031_nn[PD_1031_nn["CRI PD 1 year (%) (2019/10/31)"] < PD_1031_percentile_90].index
    PD_1031_nn.drop(IN_PD_1031, inplace = True)
    
    #make the sample volume same in certain observed date (choose the less sample volume as benchmark)
    if len(EDF_1209_nn.index) >= len(PD_1209_nn.index):
        EDF_1209_nn.sort_values(by = "Moody's EDF 1 year (%) (2019/12/09)", ascending = False, inplace = True)
        EDF_1209_nn.drop(EDF_1209_nn.index[len(PD_1209_nn.index):], axis = 0, inplace = True)
    else:
        PD_1209_nn.sort_values(by = "CRI PD 1 year (%) (2019/12/09)", ascending = False, inplace = True)
        PD_1209_nn.drop(PD_1209_nn.index[len(EDF_1209_nn.index):], axis = 0, inplace = True)
    
    if len(EDF_1031_nn.index) >= len(PD_1031_nn.index):
        EDF_1031_nn.sort_values(by = "Moody's EDF 1 year (%) (2019/10/31)", ascending = False, inplace = True)
        EDF_1031_nn.drop(EDF_1031_nn.index[len(PD_1031_nn.index):], axis = 0, inplace = True)
    else:
        PD_1031_nn.sort_values(by = "CRI PD 1 year (%) (2019/10/31)", ascending = False, inplace = True)
        PD_1031_nn.drop(PD_1031_nn.index[len(EDF_1031_nn.index):], axis = 0, inplace = True)
    
    return EDF_1209_nn, EDF_1031_nn, PD_1209_nn, PD_1031_nn
    
data_EDF_PD = pd.read_excel("EDF&PD data input.xlsx", index_col = None, columns = 0)
EDF_1209, EDF_1031, PD_1209, PD_1031 = Worst_Finding(data_EDF_PD)

#find the difference set in each observed date
#EDF_1209_nn = EDF_1209.dropna(subset = ["Moody's EDF 1 year (%) (2019/12/09)",
#                                           "Moody's EDF 1 year (%) (2019/10/31)",
#                                           "CRI PD 1 year (%) (2019/12/09)",
#                                           "CRI PD 1 year (%) (2019/10/31)"], inplace = False)
#EDF_1031_nn = EDF_1031.dropna(subset = ["Moody's EDF 1 year (%) (2019/12/09)",
#                                           "Moody's EDF 1 year (%) (2019/10/31)",
#                                           "CRI PD 1 year (%) (2019/12/09)",
#                                           "CRI PD 1 year (%) (2019/10/31)"], inplace = False)
#PD_1209_nn = PD_1209.dropna(subset = ["Moody's EDF 1 year (%) (2019/12/09)",
#                                           "Moody's EDF 1 year (%) (2019/10/31)",
#                                           "CRI PD 1 year (%) (2019/12/09)",
#                                           "CRI PD 1 year (%) (2019/10/31)"], inplace = False)
#PD_1031_nn = PD_1031.dropna(subset = ["Moody's EDF 1 year (%) (2019/12/09)",
#                                           "Moody's EDF 1 year (%) (2019/10/31)",
#                                           "CRI PD 1 year (%) (2019/12/09)",
#                                           "CRI PD 1 year (%) (2019/10/31)"], inplace = False)

#Diff_EDF_1209 = set(EDF_1209_nn["Company Name"]).difference(set(PD_1209_nn["Company Name"]))
#len(Diff_EDF_1209) #Difference set volume 20191209 = 1005

#Diff_EDF_1031 = set(EDF_1031_nn["Company Name"]).difference(set(PD_1031_nn["Company Name"]))
#len(Diff_EDF_1031) #Difference set volume 20191031 = 1194

#Diff_PD_1031 = set(PD_1031_nn["Company Name"]).difference(set(EDF_1031_nn["Company Name"]))

#pd.DataFrame(Diff_EDF_1031).to_csv('D:/实习&工作/NUS CRI/Diff EDF 1031.csv')
#pd.DataFrame(Diff_PD_1031).to_csv('D:/实习&工作/NUS CRI/Diff PD 1031.csv')




    
