from graphqlclient import GraphQLClient

client = GraphQLClient('http://172.17.0.1:3301/api')


def create_patient(name):
    result = client.execute('''
    mutation CreatePatient {
      createPatient(name: "''' + name + '''") {
        name
      }
    }
    ''')

    print(result)


def create_study(name, id_patient):
    result = client.execute('''
    mutation CreateStudy {
      createStudy(studyName: "''' + name + '''", idPatient: ''' + str(id_patient) + ''') {
        studyName
        idPatient
      }
    }
    ''')

    print(result)


def create_modality(name):
    result = client.execute('''
    mutation CreateModality {
      createModality(name: "''' + name + '''") {
        name
      }
    }
    ''')

    print(result)


def create_series(name, id_patient, id_study, id_modality):
    result = client.execute('''
    mutation CreateSeries {
      createSeries(seriesName: "''' + name + '''", idPatient: ''' + str(id_patient) + ''', idStudy: ''' + str(
        id_study) + ''', idModality: ''' + str(id_modality) + ''') { 
        seriesName
        idPatient
        idStudy
        idModality
      }
    }
    ''')

    print(result)


def create_file(filePath, id_patient, id_study, id_series):
    result = client.execute('''
    mutation CreateFile {
      createFile(filePath: "''' + filePath + '''", idPatient: ''' + str(id_patient) + ''', idStudy: ''' + str(
        id_study) + ''', idSeries: ''' + str(id_series) + ''') { 
        filePath
        idPatient
        idStudy
        idSeries
      }
    }
    ''')

    print(result)


create_modality("AR")
create_modality("ASMT")
create_modality("AU")
create_modality("BDUS")
create_modality("BI")
create_modality("BMD")
create_modality("CR")
create_modality("CT")
create_modality("DG")
create_modality("DOC")
create_modality("DX")
create_modality("ECG")
create_modality("EPS")
create_modality("ES")
create_modality("FID")
create_modality("GM")
create_modality("PLAN")
create_modality("PR")
create_modality("PT")

create_patient("HIPPOCRATES")#1
create_study("CT_ABDOMEN_W_V_CONTRAST",1)#1
create_series("SER_HORIZONTAL_AX",1,1,1)#1
create_file("./documents/dicom/images/fake.dcm",1,1,1)
create_file("./documents/dicom/images/fake.dcm",1,1,1)
create_file("./documents/dicom/images/fake.dcm",1,1,1)
create_file("./documents/dicom/images/fake.dcm",1,1,1)
create_file("./documents/dicom/images/fake.dcm",1,1,1)
create_study("TRANSREP_NOSE",1)#2
create_series("SER_HORIZONTAL_RF",1,2,2)#2
create_file("./documents/dicom/images/fake.dcm",1,2,2)
create_file("./documents/dicom/images/fake.dcm",1,2,2)
create_file("./documents/dicom/images/fake.dcm",1,2,2)
create_file("./documents/dicom/images/fake.dcm",1,2,2)
create_file("./documents/dicom/images/fake.dcm",1,2,2)
create_study("TRANSREP_MOUTH",1)#3
create_series("SER_HORIZONTAL_RF",1,3,2)#3
create_file("./documents/dicom/images/fake.dcm",1,3,3)
create_file("./documents/dicom/images/fake.dcm",1,3,3)
create_file("./documents/dicom/images/fake.dcm",1,3,3)
create_file("./documents/dicom/images/fake.dcm",1,3,3)

create_patient("PERGAMON_GALEN")#2
create_study("CT_ABDOMEN_W_WO_CONTRAST",2)#4
create_series("SER_W_CONTRAST_HORIZONTAL",2,4,3)#4
create_file("./documents/dicom/images/fake.dcm",2,4,4)
create_file("./documents/dicom/images/fake.dcm",2,4,4)
create_file("./documents/dicom/images/fake.dcm",2,4,4)
create_file("./documents/dicom/images/fake.dcm",2,4,4)
create_series("SER_W_CONTRAST_VERTICAL",2,4,3)#5
create_file("./documents/dicom/images/fake.dcm",2,4,5)
create_file("./documents/dicom/images/fake.dcm",2,4,5)
create_file("./documents/dicom/images/fake.dcm",2,4,5)
create_series("SER_HORIZONTAL_RF",2,4,3)#6
create_file("./documents/dicom/images/fake.dcm",2,4,6)
create_file("./documents/dicom/images/fake.dcm",2,4,6)
create_file("./documents/dicom/images/fake.dcm",2,4,6)
create_file("./documents/dicom/images/fake.dcm",2,4,6)
create_file("./documents/dicom/images/fake.dcm",2,4,6)

create_patient("IBN_SINA")#3
create_study("CT_ABDOMEN_W_IV",3)#5
create_series("SER_RF_HORIZONTAL",3,5,4)#7
create_file("./documents/dicom/images/fake.dcm",3,5,7)
create_file("./documents/dicom/images/fake.dcm",3,5,7)
create_file("./documents/dicom/images/fake.dcm",3,5,7)
create_file("./documents/dicom/images/fake.dcm",3,5,7)
create_file("./documents/dicom/images/fake.dcm",3,5,7)
create_file("./documents/dicom/images/fake.dcm",3,5,7)
create_series("SER_RF_W_HORIZONTAL",3,5,5)#8
create_file("./documents/dicom/images/fake.dcm",3,5,8)
create_file("./documents/dicom/images/fake.dcm",3,5,8)
create_file("./documents/dicom/images/fake.dcm",3,5,8)
create_file("./documents/dicom/images/fake.dcm",3,5,8)
create_file("./documents/dicom/images/fake.dcm",3,5,8)
create_file("./documents/dicom/images/fake.dcm",3,5,8)
create_file("./documents/dicom/images/fake.dcm",3,5,8)
create_file("./documents/dicom/images/fake.dcm",3,5,8)

create_patient("ANDREA_VESALIO")#4
create_study("CT_LEG",4)#6
create_series("SER_RF_CONTRAST_HORIZONTAL",4,6,6)#9
create_file("./documents/dicom/images/fake.dcm",4,6,9)
create_file("./documents/dicom/images/fake.dcm",4,6,9)
create_file("./documents/dicom/images/fake.dcm",4,6,9)
create_series("SER_DP_W_HORIZONTAL",4,6,7)#10
create_file("./documents/dicom/images/fake.dcm",4,6,10)
create_file("./documents/dicom/images/fake.dcm",4,6,10)
create_file("./documents/dicom/images/fake.dcm",4,6,10)
create_file("./documents/dicom/images/fake.dcm",4,6,10)
create_file("./documents/dicom/images/fake.dcm",4,6,10)
create_file("./documents/dicom/images/fake.dcm",4,6,10)
create_series("SER_W_CONTRAST_HORIZONTAL",4,6,8)#11
create_file("./documents/dicom/images/fake.dcm",4,6,11)
create_file("./documents/dicom/images/fake.dcm",4,6,11)
create_file("./documents/dicom/images/fake.dcm",4,6,11)
create_file("./documents/dicom/images/fake.dcm",4,6,11)
create_study("CT_ARM",4)#7
create_series("SER_RF_CONTRAST_HORIZONTAL",4,7,6)#12
create_file("./documents/dicom/images/fake.dcm",4,7,12)
create_file("./documents/dicom/images/fake.dcm",4,7,12)
create_series("SER_DP_W_HORIZONTAL",4,7,7)#13
create_file("./documents/dicom/images/fake.dcm",4,7,13)
create_file("./documents/dicom/images/fake.dcm",4,7,13)
create_file("./documents/dicom/images/fake.dcm",4,7,13)
create_file("./documents/dicom/images/fake.dcm",4,7,13)
create_series("SER_W_CONTRAST_HORIZONTAL",4,7,8)#14
create_file("./documents/dicom/images/fake.dcm",4,7,14)
create_file("./documents/dicom/images/fake.dcm",4,7,14)
create_file("./documents/dicom/images/fake.dcm",4,7,14)
create_file("./documents/dicom/images/fake.dcm",4,7,14)
create_file("./documents/dicom/images/fake.dcm",4,7,14)
create_file("./documents/dicom/images/fake.dcm",4,7,14)

