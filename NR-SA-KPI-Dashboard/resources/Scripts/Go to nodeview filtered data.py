from Spotfire.Dxp.Application.Visuals import *
import re

myVis = myVis.As[Visualization]()
myVis.TableColumns.Clear()

def getDataTable(tableName):
	try:
		return Document.Data.Tables[tableName]
	except:
		raise ("Error - cannot find data table: " + tableName)

try:
	kpiFormula = Document.Properties[Document.Properties["AccessibilityKPIs"][2:-1]]	
	columnName = re.findall(r'\[([^[]+)\]', kpiFormula)
	columnName = list(set(columnName))
	if Document.Properties["DisplayName"] == "DL Packet Loss in gNodeB-CU-UP":
		myVis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_EP_NGU_V_RAW_DOD_Nodeview")
		dataTable = myVis.Data.DataTableReference
		myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])
		myVis.TableColumns.Add(dataTable.Columns.Item["NE_NAME"])
		myVis.TableColumns.Add(dataTable.Columns.Item["EP_NgU"])
		myVis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
	elif Document.Properties["DisplayName"] == "Random Access Success Rate Captured in gNodeB"\
	or Document.Properties["DisplayName"] == "Average UL MAC UE Throughput"\
	or Document.Properties["DisplayName"] == "Average DL MAC DRB Throughput"\
	or Document.Properties["DisplayName"] == "Normalized Average DL MAC Cell Throughput considering traffic"\
	or Document.Properties["DisplayName"] == "Normalized Average UL MAC Cell Throughput considering successful PUSCH slot only"\
	or Document.Properties["DisplayName"] == "Normalized DL MAC Cell Throughput considering actual PDSCH slot only"\
	or Document.Properties["DisplayName"] == "Partial Cell Availability for gNodeB Cell"\
	or Document.Properties["DisplayName"] == "Normalized UL MAC Cell Throughput considering actual PUSCH slot only":
		myVis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_RAW_DOD_nodeview")
		dataTable = myVis.Data.DataTableReference
		myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])
		myVis.TableColumns.Add(dataTable.Columns.Item["NR_NAME"])
		myVis.TableColumns.Add(dataTable.Columns.Item["NRCellDU"])
		myVis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
	elif Document.Properties["DisplayName"] == "UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered"\
	or Document.Properties["DisplayName"] == "DL Packet Loss Captured in gNodeB":
		myVis.Data.DataTableReference = getDataTable("IL_DC_E_VPP_RPUSERPLANELINK_V_RAW_DOD_nodeview")
		dataTable = myVis.Data.DataTableReference
		myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])
		myVis.TableColumns.Add(dataTable.Columns.Item["NE_NAME"])
		myVis.TableColumns.Add(dataTable.Columns.Item["RP_USER_PLANE_LINK"])
		myVis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filer
	elif Document.Properties["DisplayName"] == "Average DL MAC DRB Latency per QoS covering DRX In-sync"\
	or Document.Properties["DisplayName"] == "Average DL MAC DRB Latency per QoS covering non-DRX In-sync"\
	or Document.Properties["DisplayName"] == "Average Overall DL Latency per QoS"\
	or Document.Properties["DisplayName"] == "DL MAC DRB Throughput per QoS":
		myVis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLDU_V_RAW_DOD_nodeview")
		dataTable = myVis.Data.DataTableReference
		myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])
		myVis.TableColumns.Add(dataTable.Columns.Item["NR_NAME"])
		myVis.TableColumns.Add(dataTable.Columns.Item["NRCellDU"])
		myVis.Data.Filterings.Add(Document.Data.Filterings["Filtering scheme for QoS"]) #Add Filter

	else:
		myVis.Data.DataTableReference = getDataTable("IL_DC_E_NR_NRCELLCU_RAW_DOD_nodeview")
		dataTable = myVis.Data.DataTableReference
		myVis.TableColumns.Add(dataTable.Columns.Item["DATETIME_ID"])
		myVis.TableColumns.Add(dataTable.Columns.Item["NR_NAME"])
		myVis.TableColumns.Add(dataTable.Columns.Item["NRCellCU"])
		myVis.Data.Filterings.Remove(Document.Data.Filterings["Filtering scheme for QoS"]) #Remove Filter
	myVis.TableColumns.Add(dataTable.Columns.Item["KPI Value"])
	for item in columnName:
		myVis.TableColumns.Add(dataTable.Columns.Item[item])
except KeyError:
	print "Value Error - No KPI selected"
except KeyError:
	print "Can't set KPI document property"

Document.ActivePageReference = Document.Pages[7]

