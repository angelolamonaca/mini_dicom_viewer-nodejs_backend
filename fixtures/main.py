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


create_patient("HIPPOCRATES")
create_patient("PERGAMON_GALEN")
create_patient("IBN_SINA")
create_patient("ANDREA_VESALIO")
create_patient("RENÉ_LAËNNEC")
create_patient("EDWARD_JENNER")
create_patient("IGNAZ_SEMMELWEIS")
create_patient("SIR_JOSEPH_LISTER")
create_patient("JOHN_SNOW")
create_patient("SIGMUND_FREUD")
create_patient("SIR_WILLIAM_OSLER")
create_patient("ROBERT_KOCH")
create_patient("SIR_ALEXANDER_FLEMING")
create_patient("JONAS_SALK")
create_patient("JEAN_MARTIN_CHARCOT")

create_study("CT_ABDOMEN_W_V_CONTRAST", 1)
create_study("CT_ABDOMEN_W_WO_CONTRAST", 2)
create_study("CT_ABDOMEN_W_IV", 3)
create_study("CT_LEG", 4)
create_study("CT_ARM", 4)
create_study("CT_SHOULDER_DX", 6)
create_study("CT_SHOULDER_SX", 7)
create_study("CT_ABDOMEN_W_V_CONTRAST", 8)
create_study("CT_ABDOMEN_W_WO_CONTRAST", 9)
create_study("CT_ABDOMEN_W_IV", 10)
create_study("CT_LEG", 10)
create_study("CT_ARM", 11)
create_study("CT_SHOULDER_DX", 11)
create_study("CT_SHOULDER_SX", 12)
create_study("TRANSREP_NOSE", 1)
create_study("TRANSREP_MOUTH", 1)
create_study("TRANSREP_THEET", 2)
create_study("TRANSREP_AX", 3)
create_study("TRANSREP_PX", 6)
create_study("TRANSREP_FX", 6)
create_study("TRANSREP_GX", 7)
create_study("ABDOMEN_W", 8)
create_study("TRANSREP_W_AX", 9)
create_study("TRANSREP", 13)
create_study("AATRANSREP", 14)
create_study("TRDDDANSREP", 14)
create_study("TRANSGDAREP", 14)
create_study("TRA_DNSREP", 15)
create_study("TRA_AREP", 15)

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

create_series("SER_HORIZONTAL_AX", 1, 1, 1)
create_series("SER_HORIZONTAL_RF", 2, 2, 2)
create_series("SER_W_CONTRAST_HORIZONTAL", 3, 3, 3)
create_series("SER_RF_HORIZONTAL", 4, 4, 4)
create_series("SER_RF_W_HORIZONTAL", 4, 4, 5)
create_series("SER_RF_CONTRAST_HORIZONTAL", 4, 4, 6)
create_series("SER_DP_W_HORIZONTAL", 4, 5, 7)
create_series("SER_W_CONTRAST_HORIZONTAL", 6, 6, 8)
create_series("SER_W_W_HORIZONTAL", 6, 6, 9)
create_series("SER_W_HORIZONTAL", 6, 6, 10)
create_series("SER_F_W_HORIZONTAL", 7, 7, 11)
create_series("AWS_HORIZONTAL", 8, 8, 12)
create_series("FRS_W_CONTRAST_HORIZONTAL", 9, 9, 13)
create_series("VFB_W_HORIZONTAL", 10, 10, 14)
create_series("VFB_HORIZONTAL", 10, 10, 15)
create_series("RIGJ_W_HORIZONTAL", 10, 11, 16)
create_series("RIGJ_HORIZONTAL", 10, 11, 17)
create_series("SER", 11, 12, 1)
create_series("SERGG_HORIZONTAL", 11, 13, 2)
create_series("SERGG_CONTRAST_HORIZONTAL", 11, 13, 3)
create_series("SEWERR_HORIZONTAL", 12, 14, 4)
create_series("SEWERR_W_HORIZONTAL", 12, 14, 5)
create_series("SEWERR_HORIZONTAL", 12, 14, 6)
create_series("SEWERR_W_HORIZONTAL", 12, 14, 7)
create_series("SER_GG_VERTICAL", 1, 15, 8)
create_series("SER_WEG_VERTICAL", 1, 16, 9)
create_series("SER_QWR_CONTRAST_VERTICAL", 2, 17, 10)
create_series("SER_QWR_VERTICAL", 2, 17, 11)
create_series("SER_GBFGG_W_VERTICAL", 3, 18, 12)
create_series("SER_WWRG_W_VERTICAL", 6, 19, 13)
create_series("SER_WWRG_VERTICAL", 6, 19, 14)
create_series("QERFF_SER_VERTICAL", 6, 20, 15)
create_series("QERFF_SER_CONTRAST_VERTICAL", 6, 20, 16)
create_series("QWFV_SER_VERTICAL", 7, 21, 17)
create_series("QWFV_SER_VERTICAL", 7, 21, 18)
create_series("WQFV_RUCK_RIGHT", 8, 22, 1)
create_series("WQFV_RUCK_CONTRAST_RIGHT", 8, 22, 2)
create_series("RUCK_WFV_RIGHT", 9, 23, 3)
create_series("RUCK_WFV_CONTRAST_RIGHT", 9, 23, 4)
create_series("QWFV_RUCK_RIGHT", 13, 24, 5)
create_series("EWV_RUCK_RIGHT", 14, 25, 6)
create_series("QWEFV_RUCK_CONTRAST_RIGHT", 14, 26, 7)
create_series("QWRBD_RUCK_RIGHT", 14, 27, 8)
create_series("QWFVDSA_RUCK_CONTRAST_RIGHT", 15, 28, 9)
create_series("QWSAZG_RUCK_RIGHT", 15, 29, 10)

