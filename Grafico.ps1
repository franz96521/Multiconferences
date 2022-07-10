Add-Type -assembly System.Windows.Forms
#form
$mainForm = New-Object System.Windows.Forms.Form
$mainForm.Text = 'Multi conferencias'
$mainForm.Width = 600
$mainForm.Height = 400
#flowlayaut
$flow = New-Object System.Windows.Forms.FlowLayoutPanel
$flow.AutoSize = $true

#grid
$dataGridView = New-Object System.Windows.Forms.DataGridView
$dataGridView.Width = 500
$dataGridView.Height = 300
$colum = New-Object System.Windows.Forms.DataGridViewTextBoxColumn
$colum.HeaderText = "URL de la reunion"
$colum.Width = 500
$dataGridView.Columns.Add($colum)


# botones
$starBTN = New-Object  System.Windows.Forms.Button
$starBTN.Text = "iniciar"
$starBTN.Add_click({
        $URLS = @()
        $dataGridView.Rows | ForEach-Object -Process {
            $Url = $_.Cells.Value
            $URLS += $Url
        }
        Start-Process "C:\Program Files\obs-studio\bin\64bit\obs64.exe" -WorkingDirectory "C:\Program Files\obs-studio\bin\64bit"
        ./Start.ps1 -URLS  $URLS 
    })

#mostrar
$flow.Controls.Add($dataGridView)
$flow.Controls.Add($starBTN)
$mainForm.Controls.Add($flow)

$mainForm.ShowDialog()
exit