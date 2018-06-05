#!/usr/bin/python

from math import exp
def Logistic (x) : 
    return (1/(1+exp(-x))) 

def Probability (x) : 
    if x < 0 :
        return 0
    elif x > 1 :
        return 1
    else : 
        return x

def expression (Donor_HLA_A, Patient_HLA_A, A_Match, Donor_HLA_B, Patient_HLA_B, B_Match, Donor_HLAA_DR, Patient_HLA_DR, DR_Match, Acceptable_Survival_Score_2_and_less_score=reject_, Difficulty_in_transporting_organ_score__Distance_from_Retreiving_Center,_facilities__1_most_difficult,_5_easy_, Donor=GovnOrPvtHospital_Govt=1,_Pvt=0_, PatientRegistered_in_Govt_or_pvt_hospital?__Govt=1,_Pvt=0_) : 

    scaled_Donor_HLA_A=2*(Donor_HLA_A-0)/(19-0)-1
    scaled_Patient_HLA_A=2*(Patient_HLA_A-0)/(6802-0)-1
    scaled_A_Match=2*(A_Match-0)/(1-0)-1
    scaled_Donor_HLA_B=2*(Donor_HLA_B-0)/(4402-0)-1
    scaled_Patient_HLA_B=2*(Patient_HLA_B-0)/(5703-0)-1
    scaled_B_Match=2*(B_Match-0)/(1-0)-1
    scaled_Donor_HLAA_DR=2*(Donor_HLAA_DR-0)/(302-0)-1
    scaled_Patient_HLA_DR=2*(Patient_HLA_DR-0)/(1602-0)-1
    scaled_DR_Match=2*(DR_Match-0)/(1-0)-1
    scaled_Acceptable_Survival_Score_2_and_less_score=reject_=2*(Acceptable_Survival_Score_2_and_less_score=reject_-0)/(1-0)-1
    scaled_Difficulty_in_transporting_organ_score__Distance_from_Retreiving_Center,_facilities__1_most_difficult,_5_easy_=2*(Difficulty_in_transporting_organ_score__Distance_from_Retreiving_Center,_facilities__1_most_difficult,_5_easy_-0)/(5-0)-1
    scaled_Donor=GovnOrPvtHospital_Govt=1,_Pvt=0_=2*(Donor=GovnOrPvtHospital_Govt=1,_Pvt=0_-0)/(1-0)-1
    scaled_PatientRegistered_in_Govt_or_pvt_hospital?__Govt=1,_Pvt=0_=2*(PatientRegistered_in_Govt_or_pvt_hospital?__Govt=1,_Pvt=0_-0)/(1-0)-1
    y_1_1=Logistic(-0.0879638
    -0.260873*scaled_Donor_HLA_A
    -0.309749*scaled_Patient_HLA_A
    +0.00719491*scaled_A_Match
    +0.00756205*scaled_Donor_HLA_B
    +0.220424*scaled_Patient_HLA_B
    +0.37075*scaled_B_Match
    -0.093289*scaled_Donor_HLAA_DR
    -0.214307*scaled_Patient_HLA_DR
    +0.454286*scaled_DR_Match
    +0.690212*scaled_Acceptable_Survival_Score_2_and_less_score=reject_
    +0.74048*scaled_Difficulty_in_transporting_organ_score__Distance_from_Retreiving_Center,_facilities__1_most_difficult,_5_easy_
    -0.351087*scaled_Donor=GovnOrPvtHospital_Govt=1,_Pvt=0_
    -0.573368*scaled_PatientRegistered_in_Govt_or_pvt_hospital?__Govt=1,_Pvt=0_)
    y_1_2=Logistic(-0.167891
    +0.299736*scaled_Donor_HLA_A
    +0.317569*scaled_Patient_HLA_A
    -0.58901*scaled_A_Match
    -0.221755*scaled_Donor_HLA_B
    -0.39706*scaled_Patient_HLA_B
    -0.555177*scaled_B_Match
    +0.523443*scaled_Donor_HLAA_DR
    -0.207293*scaled_Patient_HLA_DR
    -0.529751*scaled_DR_Match
    -1.30001*scaled_Acceptable_Survival_Score_2_and_less_score=reject_
    -1.04203*scaled_Difficulty_in_transporting_organ_score__Distance_from_Retreiving_Center,_facilities__1_most_difficult,_5_easy_
    +0.295424*scaled_Donor=GovnOrPvtHospital_Govt=1,_Pvt=0_
    +0.0438063*scaled_PatientRegistered_in_Govt_or_pvt_hospital?__Govt=1,_Pvt=0_)
    y_1_3=Logistic(-0.677572
    -0.52084*scaled_Donor_HLA_A
    +0.458933*scaled_Patient_HLA_A
    +0.5046*scaled_A_Match
    -0.194936*scaled_Donor_HLA_B
    +0.323266*scaled_Patient_HLA_B
    +0.0914631*scaled_B_Match
    -0.776802*scaled_Donor_HLAA_DR
    +0.520244*scaled_Patient_HLA_DR
    +0.317702*scaled_DR_Match
    -0.00416717*scaled_Acceptable_Survival_Score_2_and_less_score=reject_
    +0.376296*scaled_Difficulty_in_transporting_organ_score__Distance_from_Retreiving_Center,_facilities__1_most_difficult,_5_easy_
    -0.806743*scaled_Donor=GovnOrPvtHospital_Govt=1,_Pvt=0_
    -0.0760654*scaled_PatientRegistered_in_Govt_or_pvt_hospital?__Govt=1,_Pvt=0_)
    y_1_4=Logistic(-0.496666
    -0.396444*scaled_Donor_HLA_A
    -0.0502326*scaled_Patient_HLA_A
    +0.681284*scaled_A_Match
    -0.438962*scaled_Donor_HLA_B
    +0.132839*scaled_Patient_HLA_B
    -0.677745*scaled_B_Match
    +0.0478939*scaled_Donor_HLAA_DR
    +0.010341*scaled_Patient_HLA_DR
    -0.354408*scaled_DR_Match
    +1.74727*scaled_Acceptable_Survival_Score_2_and_less_score=reject_
    +2.87039*scaled_Difficulty_in_transporting_organ_score__Distance_from_Retreiving_Center,_facilities__1_most_difficult,_5_easy_
    -0.902147*scaled_Donor=GovnOrPvtHospital_Govt=1,_Pvt=0_
    +0.0585006*scaled_PatientRegistered_in_Govt_or_pvt_hospital?__Govt=1,_Pvt=0_)
    y_1_5=Logistic(0.0823388
    -0.585287*scaled_Donor_HLA_A
    +0.147526*scaled_Patient_HLA_A
    +0.958377*scaled_A_Match
    -0.696793*scaled_Donor_HLA_B
    -0.262506*scaled_Patient_HLA_B
    +0.167484*scaled_B_Match
    -0.0785645*scaled_Donor_HLAA_DR
    -0.0425606*scaled_Patient_HLA_DR
    -0.208792*scaled_DR_Match
    +2.37661*scaled_Acceptable_Survival_Score_2_and_less_score=reject_
    +4.01164*scaled_Difficulty_in_transporting_organ_score__Distance_from_Retreiving_Center,_facilities__1_most_difficult,_5_easy_
    -0.47934*scaled_Donor=GovnOrPvtHospital_Govt=1,_Pvt=0_
    +0.0442989*scaled_PatientRegistered_in_Govt_or_pvt_hospital?__Govt=1,_Pvt=0_)
    y_2_1=Logistic(0.212231
    -0.338729*y_1_1
    -0.524431*y_1_2
    -0.474994*y_1_3
    -0.580099*y_1_4
    -1.18787*y_1_5)
    y_2_2=Logistic(0.210087
    +0.173585*y_1_1
    +0.53582*y_1_2
    -0.232054*y_1_3
    -0.578334*y_1_4
    -1.90079*y_1_5)
    y_2_3=Logistic(1.15445
    -0.710031*y_1_1
    +1.59004*y_1_2
    -0.271465*y_1_3
    -2.03613*y_1_4
    -2.96868*y_1_5)
    y_2_4=Logistic(-0.793419
    +0.36148*y_1_1
    -1.08411*y_1_2
    -0.250952*y_1_3
    +1.81443*y_1_4
    +2.36309*y_1_5)
    y_3_1=Logistic(-0.403441
    +1.29855*y_2_1
    +1.51672*y_2_2
    +3.15785*y_2_3
    -3.71308*y_2_4)
    y_3_2=Logistic(-1.4304
    +0.0515124*y_2_1
    -0.738264*y_2_2
    -0.938553*y_2_3
    +0.0223018*y_2_4)
    y_3_3=Logistic(0.679392
    -1.12459*y_2_1
    -1.63446*y_2_2
    -2.40928*y_2_3
    +2.46758*y_2_4)
    non_probabilistic_Accepted_1_or_Rejected_0=Logistic(1.22716
    -7.78893*y_3_1
    +0.50205*y_3_2
    +4.73017*y_3_3)
    (Accepted_1_or_Rejected_0) = Probability(non_probabilistic_Accepted_1_or_Rejected_0)
    
    return Accepted_1_or_Rejected_0 
