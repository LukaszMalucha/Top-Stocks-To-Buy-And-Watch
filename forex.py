import yfinance as yf
import pandas as pd


def insert_column_value_from_dictionary(dictionary, string):
    """Helper function that unpacks metadata dict to columns"""
    for key, value in dictionary.items():
        if key == string:
            return value
        
        
def add_column_for_key(dataset, keys):
    """Helper funciton that creates column for each key"""
    for key in keys:
        dataset[key] = ""
    return dataset        
        


column_list = ['payoutRatio','trailingAnnualDividendRate','dividendRate','exDividendDate',
               'beta','trailingPE','priceToSalesTrailing12Months','forwardPE',
               'dividendYield','enterpriseToRevenue','profitMargins','enterpriseToEbitda',
               'forwardEps','trailingEps','priceToBook','enterpriseValue','earningsQuarterlyGrowth',
               'pegRatio', 'longName', 'symbol']


ratio_columns = ['dividendRate','trailingPE','forwardPE','dividendYield','enterpriseToRevenue','enterpriseToEbitda',
               'forwardEps','trailingEps','pegRatio', 'longName', 'symbol']


dataset = pd.DataFrame(columns=column_list)


string = "AAXN,AIR,AIRI,AJRD,AOBC,ASTC,ATRO,AVAV,BA,CODA,CUB,CVU,CW,DCO,ERJ,ESE,ESLT,FLIR,GD,GE,HEI,HEI.A,HII,HXL,ISSC,KAMN,KTOS,KVHI,LHX,LMT,MAGS,MAXR,MOG.A,MOG.B,MSI,NOC,PKE,RADA,RTX,SIF,SPCE,SPR,SSTI,TATT,TDG,TDY,TGI,TXT,UAVS"
stocks = string.split(",")



for stock in stocks:
    try:
        info = yf.Ticker(stock).info
        dataset = dataset.append(info, ignore_index=True )  
    except:
        pass