create_patient("RENÉ_LAËNNEC")#5
create_study("CT_SHOULDER_DX",5)#8
create_series("SER_RF_CONTRAST_HORIZONTAL",5,8,6)#15
create_file("./documents/dicom/images/fake.dcm",5,8,15)
create_file("./documents/dicom/images/fake.dcm",5,8,15)
create_file("./documents/dicom/images/fake.dcm",5,8,15)
create_file("./documents/dicom/images/fake.dcm",5,8,15)
create_file("./documents/dicom/images/fake.dcm",5,8,15)
create_file("./documents/dicom/images/fake.dcm",5,8,15)
create_file("./documents/dicom/images/fake.dcm",5,8,15)
create_file("./documents/dicom/images/fake.dcm",5,8,15)
create_series("SER_DP_W_HORIZONTAL",5,8,7)#16
create_file("./documents/dicom/images/fake.dcm",5,8,16)
create_file("./documents/dicom/images/fake.dcm",5,8,16)
create_file("./documents/dicom/images/fake.dcm",5,8,16)
create_file("./documents/dicom/images/fake.dcm",5,8,16)
create_series("SER_W_CONTRAST_HORIZONTAL",5,8,8)#17
create_file("./documents/dicom/images/fake.dcm",5,8,17)
create_file("./documents/dicom/images/fake.dcm",5,8,17)
create_file("./documents/dicom/images/fake.dcm",5,8,17)
create_file("./documents/dicom/images/fake.dcm",5,8,17)
create_file("./documents/dicom/images/fake.dcm",5,8,17)
create_file("./documents/dicom/images/fake.dcm",5,8,17)
create_file("./documents/dicom/images/fake.dcm",5,8,17)

create_patient("EDWARD_JENNER")#6
create_study("CT_SHOULDER_DX",6)#9
create_series("SER_W_W_HORIZONTAL",6,9,9)#18
create_file("./documents/dicom/images/fake.dcm",6,9,18)
create_file("./documents/dicom/images/fake.dcm",6,9,18)
create_file("./documents/dicom/images/fake.dcm",6,9,18)
create_series("SER_W_HORIZONTAL",6,9,10)#19
create_file("./documents/dicom/images/fake.dcm",6,9,19)
create_file("./documents/dicom/images/fake.dcm",6,9,19)
create_series("SER_F_W_HORIZONTAL",6,9,11)#20
create_file("./documents/dicom/images/fake.dcm",6,9,20)
create_file("./documents/dicom/images/fake.dcm",6,9,20)
create_file("./documents/dicom/images/fake.dcm",6,9,20)
create_study("CT_SHOULDER_SX",6)#10
create_series("SER_W_W_HORIZONTAL",6,10,9)#21
create_file("./documents/dicom/images/fake.dcm",6,10,21)
create_file("./documents/dicom/images/fake.dcm",6,10,21)
create_file("./documents/dicom/images/fake.dcm",6,10,21)
create_file("./documents/dicom/images/fake.dcm",6,10,21)
create_file("./documents/dicom/images/fake.dcm",6,10,21)
create_file("./documents/dicom/images/fake.dcm",6,10,21)
create_series("SER_W_HORIZONTAL",6,10,10)#22
create_file("./documents/dicom/images/fake.dcm",6,10,22)
create_file("./documents/dicom/images/fake.dcm",6,10,22)
create_file("./documents/dicom/images/fake.dcm",6,10,22)
create_file("./documents/dicom/images/fake.dcm",6,10,22)
create_file("./documents/dicom/images/fake.dcm",6,10,22)
create_file("./documents/dicom/images/fake.dcm",6,10,22)
create_file("./documents/dicom/images/fake.dcm",6,10,22)
create_file("./documents/dicom/images/fake.dcm",6,10,22)
create_file("./documents/dicom/images/fake.dcm",6,10,22)
create_series("SER_F_W_HORIZONTAL",6,10,11)#23
create_file("./documents/dicom/images/fake.dcm",6,10,23)
create_file("./documents/dicom/images/fake.dcm",6,10,23)
create_file("./documents/dicom/images/fake.dcm",6,10,23)
create_file("./documents/dicom/images/fake.dcm",6,10,23)

create_patient("IGNAZ_SEMMELWEIS")#7
create_study("CT_SHOULDER_DX",7)#11
create_series("FRS_W_CONTRAST_HORIZONTAL",7,11,13)#24
create_file("./documents/dicom/images/fake.dcm",7,11,24)
create_file("./documents/dicom/images/fake.dcm",7,11,24)
create_file("./documents/dicom/images/fake.dcm",7,11,24)
create_file("./documents/dicom/images/fake.dcm",7,11,24)
create_file("./documents/dicom/images/fake.dcm",7,11,24)
create_series("VFB_W_HORIZONTAL",7,11,14)#25
create_file("./documents/dicom/images/fake.dcm",7,11,25)
create_file("./documents/dicom/images/fake.dcm",7,11,25)
create_file("./documents/dicom/images/fake.dcm",7,11,25)
create_file("./documents/dicom/images/fake.dcm",7,11,25)
create_file("./documents/dicom/images/fake.dcm",7,11,25)
create_file("./documents/dicom/images/fake.dcm",7,11,25)
create_file("./documents/dicom/images/fake.dcm",7,11,25)
create_file("./documents/dicom/images/fake.dcm",7,11,25)
create_study("CT_SHOULDER_SX",7)#12
create_series("FRS_W_CONTRAST_HORIZONTAL",7,12,13)#26
create_file("./documents/dicom/images/fake.dcm",7,12,26)
create_file("./documents/dicom/images/fake.dcm",7,12,26)
create_file("./documents/dicom/images/fake.dcm",7,12,26)
create_file("./documents/dicom/images/fake.dcm",7,12,26)
create_file("./documents/dicom/images/fake.dcm",7,12,26)
create_file("./documents/dicom/images/fake.dcm",7,12,26)
create_series("VFB_W_HORIZONTAL",7,12,14)#27
create_file("./documents/dicom/images/fake.dcm",7,12,27)
create_file("./documents/dicom/images/fake.dcm",7,12,27)
create_file("./documents/dicom/images/fake.dcm",7,12,27)
create_file("./documents/dicom/images/fake.dcm",7,12,27)
create_file("./documents/dicom/images/fake.dcm",7,12,27)
create_file("./documents/dicom/images/fake.dcm",7,12,27)
create_file("./documents/dicom/images/fake.dcm",7,12,27)
create_file("./documents/dicom/images/fake.dcm",7,12,27)
create_file("./documents/dicom/images/fake.dcm",7,12,27)
create_study("TRANSREP_W_AX",7)#13
create_series("AWS_HORIZONTAL",7,13,12)#28
create_file("./documents/dicom/images/fake.dcm",7,13,28)
create_file("./documents/dicom/images/fake.dcm",7,13,28)
create_file("./documents/dicom/images/fake.dcm",7,13,28)
create_file("./documents/dicom/images/fake.dcm",7,13,28)
create_series("FRS_W_CONTRAST_HORIZONTAL",7,13,13)#29
create_file("./documents/dicom/images/fake.dcm",7,13,29)
create_file("./documents/dicom/images/fake.dcm",7,13,29)
create_file("./documents/dicom/images/fake.dcm",7,13,29)
create_file("./documents/dicom/images/fake.dcm",7,13,29)
create_file("./documents/dicom/images/fake.dcm",7,13,29)
create_series("VFB_W_HORIZONTAL",7,13,14)#30
create_file("./documents/dicom/images/fake.dcm",7,13,30)
create_file("./documents/dicom/images/fake.dcm",7,13,30)

create_patient("SIR_JOSEPH_LISTER")#8
create_study("CT_ABDOMEN_W_V_CONTRAST",8)#14
create_series("RIGJ_W_HORIZONTAL",8,14,16)#31
create_file("./documents/dicom/images/fake.dcm",8,14,31)
create_file("./documents/dicom/images/fake.dcm",8,14,31)
create_file("./documents/dicom/images/fake.dcm",8,14,31)
create_study("ABDOMEN_W",8)#15
create_series("RIGJ_W_HORIZONTAL",8,15,16)#32
create_file("./documents/dicom/images/fake.dcm",8,15,32)
create_file("./documents/dicom/images/fake.dcm",8,15,32)
create_file("./documents/dicom/images/fake.dcm",8,15,32)
create_file("./documents/dicom/images/fake.dcm",8,15,32)
create_file("./documents/dicom/images/fake.dcm",8,15,32)

