from net.sf.RecordEditor.copy import CopyDBLayout

class Fixture:
	def start_application(self):
		args = []
		CopyDBLayout.main(args)

	def teardown(self):
		pass

	def setup(self):
		self.start_application()
