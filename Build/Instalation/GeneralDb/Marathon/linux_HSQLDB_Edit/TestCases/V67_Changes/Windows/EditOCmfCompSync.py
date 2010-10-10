useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_10'

	if window('Record Editor'):
		if commonBits.isRecordEditor():
			select_menu('Record Layouts>>Load Cobol Copybook')
			select('FileChooser', commonBits.cobolTestDir() + 'mfCompSync.cbl')
			select('ComputerOptionCombo', 'Open Cobol Micro Focus (Intel)')
			select('BmKeyedComboBox1', '9')
			click('Go')
			assert_p('TextArea', 'Text', '''

-->> ''' + commonBits.cobolTestDir() + '''mfCompSync.cbl processed

      Copybook: mfCompSync''')
			click('BasicInternalFrameTitlePane$NoFocusButton2')
			click('Open')

		select('FileChooser', commonBits.cobolTestDir() + 'mfCompSync.bin')
		commonBits.setCobolLayout(select, 'mfCompSync', 'Open Cobol Micro Focus (Intel)')
		click('Edit1')
		select('Table', 'cell:29 - 2|Num1,8(-166.19)')
		assert_p('Table', 'Text', '-166.19', '29 - 2|Num1,8')
		select('Table', 'cell:29 - 2|Num1,10(-50.99)')
		assert_p('Table', 'RowCount', '40')
		select('Table', 'cell:29 - 2|Num1,12(-63.79)')
		assert_p('Table', 'ColumnCount', '37')
		select('Table', 'cell:29 - 2|Num1,15(68.64)')
		assert_p('Table', 'Content', '[[1.23, ;, 1, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23, ;, 1.23], [-1.23, ;, -1, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, 1.23], [23.45, ;, 23, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45, ;, 23.45], [-23.45, ;, -23, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, -23.45, ;, 23.45], [123.45, ;, 123, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45, ;, 123.45], [-123.45, ;, -123, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, -123.45, ;, 123.45], [4567.89, ;, -41, ;, -19.63, ;, -19.63, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89, ;, 4567.89], [-4567.89, ;, 41, ;, 19.63, ;, 19.63, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, -4567.89, ;, 4567.89], [34567.89, ;, 7, ;, -166.19, ;, -166.19, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89, ;, 34567.89], [-34567.89, ;, -7, ;, 166.19, ;, 166.19, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, -34567.89, ;, 34567.89], [234567.89, ;, 71, ;, -50.99, ;, -50.99, ;, 66795.73, ;, 66795.73, ;, 234567.89, ;, 234567.89, ;, 234567.89, ;, 234567.89, ;, 234567.89, ;, 234567.89, ;, 234567.89, ;, 234567.89, ;, 234567.89, ;, 234567.89, ;, 234567.89, ;, 234567.89, ;, 66795.73], [-234567.89, ;, -71, ;, 50.99, ;, 50.99, ;, -66795.73, ;, -66795.73, ;, -234567.89, ;, -234567.89, ;, -234567.89, ;, -234567.89, ;, -234567.89, ;, -234567.89, ;, -234567.89, ;, -234567.89, ;, -234567.89, ;, -234567.89, ;, -234567.89, ;, -234567.89, ;, 66795.73], [91234567.89, ;, 7, ;, -63.79, ;, -63.79, ;, -33487.15, ;, -33487.15, ;, 5335221.97, ;, 5335221.97, ;, 5335221.97, ;, 91234567.89, ;, 91234567.89, ;, 91234567.89, ;, 91234567.89, ;, 91234567.89, ;, 91234567.89, ;, 91234567.89, ;, 91234567.89, ;, 91234567.89, ;, -33487.15], [-91234567.89, ;, -7, ;, 63.79, ;, 63.79, ;, 33487.15, ;, 33487.15, ;, -5335221.97, ;, -5335221.97, ;, -5335221.97, ;, -91234567.89, ;, -91234567.89, ;, -91234567.89, ;, -91234567.89, ;, -91234567.89, ;, -91234567.89, ;, -91234567.89, ;, -91234567.89, ;, -91234567.89, ;, -33487.15], [987654321.12, ;, -79, ;, -68.64, ;, -68.64, ;, -20384.80, ;, -20384.80, ;, -188156.96, ;, -188156.96, ;, -188156.96, ;, 987654321.12, ;, 987654321.12, ;, 987654321.12, ;, 987654321.12, ;, 987654321.12, ;, 987654321.12, ;, 987654321.12, ;, 987654321.12, ;, 987654321.12, ;, -20384.80], [-987654321.12, ;, 79, ;, 68.64, ;, 68.64, ;, 20384.80, ;, 20384.80, ;, 188156.96, ;, 188156.96, ;, 188156.96, ;, -987654321.12, ;, -987654321.12, ;, -987654321.12, ;, -987654321.12, ;, -987654321.12, ;, -987654321.12, ;, -987654321.12, ;, -987654321.12, ;, -987654321.12, ;, -20384.80], [1987654321.12, ;, -79, ;, -130.08, ;, -130.08, ;, 57541.60, ;, 57541.60, ;, 11969364.96, ;, 11969364.96, ;, 11969364.96, ;, 1987654321.12, ;, 1987654321.12, ;, 1987654321.12, ;, 1987654321.12, ;, 1987654321.12, ;, 1987654321.12, ;, 1987654321.12, ;, 1987654321.12, ;, 1987654321.12, ;, 57541.60], [-1987654321.12, ;, 79, ;, 130.08, ;, 130.08, ;, -57541.60, ;, -57541.60, ;, -11969364.96, ;, -11969364.96, ;, -11969364.96, ;, -1987654321.12, ;, -1987654321.12, ;, -1987654321.12, ;, -1987654321.12, ;, -1987654321.12, ;, -1987654321.12, ;, -1987654321.12, ;, -1987654321.12, ;, -1987654321.12, ;, 57541.60], [21987654321.12, ;, -79, ;, -48.16, ;, -48.16, ;, -61652.00, ;, -61652.00, ;, -2578234.40, ;, -2578234.40, ;, -2578234.40, ;, -2578234.40, ;, -2578234.40, ;, 21987654321.12, ;, 21987654321.12, ;, 21987654321.12, ;, 21987654321.12, ;, 21987654321.12, ;, 21987654321.12, ;, 21987654321.12, ;, -61652.00], [-21987654321.12, ;, 79, ;, 48.16, ;, 48.16, ;, 61652.00, ;, 61652.00, ;, 2578234.40, ;, 2578234.40, ;, 2578234.40, ;, 2578234.40, ;, 2578234.40, ;, -21987654321.12, ;, -21987654321.12, ;, -21987654321.12, ;, -21987654321.12, ;, -21987654321.12, ;, -21987654321.12, ;, -21987654321.12, ;, -61652.00], [321987654321.12, ;, -79, ;, -130.08, ;, -130.08, ;, -4062.24, ;, -4062.24, ;, -6043860.00, ;, -6043860.00, ;, -6043860.00, ;, 3129282266.08, ;, 3129282266.08, ;, 321987654321.12, ;, 321987654321.12, ;, 321987654321.12, ;, 321987654321.12, ;, 321987654321.12, ;, 321987654321.12, ;, 321987654321.12, ;, -4062.24], [-321987654321.12, ;, 79, ;, 130.08, ;, 130.08, ;, 4062.24, ;, 4062.24, ;, 6043860.00, ;, 6043860.00, ;, 6043860.00, ;, -3129282266.08, ;, -3129282266.08, ;, -321987654321.12, ;, -321987654321.12, ;, -321987654321.12, ;, -321987654321.12, ;, -321987654321.12, ;, -321987654321.12, ;, -321987654321.12, ;, -4062.24], [4321987654321.12, ;, -79, ;, -130.08, ;, -130.08, ;, -19135.52, ;, -19135.52, ;, 5014029.28, ;, 5014029.28, ;, 5014029.28, ;, 906957161.44, ;, 906957161.44, ;, -1307511879892.00, ;, -1307511879892.00, ;, -1307511879892.00, ;, 4321987654321.12, ;, 4321987654321.12, ;, 4321987654321.12, ;, 4321987654321.12, ;, -19135.52], [-4321987654321.12, ;, 79, ;, 130.08, ;, 130.08, ;, 19135.52, ;, 19135.52, ;, -5014029.28, ;, -5014029.28, ;, -5014029.28, ;, -906957161.44, ;, -906957161.44, ;, 1307511879892.00, ;, 1307511879892.00, ;, 1307511879892.00, ;, -4321987654321.12, ;, -4321987654321.12, ;, -4321987654321.12, ;, -4321987654321.12, ;, -19135.52], [54321987654321.12, ;, -79, ;, 197.60, ;, 197.60, ;, -39779.36, ;, -39779.36, ;, 14388626.40, ;, 14388626.40, ;, 14388626.40, ;, -4881874091.04, ;, -4881874091.04, ;, 841742079296.48, ;, 841742079296.48, ;, 841742079296.48, ;, 54321987654321.12, ;, 54321987654321.12, ;, 54321987654321.12, ;, 54321987654321.12, ;, -39779.36], [-54321987654321.12, ;, 79, ;, -197.60, ;, -197.60, ;, 39779.36, ;, 39779.36, ;, -14388626.40, ;, -14388626.40, ;, -14388626.40, ;, 4881874091.04, ;, 4881874091.04, ;, -841742079296.48, ;, -841742079296.48, ;, -841742079296.48, ;, -54321987654321.12, ;, -54321987654321.12, ;, -54321987654321.12, ;, -54321987654321.12, ;, -39779.36], [654321987654321.12, ;, -79, ;, 197.60, ;, 197.60, ;, 48038.88, ;, 48038.88, ;, -1965227.04, ;, -1965227.04, ;, -1965227.04, ;, 2617964823.52, ;, 2617964823.52, ;, 1300041685599.20, ;, 1300041685599.20, ;, 1300041685599.20, ;, -66253952724958.24, ;, -66253952724958.24, ;, 654321987654321.12, ;, 654321987654321.12, ;, 48038.88], [-654321987654321.12, ;, 79, ;, -197.60, ;, -197.60, ;, -48038.88, ;, -48038.88, ;, 1965227.04, ;, 1965227.04, ;, 1965227.04, ;, -2617964823.52, ;, -2617964823.52, ;, -1300041685599.20, ;, -1300041685599.20, ;, -1300041685599.20, ;, 66253952724958.24, ;, 66253952724958.24, ;, -654321987654321.12, ;, -654321987654321.12, ;, 48038.88], [7654321987654321.12, ;, -79, ;, 197.60, ;, 197.60, ;, 10028.00, ;, 10028.00, ;, -20961492.00, ;, -20961492.00, ;, -20961492.00, ;, -5174922247.20, ;, -5174922247.20, ;, 1017370891584.48, ;, 1017370891584.48, ;, 1017370891584.48, ;, -272013356517751.84, ;, -272013356517751.84, ;, 7654321987654321.12, ;, 7654321987654321.12, ;, 10028.00], [-7654321987654321.12, ;, 79, ;, -197.60, ;, -197.60, ;, -10028.00, ;, -10028.00, ;, 20961492.00, ;, 20961492.00, ;, 20961492.00, ;, 5174922247.20, ;, 5174922247.20, ;, -1017370891584.48, ;, -1017370891584.48, ;, -1017370891584.48, ;, 272013356517751.84, ;, 272013356517751.84, ;, -7654321987654321.12, ;, -7654321987654321.12, ;, 10028.00], [-1.21, ;, -1, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, -1.21, ;, 1.21], [-1.22, ;, -1, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, -1.22, ;, 1.22], [-1.23, ;, -1, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, -1.23, ;, 1.23], [-1.24, ;, -1, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, -1.24, ;, 1.24], [-1.25, ;, -1, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, -1.25, ;, 1.25], [-1.26, ;, -1, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, -1.26, ;, 1.26], [-1.27, ;, -1, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, -1.27, ;, 1.27], [-1.28, ;, -1, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, -1.28, ;, 1.28], [-1.29, ;, -1, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, -1.29, ;, 1.29], [-1.20, ;, -1, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, -1.20, ;, 1.20]]')
		select('Table', 'cell:29 - 2|Num1,17(130.08)')
		assert_p('Table', 'Text', 'cell:29 - 2|Num1,17(130.08)')
		select('Table', 'cell:29 - 2|Num1,18(-48.16)')
		rightclick('Table', '29 - 2|Num1,18')
		select_menu('Edit Record')