create_patient("JOHN_SNOW")#9
create_study("CT_ABDOMEN_W_WO_CONTRAST",9)#16
create_series("VFB_HORIZONTAL",9,16,15)#33
create_file("./documents/dicom/images/fake.dcm",9,16,33)
create_file("./documents/dicom/images/fake.dcm",9,16,33)
create_file("./documents/dicom/images/fake.dcm",9,16,33)
create_file("./documents/dicom/images/fake.dcm",9,16,33)
create_file("./documents/dicom/images/fake.dcm",9,16,33)
create_file("./documents/dicom/images/fake.dcm",9,16,33)
create_file("./documents/dicom/images/fake.dcm",9,16,33)
create_series("RIGJ_W_HORIZONTAL",9,16,16)#34
create_file("./documents/dicom/images/fake.dcm",9,16,34)
create_file("./documents/dicom/images/fake.dcm",9,16,34)
create_file("./documents/dicom/images/fake.dcm",9,16,34)
create_file("./documents/dicom/images/fake.dcm",9,16,34)
create_series("RIGJ_HORIZONTAL",9,16,17)#35
create_file("./documents/dicom/images/fake.dcm",9,16,35)
create_file("./documents/dicom/images/fake.dcm",9,16,35)
create_file("./documents/dicom/images/fake.dcm",9,16,35)
create_file("./documents/dicom/images/fake.dcm",9,16,35)
create_file("./documents/dicom/images/fake.dcm",9,16,35)
create_study("TRANSREP_FX",9)#17
create_series("SERGG_CONTRAST_HORIZONTAL",9,17,3)#36
create_file("./documents/dicom/images/fake.dcm",9,17,36)
create_file("./documents/dicom/images/fake.dcm",9,17,36)
create_file("./documents/dicom/images/fake.dcm",9,17,36)
create_series("SEWERR_HORIZONTAL",9,17,4)#37
create_file("./documents/dicom/images/fake.dcm",9,17,37)
create_file("./documents/dicom/images/fake.dcm",9,17,37)
create_file("./documents/dicom/images/fake.dcm",9,17,37)
create_file("./documents/dicom/images/fake.dcm",9,17,37)
create_file("./documents/dicom/images/fake.dcm",9,17,37)
create_file("./documents/dicom/images/fake.dcm",9,17,37)
create_file("./documents/dicom/images/fake.dcm",9,17,37)
create_study("TRANSREP_GX",9)#18
create_series("SER",9,18,1)#38
create_file("./documents/dicom/images/fake.dcm",9,18,38)
create_file("./documents/dicom/images/fake.dcm",9,18,38)
create_file("./documents/dicom/images/fake.dcm",9,18,38)
create_file("./documents/dicom/images/fake.dcm",9,18,38)
create_series("SERGG_HORIZONTAL",9,18,2)#39
create_file("./documents/dicom/images/fake.dcm",9,18,39)
create_file("./documents/dicom/images/fake.dcm",9,18,39)
create_series("SEWERR_W_HORIZONTAL",9,18,5)#40
create_file("./documents/dicom/images/fake.dcm",9,18,40)
create_file("./documents/dicom/images/fake.dcm",9,18,40)

create_patient("SIGMUND_FREUD")#10
create_study("CT_ABDOMEN_W_IV",10)#19
create_series("SEWERR_HORIZONTAL",10,19,6)#41
create_file("./documents/dicom/images/fake.dcm",10,19,41)
create_file("./documents/dicom/images/fake.dcm",10,19,41)
create_file("./documents/dicom/images/fake.dcm",10,19,41)
create_file("./documents/dicom/images/fake.dcm",10,19,41)
create_series("SEWERR_W_HORIZONTAL",10,19,7)#42
create_file("./documents/dicom/images/fake.dcm",10,19,42)
create_file("./documents/dicom/images/fake.dcm",10,19,42)
create_file("./documents/dicom/images/fake.dcm",10,19,42)
create_series("SER_GG_VERTICAL",10,19,8)#43
create_file("./documents/dicom/images/fake.dcm",10,19,43)
create_file("./documents/dicom/images/fake.dcm",10,19,43)
create_file("./documents/dicom/images/fake.dcm",10,19,43)
create_file("./documents/dicom/images/fake.dcm",10,19,43)
create_file("./documents/dicom/images/fake.dcm",10,19,43)
create_file("./documents/dicom/images/fake.dcm",10,19,43)
create_file("./documents/dicom/images/fake.dcm",10,19,43)
create_study("CT_LEG",10)#20
create_series("SER_QWR_VERTICAL",10,20,11)#44
create_file("./documents/dicom/images/fake.dcm",10,20,44)
create_file("./documents/dicom/images/fake.dcm",10,20,44)
create_file("./documents/dicom/images/fake.dcm",10,20,44)
create_file("./documents/dicom/images/fake.dcm",10,20,44)
create_file("./documents/dicom/images/fake.dcm",10,20,44)
create_series("SER_GBFGG_W_VERTICAL",10,20,12)#45
create_file("./documents/dicom/images/fake.dcm",10,20,45)
create_file("./documents/dicom/images/fake.dcm",10,20,45)
create_file("./documents/dicom/images/fake.dcm",10,20,45)
create_file("./documents/dicom/images/fake.dcm",10,20,45)

create_patient("SIR_WILLIAM_OSLER")#11
create_study("CT_ARM",11)#21
create_series("SER_WEG_VERTICAL",11,21,9)#46
create_file("./documents/dicom/images/fake.dcm",11,21,46)
create_file("./documents/dicom/images/fake.dcm",11,21,46)
create_file("./documents/dicom/images/fake.dcm",11,21,46)
create_file("./documents/dicom/images/fake.dcm",11,21,46)
create_file("./documents/dicom/images/fake.dcm",11,21,46)
create_series("SER_QWR_CONTRAST_VERTICAL",11,21,10)#47
create_file("./documents/dicom/images/fake.dcm",11,21,47)
create_file("./documents/dicom/images/fake.dcm",11,21,47)
create_file("./documents/dicom/images/fake.dcm",11,21,47)
create_file("./documents/dicom/images/fake.dcm",11,21,47)
create_file("./documents/dicom/images/fake.dcm",11,21,47)
create_file("./documents/dicom/images/fake.dcm",11,21,47)
create_file("./documents/dicom/images/fake.dcm",11,21,47)
create_series("SER_WWRG_VERTICAL",11,21,14)#48
create_file("./documents/dicom/images/fake.dcm",11,21,48)
create_file("./documents/dicom/images/fake.dcm",11,21,48)
create_file("./documents/dicom/images/fake.dcm",11,21,48)
create_file("./documents/dicom/images/fake.dcm",11,21,48)
create_file("./documents/dicom/images/fake.dcm",11,21,48)
create_study("CT_SHOULDER_DX",11)#22
create_series("QERFF_SER_VERTICAL",11,22,15)#49
create_file("./documents/dicom/images/fake.dcm",11,22,49)
create_file("./documents/dicom/images/fake.dcm",11,22,49)
create_file("./documents/dicom/images/fake.dcm",11,22,49)
create_file("./documents/dicom/images/fake.dcm",11,22,49)
create_file("./documents/dicom/images/fake.dcm",11,22,49)
create_file("./documents/dicom/images/fake.dcm",11,22,49)
create_series("QERFF_SER_CONTRAST_VERTICAL",11,22,16)#50
create_file("./documents/dicom/images/fake.dcm",11,22,50)
create_file("./documents/dicom/images/fake.dcm",11,22,50)
create_file("./documents/dicom/images/fake.dcm",11,22,50)
create_file("./documents/dicom/images/fake.dcm",11,22,50)
create_file("./documents/dicom/images/fake.dcm",11,22,50)
create_file("./documents/dicom/images/fake.dcm",11,22,50)
create_series("QWFV_SER_VERTICAL",11,22,17)#51
create_file("./documents/dicom/images/fake.dcm",11,22,51)
create_file("./documents/dicom/images/fake.dcm",11,22,51)
create_file("./documents/dicom/images/fake.dcm",11,22,51)
create_file("./documents/dicom/images/fake.dcm",11,22,51)
create_file("./documents/dicom/images/fake.dcm",11,22,51)
create_file("./documents/dicom/images/fake.dcm",11,22,51)
create_series("QWFV_SER_VERTICAL",11,22,18)#52
create_file("./documents/dicom/images/fake.dcm",11,22,52)
create_file("./documents/dicom/images/fake.dcm",11,22,52)
create_file("./documents/dicom/images/fake.dcm",11,22,52)
create_file("./documents/dicom/images/fake.dcm",11,22,52)
create_file("./documents/dicom/images/fake.dcm",11,22,52)
create_file("./documents/dicom/images/fake.dcm",11,22,52)
create_series("WQFV_RUCK_RIGHT",11,22,1)#53
create_file("./documents/dicom/images/fake.dcm",11,22,53)
create_file("./documents/dicom/images/fake.dcm",11,22,53)
create_file("./documents/dicom/images/fake.dcm",11,22,53)
create_file("./documents/dicom/images/fake.dcm",11,22,53)
create_file("./documents/dicom/images/fake.dcm",11,22,53)
create_file("./documents/dicom/images/fake.dcm",11,22,53)

