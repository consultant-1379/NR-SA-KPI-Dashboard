from Spotfire.Dxp.Application.Visuals import *
import re
from System import DateTime

myVis = myVis.As[Visualization]()
dataTable = myVis.Data.DataTableReference
myVis.TableColumns.Clear()
activeVisual = Document.ActivePageReference.ActiveVisualReference
def getDataTable(tableName):
	try:
		return Document.Data.Tables[tableName]
	except:
		raise ("Error - cannot find data table: " + tableName)

try:
    print Document.Properties["SelectedKPI"+str(activeVisual.Title)]
    Document.Properties["DetailsKPI"] = Document.Properties["SelectedKPI"+str(activeVisual.Title)]
    Document.Properties["DetailsKPI2"] = Document.Properties["SelectedKPI"+str(activeVisual.Title)]
    Document.Properties["DetailsDisplayName"] = Document.Properties["SelectedKPIName"+str(activeVisual.Title)]
    Document.Properties["UnitsSelected"] = Document.Properties["Units"+str(activeVisual.Title)]
    print Document.Properties["UnitsSelected"]

    kpiFormula = Document.Properties[Document.Properties["SelectedKPI"+str(activeVisual.Title)][2:-1]]
    print kpiFormula
    columnName = re.findall(r'\[([^[]+)\]', kpiFormula)
    columnName = list(set(columnName))
    print columnName

    #myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])
    #myVis.TableColumns.Add(dataTable.Columns.Item["KPI Value"])
    print "mk"
    if Document.Properties["DetailsDisplayName"] == "DL Packet Loss in gNodeB-CU-UP":
        print "38"
        myVis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_EP_NGU_V_RAW_DOD")
        dataTable = myVis.Data.DataTableReference
        myVis.TableColumns.Clear()
        myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])
        myVis.TableColumns.Add(dataTable.Columns.Item["NE_NAME"])
        myVis.TableColumns.Add(dataTable.Columns.Item["EP_NgU"]) 
        myVis.TableColumns.Add(dataTable.Columns.Item["KPI Value"])
        print "42"  
    elif Document.Properties["DetailsDisplayName"] == "Random Access Success Rate Captured in gNodeB"\
    or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Throughput" \
    or Document.Properties["DetailsDisplayName"] == "Average UL MAC UE Throughput" \
    or Document.Properties["DetailsDisplayName"] == "Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only" \
    or Document.Properties["DetailsDisplayName"] == "Normalized DL MAC Cell Throughput considering actual PDSCH slot only" \
    or Document.Properties["DetailsDisplayName"] == "Normalized UL MAC Cell Throughput considering actual PUSCH slot only" \
    or Document.Properties["DetailsDisplayName"] == "Partial Cell Availability for gNodeB Cell" \
    or Document.Properties["DetailsDisplayName"] == "Normalized Average DL MAC Cell Throughput considering traffic":
        print "39"
        myVis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_RAW_DOD")
        dataTable = myVis.Data.DataTableReference
        myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])
        myVis.TableColumns.Add(dataTable.Columns.Item["NR_NAME"])
        myVis.TableColumns.Add(dataTable.Columns.Item["NRCellDU"]) 
        myVis.TableColumns.Add(dataTable.Columns.Item["KPI Value"])
        print "42" 
    elif Document.Properties["DetailsDisplayName"] == "Average Overall DL Latency per QoS"\
    or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Latency per QoS covering DRX In-sync" \
    or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Latency per QoS covering non-DRX In-sync" \
    or Document.Properties["DetailsDisplayName"] == "DL MAC DRB Throughput per QoS":
        print "39"
        myVis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_V_RAW_DOD")
        dataTable = myVis.Data.DataTableReference
        myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])
        myVis.TableColumns.Add(dataTable.Columns.Item["NR_NAME"])
        myVis.TableColumns.Add(dataTable.Columns.Item["NRCellDU"]) 
        myVis.TableColumns.Add(dataTable.Columns.Item["QOS"])
        myVis.TableColumns.Add(dataTable.Columns.Item["KPI Value"])
        print "42" 
    elif Document.Properties["DetailsDisplayName"] == "DL Packet Loss Captured in gNodeB"\
    or Document.Properties["DetailsDisplayName"] == "UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered":
        print "39"
        myVis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_RPUSERPLANELINK_V_RAW_DOD")
        dataTable = myVis.Data.DataTableReference
        myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])
        myVis.TableColumns.Add(dataTable.Columns.Item["NE_NAME"])
        myVis.TableColumns.Add(dataTable.Columns.Item["RP_USER_PLANE_LINK"]) 
        myVis.TableColumns.Add(dataTable.Columns.Item["KPI Value"])
        print "42"     
    else:
        print "43"
        myVis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLCU_RAW_DOD")
        dataTable = myVis.Data.DataTableReference    
        myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])    
        myVis.TableColumns.Add(dataTable.Columns.Item["NR_NAME"]) 
        myVis.TableColumns.Add(dataTable.Columns.Item["NRCellCU"])
        myVis.TableColumns.Add(dataTable.Columns.Item["KPI Value"])
        print "48"
    print "49"
    for item in columnName:
        if item != "DATETIME_ID":
            myVis.TableColumns.Add(dataTable.Columns.Item[item])
    print "53"
    Document.ActivePageReference = Document.Pages[3]
