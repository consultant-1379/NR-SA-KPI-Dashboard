from Spotfire.Dxp.Application.Visuals import *
import re

for page in Document.Pages:
	if page.Title == "KPI Details":
		for vis in page.Visuals:
			if "Worst Performing Cells (Latest ROP)" in vis.Title:
				vis = vis.As[Visualization]()
				Rules = vis.TryGetFilterRules()
				if Document.Properties["DetailsDisplayName"] == "DL Packet Loss Captured in gNodeB"\
				or Document.Properties["DetailsDisplayName"] == "Average Overall DL Latency per QoS"\
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Latency per QoS covering non-DRX In-sync"\
				or Document.Properties["DetailsDisplayName"] == "Average DL MAC DRB Latency per QoS covering DRX In-sync"\
				or Document.Properties["DetailsDisplayName"] == "UL Packet Loss Captured in gNodeB normalized with out of order PDU delivered"\
				or Document.Properties["DetailsDisplayName"] == "DRB Retainability - Percentage of Active Lost per mapped 5QI, RRC Inactive State" \
				or Document.Properties["DetailsDisplayName"] == "DRB Retainability - Percentage of Active Lost per mapped 5QI, RRC Inactive State, gNodeB triggered only" \
				or Document.Properties["DetailsDisplayName"] == "DRB Retainability - Percentage of Active Lost per mapped 5QI" \
				or Document.Properties["DetailsDisplayName"] == "DRB Retainability - Percentage of Active Lost per mapped 5QI, gNodeB triggered only" \
				or Document.Properties["DetailsDisplayName"] == "DRB Retainability - Session Time Normalized per mapped 5QI Loss Rate" \
				or Document.Properties["DetailsDisplayName"] == "DRB Retainability - Session Time Normalized per mapped 5QI Loss Rate, gNodeB triggered only" \
				or Document.Properties["DetailsDisplayName"] == "DL Packet Loss in gNodeB-CU-UP":
					Rules[1][0].Enabled = True
					Rules[1][1].Enabled = False
					vis.XAxis.Reversed = True
				else:
					Rules[1][1].Enabled = True
					Rules[1][0].Enabled = False
					vis.XAxis.Reversed = False