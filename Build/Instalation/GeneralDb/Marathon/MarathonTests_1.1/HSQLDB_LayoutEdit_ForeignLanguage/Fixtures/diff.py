from net.sf.RecordEditor.diff import CompareDBLayout


class Fixture:
	def start_application(self):
		args = []
		CompareDBLayout.main(args)

	def teardown(self):
		LayoutEdit.close()
		pass

	def setup(self):
		self.start_application()
