def windows():
	return 01
##	return "a" == "a"


def isMsAccess():
	return 0

def isVersion80():
	return 1

def isVersion81():
	return 1

def isVersion82():
	return 1

def Linux():
	return 'guest'
#	return 'knoppix'


def isTstLanguage():
    return 0

def isWindowsLook():
	return 0

def isNimbusLook():
	return 0


def sampleDir():
	return utilDir() + 'SampleFiles' + separator()


def fl(txt):
	if isTstLanguage():
		return '`!' + txt + '!`'
	else:
		return txt

def implementationSampleDir():
	return  sampleDir()
##	return '/C:/Program Files/RecordEdit/HSQLDB/SampleFiles/'
#	return '/home/knoppix/RecordEdit/HSQLDB/SampleFiles/'


def cobolTestDir():
	if windows():
		return "C:\\Users\\mum\\Bruce\\CobolTestData\\"
		##return "C:\\Users\\mum\\Bruce\\CobolTestData\\"
		##return 'E:\\Work\\RecordEdit\\CobolTests\\TestData\\'
	else: 	
		return '/home/bm/Programs/open-cobol-1.0/CobolSrc/z1Test/'
##		return '/home/' + Linux() + '/reTest/'


def xmlCopybookDir():
	return copybookDir() + 'Xml' + separator()

def cobolDir():
	return copybookDir()+ 'Cobol' + separator()

def csvDir():
	return copybookDir()+ 'Csv' + separator()

def copybookDir():
	return utilDir()+ 'CopyBook' + separator()

def userDir():
	return paramDir() + 'User'  + separator()


def utilDir():
	return paramDir()

def separator():
	if windows():
		return '\\'
	else: 
		return '/'


def setRecordLayout(select, recordLayout):
	select('ComboBox2', recordLayout)

def setRecordLayout2(select, recordLayout):
	select('ComboBox2', recordLayout)


def setRecordLayoutX(select, recordLayout):
##	select('BmKeyedComboBox', '0')
##	select('ComboBox', fl('RecordEditor XML Copybook'))
	select('ManagerCombo', fl('RecordEditor XML Copybook'))
	select('FileChooser1', xmlCopybookDir() + recordLayout + '.Xml')

	##select('BmKeyedComboBox', '0')
	select('BmKeyedComboBox', fl('Default'))

def closeWindow(click):
	if isNimbusLook():
		click('InternalFrameTitlePane.closeButton')
	else:
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	return


def sampleDir():
	return utilDir()+ 'SampleFiles' + fileSep()
	
def paramDir():
	if windows():
		if isVersion80():
##			return 'C:\\Users\\Mum\\RecordEditor_HSQL\\'
			return 'C:\\Users\\BruceTst2\\.RecordEditor\\HSQLDB\\'
		else:
			return 'C:\\JavaPrograms\\RecordEdit\\'

		##return 'C:\\Users\\mum\\RecordEditor_HSQL\\User\\'
		##return 'C:\\Users\\bm\\.RecordEditor\\' + version() + '\\User\\'
	else: 
		return '/home/bm' + '/.RecordEditor/' + version() + '/'


def fileSep():
	if windows():
		return '\\'
	else:
		return '/'


def selectPane():
	return 'FilePane$4'
	#return 'FilePane$3'


def checkCopybookLoad(file, copybook):
	return '\n\n' + fl('-->> ' + file + ' processed\n\n      Copybook: ' + copybook)

def selectOldFilemenu(select_menu, menu, text):
	if isVersion80():
		if isTstLanguage():
			select_menu(fl(menu) + '>>' + fl(text))
		else:
			select_menu(menu + '>>' + text)
	else:
		select_menu('File>>' + text)

def delete3(click):
	if isTstLanguage():
		click(fl('Delete') + '1')
	else:
		click('Delete3')

def delete2(click):
	if isTstLanguage():
		click(fl('Delete'))
	else:
		click('Delete2')

def paste2(click):
	if isTstLanguage():
		click(fl('Paste'))
	else:
		click('Paste2')

def copy2(click):
	if isTstLanguage():
		click(fl('Copy'))
	else:
		click('Copy2')

def cut2(click):
	if isTstLanguage():
		click(fl('Cut'))
	else:
		click('Cut2')

def save1(click):
	if isTstLanguage():
		click(fl('Save'))
	else:
		click('Save1')


def new1(click):
	if isTstLanguage():
		click(fl('New'))
	else:
		click('New2')