###		select('Table1', 'cell:29 - 2|Num1,18(-48.16)')
		select('Table', 'cell:Data,10(-61652.00)')
		assert_p('Table', 'Content', '[[NumA, 1, 25, 21987654321.12,         21,987,654,321.12, 202020202020202032312c3938372c3635342c3332312e3132], [sep0, 26, 1, ;, ;, 3b], [Num0, 27, 1, -79, �, b1], [sep1, 28, 1, ;, ;, 3b], [Num1, 29, 2, -48.16, �0, ed30], [sep2, 31, 1, ;, ;, 3b], [Num2, 32, 2, -48.16, �0, ed30], [sep3, 34, 1, ;, ;, 3b], [Num3, 35, 3, -61652.00, ��0, a1ed30], [sep4, 38, 1, ;, ;, 3b], [Num4, 39, 3, -61652.00, ��0, a1ed30], [sep5, 42, 1, ;, ;, 3b], [Num5, 43, 4, -2578234.40, ��0, f0a1ed30], [sep6, 47, 1, ;, ;, 3b], [Num6, 48, 4, -2578234.40, ��0, f0a1ed30], [sep7, 52, 1, ;, ;, 3b], [Num7, 53, 4, -2578234.40, ��0, f0a1ed30], [sep8, 57, 1, ;, ;, 3b], [Num8, 58, 5, -2578234.40, ���0, fff0a1ed30], [sep9, 63, 1, ;, ;, 3b], [Num9, 64, 5, -2578234.40, ���0, fff0a1ed30], [sep10, 69, 1, ;, ;, 3b], [Num10, 70, 6, 21987654321.12, ���0, 01fff0a1ed30], [sep11, 76, 1, ;, ;, 3b], [Num11, 77, 6, 21987654321.12, ���0, 01fff0a1ed30], [sep12, 83, 1, ;, ;, 3b], [Num12, 84, 6, 21987654321.12, ���0, 01fff0a1ed30], [sep13, 90, 1, ;, ;, 3b], [Num13, 91, 7, 21987654321.12,  ���0, 0001fff0a1ed30], [sep14, 98, 1, ;, ;, 3b], [Num14, 99, 7, 21987654321.12,  ���0, 0001fff0a1ed30], [sep15, 106, 1, ;, ;, 3b], [Num15, 107, 8, 21987654321.12,   ���0, 000001fff0a1ed30], [sep16, 115, 1, ;, ;, 3b], [Num16, 116, 8, 21987654321.12,   ���0, 000001fff0a1ed30], [sep17, 124, 1, ;, ;, 3b], [Num17, 125, 3, -61652.00, ��0, a1ed30]]')
		select('Table', 'cell:Data,12(-2578234.40)')
		assert_p('Table', 'Text', '-2578234.40', 'Data,12')
		select('Table', 'cell:Data,12(-2578234.40)')
		click('Right')
		select('Table', 'cell:Data,12(2578234.40)')
		assert_p('Table', 'Content', '[[NumA, 1, 25, -21987654321.12,        -21,987,654,321.12, 202020202020202d32312c3938372c3635342c3332312e3132], [sep0, 26, 1, ;, ;, 3b], [Num0, 27, 1, 79, O, 4f], [sep1, 28, 1, ;, ;, 3b], [Num1, 29, 2, 48.16, �, 12d0], [sep2, 31, 1, ;, ;, 3b], [Num2, 32, 2, 48.16, �, 12d0], [sep3, 34, 1, ;, ;, 3b], [Num3, 35, 3, 61652.00, ^�, 5e12d0], [sep4, 38, 1, ;, ;, 3b], [Num4, 39, 3, 61652.00, ^�, 5e12d0], [sep5, 42, 1, ;, ;, 3b], [Num5, 43, 4, 2578234.40, ^�, 0f5e12d0], [sep6, 47, 1, ;, ;, 3b], [Num6, 48, 4, 2578234.40, ^�, 0f5e12d0], [sep7, 52, 1, ;, ;, 3b], [Num7, 53, 4, 2578234.40, ^�, 0f5e12d0], [sep8, 57, 1, ;, ;, 3b], [Num8, 58, 5, 2578234.40,  ^�, 000f5e12d0], [sep9, 63, 1, ;, ;, 3b], [Num9, 64, 5, 2578234.40,  ^�, 000f5e12d0], [sep10, 69, 1, ;, ;, 3b], [Num10, 70, 6, -21987654321.12, � ^�, fe000f5e12d0], [sep11, 76, 1, ;, ;, 3b], [Num11, 77, 6, -21987654321.12, � ^�, fe000f5e12d0], [sep12, 83, 1, ;, ;, 3b], [Num12, 84, 6, -21987654321.12, � ^�, fe000f5e12d0], [sep13, 90, 1, ;, ;, 3b], [Num13, 91, 7, -21987654321.12, �� ^�, fffe000f5e12d0], [sep14, 98, 1, ;, ;, 3b], [Num14, 99, 7, -21987654321.12, �� ^�, fffe000f5e12d0], [sep15, 106, 1, ;, ;, 3b], [Num15, 107, 8, -21987654321.12, ��� ^�, fffffe000f5e12d0], [sep16, 115, 1, ;, ;, 3b], [Num16, 116, 8, -21987654321.12, ��� ^�, fffffe000f5e12d0], [sep17, 124, 1, ;, ;, 3b], [Num17, 125, 3, -61652.00, ��0, a1ed30]]')
		select('Table', 'cell:Data,12(2578234.40)')
		click('Right')
		select('Table', 'cell:Data,12(-6043860.00)')
		assert_p('Table', 'Content', '[[NumA, 1, 25, 321987654321.12,        321,987,654,321.12, 202020202020203332312c3938372c3635342c3332312e3132], [sep0, 26, 1, ;, ;, 3b], [Num0, 27, 1, -79, �, b1], [sep1, 28, 1, ;, ;, 3b], [Num1, 29, 2, -130.08, �0, cd30], [sep2, 31, 1, ;, ;, 3b], [Num2, 32, 2, -130.08, �0, cd30], [sep3, 34, 1, ;, ;, 3b], [Num3, 35, 3, -4062.24, ��0, f9cd30], [sep4, 38, 1, ;, ;, 3b], [Num4, 39, 3, -4062.24, ��0, f9cd30], [sep5, 42, 1, ;, ;, 3b], [Num5, 43, 4, -6043860.00, ���0, dbf9cd30], [sep6, 47, 1, ;, ;, 3b], [Num6, 48, 4, -6043860.00, ���0, dbf9cd30], [sep7, 52, 1, ;, ;, 3b], [Num7, 53, 4, -6043860.00, ���0, dbf9cd30], [sep8, 57, 1, ;, ;, 3b], [Num8, 58, 5, 3129282266.08, H���0, 48dbf9cd30], [sep9, 63, 1, ;, ;, 3b], [Num9, 64, 5, 3129282266.08, H���0, 48dbf9cd30], [sep10, 69, 1, ;, ;, 3b], [Num10, 70, 6, 321987654321.12, H���0, 1d48dbf9cd30], [sep11, 76, 1, ;, ;, 3b], [Num11, 77, 6, 321987654321.12, H���0, 1d48dbf9cd30], [sep12, 83, 1, ;, ;, 3b], [Num12, 84, 6, 321987654321.12, H���0, 1d48dbf9cd30], [sep13, 90, 1, ;, ;, 3b], [Num13, 91, 7, 321987654321.12,  H���0, 001d48dbf9cd30], [sep14, 98, 1, ;, ;, 3b], [Num14, 99, 7, 321987654321.12,  H���0, 001d48dbf9cd30], [sep15, 106, 1, ;, ;, 3b], [Num15, 107, 8, 321987654321.12,   H���0, 00001d48dbf9cd30], [sep16, 115, 1, ;, ;, 3b], [Num16, 116, 8, 321987654321.12,   H���0, 00001d48dbf9cd30], [sep17, 124, 1, ;, ;, 3b], [Num17, 125, 3, -4062.24, ��0, f9cd30]]')
		select('Table', 'cell:Data,12(-6043860.00)')
		click('Right')
		select('Table', 'cell:Data,14(6043860.00)')
		assert_p('Table', 'Content', '[[NumA, 1, 25, -321987654321.12,       -321,987,654,321.12, 2020202020202d3332312c3938372c3635342c3332312e3132], [sep0, 26, 1, ;, ;, 3b], [Num0, 27, 1, 79, O, 4f], [sep1, 28, 1, ;, ;, 3b], [Num1, 29, 2, 130.08, 2�, 32d0], [sep2, 31, 1, ;, ;, 3b], [Num2, 32, 2, 130.08, 2�, 32d0], [sep3, 34, 1, ;, ;, 3b], [Num3, 35, 3, 4062.24, 2�, 0632d0], [sep4, 38, 1, ;, ;, 3b], [Num4, 39, 3, 4062.24, 2�, 0632d0], [sep5, 42, 1, ;, ;, 3b], [Num5, 43, 4, 6043860.00, $2�, 240632d0], [sep6, 47, 1, ;, ;, 3b], [Num6, 48, 4, 6043860.00, $2�, 240632d0], [sep7, 52, 1, ;, ;, 3b], [Num7, 53, 4, 6043860.00, $2�, 240632d0], [sep8, 57, 1, ;, ;, 3b], [Num8, 58, 5, -3129282266.08, �$2�, b7240632d0], [sep9, 63, 1, ;, ;, 3b], [Num9, 64, 5, -3129282266.08, �$2�, b7240632d0], [sep10, 69, 1, ;, ;, 3b], [Num10, 70, 6, -321987654321.12, �$2�, e2b7240632d0], [sep11, 76, 1, ;, ;, 3b], [Num11, 77, 6, -321987654321.12, �$2�, e2b7240632d0], [sep12, 83, 1, ;, ;, 3b], [Num12, 84, 6, -321987654321.12, �$2�, e2b7240632d0], [sep13, 90, 1, ;, ;, 3b], [Num13, 91, 7, -321987654321.12, ��$2�, ffe2b7240632d0], [sep14, 98, 1, ;, ;, 3b], [Num14, 99, 7, -321987654321.12, ��$2�, ffe2b7240632d0], [sep15, 106, 1, ;, ;, 3b], [Num15, 107, 8, -321987654321.12, ���$2�, ffffe2b7240632d0], [sep16, 115, 1, ;, ;, 3b], [Num16, 116, 8, -321987654321.12, ���$2�, ffffe2b7240632d0], [sep17, 124, 1, ;, ;, 3b], [Num17, 125, 3, -4062.24, ��0, f9cd30]]')
		select('Table', 'cell:Data,14(6043860.00)')
		click('Right')
		select('Table', 'cell:Data,14(5014029.28)')
		assert_p('Table', 'Content', '[[NumA, 1, 25, 4321987654321.12,      4,321,987,654,321.12, 2020202020342c3332312c3938372c3635342c3332312e3132], [sep0, 26, 1, ;, ;, 3b], [Num0, 27, 1, -79, �, b1], [sep1, 28, 1, ;, ;, 3b], [Num1, 29, 2, -130.08, �0, cd30], [sep2, 31, 1, ;, ;, 3b], [Num2, 32, 2, -130.08, �0, cd30], [sep3, 34, 1, ;, ;, 3b], [Num3, 35, 3, -19135.52, ��0, e2cd30], [sep4, 38, 1, ;, ;, 3b], [Num4, 39, 3, -19135.52, ��0, e2cd30], [sep5, 42, 1, ;, ;, 3b], [Num5, 43, 4, 5014029.28, ��0, 1de2cd30], [sep6, 47, 1, ;, ;, 3b], [Num6, 48, 4, 5014029.28, ��0, 1de2cd30], [sep7, 52, 1, ;, ;, 3b], [Num7, 53, 4, 5014029.28, ��0, 1de2cd30], [sep8, 57, 1, ;, ;, 3b], [Num8, 58, 5, 906957161.44, ��0, 151de2cd30], [sep9, 63, 1, ;, ;, 3b], [Num9, 64, 5, 906957161.44, ��0, 151de2cd30], [sep10, 69, 1, ;, ;, 3b], [Num10, 70, 6, -1307511879892.00, ���0, 89151de2cd30], [sep11, 76, 1, ;, ;, 3b], [Num11, 77, 6, -1307511879892.00, ���0, 89151de2cd30], [sep12, 83, 1, ;, ;, 3b], [Num12, 84, 6, -1307511879892.00, ���0, 89151de2cd30], [sep13, 90, 1, ;, ;, 3b], [Num13, 91, 7, 4321987654321.12, ���0, 0189151de2cd30], [sep14, 98, 1, ;, ;, 3b], [Num14, 99, 7, 4321987654321.12, ���0, 0189151de2cd30], [sep15, 106, 1, ;, ;, 3b], [Num15, 107, 8, 4321987654321.12,  ���0, 000189151de2cd30], [sep16, 115, 1, ;, ;, 3b], [Num16, 116, 8, 4321987654321.12,  ���0, 000189151de2cd30], [sep17, 124, 1, ;, ;, 3b], [Num17, 125, 3, -19135.52, ��0, e2cd30]]')
		select('Table', 'cell:Data,18(906957161.44)')
		assert_p('Table', 'Text', '906957161.44', 'Data,18')
		select('Table', 'cell:Data,18(906957161.44)')
		click('Right')
		select('Table', 'cell:Data,18(-906957161.44)')
		assert_p('Table', 'Content', '[[NumA, 1, 25, -4321987654321.12,     -4,321,987,654,321.12, 202020202d342c3332312c3938372c3635342c3332312e3132], [sep0, 26, 1, ;, ;, 3b], [Num0, 27, 1, 79, O, 4f], [sep1, 28, 1, ;, ;, 3b], [Num1, 29, 2, 130.08, 2�, 32d0], [sep2, 31, 1, ;, ;, 3b], [Num2, 32, 2, 130.08, 2�, 32d0], [sep3, 34, 1, ;, ;, 3b], [Num3, 35, 3, 19135.52, 2�, 1d32d0], [sep4, 38, 1, ;, ;, 3b], [Num4, 39, 3, 19135.52, 2�, 1d32d0], [sep5, 42, 1, ;, ;, 3b], [Num5, 43, 4, -5014029.28, �2�, e21d32d0], [sep6, 47, 1, ;, ;, 3b], [Num6, 48, 4, -5014029.28, �2�, e21d32d0], [sep7, 52, 1, ;, ;, 3b], [Num7, 53, 4, -5014029.28, �2�, e21d32d0], [sep8, 57, 1, ;, ;, 3b], [Num8, 58, 5, -906957161.44, ��2�, eae21d32d0], [sep9, 63, 1, ;, ;, 3b], [Num9, 64, 5, -906957161.44, ��2�, eae21d32d0], [sep10, 69, 1, ;, ;, 3b], [Num10, 70, 6, 1307511879892.00, v��2�, 76eae21d32d0], [sep11, 76, 1, ;, ;, 3b], [Num11, 77, 6, 1307511879892.00, v��2�, 76eae21d32d0], [sep12, 83, 1, ;, ;, 3b], [Num12, 84, 6, 1307511879892.00, v��2�, 76eae21d32d0], [sep13, 90, 1, ;, ;, 3b], [Num13, 91, 7, -4321987654321.12, �v��2�, fe76eae21d32d0], [sep14, 98, 1, ;, ;, 3b], [Num14, 99, 7, -4321987654321.12, �v��2�, fe76eae21d32d0], [sep15, 106, 1, ;, ;, 3b], [Num15, 107, 8, -4321987654321.12, ��v��2�, fffe76eae21d32d0], [sep16, 115, 1, ;, ;, 3b], [Num16, 116, 8, -4321987654321.12, ��v��2�, fffe76eae21d32d0], [sep17, 124, 1, ;, ;, 3b], [Num17, 125, 3, -19135.52, ��0, e2cd30]]')
		select('Table', 'cell:Data,18(-906957161.44)')
		click('Right')
		select('Table', 'cell:Data,18(-4881874091.04)')
		assert_p('Table', 'Content', '[[NumA, 1, 25, 54321987654321.12,     54,321,987,654,321.12, 2020202035342c3332312c3938372c3635342c3332312e3132], [sep0, 26, 1, ;, ;, 3b], [Num0, 27, 1, -79, �, b1], [sep1, 28, 1, ;, ;, 3b], [Num1, 29, 2, 197.60, M0, 4d30], [sep2, 31, 1, ;, ;, 3b], [Num2, 32, 2, 197.60, M0, 4d30], [sep3, 34, 1, ;, ;, 3b], [Num3, 35, 3, -39779.36, �M0, c34d30], [sep4, 38, 1, ;, ;, 3b], [Num4, 39, 3, -39779.36, �M0, c34d30], [sep5, 42, 1, ;, ;, 3b], [Num5, 43, 4, 14388626.40, U�M0, 55c34d30], [sep6, 47, 1, ;, ;, 3b], [Num6, 48, 4, 14388626.40, U�M0, 55c34d30], [sep7, 52, 1, ;, ;, 3b], [Num7, 53, 4, 14388626.40, U�M0, 55c34d30], [sep8, 57, 1, ;, ;, 3b], [Num8, 58, 5, -4881874091.04, �U�M0, 8e55c34d30], [sep9, 63, 1, ;, ;, 3b], [Num9, 64, 5, -4881874091.04, �U�M0, 8e55c34d30], [sep10, 69, 1, ;, ;, 3b], [Num10, 70, 6, 841742079296.48, L�U�M0, 4c8e55c34d30], [sep11, 76, 1, ;, ;, 3b], [Num11, 77, 6, 841742079296.48, L�U�M0, 4c8e55c34d30], [sep12, 83, 1, ;, ;, 3b], [Num12, 84, 6, 841742079296.48, L�U�M0, 4c8e55c34d30], [sep13, 90, 1, ;, ;, 3b], [Num13, 91, 7, 54321987654321.12, L�U�M0, 134c8e55c34d30], [sep14, 98, 1, ;, ;, 3b], [Num14, 99, 7, 54321987654321.12, L�U�M0, 134c8e55c34d30], [sep15, 106, 1, ;, ;, 3b], [Num15, 107, 8, 54321987654321.12,  L�U�M0, 00134c8e55c34d30], [sep16, 115, 1, ;, ;, 3b], [Num16, 116, 8, 54321987654321.12,  L�U�M0, 00134c8e55c34d30], [sep17, 124, 1, ;, ;, 3b], [Num17, 125, 3, -39779.36, �M0, c34d30]]')
		select('Table', 'cell:Data,18(-4881874091.04)')
		click('Right')
		select('Table', 'cell:Data,22(-841742079296.48)')
		assert_p('Table', 'Text', '-841742079296.48', 'Data,22')
		select('Table', 'cell:Data,20(4881874091.04)')
		assert_p('Table', 'Content', '[[NumA, 1, 25, -54321987654321.12,    -54,321,987,654,321.12, 2020202d35342c3332312c3938372c3635342c3332312e3132], [sep0, 26, 1, ;, ;, 3b], [Num0, 27, 1, 79, O, 4f], [sep1, 28, 1, ;, ;, 3b], [Num1, 29, 2, -197.60, ��, b2d0], [sep2, 31, 1, ;, ;, 3b], [Num2, 32, 2, -197.60, ��, b2d0], [sep3, 34, 1, ;, ;, 3b], [Num3, 35, 3, 39779.36, <��, 3cb2d0], [sep4, 38, 1, ;, ;, 3b], [Num4, 39, 3, 39779.36, <��, 3cb2d0], [sep5, 42, 1, ;, ;, 3b], [Num5, 43, 4, -14388626.40, �<��, aa3cb2d0], [sep6, 47, 1, ;, ;, 3b], [Num6, 48, 4, -14388626.40, �<��, aa3cb2d0], [sep7, 52, 1, ;, ;, 3b], [Num7, 53, 4, -14388626.40, �<��, aa3cb2d0], [sep8, 57, 1, ;, ;, 3b], [Num8, 58, 5, 4881874091.04, q�<��, 71aa3cb2d0], [sep9, 63, 1, ;, ;, 3b], [Num9, 64, 5, 4881874091.04, q�<��, 71aa3cb2d0], [sep10, 69, 1, ;, ;, 3b], [Num10, 70, 6, -841742079296.48, �q�<��, b371aa3cb2d0], [sep11, 76, 1, ;, ;, 3b], [Num11, 77, 6, -841742079296.48, �q�<��, b371aa3cb2d0], [sep12, 83, 1, ;, ;, 3b], [Num12, 84, 6, -841742079296.48, �q�<��, b371aa3cb2d0], [sep13, 90, 1, ;, ;, 3b], [Num13, 91, 7, -54321987654321.12, �q�<��, ecb371aa3cb2d0], [sep14, 98, 1, ;, ;, 3b], [Num14, 99, 7, -54321987654321.12, �q�<��, ecb371aa3cb2d0], [sep15, 106, 1, ;, ;, 3b], [Num15, 107, 8, -54321987654321.12, ��q�<��, ffecb371aa3cb2d0], [sep16, 115, 1, ;, ;, 3b], [Num16, 116, 8, -54321987654321.12, ��q�<��, ffecb371aa3cb2d0], [sep17, 124, 1, ;, ;, 3b], [Num17, 125, 3, -39779.36, �M0, c34d30]]')
		select('Table', 'cell:Data,20(4881874091.04)')
		click('Right')
		select('Table', 'cell:Data,20(2617964823.52)')
		assert_p('Table', 'Content', '[[NumA, 1, 25, 654321987654321.12,    654,321,987,654,321.12, 2020203635342c3332312c3938372c3635342c3332312e3132], [sep0, 26, 1, ;, ;, 3b], [Num0, 27, 1, -79, �, b1], [sep1, 28, 1, ;, ;, 3b], [Num1, 29, 2, 197.60, M0, 4d30], [sep2, 31, 1, ;, ;, 3b], [Num2, 32, 2, 197.60, M0, 4d30], [sep3, 34, 1, ;, ;, 3b], [Num3, 35, 3, 48038.88, IM0, 494d30], [sep4, 38, 1, ;, ;, 3b], [Num4, 39, 3, 48038.88, IM0, 494d30], [sep5, 42, 1, ;, ;, 3b], [Num5, 43, 4, -1965227.04, �IM0, f4494d30], [sep6, 47, 1, ;, ;, 3b], [Num6, 48, 4, -1965227.04, �IM0, f4494d30], [sep7, 52, 1, ;, ;, 3b], [Num7, 53, 4, -1965227.04, �IM0, f4494d30], [sep8, 57, 1, ;, ;, 3b], [Num8, 58, 5, 2617964823.52, <�IM0, 3cf4494d30], [sep9, 63, 1, ;, ;, 3b], [Num9, 64, 5, 2617964823.52, <�IM0, 3cf4494d30], [sep10, 69, 1, ;, ;, 3b], [Num10, 70, 6, 1300041685599.20, v<�IM0, 763cf4494d30], [sep11, 76, 1, ;, ;, 3b], [Num11, 77, 6, 1300041685599.20, v<�IM0, 763cf4494d30], [sep12, 83, 1, ;, ;, 3b], [Num12, 84, 6, 1300041685599.20, v<�IM0, 763cf4494d30], [sep13, 90, 1, ;, ;, 3b], [Num13, 91, 7, -66253952724958.24, �v<�IM0, e8763cf4494d30], [sep14, 98, 1, ;, ;, 3b], [Num14, 99, 7, -66253952724958.24, �v<�IM0, e8763cf4494d30], [sep15, 106, 1, ;, ;, 3b], [Num15, 107, 8, 654321987654321.12,  �v<�IM0, 00e8763cf4494d30], [sep16, 115, 1, ;, ;, 3b], [Num16, 116, 8, 654321987654321.12,  �v<�IM0, 00e8763cf4494d30], [sep17, 124, 1, ;, ;, 3b], [Num17, 125, 3, 48038.88, IM0, 494d30]]')
	close()
