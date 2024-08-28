from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Application.Filters import *
from Spotfire.Dxp.Data import RowSelection, IndexSet

for dataTable in Document.Data.Tables:
	for marking in Document.Data.Markings:
		rows = RowSelection(IndexSet(dataTable.RowCount, False))
		marking.SetSelection(rows, dataTable)
            
	for filterScheme in Document.FilteringSchemes:
		filterScheme.ResetAllFilters()