create_patient("ROBERT_KOCH")#12
create_study("CT_SHOULDER_SX",12)#23
create_series("WQFV_RUCK_CONTRAST_RIGHT",12,23,2)#54
create_file("./documents/dicom/images/fake.dcm",12,23,54)
create_file("./documents/dicom/images/fake.dcm",12,23,54)
create_file("./documents/dicom/images/fake.dcm",12,23,54)
create_file("./documents/dicom/images/fake.dcm",12,23,54)
create_file("./documents/dicom/images/fake.dcm",12,23,54)
create_series("RUCK_WFV_RIGHT",12,23,3)#55
create_file("./documents/dicom/images/fake.dcm",12,23,55)
create_file("./documents/dicom/images/fake.dcm",12,23,55)
create_file("./documents/dicom/images/fake.dcm",12,23,55)
create_file("./documents/dicom/images/fake.dcm",12,23,55)
create_file("./documents/dicom/images/fake.dcm",12,23,55)
create_file("./documents/dicom/images/fake.dcm",12,23,55)
create_series("RUCK_WFV_CONTRAST_RIGHT",12,23,4)#56
create_file("./documents/dicom/images/fake.dcm",12,23,56)
create_file("./documents/dicom/images/fake.dcm",12,23,56)
create_file("./documents/dicom/images/fake.dcm",12,23,56)
create_file("./documents/dicom/images/fake.dcm",12,23,56)
create_file("./documents/dicom/images/fake.dcm",12,23,56)
create_series("QWFV_RUCK_RIGHT",12,23,5)#57
create_file("./documents/dicom/images/fake.dcm",12,23,57)
create_file("./documents/dicom/images/fake.dcm",12,23,57)
create_file("./documents/dicom/images/fake.dcm",12,23,57)
create_file("./documents/dicom/images/fake.dcm",12,23,57)
create_file("./documents/dicom/images/fake.dcm",12,23,57)
create_series("EWV_RUCK_RIGHT",12,23,6)#58
create_file("./documents/dicom/images/fake.dcm",12,23,58)
create_file("./documents/dicom/images/fake.dcm",12,23,58)
create_file("./documents/dicom/images/fake.dcm",12,23,58)
create_file("./documents/dicom/images/fake.dcm",12,23,58)
create_file("./documents/dicom/images/fake.dcm",12,23,58)
create_study("TRANSREP_AX",12)#24
create_series("QWEFV_RUCK_CONTRAST_RIGHT",12,24,7)#59
create_file("./documents/dicom/images/fake.dcm",12,24,59)
create_file("./documents/dicom/images/fake.dcm",12,24,59)
create_file("./documents/dicom/images/fake.dcm",12,24,59)
create_file("./documents/dicom/images/fake.dcm",12,24,59)
create_file("./documents/dicom/images/fake.dcm",12,24,59)
create_file("./documents/dicom/images/fake.dcm",12,24,59)
create_file("./documents/dicom/images/fake.dcm",12,24,59)
create_file("./documents/dicom/images/fake.dcm",12,24,59)
create_series("QWRBD_RUCK_RIGHT",12,24,8)#60
create_file("./documents/dicom/images/fake.dcm",12,24,60)
create_file("./documents/dicom/images/fake.dcm",12,24,60)
create_file("./documents/dicom/images/fake.dcm",12,24,60)
create_file("./documents/dicom/images/fake.dcm",12,24,60)
create_file("./documents/dicom/images/fake.dcm",12,24,60)
create_file("./documents/dicom/images/fake.dcm",12,24,60)
create_file("./documents/dicom/images/fake.dcm",12,24,60)
create_series("QWFVDSA_RUCK_CONTRAST_RIGHT",12,24,9)#61
create_file("./documents/dicom/images/fake.dcm",12,24,61)
create_file("./documents/dicom/images/fake.dcm",12,24,61)
create_file("./documents/dicom/images/fake.dcm",12,24,61)
create_file("./documents/dicom/images/fake.dcm",12,24,61)
create_file("./documents/dicom/images/fake.dcm",12,24,61)
create_file("./documents/dicom/images/fake.dcm",12,24,61)
create_file("./documents/dicom/images/fake.dcm",12,24,61)
create_series("QWSAZG_RUCK_RIGHT",12,24,10)#62
create_file("./documents/dicom/images/fake.dcm",12,24,62)
create_file("./documents/dicom/images/fake.dcm",12,24,62)
create_file("./documents/dicom/images/fake.dcm",12,24,62)
create_file("./documents/dicom/images/fake.dcm",12,24,62)
create_file("./documents/dicom/images/fake.dcm",12,24,62)
create_file("./documents/dicom/images/fake.dcm",12,24,62)
create_file("./documents/dicom/images/fake.dcm",12,24,62)
create_series("SER_HORIZONTAL_AX",12,24,1)#63
create_file("./documents/dicom/images/fake.dcm",12,24,63)
create_file("./documents/dicom/images/fake.dcm",12,24,63)
create_file("./documents/dicom/images/fake.dcm",12,24,63)
create_file("./documents/dicom/images/fake.dcm",12,24,63)
create_file("./documents/dicom/images/fake.dcm",12,24,63)
create_file("./documents/dicom/images/fake.dcm",12,24,63)
create_file("./documents/dicom/images/fake.dcm",12,24,63)
create_file("./documents/dicom/images/fake.dcm",12,24,63)
create_series("SER_HORIZONTAL_RF",12,24,2)#64
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_file("./documents/dicom/images/fake.dcm",12,24,64)
create_series("SER_W_CONTRAST_HORIZONTAL",12,24,3)#65
create_file("./documents/dicom/images/fake.dcm",12,24,65)
create_file("./documents/dicom/images/fake.dcm",12,24,65)
create_file("./documents/dicom/images/fake.dcm",12,24,65)
create_file("./documents/dicom/images/fake.dcm",12,24,65)
create_file("./documents/dicom/images/fake.dcm",12,24,65)
create_file("./documents/dicom/images/fake.dcm",12,24,65)
create_file("./documents/dicom/images/fake.dcm",12,24,65)
create_file("./documents/dicom/images/fake.dcm",12,24,65)
create_study("TRANSREP_PX",12)#25
create_series("SER_RF_HORIZONTAL",12,25,4)#66
create_file("./documents/dicom/images/fake.dcm",12,25,66)
create_file("./documents/dicom/images/fake.dcm",12,25,66)
create_file("./documents/dicom/images/fake.dcm",12,25,66)
create_file("./documents/dicom/images/fake.dcm",12,25,66)
create_file("./documents/dicom/images/fake.dcm",12,25,66)
create_file("./documents/dicom/images/fake.dcm",12,25,66)
create_file("./documents/dicom/images/fake.dcm",12,25,66)
create_file("./documents/dicom/images/fake.dcm",12,25,66)
create_file("./documents/dicom/images/fake.dcm",12,25,66)
create_series("SER_RF_W_HORIZONTAL",12,25,5)#67
create_file("./documents/dicom/images/fake.dcm",12,25,67)
create_file("./documents/dicom/images/fake.dcm",12,25,67)
create_file("./documents/dicom/images/fake.dcm",12,25,67)
create_file("./documents/dicom/images/fake.dcm",12,25,67)
create_file("./documents/dicom/images/fake.dcm",12,25,67)
create_file("./documents/dicom/images/fake.dcm",12,25,67)
create_file("./documents/dicom/images/fake.dcm",12,25,67)
create_series("SER_RF_CONTRAST_HORIZONTAL",12,25,6)#68
create_file("./documents/dicom/images/fake.dcm",12,25,68)
create_file("./documents/dicom/images/fake.dcm",12,25,68)
create_file("./documents/dicom/images/fake.dcm",12,25,68)
create_file("./documents/dicom/images/fake.dcm",12,25,68)
create_file("./documents/dicom/images/fake.dcm",12,25,68)
create_file("./documents/dicom/images/fake.dcm",12,25,68)
create_series("SER_DP_W_HORIZONTAL",12,25,7)#69
create_file("./documents/dicom/images/fake.dcm",12,25,69)
create_file("./documents/dicom/images/fake.dcm",12,25,69)
create_file("./documents/dicom/images/fake.dcm",12,25,69)
create_file("./documents/dicom/images/fake.dcm",12,25,69)
create_file("./documents/dicom/images/fake.dcm",12,25,69)
create_file("./documents/dicom/images/fake.dcm",12,25,69)
create_file("./documents/dicom/images/fake.dcm",12,25,69)
create_file("./documents/dicom/images/fake.dcm",12,25,69)
create_file("./documents/dicom/images/fake.dcm",12,25,69)
create_series("SER_W_CONTRAST_HORIZONTAL",12,25,8)#70
create_file("./documents/dicom/images/fake.dcm",12,25,70)
create_file("./documents/dicom/images/fake.dcm",12,25,70)
create_file("./documents/dicom/images/fake.dcm",12,25,70)
create_file("./documents/dicom/images/fake.dcm",12,25,70)
create_file("./documents/dicom/images/fake.dcm",12,25,70)
create_file("./documents/dicom/images/fake.dcm",12,25,70)
create_file("./documents/dicom/images/fake.dcm",12,25,70)
create_series("SER_HORIZONTAL_AX",12,25,1)#71
create_file("./documents/dicom/images/fake.dcm",23,36,71)
create_file("./documents/dicom/images/fake.dcm",23,36,71)
create_file("./documents/dicom/images/fake.dcm",23,36,71)
create_file("./documents/dicom/images/fake.dcm",23,36,71)
create_file("./documents/dicom/images/fake.dcm",23,36,71)
create_file("./documents/dicom/images/fake.dcm",23,36,71)
create_file("./documents/dicom/images/fake.dcm",23,36,71)
create_file("./documents/dicom/images/fake.dcm",23,36,71)
create_file("./documents/dicom/images/fake.dcm",23,36,71)
create_series("SER_HORIZONTAL_RF",12,25,2)#72
create_file("./documents/dicom/images/fake.dcm",23,36,72)
create_file("./documents/dicom/images/fake.dcm",23,36,72)
create_file("./documents/dicom/images/fake.dcm",23,36,72)
create_file("./documents/dicom/images/fake.dcm",23,36,72)
create_file("./documents/dicom/images/fake.dcm",23,36,72)
create_file("./documents/dicom/images/fake.dcm",23,36,72)
create_file("./documents/dicom/images/fake.dcm",23,36,72)
create_file("./documents/dicom/images/fake.dcm",23,36,72)
create_file("./documents/dicom/images/fake.dcm",23,36,72)
create_file("./documents/dicom/images/fake.dcm",23,36,72)
create_series("SER_W_CONTRAST_HORIZONTAL",12,25,3)#73
create_file("./documents/dicom/images/fake.dcm",12,25,73)
create_file("./documents/dicom/images/fake.dcm",12,25,73)
create_file("./documents/dicom/images/fake.dcm",12,25,73)
create_file("./documents/dicom/images/fake.dcm",12,25,73)
create_file("./documents/dicom/images/fake.dcm",12,25,73)

