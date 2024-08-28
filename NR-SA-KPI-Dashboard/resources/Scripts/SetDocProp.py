from Spotfire.Dxp.Application.Visuals import *
from Spotfire.Dxp.Application.Visuals import HtmlTextArea



vis.As[HtmlTextArea]().HtmlContent += " "
#vis2.As[HtmlTextArea]().HtmlContent += " "


kpi = Document.Properties["AccessibilityKPIs"]

names = ["${DRBAccsuccrte5qi}", "${Totdrbaccsucccrte5qi}", "${DRBretainactlost5qirrcinact}", "${DRBretainactlost5qirrcinactgnodb}", "${DRBretainactlost5qi}", \
"${DRBretainactlost5qignodb}","${DRBretainsesstime5qilossrte}", "${DRBretainsesstime5qilossrtegnodb}","${NRsuccrtegnodb}", "${NRexesuccrtegnodb}", "${NRtolteexesuccrtegnodb}", "${NRtoltesuccrtegnodb}", \
"${DLpktlossgnodbcuup}","${Parcellavailgnb}","${Ransuccratgnb}","${Avgdlmacthro}","${Avgulmacthrough}","${NorAvgDLmactraff}","${NoravgulmacPUSCH}",\
"${NorDlthroughputPDSCH}","${NorulmacthroughPUSCH}","${ULpktlosspdu}","${dlpktlossgnb}","${Avgdlmacdrbqosdrx}","${Avgdlmacdrbnondrx}","${AvgoverDLlatency}","${DLmacdrbqos}"]      

realNames = ["DRB Accessibility - Success Rate for mapped 5QI","Total DRB Accessibility - Success rate for Mapped 5QI", \
"DRB Retainability - Percentage of Active Lost per mapped 5QI, RRC Inactive State", "DRB Retainability - Percentage of Active Lost per mapped 5QI, RRC Inactive State gNodeB triggered only", \
"DRB Retainability - Percentage of Active Lost per mapped 5QI", "DRB Retainability - Percentage of Active Lost per mapped 5QI, gNodeB triggered only", \
"DRB Retainability - Session Time Normalized per mapped 5QI Loss Rate", "DRB Retainability - Session Time Normalized per mapped 5QI Loss Rate, gNodeB triggered only",\
 "NR Handover success rate captured in source gNodeB", "NR Handover Execution success rate captured in source gNodeB",\
 "NR-to-LTE Inter-RAT Handover Execution success rate captured in source gNodeB", "NR-to-LTE Inter-RAT Handover success rate captured in source gNodeB",\
 "DL Packet Loss in gNodeB-CU-UP","Partial Cell Availability for gNodeB Cell","Random Access Success Rate Captured in gNodeB",\
 "Average DL MAC DRB Throughput","Average UL MAC UE Throughput","Normalized Average DL MAC Cell Throughput considering traffic",\
 "Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only","Normalized DL MAC Cell Throughput considering actual PDSCH slot only",\
 "Normalized UL MAC Cell Throughput considering actual PUSCH slot only","UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered","DL Packet Loss Captured in gNodeB",\
"Average DL MAC DRB Latency per QoS covering DRX In-sync","Average DL MAC DRB Latency per QoS covering non-DRX In-sync","Average Overall DL Latency per QoS","DL MAC DRB Throughput per QoS"]        

def getDataTable(tableName):
	try:
		return Document.Data.Tables[tableName]
	except:
		raise ("Error - cannot find data table: " + tableName)

for name in names:
	if kpi == name:
		Document.Properties["DisplayName"] = realNames[names.index(name)]

