package net.sf.RecordEditor.re.util.wizard;

import net.sf.JRecord.Common.RecordRunTimeException;
import net.sf.RecordEditor.jibx.compare.BaseCopyDif;
import net.sf.RecordEditor.jibx.compare.File;
import net.sf.RecordEditor.re.openFile.AbstractLayoutSelection;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.msg.UtMessages;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;


@SuppressWarnings("serial")
public class StandardGetFiles<Save extends BaseCopyDif> extends  AbstractFilePnl<Save> {

	public static final int OLD = 0;
	public static final int NEW = 1;

	private static final String[] FILE_PROMPT = {"Old File Name", "New File Name"};;

	private Save values; // = new save();
//		private JPanel goPanel = new JPanel();
	private AbstractLayoutSelection layoutSelection;
	int fileNo;
	private final boolean fileMustExist;

	public StandardGetFiles(AbstractLayoutSelection selection, int fileNumber, String recentFiles, String help, boolean fileMustExist) {
		super(selection, recentFiles);

		this.layoutSelection = selection;
		this.fileNo =  fileNumber;
		this.fileMustExist = fileMustExist;

		setHelpURLre(Common.formatHelpURL(help /*Common.HELP_DIFF_TL*/));
	}


	/**
	 * @see net.sf.RecordEditor.utils.wizards.AbstractWizardPanel#getValues()
	 */
	@Override
	public Save getValues() throws Exception {

		File fileDtl = values.oldFile;
		if (fileNo == NEW) {
			fileDtl = values.newFile;
		}

		layoutSelection.forceLayoutReload();
		fileDtl.name = getCurrentFileName();
		fileDtl.getLayoutDetails().name = layoutSelection.getLayoutName();
		if (layoutSelection.getRecordLayout(fileDtl.name) == null) {
			throw new RecordRunTimeException("Layout Does not exist");
		}
		if (fileMustExist) {
			checkFile(fileDtl.name, fileName);
		} else if ((new java.io.File(fileDtl.name)).isDirectory()) {
			fileName.requestFocus();
			throw new RuntimeException(UtMessages.DIRECTORY_NOT_ALLOWED.get(fileDtl.name));
		}

		return values;
	}

	/**
	 * @see net.sf.RecordEditor.utils.wizards.AbstractWizardPanel#setValues(java.lang.Object)
	 */
	@Override
	public void setValues(Save detail) throws Exception {
		File fileDtl;
		String layoutName;

		//System.out.println("Setting Values ... ");
		values = detail;

		fileDtl = values.oldFile;
		if (fileNo == NEW) {
			fileDtl = values.newFile;
		}

		if (! "".equals(fileDtl.name)) {
			fileName.setText(fileDtl.name);
		}

//		if (! "".equals(fileDtl.name)) {
//			fileName.setText(fileDtl.name);
//		}

		layoutName = fileDtl.getLayoutDetails().name;
		if (! "".equals(layoutName)) {
			layoutSelection.setLayoutName(layoutName);
		}
	}


	/**
	 * Add a file name
	 */
	@Override
	protected void addFileName(BaseHelpPanel pnl) {

		pnl.addLineRE(FILE_PROMPT[fileNo], fileName);
	}
}