aerospace_and_defense = ['AAXN', 'AIR', 'AIRI', 'AJRD', 'AOBC', 'ASTC', 'ATRO', 'AVAV', 'BA', 'CODA', 'CUB', 'CVU', 'CW', 'DCO', 'ERJ', 'ESE', 'ESLT', 'FLIR', 'GD', 'GE', 'HEI', 'HEI.A', 'HII', 'HXL', 'ISSC', 'KAMN', 'KTOS', 'KVHI', 'LHX', 'LMT', 'MAGS', 'MAXR', 'MOG.A', 'MOG.B', 'MSI', 'NOC', 'PKE', 'RADA', 'RTX', 'SIF', 'SPCE', 'SPR', 'SSTI', 'TATT', 'TDG', 'TDY', 'TGI', 'TXT', 'UAVS']
airlines = ['AAL', 'ALGT', 'ALK', 'ATSG', 'AZUL', 'CEA', 'CPA', 'DAL', 'GOL', 'HA', 'JBLU', 'LTM', 'LUV', 'MESA', 'RYAAY', 'SAVE', 'SKYW', 'UAL', 'VLRS', 'ZNH']
telecom_equipment = ['AAPL', 'ADTN', 'AIRG', 'AKTS', 'APWC', 'AUDC', 'AVNW', 'AVYA', 'BDR', 'BKTI', 'CALX', 'CAMP', 'CASA', 'CIEN', 'CLFD', 'CLRO', 'CMBM', 'CMTL', 'COMM', 'CRNT', 'DGLY', 'DZSI', 'ERIC', 'EXFO', 'GILT', 'GRMN', 'HLIT', 'IDCC', 'INFN', 'INSG', 'ITRN', 'JCS', 'NOK', 'OCC', 'PLT', 'PWFL', 'QCOM', 'RBBN', 'SATS', 'SONM', 'SWIR', 'TCCO', 'TESS', 'UI', 'UTSI', 'VISL', 'VOXX', 'VSAT', 'WATT', 'WSTL', 'WTT']
movies_ent = ['ACEL', 'AMC', 'BATRA', 'BATRK', 'BTN', 'BWL.A', 'CNK', 'CSSE', 'DIS', 'DLB', 'DLPN', 'DS', 'DVD', 'EROS', 'FUN', 'FWONA', 'FWONK', 'GMBL', 'GNUS', 'IMAX', 'LGF.A', 'LGF.B', 'LSXMA', 'LSXMB', 'LSXMK', 'LYV', 'MANU', 'MCS', 'MSGE', 'MSGN', 'MSGS', 'PLAY', 'RICK', 'SEAS', 'SIX', 'WSG', 'WWE']
major_banks = ['ALRS', 'AMNB', 'AMTB', 'AMTBB', 'AROW', 'AVAL', 'BAC', 'BBD', 'BBDO', 'BBVA', 'BCS', 'BK', 'BMO', 'BNS', 'CADE', 'CASH', 'CBNK', 'CBTX', 'CHCO', 'CIT', 'CM', 'CMA', 'COF', 'CS', 'DB', 'ESQ', 'FBK', 'FBMS', 'FNLC', 'HOPE', 'HSBC', 'HSBC/PA', 'ITUB', 'JPM', 'KEY', 'LARK', 'LYG', 'MCB', 'MFG', 'MUFG', 'NKSH', 'OFG', 'OPOF', 'PBCT', 'PEBO', 'PNC', 'PRK', 'RBS', 'RF', 'RMBI', 'RY', 'SAN', 'SFNC', 'SMFG', 'SUPV', 'TCF', 'TD', 'THFF', 'UBS', 'USB', 'WBK', 'WF', 'WFC', 'ZIONL']
packaged_software = ['ACIW', 'ADBE', 'ADSK', 'AGYS', 'ALTR', 'AMSWA', 'ANSS', 'APPN', 'ASUR', 'AVID', 'AVLR', 'AYX', 'AZPN', 'BB', 'BILL', 'BKI', 'BL', 'BLKB', 'BNFT', 'BSQR', 'CANG', 'CDNS', 'CHNG', 'CHNGU', 'CLDR', 'CMCM', 'COUP', 'CREX', 'CRM', 'CRNC', 'CRWD', 'CSOD', 'CTK', 'CTXS', 'CVET', 'CVLT', 'CYBR', 'DAO', 'DDOG', 'DOCU', 'DOMO', 'DOYU', 'DT', 'EB', 'ECOM', 'EGHT', 'EH', 'ENV', 'EPAY', 'ESTC', 'EVBG', 'FICO', 'FNJN', 'GAN', 'GEC', 'GSB', 'GSUM', 'GTYH', 'HCAT', 'HSTM', 'HUYA', 'ICAD', 'IIIV', 'INS', 'INSE', 'INTU', 'IO', 'IZEA', 'LAIX', 'LIZI', 'LKCO', 'LN', 'LVGO', 'LYFT', 'MANH', 'MANT', 'MDB', 'MDLA', 'MFGP', 'MGIC', 'MIME', 'MSFT', 'MTLS', 'MWK', 'NATI', 'NCTY', 'NLOK', 'NTNX', 'NUAN', 'NVEC', 'OKTA', 'OPRA', 'ORCL', 'OTEX', 'PAYC', 'PBTS', 'PCTY', 'PD', 'PHR', 'PHUN', 'PING', 'PLAN', 'PRGS', 'PRSP', 'PT', 'PTC', 'QLYS', 'RDCM', 'RDVT', 'RMNI', 'RNG', 'RNWK', 'SABR', 'SAIL', 'SAP', 'SCPL', 'SCWX', 'SDGR', 'SGLB', 'SLP', 'SMAR', 'SMSI', 'SNPS', 'SPNS', 'SPRT', 'SPSC', 'SPT', 'STNE', 'SWI', 'TEAM', 'TENB', 'TIVO', 'TKAT', 'TLND', 'TWLO', 'TWOU', 'UBER', 'UEPS', 'UPWK', 'VEEV', 'VERI', 'WIMI', 'WORK', 'XAIR', 'YVR', 'ZDGE', 'ZM', 'ZS', 'ZUO']
major_telecom = ['ALSK', 'ATNI', 'AWRE', 'BCE', 'CHA', 'CHT', 'CHU', 'CNSL', 'KT', 'OIBR.C', 'ORAN', 'SHEN', 'T', 'TEO', 'TEUM', 'TLK', 'TU', 'VIV', 'VZ']
integrated_oil = ['AMPY', 'AXAS', 'BP', 'CNX', 'COG', 'CVX', 'E', 'EC', 'EQNR', 'ESTE', 'FLMN', 'GDP', 'HESM', 'IMO', 'INDO', 'NFG', 'PBR', 'PBR.A', 'PRT', 'PTR', 'PVL', 'RDS.A', 'RDS.B', 'SNDE', 'SNMP', 'SNP', 'SU', 'TALO', 'TELL', 'TOT', 'VNOM', 'XOM', 'YPF']
internet_retail = ['AMZN', 'APRN', 'BABA', 'CHWY', 'DLTH', 'FLWS', 'IMBI', 'JD', 'LE', 'LITB', 'LIVE', 'OSTK', 'PDD', 'PRTS', 'QRTEA', 'QRTEB', 'QVCD', 'REAL', 'RVLV', 'SHOP', 'SYX', 'TC', 'VIPS', 'W', 'WTRH', 'YGYI']
telecom_equipment = ['AAPL', 'ADTN', 'AIRG', 'AKTS', 'APWC', 'AUDC', 'AVNW', 'AVYA', 'BDR', 'BKTI', 'CALX', 'CAMP', 'CASA', 'CIEN', 'CLFD', 'CLRO', 'CMBM', 'CMTL', 'COMM', 'CRNT', 'DGLY', 'DZSI', 'ERIC', 'EXFO', 'GILT', 'GRMN', 'HLIT', 'IDCC', 'INFN', 'INSG', 'ITRN', 'JCS', 'NOK', 'OCC', 'PLT', 'PWFL', 'QCOM', 'RBBN', 'SATS', 'SONM', 'SWIR', 'TCCO', 'TESS', 'UI', 'UTSI', 'VISL', 'VOXX', 'VSAT', 'WATT', 'WSTL', 'WTT']
motor_vehicles = ['F', 'FCAU', 'FUV', 'GM', 'HMC', 'HOG', 'KNDI', 'NIO', 'NIU', 'RACE', 'REVG', 'SOLO', 'TM', 'TSLA', 'TTM']
internet_software = ['AEYE', 'AKAM', 'ANGI', 'APPS', 'ARCE', 'ATHM', 'BCOV', 'BIDU', 'BILI', 'BITA', 'CARG', 'CARS', 'CDLX', 'CHKP', 'CIH', 'COE', 'CRTO', 'CSGP', 'CYRN', 'DHX', 'DKNG', 'DNK', 'DUO', 'EGAN', 'EGOV', 'EVER', 'FB', 'FTCH', 'FUTU', 'GDDY', 'GLUU', 'GOOG', 'GOOGL', 'GSX', 'HHR', 'IAC', 'IQ', 'JCOM', 'JFU', 'JG', 'JMIA', 'JOBS', 'JRJC', 'KRKR', 'LEAF', 'LLNW', 'LMPX', 'LOGM', 'LPSN', 'MCHX', 'MEET', 'MELI', 'MKD', 'MSTR', 'MTCH', 'MYSZ', 'NETE', 'NTES', 'PERI', 'PFSW', 'PINS', 'QD', 'QTT', 'RENN', 'SE', 'SFUN', 'SHSP', 'SIFY', 'SINA', 'SNAP', 'SNCR', 'SOGO', 'SOHU', 'SPOT', 'SSTK', 'SY', 'TCX', 'TME', 'TRUE', 'TRVG', 'TTGT', 'TW', 'TWTR', 'UXIN', 'VALU', 'VHC', 'VNET', 'VRSN', 'WB', 'WBAI', 'WEI', 'WUBA', 'XNET', 'XP', 'XRF', 'YELP', 'YNDX', 'YRD', 'YY', 'ZNGA']
precious_metals = ['AAU', 'AEM', 'AG', 'AGI', 'ALO', 'ASM', 'AU', 'AUMN', 'AUY', 'BTG', 'BVN', 'CDE', 'DRD', 'EGO', 'EMX', 'EXK', 'FNV', 'FSM', 'GAU', 'GFI', 'GOLD', 'GORO', 'GPL', 'GSS', 'HL', 'HMY', 'IAG', 'KGC', 'KL', 'MAG', 'MUX', 'NEM', 'NG', 'NGD', 'OR', 'PAAS', 'PLG', 'PVG', 'RGLD', 'SA', 'SAND', 'SBSW', 'SILV', 'SMTS', 'SSRM', 'SVM', 'TGB', 'THM', 'TRX', 'USAU', 'VGZ', 'WPM']













yf.Ticker("MSFT").info






    
    
  
  