for page in Document.Pages:
	if page.Title == "KPI View - Node":
		for vis in page.Visuals:
			print vis.Title
			if "Selected" in vis.Title:
				vis = vis.As[Visualization]()
				if Document.Properties["DisplayName"] == "DL Packet Loss in gNodeB-CU-UP":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_EP_NGU_V_RAW")                    
					vis.HierarchyAxis.Expression = "<[NE_NAME]>"
				elif Document.Properties["DisplayName"] == "Random Access Success Rate Captured in gNodeB"\
				or Document.Properties["DisplayName"] == "Average UL MAC UE Throughput"\
                or Document.Properties["DisplayName"] == "Average DL MAC DRB Throughput"\
                or Document.Properties["DisplayName"] == "Normalized Average DL MAC Cell Throughput considering traffic"\
                or Document.Properties["DisplayName"] == "Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only"\
				or Document.Properties["DisplayName"] == "Normalized DL MAC Cell Throughput considering actual PDSCH slot only" or Document.Properties["DisplayName"] == "Partial Cell Availability for gNodeB Cell" or Document.Properties["DisplayName"] == "Normalized UL MAC Cell Throughput considering actual PUSCH slot only":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_RAW")                    
					vis.HierarchyAxis.Expression = "<[NR_NAME]>" 
				elif Document.Properties["DisplayName"] == "UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered"\
				or Document.Properties["DisplayName"] == "DL Packet Loss Captured in gNodeB":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_RPUSERPLANELINK_V_RAW")                    
					vis.HierarchyAxis.Expression = "<[NE_NAME]>"  
				elif Document.Properties["DisplayName"] == "Average Overall DL Latency per QoS"\
				or Document.Properties["DisplayName"] == "DL MAC DRB Throughput per QoS" or Document.Properties["DisplayName"] == "Average DL MAC DRB Latency per QoS covering non-DRX In-sync" or Document.Properties["DisplayName"] == "Average DL MAC DRB Latency per QoS covering DRX In-sync":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_V_RAW")                    
					vis.HierarchyAxis.Expression = "<[NR_NAME]>"                    
				else:
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLCU_RAW") 
					vis.HierarchyAxis.Expression = "<[NR_NAME]>"
			if "Up to 7 Days" in vis.Title:
				vis = vis.As[Visualization]()
				if Document.Properties["DisplayName"] == "DL Packet Loss in gNodeB-CU-UP":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_EP_NGU_V_RAW_DOD_Nodeview")                    
					#vis.XAxis.Reversed = True
					vis.ColorAxis.Expression = "<[NE_NAME]>"
					vis.Data.WhereClauseExpression = "[NE_NAME] is not null"
					vis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
				elif Document.Properties["DisplayName"] == "Random Access Success Rate Captured in gNodeB"\
				or Document.Properties["DisplayName"] == "Average UL MAC UE Throughput"\
                or Document.Properties["DisplayName"] == "Average DL MAC DRB Throughput"\
                or Document.Properties["DisplayName"] == "Normalized Average DL MAC Cell Throughput considering traffic"\
                or Document.Properties["DisplayName"] == "Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only"\
				or Document.Properties["DisplayName"] == "Normalized DL MAC Cell Throughput considering actual PDSCH slot only" or Document.Properties["DisplayName"] == "Partial Cell Availability for gNodeB Cell" or Document.Properties["DisplayName"] == "Normalized UL MAC Cell Throughput considering actual PUSCH slot only":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_RAW_DOD_nodeview")  
					vis.ColorAxis.Expression = "<[NR_NAME]>"
					vis.Data.WhereClauseExpression = "[NR_NAME] is not null"
					vis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
				elif Document.Properties["DisplayName"] == "UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered"\
				or Document.Properties["DisplayName"] == "DL Packet Loss Captured in gNodeB":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_RPUSERPLANELINK_V_RAW_DOD_nodeview")                    
					vis.ColorAxis.Expression = "<[NE_NAME]>"
					vis.Data.WhereClauseExpression = "[NE_NAME] is not null" 
					vis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
				elif Document.Properties["DisplayName"] == "Average Overall DL Latency per QoS"\
				or Document.Properties["DisplayName"] == "DL MAC DRB Throughput per QoS" or Document.Properties["DisplayName"] == "Average DL MAC DRB Latency per QoS covering non-DRX In-sync" or Document.Properties["DisplayName"] == "Average DL MAC DRB Latency per QoS covering DRX In-sync":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_V_RAW_DOD_nodeview")                    
					vis.ColorAxis.Expression = "<[NR_NAME]NEST[QOS]>"
					vis.Data.WhereClauseExpression = "[NR_NAME] is not null"   
					vis.Data.Filterings.Add(Document.Data.Filterings["Filtering scheme for QoS"]) #Add Filter                
				else:
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLCU_RAW_DOD_nodeview") 
					vis.ColorAxis.Expression = "<[NR_NAME]>"
					vis.Data.WhereClauseExpression = "[NR_NAME] is not null"
					vis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
	elif page.Title == "KPI View - Cell":
		for vis in page.Visuals:
			if "Cell View" in vis.Title:
				vis = vis.As[Visualization]()
				if Document.Properties["DisplayName"] == "DL Packet Loss in gNodeB-CU-UP":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_EP_NGU_V_RAW_DOD_Nodeview")                    
					vis.HierarchyAxis.Expression = "<[EP_NgU]>"
				elif Document.Properties["DisplayName"] == "Random Access Success Rate Captured in gNodeB"\
				or Document.Properties["DisplayName"] == "Average UL MAC UE Throughput"\
                or Document.Properties["DisplayName"] == "Average DL MAC DRB Throughput"\
                or Document.Properties["DisplayName"] == "Normalized Average DL MAC Cell Throughput considering traffic"\
                or Document.Properties["DisplayName"] == "Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only"\
				or Document.Properties["DisplayName"] == "Normalized DL MAC Cell Throughput considering actual PDSCH slot only" or Document.Properties["DisplayName"] == "Partial Cell Availability for gNodeB Cell" or Document.Properties["DisplayName"] == "Normalized UL MAC Cell Throughput considering actual PUSCH slot only":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_RAW_DOD_nodeview")  
					vis.HierarchyAxis.Expression = "<[NRCellDU]>"  
				elif Document.Properties["DisplayName"] == "UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered"\
				or Document.Properties["DisplayName"] == "DL Packet Loss Captured in gNodeB":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_RPUSERPLANELINK_V_RAW_DOD_nodeview")                    
					vis.HierarchyAxis.Expression = "<[RP_USER_PLANE_LINK]>"   
				elif Document.Properties["DisplayName"] == "Average Overall DL Latency per QoS"\
				or Document.Properties["DisplayName"] == "DL MAC DRB Throughput per QoS" or Document.Properties["DisplayName"] == "Average DL MAC DRB Latency per QoS covering non-DRX In-sync" or Document.Properties["DisplayName"] == "Average DL MAC DRB Latency per QoS covering DRX In-sync":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_V_RAW_DOD_nodeview")                    
					vis.HierarchyAxis.Expression = "<[NRCellDU]>"              
				else:
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLCU_RAW_DOD_nodeview") 
					vis.HierarchyAxis.Expression = "<[NRCellCU]>"
			elif "Up to 7 Days" in vis.Title:
				vis = vis.As[Visualization]()
				if Document.Properties["DisplayName"] == "DL Packet Loss in gNodeB-CU-UP":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_EP_NGU_V_RAW_DOD_Nodeview")                    
					vis.ColorAxis.Expression = "<[EP_NgU]>"
					vis.Data.WhereClauseExpression = "[NE_NAME] is not null"
					vis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
				elif Document.Properties["DisplayName"] == "Random Access Success Rate Captured in gNodeB"\
				or Document.Properties["DisplayName"] == "Average UL MAC UE Throughput"\
                or Document.Properties["DisplayName"] == "Average DL MAC DRB Throughput"\
                or Document.Properties["DisplayName"] == "Normalized Average DL MAC Cell Throughput considering traffic"\
                or Document.Properties["DisplayName"] == "Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only"\
				or Document.Properties["DisplayName"] == "Normalized DL MAC Cell Throughput considering actual PDSCH slot only" or Document.Properties["DisplayName"] == "Partial Cell Availability for gNodeB Cell" or Document.Properties["DisplayName"] == "Normalized UL MAC Cell Throughput considering actual PUSCH slot only":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_RAW_DOD_nodeview")  
					vis.ColorAxis.Expression = "<[NRCellDU]>"
					vis.Data.WhereClauseExpression = "[NR_NAME] is not null" 
					vis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
				elif Document.Properties["DisplayName"] == "UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered"\
				or Document.Properties["DisplayName"] == "DL Packet Loss Captured in gNodeB":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_RPUSERPLANELINK_V_RAW_DOD_nodeview")                    
					vis.ColorAxis.Expression = "<[RP_USER_PLANE_LINK]>"
					vis.Data.WhereClauseExpression = "[NE_NAME] is not null" 
					vis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
				elif Document.Properties["DisplayName"] == "Average Overall DL Latency per QoS"\
				or Document.Properties["DisplayName"] == "DL MAC DRB Throughput per QoS" or Document.Properties["DisplayName"] == "Average DL MAC DRB Latency per QoS covering non-DRX In-sync" or Document.Properties["DisplayName"] == "Average DL MAC DRB Latency per QoS covering DRX In-sync":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_V_RAW_DOD_nodeview")                    
					vis.ColorAxis.Expression = "<[NRCellDU]NEST[QOS]>"
					vis.Data.WhereClauseExpression = "[NR_NAME] is not null"   
					vis.Data.Filterings.Add(Document.Data.Filterings["Filtering scheme for QoS"]) #Add Filter                 
				else:
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLCU_RAW_DOD_nodeview") 
					vis.ColorAxis.Expression = "<[NRCellCU]>"
					vis.Data.WhereClauseExpression = "[NR_NAME] is not null"
					vis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
