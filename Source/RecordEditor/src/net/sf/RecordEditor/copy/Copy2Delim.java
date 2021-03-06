/**
 *
 */
package net.sf.RecordEditor.copy;

import java.awt.BorderLayout;
import java.nio.charset.Charset;

import javax.swing.JCheckBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

import net.sf.JRecord.Common.Conversion;
import net.sf.RecordEditor.jibx.JibxCall;
import net.sf.RecordEditor.jibx.compare.CopyDefinition;
import net.sf.RecordEditor.re.openFile.AbstractLayoutSelection;
import net.sf.RecordEditor.re.util.csv.CsvCode;
import net.sf.RecordEditor.re.util.wizard.AbstractFilePnl;
import net.sf.RecordEditor.utils.charsets.FontCombo;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.common.ReActionHandler;
import net.sf.RecordEditor.utils.swing.BaseHelpPanel;
import net.sf.RecordEditor.utils.swing.ComboBoxs.DelimiterCombo;
import net.sf.RecordEditor.utils.swing.ComboBoxs.QuoteCombo;
import net.sf.RecordEditor.utils.swing.treeCombo.TreeComboFileSelect;
import net.sf.RecordEditor.utils.wizards.AbstractWizard;
import net.sf.RecordEditor.utils.wizards.AbstractWizardPanel;


/**
 * @author Bruce Martin
 *
 */
public class Copy2Delim extends AbstractWizard<CopyDefinition> {


	private CopyWizardFinalPnl finalScreen;
	private JibxCall<CopyDefinition> jibx = null;
//	private final  LayoutSelectionFile recordSelection = new LayoutSelectionFile();


	/**
	 * Create Single layout
	 * @param selection record layout selection class
	 */
	public Copy2Delim(AbstractLayoutSelection recordSelection1) {
		this(recordSelection1, new net.sf.RecordEditor.jibx.compare.CopyDefinition());
	}


	/**
	 * Create Single layout
	 * @param selection record layout selection class
	 * @param definition record filter definition
	 */
	public Copy2Delim(
			AbstractLayoutSelection recordSelection1 , CopyDefinition definition) {
		super("Copy to Delimited file", definition);

		AbstractWizardPanel<CopyDefinition>[] pnls = new AbstractWizardPanel[3];

		recordSelection1.setMessage(super.getMessage());

		definition.type = CopyDefinition.DELIM_COPY;

		finalScreen = new CopyWizardFinalPnl(recordSelection1, null);
		pnls[0] = new GetFiles(recordSelection1);
		pnls[1] = new FieldSelection(recordSelection1, null, "");
		pnls[2] = finalScreen;

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



	@SuppressWarnings("serial")
	public static class GetFiles extends  AbstractFilePnl<CopyDefinition> {

		private CopyDefinition values = new net.sf.RecordEditor.jibx.compare.CopyDefinition();
//		private JPanel goPanel = new JPanel();
//		private FileChooser newFileName = new FileChooser();
		private TreeComboFileSelect newFileName = new TreeComboFileSelect(true, false, true, getRecentList(), getRecentDirectoryList());

		private AbstractLayoutSelection layoutSelection1;

		private DelimiterCombo delimCombo = DelimiterCombo.NewDelimCombo();
		private JTextField delimTxt = new JTextField(8);
		private JCheckBox names1stLineChk = new JCheckBox();
		private QuoteCombo quoteTxt = QuoteCombo.newCombo();
		private FontCombo fontCombo = new FontCombo();


		public GetFiles(AbstractLayoutSelection selection1) {
			super(selection1, "CobolFiles.txt");

			newFileName.setText(Common.OPTIONS.DEFAULT_FILE_DIRECTORY.getWithStar());
			layoutSelection1 = selection1;

			setHelpURLre(Common.formatHelpURL(Common.HELP_DIFF_SL));
		}


		/**
		 * @see net.sf.RecordEditor.utils.wizards.AbstractWizardPanel#getValues()
		 */
		@Override
		public CopyDefinition getValues() throws Exception {

			values.oldFile.name = getCurrentFileName();
			values.newFile.name = newFileName.getText();

			values.oldFile.getLayoutDetails().name  = layoutSelection1.getLayoutName();

			values.font = fontCombo.getText();
			values.delimiter = getDelim(values.font);
			values.namesOnFirstLine = names1stLineChk.isSelected();
			values.quote = getQuote(values.font);
			
			if ((! "".equals(values.font) && ! Charset.isSupported(values.font))) {
				fontCombo.requestFocus();
				throw new RuntimeException("font (charset) is not supported");
			} 
//			if ((      values.delimiter.toLowerCase().startsWith("x'") 
//					|| (values.quote != null && values.quote.toLowerCase().startsWith("x'")))
//			&& Conversion.isMultiByte(values.font)) {
//				throw new RuntimeException("Hex field sperators are only supported for single byte charsets (fonts)");
//			}
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

			delimTxt.setText("");
			delimCombo.setDelimiter(values.delimiter);
			if (values.delimiter != null && ! values.delimiter.equals(delimCombo.getDelimiter())) {
				delimTxt.setText(values.delimiter);
			}
			names1stLineChk.setSelected(values.namesOnFirstLine);
			quoteTxt.setText(values.quote);
			fontCombo.setText(values.font);
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
			JPanel delimPnl = new JPanel(new BorderLayout());
			JPanel orLabel = new JPanel();
			orLabel.add(new JLabel("or"));

			delimPnl.add(BorderLayout.WEST, delimCombo);
			delimPnl.add(BorderLayout.CENTER, orLabel);
			delimPnl.add(BorderLayout.EAST, delimTxt);

			this.setGapRE(GAP3);
			this.addLineRE("Field Delimiter", delimPnl);
			this.setHeightRE(HEIGHT_1P1);
			this.setGapRE(GAP1);

			this.addLineRE("Names on 1st Line", names1stLineChk);
			this.addLineRE("Quote", quoteTxt);
			this.addLineRE("Font Name", fontCombo);

			this.setGapRE(GAP3);
		}


		private String getDelim(String font) {
			String txt = delimTxt.getText();
			return CsvCode.checkDelimiter("".equals(txt) ? delimCombo.getDelimiter() : txt, font);
		}


		private String getQuote(String font) {
			//String txt = quoteTxt.getText();
			return CsvCode.checkQuote( quoteTxt.getQuote(), font);
		}

//		protected String checkCsvItem(String txt, String id) {
//			if (txt == null || txt.length() < 2) {
//			} else if (((txt.length() == 5) && txt.toLowerCase().startsWith("x'") && txt.endsWith("'"))) {
//				try {
//					Conversion.getByteFromHexString(txt);
//				} catch (Exception e) {
//					String msg1 = LangConversion.convert(
//							LangConversion.ST_ERROR,
//							"Invalid " + id+ " - Invalid  hex string: {0}",
//							txt.substring(2, 3));
//					//Common.logMsg(msg1, null);
//					throw new RuntimeException(msg1);
//				}
//			} else {
//				String msg1 = "Invalid " + id+ ", should be a single character or a hex character";
//				//Common.logMsg(msg1, null);
//				throw new RecordRunTimeException(msg1);
//			}
//
//			return txt;
//		}
	}

}