create_file("./documents/dicom/images/fake.dcm", 1, 1, 1)
create_file("./documents/dicom/images/fake.dcm", 2, 2, 2)
create_file("./documents/dicom/images/fake.dcm", 3, 3, 3)
create_file("./documents/dicom/images/fake.dcm", 4, 4, 4)
create_file("./documents/dicom/images/fake.dcm", 4, 4, 5)
create_file("./documents/dicom/images/fake.dcm", 4, 4, 6)
create_file("./documents/dicom/images/fake.dcm", 4, 5, 7)
create_file("./documents/dicom/images/fake.dcm", 6, 6, 8)
create_file("./documents/dicom/images/fake.dcm", 6, 6, 9)
create_file("./documents/dicom/images/fake.dcm", 6, 6, 10)
create_file("./documents/dicom/images/fake.dcm", 7, 7, 11)
create_file("./documents/dicom/images/fake.dcm", 8, 8, 12)
create_file("./documents/dicom/images/fake.dcm", 9, 9, 13)
create_file("./documents/dicom/images/fake.dcm", 10, 10, 14)
create_file("./documents/dicom/images/fake.dcm", 10, 10, 15)
create_file("./documents/dicom/images/fake.dcm", 10, 11, 16)
create_file("./documents/dicom/images/fake.dcm", 10, 11, 17)
create_file("./documents/dicom/images/fake.dcm", 11, 12, 18)
create_file("./documents/dicom/images/fake.dcm", 11, 13, 19)
create_file("./documents/dicom/images/fake.dcm", 11, 13, 20)
create_file("./documents/dicom/images/fake.dcm", 12, 14, 21)
create_file("./documents/dicom/images/fake.dcm", 12, 14, 22)
create_file("./documents/dicom/images/fake.dcm", 12, 14, 23)
create_file("./documents/dicom/images/fake.dcm", 12, 14, 24)
create_file("./documents/dicom/images/fake.dcm", 1, 15, 25)
create_file("./documents/dicom/images/fake.dcm", 1, 16, 26)
create_file("./documents/dicom/images/fake.dcm", 2, 17, 27)
create_file("./documents/dicom/images/fake.dcm", 2, 17, 28)
create_file("./documents/dicom/images/fake.dcm", 3, 18, 29)
create_file("./documents/dicom/images/fake.dcm", 6, 19, 30)
create_file("./documents/dicom/images/fake.dcm", 6, 19, 31)
create_file("./documents/dicom/images/fake.dcm", 6, 20, 32)
create_file("./documents/dicom/images/fake.dcm", 6, 20, 33)
create_file("./documents/dicom/images/fake.dcm", 7, 21, 34)
create_file("./documents/dicom/images/fake.dcm", 7, 21, 35)
create_file("./documents/dicom/images/fake.dcm", 8, 22, 36)
create_file("./documents/dicom/images/fake.dcm", 8, 22, 37)
create_file("./documents/dicom/images/fake.dcm", 9, 23, 38)
create_file("./documents/dicom/images/fake.dcm", 9, 23, 39)
create_file("./documents/dicom/images/fake.dcm", 13, 24, 40)
create_file("./documents/dicom/images/fake.dcm", 14, 25, 41)
create_file("./documents/dicom/images/fake.dcm", 14, 26, 42)
create_file("./documents/dicom/images/fake.dcm", 14, 27, 43)
create_file("./documents/dicom/images/fake.dcm", 15, 28, 44)
create_file("./documents/dicom/images/fake.dcm", 15, 29, 45)
