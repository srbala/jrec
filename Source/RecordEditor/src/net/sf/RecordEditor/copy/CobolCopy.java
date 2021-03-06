/**
 *
 */
package net.sf.RecordEditor.copy;

import javax.swing.JPanel;

import net.sf.RecordEditor.jibx.JibxCall;
import net.sf.RecordEditor.jibx.compare.CopyDefinition;
import net.sf.RecordEditor.re.openFile.LayoutSelectionFile;
import net.sf.RecordEditor.re.util.wizard.AbstractFilePnl;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.common.ReActionHandler;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;
import net.sf.RecordEditor.utils.swing.treeCombo.TreeComboFileSelect;
import net.sf.RecordEditor.utils.wizards.AbstractWizard;
import net.sf.RecordEditor.utils.wizards.AbstractWizardPanel;

/**
 * Copy a file from one Cobol-Format to a new Cobol-Format
 * @author Bruce Martin
 *
 */
public class CobolCopy extends AbstractWizard<CopyDefinition> {

	private CopyWizardFinalPnl finalScreen;
	private JibxCall<CopyDefinition> jibx = null;
//	private final  LayoutSelectionFile recordSelection = new LayoutSelectionFile();


	/**
	 * Create Single layout
	 * @param selection record layout selection class
	 */
	public CobolCopy() {
		this(new net.sf.RecordEditor.jibx.compare.CopyDefinition());
	}


	/**
	 * Create Single layout
	 * @param selection record layout selection class
	 * @param definition record filter definition
	 */
	@SuppressWarnings("unchecked")
	public CobolCopy(CopyDefinition definition) {
		super("Cobol Copy", definition);

		AbstractWizardPanel<CopyDefinition>[] pnls = new AbstractWizardPanel[2];
		LayoutSelectionFile recordSelection1 = new LayoutSelectionFile(true);
		LayoutSelectionFile recordSelection2 = new LayoutSelectionFile(true);

		recordSelection1.setMessage(super.getMessage());

		definition.type = CopyDefinition.COBOL_COPY;

		finalScreen = new CopyWizardFinalPnl(recordSelection1, recordSelection2);
		pnls[0] = new GetFiles(recordSelection1, recordSelection2);
//		pnls[1] = new CmpFieldSelection(selection);
		pnls[1] = finalScreen;

		super.setPanels(pnls);
	}



	/**
	 * @see net.sf.RecordEditor.utils.wizards.AbstractWizard#finished(java.lang.Object)
	 */
	@Override
	public void finished(CopyDefinition details) {

		if (finalScreen.isToRun()) {
			finalScreen.run();
		}
	}




	/**
	 * @see net.sf.RecordEditor.utils.wizards.AbstractWizard#executeAction(int)
	 */
	@Override
	public void executeAction(int action) {
       if (action == ReActionHandler.SAVE) {
    	   try {
    		   CopyDefinition diff = super.getActivePanel().getValues();

    		   if (! "".equals(diff.saveFile)) {
    			   if (jibx == null) {
    				   jibx = new JibxCall<CopyDefinition>(CopyDefinition.class);
    			   }

    			   jibx.unmarshal(diff.saveFile, diff);
    			   diff.fileSaved = true;
    		   }
    	   } catch (Exception e) {
    		   e.printStackTrace();
    		   Common.logMsgRaw(FILE_SAVE_FAILED, e);
    	   }
        } else {
            super.executeAction(action);
        }
	}

	/**
	 * @see net.sf.RecordEditor.utils.wizards.AbstractWizard#isActionAvailable(int)
	 */
	@Override
	public boolean isActionAvailable(int action) {
		if (action == ReActionHandler.SAVE) {
			return true;
		}
		return super.isActionAvailable(action);
	}


	/* ---------------------------------------------------------------------------------------*/


	@SuppressWarnings("serial")
	public static class GetFiles extends  AbstractFilePnl<CopyDefinition> {



		private CopyDefinition values = new net.sf.RecordEditor.jibx.compare.CopyDefinition();
//		private JPanel goPanel = new JPanel();
//		private FileChooser newFileName = new FileChooser();
		private TreeComboFileSelect newFileName = new TreeComboFileSelect(true, false, true, recent);
		private LayoutSelectionFile layoutSelection1;
		private LayoutSelectionFile layoutSelection2;

		public GetFiles(LayoutSelectionFile selection1, LayoutSelectionFile selection2) {
			super(selection1, "CobolFiles.txt");

			String s = Common.OPTIONS.DEFAULT_FILE_DIRECTORY.getWithStar();
//			newFileName.setDefaultDirectory(s);
			newFileName.setText(s);
			layoutSelection1 = selection1;
			layoutSelection2 = selection2;

			layoutSelection1.setLayoutName(Common.OPTIONS.DEFAULT_COBOL_DIRECTORY.get());
			//setHelpURL(Common.formatHelpURL(Common.HELP_DIFF_SL));
		}


		/**
		 * @see net.sf.RecordEditor.utils.wizards.AbstractWizardPanel#getValues()
		 */
		@Override
		public CopyDefinition getValues() throws Exception {

			values.oldFile.name = getCurrentFileName();
			values.newFile.name = newFileName.getText();

			values.oldFile.getLayoutDetails().name  = layoutSelection1.getLayoutName();
			values.newFile.getLayoutDetails().name = layoutSelection2.getLayoutName();
			if (layoutSelection1.getRecordLayout(getCurrentFileName()) == null) {
				throw new RuntimeException("Layout Does not exist");
			}

			return values;
		}

		/**
		 * @see net.sf.RecordEditor.utils.wizards.AbstractWizardPanel#setValues(java.lang.Object)
		 */
		@Override
		public void setValues(CopyDefinition detail) throws Exception {
			System.out.println("Setting Values ... ");
			values = detail;

			if (! "".equals(values.oldFile.name)) {
				fileName.setText(values.oldFile.name);
			}

			if (! "".equals(values.newFile.name)) {
				newFileName.setText(values.newFile.name);
			}

			if (! "".equals(values.oldFile.getLayoutDetails().name)) {
				layoutSelection1.setLayoutName(values.oldFile.getLayoutDetails().name);
			}

			if (! "".equals(values.newFile.getLayoutDetails().name)) {
				layoutSelection2.setLayoutName(values.newFile.getLayoutDetails().name);
			}


//			if (! "".equals(values.getLayoutDetails().name)) {
//				layoutSelection1.setLayoutName(values.getLayoutDetails().name);
//			}
		}

		@Override
		protected void addFileName(BaseHelpPanel pnl) {

			pnl.addLineRE("Old File", fileName);
//			pnl.addLine("New File", newFileName, newFileName.getChooseFileButton());
			pnl.addLineRE("New File", newFileName);
		}

		@Override
		protected void addLayoutSelection() {

			layoutSelection1.addLayoutSelection(this, fileName, new JPanel(), null, null);
			this.setGapRE(GAP3);
			layoutSelection2.addLayoutSelection(this, getGoPanel(), layoutSelection1.getCopybookFile());
			this.setGapRE(GAP3);
		}
	}


//	/**
//	 * @param args
//	 */
//	public static void main(String[] args) {
//
//		 new ReMainFrame("File Compare", "");
//		 new CmpSingleLayout(new LayoutSelectionDB(new CopyBookDbReader()));
//	}

}