except KeyError:
	print "Value Error - No KPI selected"
except ValueError:
	print "Can't set KPI document property"



for page in Document.Pages:
	if page.Title == "KPI Details":
		for vis in page.Visuals:
			print vis.Title
			if "Worst Performing Cells (Latest ROP)" in vis.Title:
				vis = vis.As[Visualization]()
				Rules = vis.TryGetFilterRules()
				if Document.Properties["DetailsDisplayName"] ==  "DL Packet Loss in gNodeB-CU-UP":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_EP_NGU_V_RAW") 
					vis.XAxis.Expression = "<[EP_NgU] NEST [NE_NAME]>" 
				elif Document.Properties["DetailsDisplayName"] == "Random Access Success Rate Captured in gNodeB"\
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Throughput" \
				or Document.Properties["DetailsDisplayName"] == "Average UL MAC UE Throughput" \
				or Document.Properties["DetailsDisplayName"] == "Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only" \
				or Document.Properties["DetailsDisplayName"] == "Normalized DL MAC Cell Throughput considering actual PDSCH slot only" \
				or Document.Properties["DetailsDisplayName"] == "Normalized UL MAC Cell Throughput considering actual PUSCH slot only" \
				or Document.Properties["DetailsDisplayName"] == "Partial Cell Availability for gNodeB Cell" \
				or Document.Properties["DetailsDisplayName"] == "Normalized Average DL MAC Cell Throughput considering traffic":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_RAW") 
					vis.XAxis.Expression = "<[NRCellDU] NEST [NR_NAME]>"  
				elif Document.Properties["DetailsDisplayName"] == "Average Overall DL Latency per QoS"\
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Latency per QoS covering DRX In-sync" \
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Latency per QoS covering non-DRX In-sync" \
				or Document.Properties["DetailsDisplayName"] == "DL MAC DRB Throughput per QoS":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_V_RAW") 
					vis.XAxis.Expression = "<[NRCellDU] NEST [NR_NAME]>" 
				elif Document.Properties["DetailsDisplayName"] == "DL Packet Loss Captured in gNodeB"\
				or Document.Properties["DetailsDisplayName"] == "UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered":  
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_RPUSERPLANELINK_V_RAW") 
					vis.XAxis.Expression = "<[RP_USER_PLANE_LINK] NEST [NE_NAME]>"                 
				else:
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLCU_RAW")
					vis.XAxis.Expression = "<[NRCellCU] NEST [NR_NAME]>"
			if "Up to 7 Days" in vis.Title:
				#print vis.Title
				vis = vis.As[Visualization]()
				if Document.Properties["DetailsDisplayName"] ==  "DL Packet Loss in gNodeB-CU-UP":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_EP_NGU_V_RAW_DOD")
					vis.ColorAxis.Expression = "<[EP_NgU]>"  
				elif Document.Properties["DetailsDisplayName"] == "Random Access Success Rate Captured in gNodeB"\
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Throughput" \
				or Document.Properties["DetailsDisplayName"] == "Average UL MAC UE Throughput" \
				or Document.Properties["DetailsDisplayName"] == "Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only" \
				or Document.Properties["DetailsDisplayName"] == "Normalized DL MAC Cell Throughput considering actual PDSCH slot only" \
				or Document.Properties["DetailsDisplayName"] == "Normalized UL MAC Cell Throughput considering actual PUSCH slot only" \
				or Document.Properties["DetailsDisplayName"] == "Partial Cell Availability for gNodeB Cell" \
				or Document.Properties["DetailsDisplayName"] == "Normalized Average DL MAC Cell Throughput considering traffic":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_RAW_DOD")
					vis.ColorAxis.Expression = "<[NRCellDU]>"  
				elif Document.Properties["DetailsDisplayName"] == "Average Overall DL Latency per QoS"\
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Latency per QoS covering DRX In-sync" \
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Latency per QoS covering non-DRX In-sync" \
				or Document.Properties["DetailsDisplayName"] == "DL MAC DRB Throughput per QoS":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_V_RAW_DOD")
					vis.ColorAxis.Expression = "<[NRCellDU]NEST[QOS]>" 
				elif Document.Properties["DetailsDisplayName"] == "DL Packet Loss Captured in gNodeB"\
				or Document.Properties["DetailsDisplayName"] == "UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_RPUSERPLANELINK_V_RAW_DOD") 
					vis.ColorAxis.Expression = "<[RP_USER_PLANE_LINK]>"                  
				else:
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLCU_RAW_DOD")
					vis.ColorAxis.Expression = "<[NRCellCU]>"

			'''if "Network View (Up to  7 Days)" in vis.Title:
				#print vis.Title
				vis = vis.As[Visualization]()
				if Document.Properties["DetailsDisplayName"] ==  "DL Packet Loss in gNodeB-CU-UP":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_EP_NGU_V_RAW_NW")
					#vis.ColorAxis.Expression = "<[EP_NgU]>"  
				elif Document.Properties["DetailsDisplayName"] == "Random Access Success Rate Captured in gNodeB"\
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Throughput" \
				or Document.Properties["DetailsDisplayName"] == "Average UL MAC UE Throughput" \
				or Document.Properties["DetailsDisplayName"] == "Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only" \
				or Document.Properties["DetailsDisplayName"] == "Normalized DL MAC Cell Throughput considering actual PDSCH slot only" \
				or Document.Properties["DetailsDisplayName"] == "Normalized UL MAC Cell Throughput considering actual PUSCH slot only" \
				or Document.Properties["DetailsDisplayName"] == "Partial Cell Availability for gNodeB Cell" \
				or Document.Properties["DetailsDisplayName"] == "Normalized Average DL MAC Cell Throughput considering traffic":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_RAW_NW")
					#vis.ColorAxis.Expression = "<[EP_NgU]>"                    
				elif Document.Properties["DetailsDisplayName"] == "Average Overall DL Latency per QoS"\
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Latency per QoS covering DRX In-sync" \
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Latency per QoS covering non-DRX In-sync" \
				or Document.Properties["DetailsDisplayName"] == "DL MAC DRB Throughput per QoS":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_V_RAW_NW")
				elif Document.Properties["DetailsDisplayName"] == "DL Packet Loss Captured in gNodeB"\
				or Document.Properties["DetailsDisplayName"] == "UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered":
					vis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_RPUSERPLANELINK_V_RAW_NW")
				else:
					vis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLCU_RAW_NW")
					#vis.ColorAxis.Expression = "<[NRCellCU]>"'''

#Document.Properties["triggerscript"] = DateTime.UtcNow
Document.Properties["triggerscript"] = DateTime.Now