create_patient("SIR_ALEXANDER_FLEMING")#13
create_study("TRANSREP",13)#26
create_series("SER_F_W_HORIZONTAL",13,26,11)#74
create_file("./documents/dicom/images/fake.dcm",13,26,74)
create_file("./documents/dicom/images/fake.dcm",13,26,74)
create_file("./documents/dicom/images/fake.dcm",13,26,74)
create_file("./documents/dicom/images/fake.dcm",13,26,74)
create_file("./documents/dicom/images/fake.dcm",13,26,74)
create_file("./documents/dicom/images/fake.dcm",13,26,74)
create_file("./documents/dicom/images/fake.dcm",13,26,74)
create_file("./documents/dicom/images/fake.dcm",13,26,74)
create_series("AWS_HORIZONTAL",13,26,12)#75
create_file("./documents/dicom/images/fake.dcm",13,26,75)
create_file("./documents/dicom/images/fake.dcm",13,26,75)
create_file("./documents/dicom/images/fake.dcm",13,26,75)
create_file("./documents/dicom/images/fake.dcm",13,26,75)
create_file("./documents/dicom/images/fake.dcm",13,26,75)
create_series("FRS_W_CONTRAST_HORIZONTAL",13,26,13)#76
create_file("./documents/dicom/images/fake.dcm",13,26,76)
create_file("./documents/dicom/images/fake.dcm",13,26,76)
create_file("./documents/dicom/images/fake.dcm",13,26,76)
create_file("./documents/dicom/images/fake.dcm",13,26,76)
create_file("./documents/dicom/images/fake.dcm",13,26,76)
create_file("./documents/dicom/images/fake.dcm",13,26,76)
create_file("./documents/dicom/images/fake.dcm",13,26,76)
create_series("VFB_W_HORIZONTAL",13,26,14)#77
create_file("./documents/dicom/images/fake.dcm",13,26,77)
create_file("./documents/dicom/images/fake.dcm",13,26,77)
create_file("./documents/dicom/images/fake.dcm",13,26,77)
create_file("./documents/dicom/images/fake.dcm",13,26,77)
create_file("./documents/dicom/images/fake.dcm",13,26,77)
create_series("VFB_HORIZONTAL",13,26,15)#78
create_file("./documents/dicom/images/fake.dcm",13,26,78)
create_file("./documents/dicom/images/fake.dcm",13,26,78)
create_file("./documents/dicom/images/fake.dcm",13,26,78)
create_file("./documents/dicom/images/fake.dcm",13,26,78)
create_file("./documents/dicom/images/fake.dcm",13,26,78)
create_file("./documents/dicom/images/fake.dcm",13,26,78)
create_file("./documents/dicom/images/fake.dcm",13,26,78)
create_file("./documents/dicom/images/fake.dcm",13,26,78)
create_series("RIGJ_W_HORIZONTAL",13,26,16)#79
create_file("./documents/dicom/images/fake.dcm",13,26,79)
create_file("./documents/dicom/images/fake.dcm",13,26,79)
create_file("./documents/dicom/images/fake.dcm",13,26,79)
create_file("./documents/dicom/images/fake.dcm",13,26,79)
create_file("./documents/dicom/images/fake.dcm",13,26,79)
create_file("./documents/dicom/images/fake.dcm",13,26,79)
create_file("./documents/dicom/images/fake.dcm",13,26,79)
create_file("./documents/dicom/images/fake.dcm",13,26,79)
create_file("./documents/dicom/images/fake.dcm",13,26,79)
create_file("./documents/dicom/images/fake.dcm",13,26,79)
create_series("RIGJ_HORIZONTAL",13,26,17)#80
create_file("./documents/dicom/images/fake.dcm",13,26,80)
create_file("./documents/dicom/images/fake.dcm",13,26,80)
create_file("./documents/dicom/images/fake.dcm",13,26,80)
create_file("./documents/dicom/images/fake.dcm",13,26,80)
create_file("./documents/dicom/images/fake.dcm",13,26,80)
create_file("./documents/dicom/images/fake.dcm",13,26,80)
create_file("./documents/dicom/images/fake.dcm",13,26,80)
create_series("SER",13,26,1)#81
create_file("./documents/dicom/images/fake.dcm",13,26,81)
create_file("./documents/dicom/images/fake.dcm",13,26,81)
create_file("./documents/dicom/images/fake.dcm",13,26,81)
create_file("./documents/dicom/images/fake.dcm",13,26,81)
create_file("./documents/dicom/images/fake.dcm",13,26,81)
create_file("./documents/dicom/images/fake.dcm",13,26,81)
create_study("TRANSREP_THEET",13)#27
create_series("SERGG_HORIZONTAL",13,27,2)#82
create_file("./documents/dicom/images/fake.dcm",13,27,82)
create_file("./documents/dicom/images/fake.dcm",13,27,82)
create_file("./documents/dicom/images/fake.dcm",13,27,82)
create_file("./documents/dicom/images/fake.dcm",13,27,82)
create_file("./documents/dicom/images/fake.dcm",13,27,82)
create_file("./documents/dicom/images/fake.dcm",13,27,82)
create_series("SERGG_CONTRAST_HORIZONTAL",13,27,3)#83
create_file("./documents/dicom/images/fake.dcm",13,27,83)
create_file("./documents/dicom/images/fake.dcm",13,27,83)
create_file("./documents/dicom/images/fake.dcm",13,27,83)
create_file("./documents/dicom/images/fake.dcm",13,27,83)
create_file("./documents/dicom/images/fake.dcm",13,27,83)
create_series("SEWERR_HORIZONTAL",13,27,4)#84
create_file("./documents/dicom/images/fake.dcm",13,27,84)
create_file("./documents/dicom/images/fake.dcm",13,27,84)
create_file("./documents/dicom/images/fake.dcm",13,27,84)
create_file("./documents/dicom/images/fake.dcm",13,27,84)
create_file("./documents/dicom/images/fake.dcm",13,27,84)
create_file("./documents/dicom/images/fake.dcm",13,27,84)
create_series("SEWERR_W_HORIZONTAL",13,27,5)#85
create_file("./documents/dicom/images/fake.dcm",13,27,85)
create_file("./documents/dicom/images/fake.dcm",13,27,85)
create_file("./documents/dicom/images/fake.dcm",13,27,85)
create_file("./documents/dicom/images/fake.dcm",13,27,85)
create_file("./documents/dicom/images/fake.dcm",13,27,85)
create_file("./documents/dicom/images/fake.dcm",13,27,85)
create_file("./documents/dicom/images/fake.dcm",13,27,85)
create_series("SEWERR_HORIZONTAL",13,27,6)#86
create_file("./documents/dicom/images/fake.dcm",13,27,86)
create_file("./documents/dicom/images/fake.dcm",13,27,86)
create_file("./documents/dicom/images/fake.dcm",13,27,86)
create_file("./documents/dicom/images/fake.dcm",13,27,86)
create_file("./documents/dicom/images/fake.dcm",13,27,86)
create_file("./documents/dicom/images/fake.dcm",13,27,86)
create_file("./documents/dicom/images/fake.dcm",13,27,86)
create_file("./documents/dicom/images/fake.dcm",13,27,86)
create_series("SEWERR_W_HORIZONTAL",13,27,7)#87
create_file("./documents/dicom/images/fake.dcm",13,27,87)
create_file("./documents/dicom/images/fake.dcm",13,27,87)
create_file("./documents/dicom/images/fake.dcm",13,27,87)
create_file("./documents/dicom/images/fake.dcm",13,27,87)
create_file("./documents/dicom/images/fake.dcm",13,27,87)
create_file("./documents/dicom/images/fake.dcm",13,27,87)
create_file("./documents/dicom/images/fake.dcm",13,27,87)
create_file("./documents/dicom/images/fake.dcm",13,27,87)
create_file("./documents/dicom/images/fake.dcm",13,27,87)
create_series("SER_GG_VERTICAL",13,27,8)#88
create_file("./documents/dicom/images/fake.dcm",13,27,88)
create_file("./documents/dicom/images/fake.dcm",13,27,88)
create_file("./documents/dicom/images/fake.dcm",13,27,88)
create_file("./documents/dicom/images/fake.dcm",13,27,88)
create_file("./documents/dicom/images/fake.dcm",13,27,88)
create_file("./documents/dicom/images/fake.dcm",13,27,88)
create_file("./documents/dicom/images/fake.dcm",13,27,88)
create_file("./documents/dicom/images/fake.dcm",13,27,88)
create_file("./documents/dicom/images/fake.dcm",13,27,88)
create_series("SER_WEG_VERTICAL",13,27,9)#89
create_file("./documents/dicom/images/fake.dcm",13,27,89)
create_file("./documents/dicom/images/fake.dcm",13,27,89)
create_file("./documents/dicom/images/fake.dcm",13,27,89)
create_file("./documents/dicom/images/fake.dcm",13,27,89)
create_file("./documents/dicom/images/fake.dcm",13,27,89)
create_series("SER_QWR_CONTRAST_VERTICAL",13,27,10)#90
create_file("./documents/dicom/images/fake.dcm",13,27,90)
create_file("./documents/dicom/images/fake.dcm",13,27,90)
create_file("./documents/dicom/images/fake.dcm",13,27,90)
create_file("./documents/dicom/images/fake.dcm",13,27,90)
create_file("./documents/dicom/images/fake.dcm",13,27,90)
create_file("./documents/dicom/images/fake.dcm",13,27,90)
create_file("./documents/dicom/images/fake.dcm",13,27,90)
create_file("./documents/dicom/images/fake.dcm",13,27,90)
create_file("./documents/dicom/images/fake.dcm",13,27,90)

