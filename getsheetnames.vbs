Sub SheetNames()
    Columns(1).Insert
    For i = 1 To Sheets.Count
        Cells(i, 1) = Sheets(i).Name
    Next i
End Sub
