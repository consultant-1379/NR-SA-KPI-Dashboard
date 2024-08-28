from System.Collections.Generic import List, Dictionary
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data import RowSelection, IndexSet

if len(Document.Properties["KPIList"].split(';')) == 12:
	Document.Properties["SelectionWarning"] = "Your 12 KPIs have been selected. To change your selection, click the Clear button"
else:
	Document.Properties["SelectionWarning"] = ""

dict = {
	"${DRBAccsuccrte5qi}":"DRB Accessibility - Success Rate for mapped 5QI",
	"${Totdrbaccsucccrte5qi}":"Total DRB Accessibility - Success rate for Mapped 5QI",
	"${DRBretainactlost5qirrcinact}":"DRB Retainability - Percentage of Active Lost per mapped 5QI, RRC Inactive State",
	"${DRBretainactlost5qirrcinactgnodb}":"DRB Retainability - Percentage of Active Lost per mapped 5QI, RRC Inactive State, gNodeB triggered only",
	"${DRBretainactlost5qi}":"DRB Retainability - Percentage of Active Lost per mapped 5QI",
	"${DRBretainactlost5qignodb}":"DRB Retainability - Percentage of Active Lost per mapped 5QI, gNodeB triggered only",
	"${DRBretainsesstime5qilossrte}":"DRB Retainability - Session Time Normalized per mapped 5QI Loss Rate",
	"${DRBretainsesstime5qilossrtegnodb}":"DRB Retainability - Session Time Normalized per mapped 5QI Loss Rate, gNodeB triggered only",    
	"${NRsuccrtegnodb}":"NR Handover success rate captured in source gNodeB",
	"${NRexesuccrtegnodb}":"NR Handover Execution success rate captured in source gNodeB",
	"${NRtolteexesuccrtegnodb}":"NR-to-LTE Inter-RAT Handover Execution success rate captured in source gNodeB",
	"${NRtoltesuccrtegnodb}":"NR-to-LTE Inter-RAT Handover success rate captured in source gNodeB",    
	"${DLpktlossgnodbcuup}":"DL Packet Loss in gNodeB-CU-UP",
	"${Ransuccratgnb}":"Random Access Success Rate Captured in gNodeB",
	"${Avgdlmacthro}":"Average DL MAC DRB Throughput",
	"${Avgulmacthrough}":"Average UL MAC UE Throughput",
	"${NorAvgDLmactraff}":"Normalized Average DL MAC Cell Throughput considering traffic",
	"${NoravgulmacPUSCH}":"Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only",
	"${NorDlthroughputPDSCH}":"Normalized DL MAC Cell Throughput considering actual PDSCH slot only",
	"${NorulmacthroughPUSCH}":"Normalized UL MAC Cell Throughput considering actual PUSCH slot only",
	"${Avgdlmacdrbqosdrx}":"Average DL MAC DRB Latency per QoS covering DRX In-sync",
	"${Avgdlmacdrbnondrx}":"Average DL MAC DRB Latency per QoS covering non-DRX In-sync",
	"${AvgoverDLlatency}":"Average Overall DL Latency per QoS",
	"${DLmacdrbqos}":"DL MAC DRB Throughput per QoS",
	"${ULpktlosspdu}":"UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered",
	"${dlpktlossgnb}":"DL Packet Loss Captured in gNodeB",
	"${Parcellavailgnb}":"Partial Cell Availability for gNodeB Cell"
}

unitsDict = {
	"${DRBAccessibiltysuccratemap5qi}":"%",
	"${Totdrbaccsucccrte5qi}":"%",
	"${DRBretainactlost5qirrcinact}":"%",
	"${DRBretainactlost5qirrcinactgnodb}":"%",
    "${DRBRetainabilitypercentactivelostmap5qignodebtrigger}":"%",
	"${DRBRetainabilitypercentactivelostmap5qi}":"%",
	"${NRtoltesuccrtegnodb}":"%",
	"${NRtolteexesuccrtegnodb}":"%",
    "${NRsuccrtegnodb}":"%",
	"${NRexesuccrtegnodb}":"%",
	"${DRBretainactlost5qi}":"%",
	"${DRBretainactlost5qignodb}":"%",
	"${DRBretainsesstime5qilossrte}":"%",
	"${DRBretainsesstime5qilossrtegnodb}":"%",
	"${DRBAccsuccrte5qi}":"%",
	"${DLpktlossgnodbcuup}":"Ratio",
	"${Ransuccratgnb}":"%",
	"${Avgdlmacthro}":"Kbps",
	"${Avgulmacthrough}":"Kbps",
	"${NorAvgDLmactraff}":"Kbps",
	"${NoravgulmacPUSCH}":"Kbps",
	"${NorDlthroughputPDSCH}":"Kbps",
	"${NorulmacthroughPUSCH}":"Kbps",
	"${AvgoverDLlatency}":"Ms",
	"${Avgdlmacdrbnondrx}":"Ms",
	"${Avgdlmacdrbqosdrx}":"Ms",
	"${DLmacdrbqos}":"Kbps",
	"${ULpktlosspdu}":"Ratio",
	"${dlpktlossgnb}":"Ratio",
	"${Parcellavailgnb}":"%"
	
    
}

counter = 1

for item in Document.Properties["KPISelection"]:
		if item not in Document.Properties["KPIList"] and len(Document.Properties["KPIList"].split(';')) < 12:
			if Document.Properties["KPIList"] != '':
				Document.Properties["KPIList"] += ';' + item
			else:
				Document.Properties["KPIList"] = item



for item in Document.Properties["KPIList"].split(';'):
	if len(Document.Properties["KPIList"].split(';')) <= 12:
		Document.Properties["SelectedKPI"+str(counter)] = item
		#print Document.Properties["SelectedKPI"+str(counter)]
		Document.Properties["SelectedKPIName"+str(counter)] = dict[item]
		Document.Properties["Units"+str(counter)] = unitsDict[item]
		counter+=1