create_patient("JONAS_SALK")#14
create_study("AATRANSREP",14)#28
create_series("SER_RF_HORIZONTAL",14,28,4)#91
create_file("./documents/dicom/images/fake.dcm",14,28,91)
create_file("./documents/dicom/images/fake.dcm",14,28,91)
create_file("./documents/dicom/images/fake.dcm",14,28,91)
create_file("./documents/dicom/images/fake.dcm",14,28,91)
create_file("./documents/dicom/images/fake.dcm",14,28,91)
create_file("./documents/dicom/images/fake.dcm",14,28,91)
create_file("./documents/dicom/images/fake.dcm",14,28,91)
create_file("./documents/dicom/images/fake.dcm",14,28,91)
create_series("SER_RF_W_HORIZONTAL",14,28,5)#92
create_file("./documents/dicom/images/fake.dcm",14,28,92)
create_file("./documents/dicom/images/fake.dcm",14,28,92)
create_file("./documents/dicom/images/fake.dcm",14,28,92)
create_file("./documents/dicom/images/fake.dcm",14,28,92)
create_file("./documents/dicom/images/fake.dcm",14,28,92)
create_file("./documents/dicom/images/fake.dcm",14,28,92)
create_series("SER_RF_CONTRAST_HORIZONTAL",14,28,6)#93
create_file("./documents/dicom/images/fake.dcm",14,28,93)
create_file("./documents/dicom/images/fake.dcm",14,28,93)
create_file("./documents/dicom/images/fake.dcm",14,28,93)
create_file("./documents/dicom/images/fake.dcm",14,28,93)
create_file("./documents/dicom/images/fake.dcm",14,28,93)
create_file("./documents/dicom/images/fake.dcm",14,28,93)
create_file("./documents/dicom/images/fake.dcm",14,28,93)
create_file("./documents/dicom/images/fake.dcm",14,28,93)
create_series("SER_DP_W_HORIZONTAL",14,28,7)#94
create_file("./documents/dicom/images/fake.dcm",14,28,94)
create_file("./documents/dicom/images/fake.dcm",14,28,94)
create_file("./documents/dicom/images/fake.dcm",14,28,94)
create_file("./documents/dicom/images/fake.dcm",14,28,94)
create_file("./documents/dicom/images/fake.dcm",14,28,94)
create_file("./documents/dicom/images/fake.dcm",14,28,94)
create_series("SER_W_CONTRAST_HORIZONTAL",14,28,8)#95
create_file("./documents/dicom/images/fake.dcm",14,28,95)
create_file("./documents/dicom/images/fake.dcm",14,28,95)
create_file("./documents/dicom/images/fake.dcm",14,28,95)
create_file("./documents/dicom/images/fake.dcm",14,28,95)
create_file("./documents/dicom/images/fake.dcm",14,28,95)
create_series("SER_W_W_HORIZONTAL",14,28,9)#96
create_file("./documents/dicom/images/fake.dcm",14,28,96)
create_file("./documents/dicom/images/fake.dcm",14,28,96)
create_file("./documents/dicom/images/fake.dcm",14,28,96)
create_file("./documents/dicom/images/fake.dcm",14,28,96)
create_file("./documents/dicom/images/fake.dcm",14,28,96)
create_file("./documents/dicom/images/fake.dcm",14,28,96)
create_file("./documents/dicom/images/fake.dcm",14,28,96)
create_file("./documents/dicom/images/fake.dcm",14,28,96)
create_file("./documents/dicom/images/fake.dcm",14,28,96)
create_file("./documents/dicom/images/fake.dcm",14,28,96)
create_series("SER_W_HORIZONTAL",14,28,10)#97
create_file("./documents/dicom/images/fake.dcm",14,28,97)
create_file("./documents/dicom/images/fake.dcm",14,28,97)
create_file("./documents/dicom/images/fake.dcm",14,28,97)
create_file("./documents/dicom/images/fake.dcm",14,28,97)
create_file("./documents/dicom/images/fake.dcm",14,28,97)
create_file("./documents/dicom/images/fake.dcm",14,28,97)
create_file("./documents/dicom/images/fake.dcm",14,28,97)
create_file("./documents/dicom/images/fake.dcm",14,28,97)
create_file("./documents/dicom/images/fake.dcm",14,28,97)
create_file("./documents/dicom/images/fake.dcm",14,28,97)
create_study("TRDDDANSREP",14)#29
create_series("SER_QWR_VERTICAL",14,29,11)#98
create_file("./documents/dicom/images/fake.dcm",14,29,98)
create_file("./documents/dicom/images/fake.dcm",14,29,98)
create_file("./documents/dicom/images/fake.dcm",14,29,98)
create_file("./documents/dicom/images/fake.dcm",14,29,98)
create_file("./documents/dicom/images/fake.dcm",14,29,98)
create_file("./documents/dicom/images/fake.dcm",14,29,98)
create_file("./documents/dicom/images/fake.dcm",14,29,98)
create_file("./documents/dicom/images/fake.dcm",14,29,98)
create_file("./documents/dicom/images/fake.dcm",14,29,98)
create_file("./documents/dicom/images/fake.dcm",14,29,98)
create_series("SER_GBFGG_W_VERTICAL",14,29,12)#99
create_file("./documents/dicom/images/fake.dcm",14,29,99)
create_file("./documents/dicom/images/fake.dcm",14,29,99)
create_file("./documents/dicom/images/fake.dcm",14,29,99)
create_file("./documents/dicom/images/fake.dcm",14,29,99)
create_file("./documents/dicom/images/fake.dcm",14,29,99)
create_file("./documents/dicom/images/fake.dcm",14,29,99)
create_series("SER_WWRG_W_VERTICAL",14,29,13)#100
create_file("./documents/dicom/images/fake.dcm",14,29,100)
create_file("./documents/dicom/images/fake.dcm",14,29,100)
create_file("./documents/dicom/images/fake.dcm",14,29,100)
create_file("./documents/dicom/images/fake.dcm",14,29,100)
create_file("./documents/dicom/images/fake.dcm",14,29,100)
create_file("./documents/dicom/images/fake.dcm",14,29,100)
create_series("SEWERR_W_HORIZONTAL",14,29,5)#101
create_file("./documents/dicom/images/fake.dcm",14,29,101)
create_file("./documents/dicom/images/fake.dcm",14,29,101)
create_file("./documents/dicom/images/fake.dcm",14,29,101)
create_file("./documents/dicom/images/fake.dcm",14,29,101)
create_file("./documents/dicom/images/fake.dcm",14,29,101)
create_file("./documents/dicom/images/fake.dcm",14,29,101)
create_file("./documents/dicom/images/fake.dcm",14,29,101)
create_file("./documents/dicom/images/fake.dcm",14,29,101)
create_series("SEWERR_HORIZONTAL",14,29,6)#102
create_file("./documents/dicom/images/fake.dcm",14,29,102)
create_file("./documents/dicom/images/fake.dcm",14,29,102)
create_file("./documents/dicom/images/fake.dcm",14,29,102)
create_file("./documents/dicom/images/fake.dcm",14,29,102)
create_file("./documents/dicom/images/fake.dcm",14,29,102)
create_file("./documents/dicom/images/fake.dcm",14,29,102)
create_file("./documents/dicom/images/fake.dcm",14,29,102)
create_file("./documents/dicom/images/fake.dcm",14,29,102)
create_file("./documents/dicom/images/fake.dcm",14,29,102)
create_series("SEWERR_W_HORIZONTAL",14,29,7)#103
create_file("./documents/dicom/images/fake.dcm",14,29,103)
create_file("./documents/dicom/images/fake.dcm",14,29,103)
create_file("./documents/dicom/images/fake.dcm",14,29,103)
create_file("./documents/dicom/images/fake.dcm",14,29,103)
create_file("./documents/dicom/images/fake.dcm",14,29,103)
create_file("./documents/dicom/images/fake.dcm",14,29,103)
create_file("./documents/dicom/images/fake.dcm",14,29,103)
create_file("./documents/dicom/images/fake.dcm",14,29,103)
create_file("./documents/dicom/images/fake.dcm",14,29,103)
create_file("./documents/dicom/images/fake.dcm",14,29,103)
create_series("SER_GG_VERTICAL",14,29,8)#104
create_file("./documents/dicom/images/fake.dcm",14,29,104)
create_file("./documents/dicom/images/fake.dcm",14,29,104)
create_file("./documents/dicom/images/fake.dcm",14,29,104)
create_file("./documents/dicom/images/fake.dcm",14,29,104)
create_file("./documents/dicom/images/fake.dcm",14,29,104)
create_file("./documents/dicom/images/fake.dcm",14,29,104)
create_file("./documents/dicom/images/fake.dcm",14,29,104)
create_file("./documents/dicom/images/fake.dcm",14,29,104)
create_file("./documents/dicom/images/fake.dcm",14,29,104)
create_file("./documents/dicom/images/fake.dcm",14,29,104)
create_series("SER_WEG_VERTICAL",14,29,9)#105
create_file("./documents/dicom/images/fake.dcm",14,29,105)
create_file("./documents/dicom/images/fake.dcm",14,29,105)
create_file("./documents/dicom/images/fake.dcm",14,29,105)
create_file("./documents/dicom/images/fake.dcm",14,29,105)
create_file("./documents/dicom/images/fake.dcm",14,29,105)
create_file("./documents/dicom/images/fake.dcm",14,29,105)
create_series("SER_QWR_CONTRAST_VERTICAL",14,29,10)#106
create_file("./documents/dicom/images/fake.dcm",14,29,106)
create_file("./documents/dicom/images/fake.dcm",14,29,106)
create_file("./documents/dicom/images/fake.dcm",14,29,106)
create_file("./documents/dicom/images/fake.dcm",14,29,106)
create_file("./documents/dicom/images/fake.dcm",14,29,106)
create_file("./documents/dicom/images/fake.dcm",14,29,106)
create_file("./documents/dicom/images/fake.dcm",14,29,106)
create_file("./documents/dicom/images/fake.dcm",14,29,106)
create_file("./documents/dicom/images/fake.dcm",14,29,106)
create_study("TRANSGDAREP",14)#30
create_series("SER_QWR_VERTICAL",14,30,11)#107
create_file("./documents/dicom/images/fake.dcm",14,30,107)
create_file("./documents/dicom/images/fake.dcm",14,30,107)
create_file("./documents/dicom/images/fake.dcm",14,30,107)
create_file("./documents/dicom/images/fake.dcm",14,30,107)
create_file("./documents/dicom/images/fake.dcm",14,30,107)
create_file("./documents/dicom/images/fake.dcm",14,30,107)
create_file("./documents/dicom/images/fake.dcm",14,30,107)
create_series("SER_GBFGG_W_VERTICAL",14,30,12)#108
create_file("./documents/dicom/images/fake.dcm",10,30,108)
create_file("./documents/dicom/images/fake.dcm",10,30,108)
create_file("./documents/dicom/images/fake.dcm",10,30,108)
create_file("./documents/dicom/images/fake.dcm",10,30,108)
create_file("./documents/dicom/images/fake.dcm",10,30,108)
create_file("./documents/dicom/images/fake.dcm",10,30,108)
create_file("./documents/dicom/images/fake.dcm",10,30,108)
create_series("SER_WWRG_W_VERTICAL",14,30,13)#109
create_file("./documents/dicom/images/fake.dcm",14,30,109)
create_file("./documents/dicom/images/fake.dcm",14,30,109)
create_file("./documents/dicom/images/fake.dcm",14,30,109)
create_file("./documents/dicom/images/fake.dcm",14,30,109)
create_file("./documents/dicom/images/fake.dcm",14,30,109)
create_file("./documents/dicom/images/fake.dcm",14,30,109)
create_file("./documents/dicom/images/fake.dcm",14,30,109)
create_series("SER_WWRG_VERTICAL",14,30,14)#110
create_file("./documents/dicom/images/fake.dcm",14,30,110)
create_file("./documents/dicom/images/fake.dcm",14,30,110)
create_file("./documents/dicom/images/fake.dcm",14,30,110)
create_file("./documents/dicom/images/fake.dcm",14,30,110)
create_file("./documents/dicom/images/fake.dcm",14,30,110)
create_file("./documents/dicom/images/fake.dcm",14,30,110)
create_file("./documents/dicom/images/fake.dcm",14,30,110)
create_file("./documents/dicom/images/fake.dcm",14,30,110)
create_series("QERFF_SER_VERTICAL",14,30,15)#111
create_file("./documents/dicom/images/fake.dcm",14,30,111)
create_file("./documents/dicom/images/fake.dcm",14,30,111)
create_file("./documents/dicom/images/fake.dcm",14,30,111)
create_file("./documents/dicom/images/fake.dcm",14,30,111)
create_file("./documents/dicom/images/fake.dcm",14,30,111)
create_file("./documents/dicom/images/fake.dcm",14,30,111)
create_file("./documents/dicom/images/fake.dcm",14,30,111)
create_series("QERFF_SER_CONTRAST_VERTICAL",14,30,16)#112
create_file("./documents/dicom/images/fake.dcm",14,30,112)
create_file("./documents/dicom/images/fake.dcm",14,30,112)
create_file("./documents/dicom/images/fake.dcm",14,30,112)
create_file("./documents/dicom/images/fake.dcm",14,30,112)
create_file("./documents/dicom/images/fake.dcm",14,30,112)
create_file("./documents/dicom/images/fake.dcm",14,30,112)
create_series("QWFV_SER_VERTICAL",14,30,17)#113
create_file("./documents/dicom/images/fake.dcm",14,30,113)
create_file("./documents/dicom/images/fake.dcm",14,30,113)
create_file("./documents/dicom/images/fake.dcm",14,30,113)
create_file("./documents/dicom/images/fake.dcm",14,30,113)
create_file("./documents/dicom/images/fake.dcm",14,30,113)
create_file("./documents/dicom/images/fake.dcm",14,30,113)
create_series("QWFV_SER_VERTICAL",14,30,18)#114
create_file("./documents/dicom/images/fake.dcm",14,30,114)
create_file("./documents/dicom/images/fake.dcm",14,30,114)
create_file("./documents/dicom/images/fake.dcm",14,30,114)
create_file("./documents/dicom/images/fake.dcm",14,30,114)
create_file("./documents/dicom/images/fake.dcm",14,30,114)
create_file("./documents/dicom/images/fake.dcm",14,30,114)
create_file("./documents/dicom/images/fake.dcm",14,30,114)
create_file("./documents/dicom/images/fake.dcm",14,30,114)
create_file("./documents/dicom/images/fake.dcm",14,30,114)

