useFixture(default)

def test():
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		click('Preferences')

		if window('Record Editor Options Editor'):
			select('TabbedPane', 'Properties')
			select('PropertiesTab', 'Test')
			select('Test Mode_Chk', 'true')
			select('Warn on Structure change_Chk', 'false')
			select('Load In background_Chk', 'false')
			select('Use New Tree Expansion_Chk', 'true')
			select('On Search Screen default to "All Fields"_Chk', 'true')
			select('Add names to JComponents for use by testing tools_Chk', 'true')

			select('PropertiesTab', 'Behaviour')
			select('Bring log to Front_Chk', 'false')
			select('Default to prefered layout_Chk', 'false')
			select('Delete Selected rows with the delete key_Chk', 'true')
			select('Show all export panels on the export Screen_Chk', 'false')

			click('Save')
			click('Save')
		close()
	close()