if kpi == "${DLmacdrbqos}" or kpi == "${NorulmacthroughPUSCH}" or kpi == "${NorDlthroughputPDSCH}" or kpi == "${NoravgulmacPUSCH}" or kpi == "${NorAvgDLmactraff}"\
or kpi == "${Avgulmacthrough}" or kpi == "${Avgdlmacthro}":
	Document.Properties["Units"] = "kbps"
elif kpi == "${ULpktlosspdu}" or kpi == "${dlpktlossgnb}" or kpi == "${DLpktlossgnodbcuup}" :
	Document.Properties["Units"] = "Ratio"
elif kpi == "${Avgdlmacdrbnondrx}" or kpi == "${Avgdlmacdrbqosdrx}" or kpi == "${AvgoverDLlatency}":
	Document.Properties["Units"] = "ms"
elif kpi == "${DRBretainsesstime5qilossrte}" or kpi == "${DRBretainsesstime5qilossrtegnodb}":
	Document.Properties["Units"] = "1/s"
else:
	Document.Properties["Units"] = "%"
	'''elif page.Title == "Filtered Data - Node view":
		for vis in page.Visuals:
			print vis.Title
			if "Raw Filtered Data" in vis.Title:
				vis = vis.As[Visualization]()
				if Document.Properties["DisplayName"] == "DL Packet Loss in gNodeB-CU-UP":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_EP_NGU_V_RAW_DOD_Nodeview")                    
				else:
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLCU_RAW_DOD_nodeview")'''