# import the python mysql client

import pymysql
from random import randrange

# Create a connection object to the MySQL Database Server

ipOfHost = "172.17.0.1"

dbUser = "root"

dbUserPassword = "angelo_lamonaca"

dbName = "dicom-viewer"

dbCharset = "utf8mb4"

cursorType = pymysql.cursors.DictCursor

databaseConnection = pymysql.connect(host=ipOfHost,

                                     user=dbUser,

                                     password=dbUserPassword,

                                     db=dbName,

                                     charset=dbCharset,

                                     cursorclass=cursorType,

                                     autocommit=True)

try:

    # Cursor object creation

    cursorObject = databaseConnection.cursor()
    for x in range(1, 689):
        updateStatement = "UPDATE `dicom-viewer`.Files t SET t.createdAt = '2021-" + str(randrange(1, 11)) + "-" \
                          + str(randrange(1, 28)) + " "+str(randrange(1, 23))+":"+str(randrange(0, 59))+":"+str(randrange(0, 59))+"' WHERE t.id = " + str(x)
        cursorObject.execute(updateStatement)
        updateStatement = "UPDATE `dicom-viewer`.Files t SET t.updatedAt = '2021-" + str(randrange(1, 11)) + "-" \
                          + str(randrange(1, 28)) + " "+str(randrange(1, 23))+":"+str(randrange(0, 59))+":"+str(randrange(0, 59))+"' WHERE t.id = " + str(x)
        cursorObject.execute(updateStatement)

    for x in range(1, 14):
        updateStatement = "UPDATE `dicom-viewer`.Patients t SET t.createdAt = '2021-" + str(randrange(1, 11)) + "-" \
                          + str(randrange(1, 28)) + " "+str(randrange(1, 23))+":"+str(randrange(0, 59))+":"+str(randrange(0, 59))+"' WHERE t.id = " + str(x)
        cursorObject.execute(updateStatement)
        updateStatement = "UPDATE `dicom-viewer`.Patients t SET t.updatedAt = '2021-" + str(randrange(1, 11)) + "-" \
                          + str(randrange(1, 28)) + " "+str(randrange(1, 23))+":"+str(randrange(0, 59))+":"+str(randrange(0, 59))+"' WHERE t.id = " + str(x)
        cursorObject.execute(updateStatement)

    for x in range(1, 30):
        updateStatement = "UPDATE `dicom-viewer`.Studies t SET t.createdAt = '2021-" + str(randrange(1, 11)) + "-" \
                          + str(randrange(1, 28)) + " "+str(randrange(1, 23))+":"+str(randrange(0, 59))+":"+str(randrange(0, 59))+"' WHERE t.id = " + str(x)
        cursorObject.execute(updateStatement)
        updateStatement = "UPDATE `dicom-viewer`.Studies t SET t.updatedAt = '2021-" + str(randrange(1, 11)) + "-" \
                          + str(randrange(1, 28)) + " "+str(randrange(1, 23))+":"+str(randrange(0, 59))+":"+str(randrange(0, 59))+"' WHERE t.id = " + str(x)
        cursorObject.execute(updateStatement)

    for x in range(1, 114):
        updateStatement = "UPDATE `dicom-viewer`.Series t SET t.createdAt = '2021-" + str(randrange(1, 11)) + "-" \
                          + str(randrange(1, 28)) + " "+str(randrange(1, 23))+":"+str(randrange(0, 59))+":"+str(randrange(0, 59))+"' WHERE t.id = " + str(x)
        cursorObject.execute(updateStatement)
        updateStatement = "UPDATE `dicom-viewer`.Series t SET t.updatedAt = '2021-" + str(randrange(1, 11)) + "-" \
                          + str(randrange(1, 28)) + " "+str(randrange(1, 23))+":"+str(randrange(0, 59))+":"+str(randrange(0, 59))+"' WHERE t.id = " + str(x)
        cursorObject.execute(updateStatement)


except Exception as e:

    print("Exeception occured:{}".format(e))



finally:

    databaseConnection.close()
